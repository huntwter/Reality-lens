from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from fastapi.templating import Jinja2Templates
from app.services.orchestrator import Orchestrator

# Setup templates via dependency or global
templates = Jinja2Templates(directory="app/templates")

router = APIRouter()
# In a real app, use Dependency Injection: 
# async def get_orchestrator(): return Orchestrator()
orchestrator = Orchestrator() 

@router.get("/")
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/stream")
async def stream_analysis(request: Request, q: str):
    """
    SSE Endpoint for real-time analysis streaming.
    Checks for client disconnects via request state.
    """
    
    async def event_generator():
        # The Orchestrator.run_investigation is designed to yield events
        # If the client disconnects, FastAPI raises CancelledError inside this generator
        # which propagates to the orchestrator's try/finally block
        async for event in orchestrator.run_investigation(q):
            if await request.is_disconnected():
                break
            yield event

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )
