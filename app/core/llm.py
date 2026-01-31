import asyncio
import os
from dotenv import load_dotenv
load_dotenv()
import re
import zlib
import logging
from google import genai
from google.genai import types


from app.tools.search import search_web

logger = logging.getLogger(__name__)

import json
import difflib
import re

class LLMProvider:
    """
    Centralized provider for LLM interactions.
    Uses Google GenAI SDK with offline fallback.
    """
    
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self._cache = self._load_cache()
        
        if not self.api_key:
            logger.error("GEMINI_API_KEY is not set. Using offline mode.")
            self.client = None
        else:
            try:
                self.client = genai.Client(api_key=self.api_key)
            except Exception as e:
                logger.error(f"Failed to initialize Gemini client: {e}")
                self.client = None

    def _load_cache(self):
        try:
            cache_path = os.path.join("app", "core", "cached_responses.json")
            if os.path.exists(cache_path):
                with open(cache_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            return []
        except Exception as e:
            logger.error(f"Failed to load cache: {e}")
            return []

    def _get_fallback_response(self, prompt: str) -> str:
        """
        Retrieves a fuzzy-matched response from cache if API fails.
        Handles specific agent card extraction.
        """
        if not self._cache:
            return "<div><p>Analysis engine unavailable (Offline).</p></div>"

        # 1. Clean prompt to find the core user query
        # Agents wrap queries like: 'Analyze logic for: "User Query"'
        match = re.search(r':\s*"(.*?)"', prompt, re.DOTALL)
        user_query = match.group(1) if match else prompt
        
        # 2. Find best match
        best_match = None
        highest_ratio = 0.0
        
        for entry in self._cache:
            ratio = difflib.SequenceMatcher(None, user_query.lower(), entry["query"].lower()).ratio()
            if ratio > highest_ratio:
                highest_ratio = ratio
                best_match = entry

        # Threshold for fuzzy match
        if highest_ratio < 0.6 or not best_match:
             return "<div><p>Analysis details unavailable (Offline - No Match).</p></div>"

        # 3. Extract the specific card based on the agent's prompt signature
        full_html = best_match["response"]
        
        if "Analyze logic for" in prompt:
            # Extract Logic Card
            card_match = re.search(r'<div id="logic-card">(.*?)</div>', full_html, re.DOTALL)
            return card_match.group(1) if card_match else "<p>Logic data unavailable.</p>"
            
        elif "Trace origin for" in prompt:
            # Extract Origin Card
            card_match = re.search(r'<div id="origin-card">(.*?)</div>', full_html, re.DOTALL)
            return card_match.group(1) if card_match else "<p>Origin data unavailable.</p>"
            
        elif "Analyze tone for" in prompt:
            # Extract Context Card
            card_match = re.search(r'<div id="context-card">(.*?)</div>', full_html, re.DOTALL)
            return card_match.group(1) if card_match else "<p>Context data unavailable.</p>"
            
        return full_html


    def _save_to_cache(self, prompt: str, response_text: str):
        """
        Saves the successful API response to the local cache for future offline use.
        Merges partial responses (Logic/Origin/Context) into the single HTML entry.
        """
        try:
            # 1. Extract query
            match = re.search(r':\s*"(.*?)"', prompt, re.DOTALL)
            user_query = match.group(1) if match else prompt
            user_query_lower = user_query.lower()

            cache_path = os.path.join("app", "core", "cached_responses.json")
            data = []
            if os.path.exists(cache_path):
                with open(cache_path, "r", encoding="utf-8") as f:
                    data = json.load(f)

            # 2. Find existing entry or create new
            target_entry = None
            for entry in data:
                if entry["query"].lower() == user_query_lower:
                    target_entry = entry
                    break
            
            if not target_entry:
                # Initialize with empty placeholders if new
                target_entry = {
                    "query": user_query,
                    "response": '<div id="logic-card"></div><div id="origin-card"></div><div id="context-card"></div>'
                }
                data.append(target_entry)

            # 3. Update the specific section based on prompt type
            # We use regex to replace the content inside the specific div
            current_html = target_entry["response"]
            
            if "Analyze logic for" in prompt:
                # Replace content of logic-card
                # Use a reliable regex that handles newlines
                snippet = f'<div id="logic-card">{response_text}</div>'
                current_html = re.sub(r'<div id="logic-card">.*?</div>', snippet, current_html, flags=re.DOTALL)
                
            elif "Trace origin for" in prompt:
                snippet = f'<div id="origin-card">{response_text}</div>'
                current_html = re.sub(r'<div id="origin-card">.*?</div>', snippet, current_html, flags=re.DOTALL)
                
            elif "Analyze tone for" in prompt:
                snippet = f'<div id="context-card">{response_text}</div>'
                current_html = re.sub(r'<div id="context-card">.*?</div>', snippet, current_html, flags=re.DOTALL)

            target_entry["response"] = current_html

            # 4. Write back to disk
            with open(cache_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
                
            # Update memory cache too
            self._cache = data

        except Exception as e:
            logger.error(f"Failed to save to cache: {e}")

    async def run_prompt(self, prompt: str, system_instruction: str = "") -> str:
        """
        Executes a prompt against Gemini 3 via SDK.
        Falls back to cache on failure.
        """
        # If no client, go straight to fallback
        if not self.client:
             logger.warning("Client not initialized. Using fallback.")
             return self._get_fallback_response(prompt)
        
        tools = [types.Tool(google_search=types.GoogleSearch())]
        
        if system_instruction:
            config = types.GenerateContentConfig(
                system_instruction=system_instruction,
                tools=tools
            )
        else:
             config = types.GenerateContentConfig(
                tools=tools
            )
        
        try:
            response = await self.client.aio.models.generate_content(
                model='gemini-3-flash-preview', 
                contents=prompt,
                config=config
            )
            
            if not response.text:
                 return "<div><p>Analysis details unavailable.</p></div>"

            result_text = response.text.strip()
            
            # Save to cache for future offline use
            self._save_to_cache(prompt, result_text)
            
            return result_text

        except Exception as e:
            error_str = str(e)
            logger.error(f"Gemini SDK Error: {error_str}")
            
            # Circuit Breaker: Stop spamming if key is invalid or quota exceeded
            if "403" in error_str or "PERMISSION_DENIED" in error_str:
                logger.critical("API Key reported as LEAKED/INVALID. Disabling Online Mode permanently for this session.")
                self.client = None
            elif "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                logger.warning("Quota exceeded. temporary fallback.")
                # We don't disable permanently for 429, but maybe we should for a short time? 
                # For now, just fallback.

            logger.info("Attempting offline fallback...")
            # Fallback to cache
            return self._get_fallback_response(prompt)




