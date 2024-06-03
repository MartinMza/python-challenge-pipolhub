from pydantic import BaseModel

class Token(BaseModel):
    """
    Represents an authentication token.

    Attributes:
        access_token (str): The access token string.
        token_type (str): The type of the token, typically "Bearer".
    """
    access_token: str
    token_type: str

class TokenData(BaseModel):
    """
    Represents the data contained within a token.

    Attributes:
        username (str | None): The username associated with the token, or None if not available.
    """
    username: str | None = None