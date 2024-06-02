import os
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from src.graphql import graphql_app
from src.auth import user,auth, validate_auth

load_dotenv()

app = FastAPI()
    
@app.get(path="/health", tags=["Health"])
async def health():
    """ This endpoint checks if the server is active. """
    return JSONResponse(content="OK", status_code=200)

#app.include_router(graphql_app, prefix="/api/graphql", dependencies=[Depends(validate_auth)])
app.include_router(graphql_app, prefix="/api/graphql")
app.include_router(user, prefix="/api")
app.include_router(auth, prefix="/api")
