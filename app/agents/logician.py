from app.agents.base import BaseAgent
from app.schemas.responses import AgentResponse

class LogicianAgent(BaseAgent):
    """
    Performs consequence reasoning via LLM Provider.
    """
    
    def __init__(self):
        super().__init__(name="logician")
        
    async def analyze(self, input_text: str) -> AgentResponse:
        system_instruction = """
        You are The Logician. Analyze the user's query for internal consistency and logic.
        
        STRICT RULES:
        1. Output ONE short, simple paragraph using clear everyday language.
        2. No academic jargon, no philosophical complexity.
        3. "A normal internet user should immediately understand what the analysis means."
        4. Do not reference real institutions or external facts unless checking consistency.
        5. Output ONLY valid HTML (e.g., <p>...</p>). No markdown.
        """
        
        prompt = f"""
        Analyze logic for: "{input_text}"
        """
        
        # The provider does the work
        html_content = await self.llm.run_prompt(prompt, system_instruction=system_instruction)
        
        return AgentResponse(
            agent_name=self.name,
            status="completed",
            html_payload=self.format_html("Logic Analysis", html_content)
        )
