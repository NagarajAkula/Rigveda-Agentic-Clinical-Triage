from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class TriageRequest(BaseModel):
    symptoms: str
    patient_id: str

class TriageResponse(BaseModel):
    triage_level: str
    recommendation: str

@app.post("/triage")
async def clinical_triage(request: TriageRequest):
    """Clinical triage endpoint for Rigveda Health AGI"""
    return TriageResponse(
        triage_level="moderate",
        recommendation="Consult healthcare provider"
    )

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)