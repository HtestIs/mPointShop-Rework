import pytest
import allure
@pytest.mark.security
@allure.story("Changing store password")
@allure.title("Change store password")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("password,toast",[
    ("123456789","Thành công"),
    ("","Vui lòng nhập"),
    ])
def test_change_store_password(login_partner_success,password,toast):
    menu = login_partner_success
    page = menu.navigate_to_store_manage()
    page.change_password(password)
    assert toast in page.get_toast_msg()


@pytest.mark.security
@allure.story("Locking stores")
@allure.title("Lock store")
@allure.severity(allure.severity_level.CRITICAL)
def test_lock_store(login_partner_success):
    menu = login_partner_success
    page = menu.navigate_to_store_manage()
    page.ensure_locked()
    locked_username = page.get_first_store_username_from_edit_modal()
    page.hover_user()
    login = page.click_logout()
    login.fill_login(locked_username,"1")
    assert "Tài khoản đang bị khóa!" in login.get_toast_message()
    assert "/login" in login.get_current_url()