class VoucherAPI:
    FIND_ENDPOINT = "api/admin/application/voucher/find-application-voucher"
    UPDATE_ENDPOINT ="api/admin/application/voucher/update-app-voucher/"
    def __init__(self, client):
        self.client = client
    def find_voucher(self, params=None):
        return self.client.get(endpoint=self.FIND_ENDPOINT, params=params)
    def update_voucher(self, voucher_id, payload, use_json=True, params=None):
        endpoint = self.UPDATE_ENDPOINT + str(voucher_id)
        if use_json:
            return self.client.patch(endpoint=endpoint, json_data=payload, params=params)
        return self.client.patch(endpoint=endpoint, data=payload, params=params)