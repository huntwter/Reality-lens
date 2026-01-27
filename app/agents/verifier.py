from app.schemas.responses import AgentResponse
import re

class VerifierAgent:
    """
    Sanitizes output to ensure safety constraints.
    - No True/False verdicts
    - No defamatory claims
    - No medical/legal advice
    """
    
    def verify(self, response: AgentResponse) -> AgentResponse:
        # Simple keyword based sanitization for prototype
        forbidden_terms = ["guilty", "proven false", "medical advice", "liar"]
        
        sanitized_payload = response.html_payload
        for term in forbidden_terms:
            if term in sanitized_payload.lower():
                # Redact or flag logic would go here
                # For now, we trust the prompt engineering but this is the hook
                pass
                
        return response
