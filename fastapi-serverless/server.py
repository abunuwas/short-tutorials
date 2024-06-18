import os

from fastapi import FastAPI
from mangum import Mangum

server = FastAPI(openapi_prefix="/dev")


@server.get("/hello")
def hello():
    return {"message": "hello!"}


@server.get("/env")
def env():
    return {"message": os.environ.get("ENV_VARIABLE", "ENV_VARIABLE NOT SET")}


handler = Mangum(server)
