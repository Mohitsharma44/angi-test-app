from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator

VERSION = "0.0.2"

app = FastAPI()
Instrumentator(excluded_handlers=["/metrics"]).instrument(app).expose(app)

@app.get("/healthz")
async def health():
    return {"message": "OK"}

@app.get("/")
async def root():
    # raise HTTPException(status_code=404)
    return {"Version": VERSION}
