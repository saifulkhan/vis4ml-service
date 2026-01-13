from fastapi import APIRouter

router = APIRouter(prefix="/model", tags=["Model"])


@router.get("/hello")
async def hello_world():
    """
    simple hello world endpoint for model domain.

    returns:
        dict: welcome message from the model api

    example:
        ```json
        {
            "message": "hello world from model api",
            "status": "success"
        }
        ```
    """
    return {"message": "hello world from model api", "status": "success"}
