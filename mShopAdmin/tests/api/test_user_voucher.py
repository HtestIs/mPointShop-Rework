import pytest
import allure
from mShopAdmin.api.endpoints.customer_voucher_api import CustomerVoucherAPI

pytestmark = [
    pytest.mark.mshopadmin,
    allure.parent_suite("mShopAdmin"),
    allure.suite("API"),
    allure.sub_suite("User Vouchers"),
]

@pytest.mark.api
@allure.feature("User Voucher")
@allure.story("Create valid order with voucher")
@allure.title("Create valid order with voucher")
@allure.severity(allure.severity_level.NORMAL)
def test_create_order_valid(app_logged_in_client):
    login = CustomerVoucherAPI(app_logged_in_client)
    payload = {
    "listOrderItems": [
    {
      "type": "voucher",
      "typeId": 146,
      "quantity": 1
        }
    ]
    }
    response = login.create_order(payload = payload)
    login.client.debug_response(response)
    data = response.json()
    code = data["orderItemInfos"][0]["code"]["code"]
    assert response.status_code == 200  
    assert code is not None