import asyncio
import os
import sys

# Mock API Key to force fallback initialization logic check or bypass
os.environ["GEMINI_API_KEY"] = "fake_key_for_testing"

# Add project root to path
sys.path.append(os.getcwd())

from app.core.llm import LLMProvider

async def test_fallback():
    print("--- Testing Offline Fallback ---")
    provider = LLMProvider()
    
    # Mock client to force failure
    provider.client = None 
    print("1. Force disabled client (Simulate API failure or Offline mode)")

    # Test Case 1: Logic Query
    print("\n[Test 1] Logic Agent Query: 'Is earth flat?'")
    prompt_logic = 'Analyze logic for: "Is earth flat?"'
    response = await provider.run_prompt(prompt_logic)
    print(f"Response prefix: {response[:50]}...")
    if "Logic dictates that" in response or "logic-card" in response or "contradicts all geodetic" in response:
        print("✅ Success: Logic card content returned.")
    else:
        print(f"❌ Failure: Unexpected response: {response}")

    # Test Case 2: Historian Query (Fuzzy match)
    print("\n[Test 2] Historian Agent Query: 'Trace origin for: \"Do vax cause autsim?\"' (intentional typo)")
    prompt_history = 'Trace origin for: "Do vax cause autsim?"'
    response = await provider.run_prompt(prompt_history)
    print(f"Response prefix: {response[:50]}...")
    if "Andrew Wakefield" in response or "1998" in response:
        print("✅ Success: Origin card returned despite typo.")
    else:
        print(f"❌ Failure: Fuzzy match failed or content missing. Response: {response}")

    # Test Case 3: Profiler Query
    print("\n[Test 3] Profiler Agent Query: 'Analyze tone for: \"Is tomato a vegetable?\"'")
    prompt_profile = 'Analyze tone for: "Is tomato a vegetable?"'
    response = await provider.run_prompt(prompt_profile)
    print(f"Response prefix: {response[:50]}...")
    if "playful" in response or "argumentative" in response:
        print("✅ Success: Context card returned.")
    else:
        print(f"❌ Failure: Context card missing. Response: {response}")

    # Test Case 4: No Match
    print("\n[Test 4] Unique Query: 'What is the capital of Mars?'")
    prompt_miss = 'Analyze logic for: "What is the capital of Mars?"'
    response = await provider.run_prompt(prompt_miss)
    if "Analysis details unavailable" in response:
        print("✅ Success: Correctly handled no match.")
    else:
        print(f"❌ Failure: Should have returned unavailability message. Got: {response}")

if __name__ == "__main__":
    asyncio.run(test_fallback())
