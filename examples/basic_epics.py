"""
Example of using the `CaClient` class to get PV values from the EPICS Docker
container. Follow the steps below to run the container and this example.

1) Start up Docker
2) Follow steps in the Dockerfile to run the EPICS container
3) Run this example with `python basic_epics.py`
"""

from beemer import CaClient


def main():
    """
    Run this example.
    """
    client = CaClient()
    values = client.get_pv_values("water", "air")

    for key, value in values.items():
        print(f"PV {key} value is {value}")


if __name__ == "__main__":
    main()
