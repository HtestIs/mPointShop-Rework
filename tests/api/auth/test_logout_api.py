import pytest
from api.endpoints.auth_api import AuthAPI
from api.endpoints.store_api import StoreAPI

@pytest.mark.ongoing
def test_logout_api(auth_api,env_config):
    creds = env_config["users"]["partner"]
    payload = {
        "username": creds["username"],
        "password": creds["password"]
    }
    # First, log in to get a valid token
    data, response_json = auth_api.get_data(payload)
    # auth_api.client.debug_response(data)
    old_token = response_json["data"]["token"]
    auth_api.logout()
