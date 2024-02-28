"""
Example of using the `CaClient` class to get PV values. Requires the simple
IOC server from `simple_ioc.py` to be running. Follow the steps below to run
this example.

1) Run the IOC server with `python simple_ioc.py`
2) Run this example with `python simple_caclient.py`
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
