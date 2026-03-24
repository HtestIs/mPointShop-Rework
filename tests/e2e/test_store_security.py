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
    login_partner_success.change_password(password)
    assert toast in login_partner_success.get_toast_msg()


@pytest.mark.security
@allure.story("Locking stores")
@allure.title("Lock store")
@allure.severity(allure.severity_level.CRITICAL)
def test_lock_store(login_partner_success):
    login_partner_success.ensure_locked()
    locked_username = login_partner_success.get_first_store_username_from_edit_modal()
    login_partner_success.hover_user()
    login = login_partner_success.click_logout()
    login.fill_login(locked_username,"1")
    assert "Tài khoản đang bị khóa!" in login.get_toast_message()
    assert "/login" in login.get_current_url()