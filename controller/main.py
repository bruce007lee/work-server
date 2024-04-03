from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/")
async def main():
    return HTMLResponse("working")
