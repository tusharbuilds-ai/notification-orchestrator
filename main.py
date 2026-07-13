import uvicorn
from fastapi import FastAPI
from schemas.return_schema import ApiResponse
from api.routes.api import api_route

app = FastAPI(title="Notification Orchestrator")
app.include_router(api_route,prefix="/api")


@app.get("/")
def home():
    return ApiResponse(
        success=True,
        message="Server up and running"
    )