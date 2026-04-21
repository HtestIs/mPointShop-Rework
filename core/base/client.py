import requests


class APIClient:
    def __init__(self, base_url, default_headers=None):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.token = None

        if default_headers:
            self.session.headers.update(default_headers)

    def set_token(self, token):
        self.token = token
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Accept": "application/json"
        })
    def set_x_access_token(self, token):
        self.token = token
        self.session.headers.update({
            "X-Access-Token": token,
            "Accept": "application/json"
        })
    def get(self, endpoint, params=None, data=None, json_data=None, headers=None):
        url = self.base_url + "/" + endpoint.lstrip("/")
        response = self.session.get(
            url,
            params=params,
            data=data,
            json=json_data,
            headers=headers
        )
        return response

    def post(self, endpoint, data=None, json_data=None, headers=None, params=None):
        url = self.base_url + "/" + endpoint.lstrip("/")
        response = self.session.post(
            url,
            data=data,
            json=json_data,
            headers=headers,
            params=params
        )
        return response

    def patch(self, endpoint, data=None, json_data=None, headers=None, params=None):
        url = self.base_url + "/" + endpoint.lstrip("/")
        response = self.session.patch(
            url,
            data=data,
            json=json_data,
            headers=headers,
            params=params
        )
        return response

    def set_key_app(self, key="mcoffee"):
        self.session.headers.update({
            "x-keyapp": key
        })
    @staticmethod
    def debug_response(response):
        print("\n========== API DEBUG ==========")
        print("REQUEST METHOD:", response.request.method)
        print("REQUEST URL:", response.request.url)
        print("REQUEST HEADERS:", dict(response.request.headers))
        print("REQUEST BODY:", response.request.body)
        print("STATUS CODE:", response.status_code)
        print("RESPONSE TEXT:", response.text)
        print("================================\n")