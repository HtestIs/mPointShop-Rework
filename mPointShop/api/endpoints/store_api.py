import random
class StoreAPI:
    STORE_LIST_ENDPOINT = "/api/v1/store/get-list-retail-stores"
    STORE_CREATE_ENDPOINT = "/api/v1/store/sub-store/create-sub-store"
    STORE_SEARCH_ENDPOINT = "/api/v1/store/sub-store/get-sub-store"
    def __init__(self, client):
        self.client = client
    def get_store_list(self, params=None):
        return self.client.get(self.STORE_LIST_ENDPOINT, params=params)
    def post_store_list(self, payload=None, headers=None, use_json=True):
        if use_json:
            return self.client.post(self.STORE_LIST_ENDPOINT, json_data=payload, headers=headers)
        return self.client.post(self.STORE_LIST_ENDPOINT, data=payload, headers=headers)
    def post_store(self, payload=None, headers=None, use_json=True):
        if use_json:
            return self.client.post(self.STORE_LIST_ENDPOINT, json_data=payload, headers=headers)
        return self.client.post(self.STORE_LIST_ENDPOINT, data=payload, headers=headers)
    def create_store(self, payload, headers=None, use_json=True):
        if use_json:
            return self.client.post(self.STORE_CREATE_ENDPOINT, json_data=payload, headers=headers)
        return self.client.post(self.STORE_CREATE_ENDPOINT, data=payload, headers=headers)
    def search_store(self,payload, headers=None, use_json=True):
        if use_json:
            return self.client.post(self.STORE_SEARCH_ENDPOINT, json_data=payload, headers=headers)
        return self.client.post(self.STORE_SEARCH_ENDPOINT, data=payload, headers=headers)