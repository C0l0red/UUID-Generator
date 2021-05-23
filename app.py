from fastapi import FastAPI
from redis import StrictRedis
# from typing import Optional

app = FastAPI()

r = StrictRedis()

@app.get("/uuid")
async def index():

    return "Hello world"