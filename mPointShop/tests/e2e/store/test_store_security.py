import pytest
import allure
from time import sleep
from mPointShop.api.endpoints.store_api import StoreAPI

pytestmark = [
    pytest.mark.mpointshop,
    allure.parent_suite("mPointShop"),
    allure.suite("E2E"),
    allure.sub_suite("Store Security"),
]

@pytest.mark.e2e
@pytest.mark.security
@allure.story("Changing store password")
@allure.title("Change store password")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("password,toast",[
    ("123456789","Thành công"),
    ("","Vui lòng điền"),
    ])
def test_change_store_password(login_partner_success,password,toast):
    menu = login_partner_success
    page = menu.navigate_to_store_manage()
    page.change_password(password)
    assert toast in page.get_toast_msg()


@pytest.mark.e2e
@pytest.mark.security
@allure.story("Locking stores")
@allure.title("Lock store")
@allure.severity(allure.severity_level.CRITICAL)
def test_lock_store(login_partner_success,mpointshop_logged_in_client_partner,store_api_data):
    store_api = StoreAPI(client=mpointshop_logged_in_client_partner)
    payload = store_api_data.copy()
    store_api.create_store(payload=payload)
    menu = login_partner_success
    page = menu.navigate_to_store_manage()
    page.toggle_store()
    locked_username = page.get_first_store_username_from_edit_modal()
    page.hover_user()
    login = page.click_logout()
    login.fill_login(locked_username,payload["password"])
    assert "Tài khoản đang bị khóa!" in login.get_toast_message()
    assert "/login" in login.get_current_url()