import requests
class APIClient:
    def __init__(self,base_url,default_headers=None):
        self.base_url = base_url
        self.session = requests.Session()
        if default_headers:
            self.session.headers.update(default_headers)
    def get(self,endpoint,params=None,headers=None):
        url = self.base_url + endpoint
        response = self.session.get(url,params=params,headers=headers)
        return response
    def post(self,endpoint,data=None,json_data=None,headers=None):
        url = self.base_url + endpoint
        response = self.session.post(url,data=data,json=json_data,headers=headers)
        return response
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