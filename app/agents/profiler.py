from app.agents.base import BaseAgent
from app.schemas.responses import AgentResponse

class ProfilerAgent(BaseAgent):
    """
    Analyzes rhetorical intensity via LLM Provider.
    """
    
    def __init__(self):
        super().__init__(name="profiler")
        
    async def analyze(self, input_text: str) -> AgentResponse:
        system_instruction = """
        You are The Profiler. Analyze the emotional and rhetorical tone of the query.
        
        STRICT RULES:
        1. Output ONE short, simple paragraph explaining the intent (curiosity, aggression, satire, etc.).
        2. Use clear everyday language. No academic jargon.
        3. "A normal internet user should immediately understand what the analysis means."
        4. Do not invent metrics or scores.
        5. Output ONLY valid HTML (e.g., <p>...</p>). No markdown.
        """
        
        prompt = f"""
        Analyze tone for: "{input_text}"
        """
        
        html_content = await self.llm.run_prompt(prompt, system_instruction=system_instruction)
        
        return AgentResponse(
            agent_name=self.name,
            status="completed",
            html_payload=self.format_html("Rhetorical Profile", html_content)
        )
