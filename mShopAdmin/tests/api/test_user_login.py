import pytest
import allure

from mShopAdmin.api.endpoints.customer_auth_api import CustomerLoginAPI

pytestmark = [
    pytest.mark.mshopadmin,
    allure.parent_suite("mShopAdmin"),
    allure.suite("API"),
    allure.sub_suite("User Login"),
]

@pytest.mark.api
@allure.feature("User Login")
@allure.story("Valid user login")
@allure.title("User can login with valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_login_user(app_api_client,env_config):
    app_api_client.set_key_app()
    login = CustomerLoginAPI(app_api_client)
    payload = {
        "phone": env_config["app_username"],
        "password": env_config["app_password"]
    }
    response = login.login(payload = payload)
    data = response.json()
    login.client.debug_response(response)
    assert response.status_code == 200
    assert data["accessToken"] is not None