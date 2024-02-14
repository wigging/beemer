"""
An HTTP client to communicate with a HTTP server.

This requires the HTTP server to already be running. See the
beemer/http_server module to run the server.
"""

import httpx


class HttpClient:
    def __init__(self, url) -> None:
        self.url = url

    def get_pv_values(self, *pvs: str) -> dict[str, object]:
        """
        Get values from PVs.
        """
        pvs_string = ",".join(pvs)
        response = httpx.get(f"{self.url}/pv_values/{pvs_string}")
        return response.json()
