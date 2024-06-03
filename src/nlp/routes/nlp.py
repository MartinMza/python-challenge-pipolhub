from fastapi import APIRouter,HTTPException,Body
from src.dataservice import DS
from typing import Optional,Union
from ..models.nlp import Question, ResponseModel
from ..handler.chains import nlp_response

nlp = APIRouter(prefix="/nlp", tags=["NLP"])

@nlp.post(path="/question",response_model=ResponseModel, status_code=201)
async def post_question(question:Question=Body()):
    return nlp_response(question=question)