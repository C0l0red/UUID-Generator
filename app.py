from fastapi import FastAPI
from redis import StrictRedis
from uuid import uuid4
from datetime import datetime

app = FastAPI()

r = StrictRedis(decode_responses=True)

@app.get("/uuid")
async def index():
    date = str(datetime.now())
    uuid = str(uuid4())

    r.hset("uuids", date, uuid)
    uuids = r.hgetall("uuids")

    response = dict(reversed(uuids.items()))

    return response