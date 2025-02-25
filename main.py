# main.py

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from config import settings
import os
from agent_logic import ask_ai_agent

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
    text = ask_ai_agent(input_query.query, model="gpt-4o")
    response =  {"message": text}
    
    print(input_query.userId,"get-response END")

    return response