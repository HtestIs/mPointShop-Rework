import allure
import pytest

from mExchange.api.endpoints.user_api import ExchangeAuthAPI

pytestmark = [
    pytest.mark.mexchange,
    allure.parent_suite("mExchange"),
    allure.suite("API"),
    allure.sub_suite("Authentication"),
]


@pytest.mark.api
@pytest.mark.e2e
@pytest.mark.defect
@allure.story("Authentication")
@allure.title("Get current mExchange user information")
@allure.severity(allure.severity_level.NORMAL)
def test_mexchange_me(mexchange_client_ui):
    login = ExchangeAuthAPI(client = mexchange_client_ui)
    response = login.get_info()
    data = response.json()
    login.client.debug_response(response)

    assert response.status_code == 200
    assert data is not None