class StoreAPI:
    STORE_LIST_ENDPOINT = "/api/v1/store/get-list-retail-stores"
    def __init__(self, client):
        self.client = client
    def get_store_list(self, params=None):
        return self.client.get(self.STORE_LIST_ENDPOINT, params=params)
    def post_store_list(self, data=None):
        return self.client.post(self.STORE_LIST_ENDPOINT, json_data=data)