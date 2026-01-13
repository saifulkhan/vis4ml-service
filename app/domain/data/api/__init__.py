from fastapi import APIRouter

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
