from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from datetime import timedelta
from ..models.auth import Token
from ..models.user import User
from ..utils.fake_db import get_db
from ..handler.auth import authenticate_user, create_access_token, validate_auth


fake_users_db = get_db()

auth = APIRouter(prefix="/auth", tags=["Auth"])

@auth.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    """
    Logs in a user and returns an access token.

    Args:
        form_data (OAuth2PasswordRequestForm): The form data containing username and password.

    Returns:
        Token: The access token and its type.

    Raises:
        HTTPException: If the username or password is incorrect.
    """
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@auth.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(validate_auth)],
):
    """
    Retrieves the current authenticated user.

    Args:
        current_user (User): The currently authenticated user.

    Returns:
        User: The user object.
    """
    return current_user