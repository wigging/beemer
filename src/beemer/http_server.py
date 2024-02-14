"""
An HTTP server that uses a CA client to communicate with a CA server.

This requires the CA server to already be running. See the beemer/ca_servers
directory for examples of channel access servers.
"""

import uvicorn
from fastapi import FastAPI
from .ca_client import CaClient

app = FastAPI()
client = CaClient()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/pv_values/{pvs}")
def read_pv_values(pvs: str):
    pv_values = client.get_pv_values(*pvs.split(","))
    return pv_values


if __name__ == "__main__":
    uvicorn.run("beemer.http_server:app")
