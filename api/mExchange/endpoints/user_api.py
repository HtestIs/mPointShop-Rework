class ExchangeAuthAPI:
    ME_TEST_ENDPOINT = "/admin/user/me"
    def __init__(self, client):
        self.client = client
 
    def get_info(self, headers=None):
        return self.client.get(self.ME_TEST_ENDPOINT, headers=headers)