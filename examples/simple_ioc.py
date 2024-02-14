"""
Example of using the CaClient to get PV values. Requires the simple IOC server
to be running. Follow steps below to run this example.

1) Run the IOC server with `python -m beemer.ca_servers.simple`
2) Run this example with `python simple_ioc.py`
"""

from beemer import CaClient


def main():
    """
    Run this example.
    """
    client = CaClient()
    values = client.get_pv_values("simple:A", "simple:B", "simple:C")

    for key, value in values.items():
        print(f"PV {key} value is {value}")


if __name__ == "__main__":
    main()
