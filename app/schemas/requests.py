from pydantic import BaseModel
from typing import Optional

class AnalysisRequest(BaseModel):
    """
    Schema for incoming user requests.
    """
    query: str
    context: Optional[str] = None
