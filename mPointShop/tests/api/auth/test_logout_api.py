import pytest
import allure

pytestmark = [
    pytest.mark.mpointshop,
    allure.parent_suite("mPointShop"),
    allure.suite("API"),
    allure.sub_suite("Authentication"),
]

@pytest.mark.api
@allure.story("Authentication")
@allure.title("Logout API invalidates active session")
@allure.severity(allure.severity_level.NORMAL)
def test_logout_api(mpointshop_auth_api,env_config):
    creds = env_config["users"]["partner"]
    payload = {
        "username": creds["username"],
        "password": creds["password"]
    }
    # First, log in to get a valid token
    data, response_json = mpointshop_auth_api.get_data(payload)
    # mpointshop_auth_api.client.debug_response(data)
    old_token = response_json["data"]["token"]
    mpointshop_auth_api.logout()
