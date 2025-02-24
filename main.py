# main.py

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from config import settings
import cohere
import qdrant_client
from qdrant_client.models import Batch
from qdrant_client import QdrantClient, models
from qdrant_client.http.models import PointStruct
import os

app = FastAPI()

class InputQuery(BaseModel):
    query: str
    language: str
    userId: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/get-response/")
async def get_response(input_query: InputQuery):
    print(input_query.userId,"get-response INIT")
    print(input_query.userId,"get-response Query: ",input_query.query)
    print(settings.COHERE_API_KEY)
    cohere_client = cohere.Client(settings.COHERE_API_KEY)
    client = qdrant_client.QdrantClient(
        url=settings.QDRANT_URL, 
        api_key=settings.QDRANT_API_KEY,
    )
    embeddings_retrieved = client.search(
        collection_name=settings.QDRANT_COLLECTION,
        query_vector=cohere_client.embed(
            model="embed-multilingual-v3.0",  # New Embed v3 model
            input_type="search_query",  # Input type for search queries
            texts=[input_query.query],
        ).embeddings[0],
    )
    print(input_query.userId,"get-response END")

    return embeddings_retrieved