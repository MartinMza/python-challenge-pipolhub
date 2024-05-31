import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from src.dataservice import DataService, download_file

load_dotenv()

URL = os.getenv("URL_FILE")


app = FastAPI()

@app.on_event("startup")
async def startup_event():
    download_file(url="https://file.notion.so/f/f/8bdb40ef-cc0d-4853-862c-95ff2b4790ca/b82763a3-3ac0-4c8a-99bb-d763c0b00b54/Data_example_-_Python_Coding_Challenge_-_GraphQL.csv?id=76b87f9a-9e0f-4ca9-bd31-a2b4fd1b0a1d&table=block&spaceId=8bdb40ef-cc0d-4853-862c-95ff2b4790ca&expirationTimestamp=1717257600000&signature=sumM_Jp4r6FPSxCIpIcTPTPWUgjtayUUea2J0enEKbY&downloadName=Data+example+-+Python+Coding+Challenge+-+GraphQL.csv")
    DS = DataService()
    print(DS.get_line(where="id_cli_cliente=4"))
    print(DS.get_multi_lines(where="id_cli_cliente=4"))

    pass
    
@app.get(path="/health", tags=["Health"])
async def health():
    """ This endpoint checks if the server is active. """
    return JSONResponse(content="OK", status_code=200)