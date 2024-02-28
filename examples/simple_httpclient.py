"""
Example of using the `HttpClient` class to get PV values. Requires the simple
IOC server from `simple_ioc.py` to be running and the web server to be
running. Follow the steps below to run this example.

1) Run the IOC server with `python simple_ioc.py`
2) Run the web server with `python -m beemer.http_server`
3) Run this example with `python simple_httpclient.py`
"""

from beemer import HttpClient


def main():
    """
    Run this example.
    """
    client = HttpClient("http://127.0.0.1:8000")

    status = client.get_status()
    print("Status is", status)

    values = client.get_pv_values("simple:A", "simple:B", "simple:C")

    for key, value in values.items():
        print(f"PV {key} value is {value}")


if __name__ == "__main__":
    main()
