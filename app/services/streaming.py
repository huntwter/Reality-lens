import json
from typing import AsyncGenerator
from app.schemas.responses import AgentResponse, StreamEvent

class SSEGenerator:
    """
    Helper to format SSE events.
    """
    
    @staticmethod
    def format(data: dict) -> str:
        return f"data: {json.dumps(data)}\n\n"
    
    @staticmethod
    def stop() -> str:
        return "event: done\ndata: {}\n\n"
