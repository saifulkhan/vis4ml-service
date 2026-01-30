from fastapi import APIRouter
from app.domain.data.api.alphabet import router as alphabet_router

router = APIRouter(prefix="/data", tags=["Data"])


@router.get("/hello")
async def hello_world():
    """
    simple hello world endpoint for data domain.

    returns:
        dict: welcome message from the data api

    example:
        ```json
        {
            "message": "hello world from data api",
            "status": "success"
        }
        ```
    """
    return {"message": "hello world from data api", "status": "success"}

router.include_router(alphabet_router)