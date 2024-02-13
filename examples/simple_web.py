"""
Example of using the WebClient to get PV values. Requires the simple IOC
server and web server to be running. Follow steps below to run this example.

1) Run the IOC server with `python -m beemer.ioc_servers.simple`
2) Run the web server with `python -m beemer.web_server`
3) Run this example with `python simple_web.py`
"""

from beemer import WebClient


def main():
    """
    Run this example.
    """
    client = WebClient("http://127.0.0.1:8000")
    values = client.get_pv_values("simple:A", "simple:B", "simple:C")

    for key, value in values.items():
        print(f"PV {key} value is {value}")


if __name__ == "__main__":
    main()
