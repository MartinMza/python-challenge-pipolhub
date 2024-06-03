from ..models.user import UserRequest
from ..handler.user import created_new_user
from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

user = APIRouter(prefix="/user")

@user.post("/new", tags=["Users", "Auth"])
async def new_user(user: UserRequest = Body(
    example=UserRequest(username="Juan1", email="j@j.com", password="abc123"))):
    """
    Endpoint to create a new user.

    Args:
        user (UserRequest): The user request object containing user details.

    Returns:
        JSONResponse: A JSON response with a success or error message.
    """
    result = await created_new_user(user)

    error = result.get("error", None)

    if not error:
        return JSONResponse(content=result, status_code=201)
    
    return JSONResponse(content=result, status_code=400)