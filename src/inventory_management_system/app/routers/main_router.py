from fastapi import APIRouter

from .example_router import router as example_router

api_router = APIRouter()
api_router.include_router(example_router, tags=["example_router"])
