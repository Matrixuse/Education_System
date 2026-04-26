"""
Multi-Agent Education System — FastAPI Backend
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import json
import os
from dotenv import load_dotenv
from agents import EducationOrchestrator

load_dotenv()

app = FastAPI(title="Multi-Agent Education System API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:3001",
        "http://127.0.0.1:3001",
        "https://education-system-vib8.onrender.com",
        "http://65.2.144.13:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GenerateRequest(BaseModel):
    topic: str
    depth: str = "intermediate"
    model: str = "llama-3.3-70b-versatile"


@app.get("/")
def root():
    return {"status": "running", "service": "Multi-Agent Education System"}


@app.post("/generate")
async def generate(req: GenerateRequest):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="GROQ_API_KEY not set in .env file")

    if not req.topic.strip():
        raise HTTPException(status_code=400, detail="Topic is required")

    try:
        orchestrator = EducationOrchestrator(groq_api_key=api_key, model=req.model)
        state = orchestrator.run(req.topic.strip(), req.depth)
        return {
            "topic": state["topic"],
            "depth": state["depth"],
            "final_output": state["final_output"],
            "handoff_log": state["handoff_log"],
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate/stream")
async def generate_stream(req: GenerateRequest):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="GROQ_API_KEY not set in .env file")

    if not req.topic.strip():
        raise HTTPException(status_code=400, detail="Topic is required")

    def event_stream():
        try:
            orchestrator = EducationOrchestrator(groq_api_key=api_key, model=req.model)

            def on_update(msg, state):
                data = json.dumps({"type": "status", "message": msg, "log": state["handoff_log"][-1] if state["handoff_log"] else ""})
                yield f"data: {data}\n\n"

            # Manual pipeline for streaming events
            from agents import EducationState

            state: EducationState = {
                "topic": req.topic.strip(),
                "depth": req.depth,
                "raw_research": "",
                "structured_content": "",
                "final_output": "",
                "handoff_log": ["[Orchestrator] Pipeline initialized."],
            }

            yield f"data: {json.dumps({'type': 'status', 'message': 'researcher_start'})}\n\n"
            state = orchestrator.researcher.research(state)
            yield f"data: {json.dumps({'type': 'status', 'message': 'researcher_done'})}\n\n"

            yield f"data: {json.dumps({'type': 'status', 'message': 'writer_start'})}\n\n"
            state = orchestrator.writer.write(state)
            state["final_output"] = state["structured_content"]
            state["handoff_log"].append("[Orchestrator] Pipeline complete.")
            yield f"data: {json.dumps({'type': 'status', 'message': 'writer_done'})}\n\n"

            result = json.dumps({
                "type": "result",
                "topic": state["topic"],
                "depth": state["depth"],
                "final_output": state["final_output"],
                "handoff_log": state["handoff_log"],
            })
            yield f"data: {result}\n\n"
            yield "data: [DONE]\n\n"

        except Exception as e:
            yield f"data: {json.dumps({'type': 'error', 'message': str(e)})}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")