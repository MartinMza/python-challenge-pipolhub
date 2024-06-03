from langchain.chains import LLMChain
from langchain_core.language_models.llms import LLM
from ..utils.templates import prompt_response, prompt_sql_query
from ..models.nlp import Question, ResponseModel
from ..models.openia import llm_openia_model as llm_model
from src.dataservice import DS



def _remove_character(query:str)->str:
    """ Remove characters """
    return query.replace("\n", " ").replace(";","")

# Return a sql expresion 
chain_sql_query = LLMChain(
    llm = llm_model,
    prompt=prompt_sql_query,
    output_key="sql_query"
)

chain_response_user = LLMChain(
    llm = llm_model,
    prompt=prompt_response,
    output_key="response"
)

def nlp_response(question:Question)->str:
    """ Model NLP Response """

    columns= DS.lazy_frame.columns
    sql_query = chain_sql_query.invoke({"columns":columns, "text":question.text})
    sql_query = _remove_character(sql_query.get("sql_query"))
    print(sql_query)
    data_result = DS.get_multi_lines_by_query(query=sql_query)
    response = chain_response_user.invoke({"columns":columns,"data": data_result, "context":question.context, "text":question.text})
    
    return ResponseModel(response=response.get("response"))

