from app.agents.base import BaseAgent
from app.schemas.responses import AgentResponse

class HistorianAgent(BaseAgent):
    """
    Traces narrative origins via LLM Provider.
    """
    
    def __init__(self):
        super().__init__(name="historian")
        
    async def analyze(self, input_text: str) -> AgentResponse:
        system_instruction = """
        You are The Historian. Trace the origin or context of the query using Google Search Grounding to verify facts.
        
        STRICT RULES:
        1. Output ONE short, simple paragraph explaining where this idea comes from.
        2. Use clear everyday language. No academic jargon.
        3. "A normal internet user should immediately understand what the analysis means."
        4. VERIFY ALL FACTS. Do not hallucinate dates or names.
        5. Include 1-2 derived clickable source links if relevant facts are found: <a href="..." target="_blank" class="text-[#C5A059] underline">Source</a>
        6. Output ONLY valid HTML (e.g., <p>...</p>). No markdown.
        """
        
        prompt = f"""
        Trace origin for: "{input_text}"
        """
        
        html_content = await self.llm.run_prompt(prompt, system_instruction=system_instruction)
        
        return AgentResponse(
            agent_name=self.name,
            status="completed",
            html_payload=self.format_html("Historical Context", html_content)
        )
