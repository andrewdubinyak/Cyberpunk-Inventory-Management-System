from fastapi import APIRouter

router = APIRouter()


@router.get("/example/")
async def example_get():
    pass
