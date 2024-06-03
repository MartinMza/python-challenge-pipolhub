from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPEN_IA")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

llm_openia_model = OpenAI(temperature=0.2, max_tokens=500, n=2)