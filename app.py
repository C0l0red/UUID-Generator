from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/uuid")
async def index():
    return "Hello world"