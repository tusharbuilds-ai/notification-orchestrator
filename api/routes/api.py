from fastapi import APIRouter
from api.routes import job


api_route = APIRouter()


api_route.include_router(job.router,prefix="/post_job")