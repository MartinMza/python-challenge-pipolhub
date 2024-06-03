from fastapi import FastAPI,APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from src.graphql import graphql_app
from src.auth import user,auth, validate_auth
from src.dataservice import data
from src.nlp import nlp
from docs.schema import custom_openapi

load_dotenv()

app = FastAPI()
api = APIRouter(prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["0.0.0.0","127.0.0.1"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api.include_router(graphql_app, prefix="/graphql", dependencies=[Depends(validate_auth)])
api.include_router(user)
api.include_router(data)
api.include_router(nlp, dependencies=[Depends(validate_auth)])

app.include_router(auth)
app.include_router(api)

@app.on_event("startup")
async def startup_event():
    app.openapi_schema = custom_openapi(app)
    
@app.get(path="/health", tags=["Health"])
async def health():
    """
    Health check endpoint.

    Returns:
        JSONResponse: A JSON response indicating the health status.
    """
    return JSONResponse(content="OK", status_code=200)

