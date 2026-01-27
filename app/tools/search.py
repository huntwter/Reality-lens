import random
import re

async def search_web(query: str) -> str:
    """
    Simulates a Google Search Grounding call.
    Returns deterministic textual content based on query keywords
    to allow agents to perform "real" parsing logic.
    """
    query_lower = query.lower()
    
    # 1. Historical Queries (Historian Agent)
    if "earliest mention" in query_lower or "origin" in query_lower:
        # Generate text with years based on a hash of the query to be deterministic
        # but varied across different inputs.
        base_year = 2010 + (len(query) % 15) # 2010-2024
        
        return f"""
        Search Results for "{query}":
        1. Archived Report ({base_year}): The initial discussion of this topic appeared in late {base_year}.
        2. Timeline Analysis: Recycled narrative observed in {base_year + 2} and again in {base_year + 5}.
        3. Fact Check Database: First debunked in {base_year}.
        """

    # 2. Consequence/Logic Queries (Logician Agent)
    # Return text containing "evidence" keywords if the query asks for them
    content_snippets = []
    
    # Keywords often used by the Logician to form hypothesis Q
    risk_terms = ["incident", "ban", "warning", "recall", "injury"]
    safety_terms = ["approval", "study", "endorsement", "clinical trial", "safe"]
    neutral_terms = ["report", "analysis", "data", "observation"]
    
    # Seed generator for determinism
    random.seed(query)
    
    if any(w in query_lower for w in ["risk", "harm", "danger"]):
        # Simulate mixed findings
        count = random.randint(0, 3)
        content_snippets.extend([f"Reported {term} in region..." for term in random.sample(risk_terms, count)])
        content_snippets.append("No widespread bans observed.")
        
    elif any(w in query_lower for w in ["safety", "benefit", "approval"]):
        # Simulate positive findings
        count = random.randint(1, 4)
        content_snippets.extend([f"FDA {term} confirmed..." for term in random.sample(safety_terms, count)])
    
    else:
        # Neutral
        content_snippets.append("General discussion found.")
        content_snippets.append("Mixed anecdotal evidence.")

    return " ... ".join(content_snippets)
