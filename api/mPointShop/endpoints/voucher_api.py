class VoucherAPI:
    VOUCHER_ENDPOINT = "/api/v1/store/voucher/create-voucher"
    ADD_STORE_TO_VOUCHER_ENDPOINT = "/api/v1/store/voucher/choose-stores-apply"
    SYNC_VOUCHER_TO_MEXCHANGE_ENDPOINT = "/api/v1/store/voucher/sync-voucher"
    def __init__(self, client):
        self.client = client
    def create_voucher(self, payload, headers=None, use_json=True):
        if use_json:
            return self.client.post(self.VOUCHER_ENDPOINT, json_data=payload, headers=headers)
        return self.client.post(self.VOUCHER_ENDPOINT, data=payload, headers=headers)
    
    def add_store_to_voucher(self, payload, headers=None, use_json=True):
        if use_json:
            return self.client.post(self.ADD_STORE_TO_VOUCHER_ENDPOINT, json_data=payload, headers=headers)
        return self.client.post(self.ADD_STORE_TO_VOUCHER_ENDPOINT, data=payload, headers=headers)
    def sync_voucher_to_mexchange(self, payload, headers=None, use_json=True):
        if use_json:
            return self.client.post(self.SYNC_VOUCHER_TO_MEXCHANGE_ENDPOINT, json_data=payload, headers=headers)
        return self.client.post(self.SYNC_VOUCHER_TO_MEXCHANGE_ENDPOINT, data=payload, headers=headers)