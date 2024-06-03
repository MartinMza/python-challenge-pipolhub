from pydantic import BaseModel, Field
from typing import Optional

class Question(BaseModel):
    """
    Represents a question for NLP processing.

    Attributes:
        text (str): The text of the question.
        context (Optional[str]): The context of the question.
    """
    text: str = Field(..., max_length=200, min_length=5)
    context: Optional[str] = Field(None, max_length=200, min_length=5)

class ResponseModel(BaseModel):
    """
    Represents a response from the NLP model.

    Attributes:
        response (str): The response text.
    """
    response: str