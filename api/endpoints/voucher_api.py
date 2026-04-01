class VoucherAPI:
    VOUCHER_ENDPOINT = "/api/v1/store/voucher/create-voucher"
    def __init__(self, client):
        self.client = client
    def create_voucher(self, payload, headers=None, use_json=True):
        if use_json:
            return self.client.post(self.VOUCHER_ENDPOINT, json_data=payload, headers=headers)
        return self.client.post(self.VOUCHER_ENDPOINT, data=payload, headers=headers)
