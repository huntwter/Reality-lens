# RealityLens — Cognitive Firewall

RealityLens performs live cognitive analysis using the Gemini 3 model via the google-genai SDK.
During hackathon demos, external AI services can occasionally experience quota or latency limitations.

To ensure a smooth and uninterrupted demonstration experience, the application includes a graceful fallback mode that displays previously generated Gemini 3 sample analyses when live model access is temporarily unavailable.

When Gemini 3 is reachable, all analyses are generated live.
When it is not, the system transparently switches to demo-sample mode while keeping full UI and orchestration behavior identical.

This approach guarantees stability without misrepresenting functionality.

## Architecture

- **Backend**: FastAPI (Python) with Asyncio
- **AI Layer**: Gemini 3 via `google-genai` SDK + Google Search Grounding with Cached Fallback
- **Frontend**: Vanilla ES6 JS + TailwindCSS (Glassmorphism design)
- **Streaming**: Server-Sent Events (SSE) for real-time agent responses

## Quick Start

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run Application**:
    ```bash
    uvicorn main:app --reload
    ```
    or simply run:
    ```bash
    python main.py
    ```

3.  **Access UI**:
    Open `http://localhost:8000`

## Modules

- `app/api`: API Routes
- `app/agents`: Logic Engines (Logician, Historian, Profiler)
- `app/services`: Orchestrator and Streaming Logic
- `app/tools`: External integrations (Search)
- `app/core`: Config and Logging
