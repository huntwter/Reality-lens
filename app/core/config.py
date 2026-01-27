import os
from dotenv import load_dotenv
load_dotenv()
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "RealityLens — Cognitive Firewall"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # AI Configuration
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    GOOGLE_SEARCH_API_KEY: str = os.getenv("GOOGLE_SEARCH_API_KEY", "")
    
    # Application State
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    class Config:
        case_sensitive = True

settings = Settings()
