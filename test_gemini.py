import os
import asyncio
from dotenv import load_dotenv
load_dotenv()
from google import genai

async def test():
    api_key = os.getenv('GEMINI_API_KEY')
    print(f"API Key present: {bool(api_key)}")
    
    client = genai.Client(api_key=api_key)
    
    print("Making request...")
    try:
        response = await client.aio.models.generate_content(
            model='gemini-2.0-flash',
            contents='Say hello in one word'
        )
        print(f"SUCCESS: {response.text}")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    asyncio.run(test())
