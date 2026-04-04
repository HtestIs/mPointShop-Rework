import pytest
import allure
from api.mPointShop.api_assertions.menu_assertions import assert_menu_response
from api.mPointShop.endpoints.menu_api import MenuAPI

@pytest.mark.api
@allure.story("Menu access")
@allure.title("Partner can get menu")
@allure.severity(allure.severity_level.NORMAL)
def test_menu_partner_api(logged_in_client_partner):
    menu_api = MenuAPI(client=logged_in_client_partner)
    response = menu_api.get_menu()
    menu_api.client.debug_response(response)
    body = response.json()
    assert_menu_response(body)

@pytest.mark.api
@allure.story("Menu access")
@allure.title("Merchant can get menu")
@allure.severity(allure.severity_level.NORMAL)
def test_menu_merchant_api(logged_in_client_merchant):
    menu_api = MenuAPI(client=logged_in_client_merchant)
    response = menu_api.get_menu()
    menu_api.client.debug_response(response)
    body = response.json()
    assert_menu_response(body)

@pytest.mark.api
@allure.story("Menu access")
@allure.title("Unauthorized menu request returns token error")
@allure.severity(allure.severity_level.NORMAL)
def test_menu_unauthorized(api_client):
    menu_api = MenuAPI(client=api_client)
    response = menu_api.get_menu()
    # menu_api.client.debug_response(response)
    body = response.json()
    assert response.status_code == 401, f"Expected status code 401 for unauthorized access, got {response.status_code}"
    assert body["code"] == 401, f"Expected code 401 for unauthorized access, got {body['code']}"
    assert body["message"] == "Token này đã hết hạn", f"Expected message 'Token này đã hết hạn' for unauthorized access, got {body['message']}"
    assert body["type"] == "ERR_TOKEN_EXPIRED", f"Expected type 'ERR_TOKEN_EXPIRED' for unauthorized access, got {body['type']}"

@pytest.mark.api
@allure.story("Menu access")
@allure.title("Invalid token menu request returns token error")
@allure.severity(allure.severity_level.NORMAL)
def test_menu_invalid_token(api_client):
    menu_api = MenuAPI(client=api_client)
    menu_api.client.set_token("invalid_token")
    response = menu_api.get_menu()
    menu_api.client.debug_response(response)
    body = response.json()
    assert response.status_code == 401, f"Expected status code 401 for unauthorized access, got {response.status_code}"
    assert body["code"] == 401, f"Expected code 401 for unauthorized access, got {body['code']}"
    assert body["message"] == "Token này đã hết hạn", f"Expected message 'Token này đã hết hạn' for unauthorized access, got {body['message']}"
    assert body["type"] == "ERR_TOKEN_EXPIRED", f"Expected type 'ERR_TOKEN_EXPIRED' for unauthorized access, got {body['type']}"