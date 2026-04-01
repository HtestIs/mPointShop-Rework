import pytest
import allure
from api.endpoints.auth_api import AuthAPI
from api.endpoints.store_api import StoreAPI

@pytest.mark.api
<<<<<<< HEAD
@allure.story("Authentication")
@allure.title("Logout API invalidates active session")
@allure.severity(allure.severity_level.NORMAL)
=======
>>>>>>> 82f30fe4029a5d311e8a853e934c4bf1e1af1b8d
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
