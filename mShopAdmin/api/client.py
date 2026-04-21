from core.base.client import APIClient


class MSHopAdminClient(APIClient):
    def __init__(self, base_url, default_headers=None):
        super().__init__(base_url=base_url, default_headers=default_headers)

