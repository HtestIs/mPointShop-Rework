class mExchangeVoucherAPI:
    ENDPOINT = "/admin/voucher/voucher-pool/"
    ADDITIONAL_STORE_ENDPOINT = "/admin/voucher/voucher-pool/commit/"
    SYNC_VOUCHER_ENDPOINT = "/admin/voucher/sync-voucher-to-partner/"
    def __init__(self, client):
        self.client = client
    def get_find_voucher_pools(self, headers=None, params=None):
        return self.client.get(self.ENDPOINT, headers=headers, params=params)
    def post_commit_voucher_pool(self, payload=None, headers=None, use_json=True):
        if use_json:
            return self.client.post(self.ADDITIONAL_STORE_ENDPOINT, json_data=payload, headers=headers)
        return self.client.post(self.ADDITIONAL_STORE_ENDPOINT, data=payload, headers=headers)
    def post_sync_voucher_to_partner(self, payload=None, headers=None, use_json=True):
        if use_json:
            return self.client.post(self.SYNC_VOUCHER_ENDPOINT, json_data=payload, headers=headers)
        return self.client.post(self.SYNC_VOUCHER_ENDPOINT, data=payload, headers=headers)