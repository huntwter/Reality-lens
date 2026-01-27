from pydantic import BaseModel
from typing import Dict, Any

class AgentResponse(BaseModel):
    """
    Standardized response schema for internal agent communication.
    """
    agent_name: str
    status: str
    html_payload: str
    metadata: Dict[str, Any] = {}

class StreamEvent(BaseModel):
    """
    Schema for SSE event payloads.
    """
    event: str = "message"
    data: str
