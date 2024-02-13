"""
Web client for interacting with the web server. Requires the IOC server and
web server to already be running.
"""

import httpx


class WebClient:
    def __init__(self, url) -> None:
        self.url = url

    def get_pv_values(self, *pvs: str) -> dict[str, object]:
        """
        Get values from PVs.
        """
        pvs_string = ",".join(pvs)
        response = httpx.get(f"{self.url}/pv_values/{pvs_string}")
        return response.json()
