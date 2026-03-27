from wsgiref import headers


class AuthAPI:
    LOGIN_ENDPOINT = "/login"
    def __init__(self, client):
        self.client = client

    def login(self, payload, headers=None, use_json=True):
        if use_json:
            return self.client.post(self.LOGIN_ENDPOINT, json_data=payload, headers=headers)
        return self.client.post(self.LOGIN_ENDPOINT, data=payload, headers=headers)
    def login_request(self, payload=None,method ="post",headers=None, use_json=True):
        method = method.lower()
        request_method = getattr(self.client, method)
        return request_method(self.LOGIN_ENDPOINT, json_data=payload, headers=headers)
    def get_data(self, payload):
        response = self.login(payload)
        return response,response.json()