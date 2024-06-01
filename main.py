import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from src.graphql import graphql_app

load_dotenv()

app = FastAPI()
    
@app.get(path="/health", tags=["Health"])
async def health():
    """ This endpoint checks if the server is active. """
    return JSONResponse(content="OK", status_code=200)

app.include_router(graphql_app, prefix="/graphql")