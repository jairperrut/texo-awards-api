from fastapi import APIRouter

from awards_api.api import awards

api_routers = APIRouter(prefix="/api")

api_routers.include_router(router=awards.router, tags=["Awards"])
