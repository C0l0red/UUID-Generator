import uvicorn
import base64

from fastapi import FastAPI
from redis import StrictRedis
from uuid import uuid4
from datetime import datetime

app = FastAPI()

ENCODED_REDIS_PASSWORD = b'T01iRXlZZjFtbXZ6aTlSOWN0eXVkQ3BxYkxpU2JmYjE='
REDIS_PASSWORD = base64.b64decode(ENCODED_REDIS_PASSWORD).decode("ascii")

r = StrictRedis(host="redis-12313.c267.us-east-1-4.ec2.cloud.redislabs.com",
                password=REDIS_PASSWORD,
                port=12313,
                db=0,
                decode_responses=True) 
                # using StrictRedis to allow decode the results from bytes to string

@app.get("/")
async def index():
    date = str(datetime.now())
    uuid = str(uuid4())

    r.hset("uuids", date, uuid)
    uuids = r.hgetall("uuids")

    response = dict(reversed(uuids.items())) # reverses the dictionary

    return response

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000)#, reload=True) #reload can be turned on