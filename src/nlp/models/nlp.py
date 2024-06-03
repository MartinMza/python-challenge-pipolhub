from pydantic import BaseModel, Field
from typing import Optional

class Question(BaseModel):
    text: str = Field(max_length=200, min_length=5)
    context: Optional[str] = Field(default=None,max_length=200, min_length=5)

class ResponseModel(BaseModel):
    response: str 
