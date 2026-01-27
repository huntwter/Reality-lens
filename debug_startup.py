
try:
    print("Attempting to import google.genai...")
    from google import genai
    print("Import google.genai successful")
    from google.genai import types
    print("Import google.genai.types successful")
    
    import app.core.llm
    print("Import app.core.llm successful")
    
    import app.services.orchestrator
    print("Import app.services.orchestrator successful")
    
except Exception as e:
    print(f"FAILED: {e}")
    import traceback
    traceback.print_exc()
