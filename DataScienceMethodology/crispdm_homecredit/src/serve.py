from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(title="CRISPDM HomeCredit Scorer")

class ScoreRequest(BaseModel):
    features: dict

@app.post("/score")
def score(req: ScoreRequest):
    # TODO: load model & transform
    return {"prob_default": 0.123, "note": "stub - replace with real model"}
