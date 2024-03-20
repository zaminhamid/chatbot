

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Any
from gridfs import GridFS
from pymongo import MongoClient

import textract




import os
import tempfile

import PyPDF2



import pandas as pd











from typing import Any, Optional
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch

app = FastAPI()

# Enable CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Response(BaseModel):
    content: Optional[str] = None
    word_count: Optional[int] = None
    answer: Optional[str] = None

@app.post("/predict", response_model=Response)
async def predict(file: UploadFile = File(...), query: str = '') -> Any:
    try:
        # Get the content of the file
        content = get_file_content(file)
        print("File Content:", content)

        # Count the number of words in the content
        word_count = len(content.split())
        print("Word Count:", word_count)

        # Process user query and generate response
        answer = generate_response(content, query)
        print("Generated Answer:", answer)

        return Response(
            content=content,
            word_count=word_count,
            answer=answer
        )
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": str(e)}

# Function to get the content of the uploaded file
def get_file_content(file: UploadFile) -> str:
    content = file.file.read().decode("utf-8")
    file.file.seek(0)  # Reset file pointer after reading
    return content

# Function to generate response to user query using the GPT model
def generate_response(content: str, query: str) -> str:
    # Load GPT model and tokenizer
    model_name = "deepset/gbert-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)

    # Tokenize input
    inputs = tokenizer.encode_plus(query, content, return_tensors="pt", max_length=512, truncation=True)

    # Generate response
    outputs = model(**inputs)
    answer_start_scores = outputs.start_logits
    answer_end_scores = outputs.end_logits

    # Get the most probable answer
    answer_start = torch.argmax(answer_start_scores)
    answer_end = torch.argmax(answer_end_scores) + 1
    answer = tokenizer.decode(inputs["input_ids"][0][answer_start:answer_end])

    return answer

