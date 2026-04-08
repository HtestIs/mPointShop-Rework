from mPointShop.pages.login_page import LoginPage
from mPointShop.pages.voucher_scan_page import VoucherScan
from mPointShop.pages.store_manage_page import StoreManage
import allure
import pytest

pytestmark = [
    pytest.mark.mpointshop,
    allure.parent_suite("mPointShop"),
    allure.suite("E2E"),
    allure.sub_suite("Authentication"),
]

@allure.feature("Login authentication")
@pytest.mark.smoke
class TestsLogin:
    @pytest.mark.e2e
    @allure.story("Successful login")
    @allure.title("Test successful login for merchant")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_success_merchant(self, driver):
        login = LoginPage(driver)
        login.open_url()
        login.fill_login("craftmbeer_1","123456789")
        voucher_scan = VoucherScan(driver)
        assert voucher_scan.is_loaded(), \
            "Voucher scan page is not loaded"


    @pytest.mark.e2e
    @allure.story("Successful login")
    @allure.title("Test successful login for partner")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_success_partner(self, driver):
        login = LoginPage(driver)
        login.open_url()
        login.fill_login("mbeer_partner","123456789")
        storeman = StoreManage(driver)
        assert "Quản lý cửa hàng" in storeman.get_page_name(), \
            "Store manage page is not loaded"



    @pytest.mark.e2e
    @allure.story("Invalid login")
    @allure.title("Test invalid login attempts")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("username,password,message",[
        ("Solaire","123456789","không tồn tại"),
        ("craftmbeer_1","q1232","không đúng"),
        ("","","điền các trường còn thiếu"),
        ("craftmbeer_2","123456789","bị khóa")
    ],
        ids=[
            "User not exist",
            "Wrong password",
            "Empty form",
            "Locked account"
        ]
    )
    def test_login_invalid(self, driver, username, password, message):
        login = LoginPage(driver)
        login.open_url()
        login.fill_login(username,password)
        assert message in login.get_toast_message(),\
            "Toast message is not correct"
        assert "/login" in login.get_current_url(), \
            "User is not on login page after failed login attempt"
        
