from pydantic import BaseModel, Field

class User(BaseModel):
    username: str
    email: str | None = None

class UserInDB(User):
    hashed_password: str

class UserResquest(User):
    password: str

