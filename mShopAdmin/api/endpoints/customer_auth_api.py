class CustomerLoginAPI:
    LOGIN_ENDPOINT = "api/customer/login-by-password"

    def __init__(self, client):
        self.client = client
    def login(self, payload, use_json=True, params=None):
        endpoint = self.LOGIN_ENDPOINT
        if use_json:
            return self.client.post(endpoint=endpoint, json_data=payload, params=params)
        return self.client.post(endpoint=endpoint, data=payload, params=params)