import os
from fastapi import FastAPI,APIRouter, Depends
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from src.graphql import graphql_app
from src.auth import user,auth, validate_auth
from src.dataservice import data
from src.nlp import nlp
from docs.schema import custom_openapi

load_dotenv()

app = FastAPI()
api = APIRouter(prefix="/api")

#app.include_router(graphql_app, prefix="/api/graphql", dependencies=[Depends(validate_auth)])
api.include_router(graphql_app, prefix="/graphql")
api.include_router(user)
api.include_router(data)
api.include_router(nlp)

app.include_router(auth)
app.include_router(api)

@app.on_event("startup")
async def startup_event():
    app.openapi_schema = custom_openapi(app)
    
@app.get(path="/health", tags=["Health"])
async def health():
    """ This endpoint checks if the server is active. """
    return JSONResponse(content="OK", status_code=200)

