from fastapi import APIRouter,HTTPException,Body
from src.dataservice import DS
from typing import Optional,Union
from ..models.nlp import Question, ResponseModel
from ..handler.chains import nlp_response

nlp = APIRouter(prefix="/nlp", tags=["NLP"])

@nlp.post(path="/question",response_model=ResponseModel, status_code=201)
async def post_question(
    question:Question=Body(
        example=Question(
            text="Necesito que me retornes los datos donde el id del cliente sea igual a 8 y que me de los resultados de id_ga_vista, id_cli_cliente, desc_ga_sku_producto y quiero los primeros 5 resultados",
            context="La información proviene de metricas de e-commerces"
            ))):
    
    """
    NLP endpoint for processing questions.

    Args:
        question (Question): The question to process.

    Returns:
        ResponseModel: The response from the NLP model.
    """
    
    return nlp_response(question=question)