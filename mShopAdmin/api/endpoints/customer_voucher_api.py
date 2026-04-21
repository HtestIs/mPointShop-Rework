class CustomerVoucherAPI:
    CREATE_ORDER_ENDPOINT = "api/order/create-order"
    GET_CODE_INFO_ENDPOINT = "api/voucher/get-code-info"
    def __init__(self, client):
        self.client = client
    def create_order(self, payload, use_json=True, params=None):
        endpoint = self.CREATE_ORDER_ENDPOINT
        if use_json:
            return self.client.post(endpoint=endpoint, json_data=payload, params=params)
        return self.client.post(endpoint=endpoint, data=payload, params=params)
    def get_code_info(self, payload, use_json=True, params=None):
        endpoint = self.GET_CODE_INFO_ENDPOINT
        if use_json:
            return self.client.post(endpoint=endpoint, json_data=payload, params=params)
        return self.client.post(endpoint=endpoint, data=payload, params=params)