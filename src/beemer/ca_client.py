"""
A channel access (CA) client to communicate with a CA server.

This requires the CA server to already be running. See the beemer/ca_servers
directory for examples of channel access servers.
"""

from caproto.threading.client import Context


class CaClient:
    def __init__(self) -> None:
        self.ctx = Context()

    def get_pv_values(self, *pvs: str) -> dict[str, object]:
        """
        Get values from PVs.
        """
        values = {}
        pv_objects = self.ctx.get_pvs(*pvs)

        for i, pv in enumerate(pv_objects):
            x = pv.read()

            if x.data_count > 1:
                v = [x for x in x.data]
            else:
                v = x.data[0]

            values[pvs[i]] = v

        return values
