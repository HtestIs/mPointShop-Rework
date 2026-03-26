class AuthAPI:
    def __init__(self, client):
        self.client = client

    def login(self, payload, headers=None, use_json=True):
        if use_json:
            return self.client.post("/login", json_data=payload, headers=headers)
        return self.client.post("/login", data=payload, headers=headers)
    def get_data(self,payload):
        response = self.login(payload)
        return response,response.json()