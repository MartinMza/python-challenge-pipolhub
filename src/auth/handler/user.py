from ..models.user import UserInDB, UserRequest
from .auth import get_password_hash
from ..utils.fake_db import get_db, update_db


async def created_new_user(user: UserRequest)->dict:

    """
    Create a new user and update the fake DB.

    Args:
        user (UserRequest): The user request object containing user details.

    Returns:
        dict: A dictionary with a success message or an error message.
    """

    try:

        fake_users_db = get_db()
        
        exist_user = fake_users_db.get(user.username, None)

        if exist_user:
            return {"error":"exist user in the db"}

        hash_password = get_password_hash(user.password)

        user_db = {user.username: UserInDB(username=user.username,email=user.email, hashed_password=hash_password).model_dump()}
        
        update_db(user_db,fake_users_db)

        return {"message": "User was created"}
    
    except Exception as e:

        return {"error": str(e)}