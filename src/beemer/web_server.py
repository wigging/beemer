"""
Web server using uvicorn and API built with fastapi. Requires the IOC server
to already be running.
"""

import uvicorn
from fastapi import FastAPI
from .ioc_client import IocClient

app = FastAPI()
client = IocClient()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/pv_values/{pvs}")
def read_pv_values(pvs: str):
    pv_values = client.get_pv_values(*pvs.split(","))
    return pv_values


if __name__ == "__main__":
    uvicorn.run("beemer.web_server:app")
