from ..models.user import UserResquest
from ..handler.user import created_new_user
from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

user = APIRouter(prefix="/user")

@user.post("/new", tags=["Users"])
async def new_user(user: UserResquest = Body()):

    """ Endpoint to creat user"""

    result = await created_new_user(user)

    error = result.get("error", None)

    if not error:
        return JSONResponse(content=result, status_code=201)
    
    return JSONResponse(content=result, status_code=400)