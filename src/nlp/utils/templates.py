from langchain_core.prompts import PromptTemplate

template_sql = """ Debe de manera imperativa devolver la siguiente consulta como si se tratara de una consulta SQL, tienes que tener encuenta las siguientes restricciones. Si no se puede formular como una consulta SQL retornar un string vacio ejemplo: "", Segun corresponda y no se expecifica un LIMIT el por defecto debe ser 5 y como maximo 10, solo si se requiere retornar campos de informacion :

campos tabla: {columns}
tabla: self

consulta: {text}

"""

template_respuesta_nlp = """ Debera responder de manera natural para que un usuario humano entienda los datos proporcionados en el campo 'data' que es el resultado de la busqueda en una base de datos según lo requerido en la pregunta. A continuación formule una respuesta con la información dada, es libre de interpretar los datos:
datos : {data}
contexto : {context}
pregunta : {text}

"""

prompt_sql_query = PromptTemplate(
    template = template_sql,
    input_variables=["columns","text"]
)

prompt_response = PromptTemplate(
    template = template_respuesta_nlp,
    input_variables=["data","columns","context","text"]
)