from langchain_core.prompts import PromptTemplate

template_sql = """ 
You must imperatively return the following query as an SQL query, considering the given constraints. 
If it cannot be formulated as an SQL query, return an empty string (""). 
By default, the LIMIT should be 5 if not specified, with a maximum of 10, only if it is required to return fields of information:

- **Table Schema:** {schema}
- **Table Name:** self
- **Query:** {text}
"""

template_respuesta_nlp = """ You should respond naturally so that a human user can understand the data provided in the 'data' field, which is the result of a database search based on the question asked. 
Formulate a response using the given information, and feel free to interpret the data:

- **Data:** {data}
- **Context:** {context}
- **Question:** {text}

"""

prompt_sql_query = PromptTemplate(
    template = template_sql,
    input_variables=["schema","text"]
)

prompt_response = PromptTemplate(
    template = template_respuesta_nlp,
    input_variables=["data","context","text"]
)