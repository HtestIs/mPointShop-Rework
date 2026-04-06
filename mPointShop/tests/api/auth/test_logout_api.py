import pytest
import allure
from mPointShop.api.endpoints.auth_api import AuthAPI
from mPointShop.api.endpoints.store_api import StoreAPI

@pytest.mark.api
@allure.story("Authentication")
@allure.title("Logout API invalidates active session")
@allure.severity(allure.severity_level.NORMAL)
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
