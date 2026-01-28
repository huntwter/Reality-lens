import asyncio
import logging
from typing import AsyncGenerator

from app.agents.logician import LogicianAgent
from app.agents.historian import HistorianAgent
from app.agents.profiler import ProfilerAgent
from app.services.streaming import SSEGenerator

logger = logging.getLogger(__name__)

class Orchestrator:
    """
    Manages the parallel execution of reasoning agents.
    """
    
    def __init__(self):
        self.logician = LogicianAgent()
        self.historian = HistorianAgent()
        self.profiler = ProfilerAgent()
        
    async def run_investigation(self, query: str) -> AsyncGenerator[str, None]:
        """
        Runs agents and yields SSE events.
        """
        
        
        
        agents = [self.logician, self.historian, self.profiler]
        
        try:
            for i, agent in enumerate(agents):
                # Small delay to mitigate rate limits (429) on free tier
                if i > 0:
                    await asyncio.sleep(4) 
                
                try:
                    # Run sequentially
                    result = await agent.analyze(query)
                    yield SSEGenerator.format(result.model_dump())
                except Exception as e:
                    logger.error(f"Agent task failed: {e}")
                    # Allow continuity for other agents even if one fails
                    pass

        except asyncio.CancelledError:
            logger.warning("Client disconnected.")
            raise
        finally:
            yield SSEGenerator.stop()
