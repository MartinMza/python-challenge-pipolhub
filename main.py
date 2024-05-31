from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI()

@app.get(path="/health", tags=["Health"])
async def health():
    """ This endpoint checks if the server is active. """
    return JSONResponse(content="OK", status_code=200)