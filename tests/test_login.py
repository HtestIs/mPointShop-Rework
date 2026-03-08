from pages.login_page import LoginPage
from pages.voucher_scan_page import VoucherScan
from pages.store_manage_page import StoreManage
import pytest
def test_login_success_merchant(driver,base_url):
    login = LoginPage(driver)
    login.open_url(base_url)
    login.fill_login("craftmbeer_1","123456789")
    voucher_scan = VoucherScan(driver)
    assert voucher_scan.is_loaded()
def test_login_success_partner(driver,base_url):
    login = LoginPage(driver)
    login.open_url(base_url)
    login.fill_login("mbeer_partner","123456789")
    storeman = StoreManage(driver)
    assert "Quản lý cửa hàng" in storeman.get_page_name()
@pytest.mark.parametrize("username,password,message",[
    ("Solaire","123456789","không tồn tại"),
    ("craftmbeer_1","q1232","không đúng"),
    ("","","điền các trường còn thiếu"),
    ("craftmbeer_2","123456789","bị khóa")
])
def test_login_invalid(driver,base_url,username,password,message):
    login = LoginPage(driver)
    login.open_url(base_url)
    login.fill_login(username,password)
    assert message in login.get_toast_message()
    assert "/login" in login.get_current_url()