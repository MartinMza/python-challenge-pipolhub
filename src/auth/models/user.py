from pydantic import BaseModel, Field

class User(BaseModel):
    """
    Represents a user.

    Attributes:
        username (str): The username of the user.
        email (str | None): The email address of the user, optional.
    """
    username: str
    email: str | None = None

class UserInDB(User):
    """
    Represents a user stored in the database.

    Inherits from User and adds the hashed password attribute.

    Attributes:
        hashed_password (str): The hashed password of the user.
    """
    hashed_password: str

class UserRequest(User):
    """
    Represents a user request.

    Inherits from User and adds the plain text password attribute.

    Attributes:
        password (str): The plain text password of the user.
    """
    password: str