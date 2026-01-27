from abc import ABC, abstractmethod
from app.schemas.responses import AgentResponse
from app.core.llm import LLMProvider

class BaseAgent(ABC):
    """
    Abstract Base Class for all Reasoning Agents.
    Enforces a standard analyze interface.
    """
    
    def __init__(self, name: str):
        self.name = name
        self.llm = LLMProvider()
        
    @abstractmethod
    async def analyze(self, input_text: str) -> AgentResponse:
        """
        Main entry point for the agent's logic.
        """
        pass
    
    def format_html(self, title: str, content: str, verified: bool = True) -> str:
        """
        No-op wrapper for the new Editorial design. 
        The HTML structure is handled by the Agent's system prompt and the main layout.
        We just add the entrance animation.
        """
        return f"""
            <div class="animate-reveal">
                {content}
            </div>
        """
