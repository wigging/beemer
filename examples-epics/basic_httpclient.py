"""
Example of using the `HttpClient` class to get PV values from the EPICS Docker
container via HTTP requests. Follow the steps below to run the container,
HTTP server, and this example.

1) Start up Docker
2) Follow steps in the Dockerfile to run the EPICS container
3) Run the HTTP server with `python -m beemer.http_server`
4) Run this example with `python basic_httpclient.py`
"""

from beemer import HttpClient


def main():
    """
    Run this example.
    """
    client = HttpClient("http://127.0.0.1:8000")

    status = client.get_status()
    print("Status is", status)

    values = client.get_pv_values("water", "air")

    for key, value in values.items():
        print(f"PV {key} value is {value}")


if __name__ == "__main__":
    main()
