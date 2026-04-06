import json
from time import sleep

from mPointShop.pages.base_page import BasePage
from mPointShop.pages.login_page import LoginPage
from mPointShop.pages.voucher_scan_page import VoucherScan
from mPointShop.pages.store_manage_page import StoreManage
import allure
import pytest

from mPointShop.pages.warehouse_page import WarehousePage

@allure.feature("Login authentication")
@pytest.mark.smoke
class TestsLogin:
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
        
    def test_login_with_api_then_ui(self, driver, auth_api, env_config):
        creds = env_config["users"]["partner"]
        payload = {
            "username": creds["username"],
            "password": creds["password"]
        }
        response, data = auth_api.get_data(payload)
        auth_store = {
            "token": data["data"]["token"]
            }
        # Set token in local storage to simulate logged-in state
        auth = BasePage(driver)
        auth.open()
        auth.dump_token(auth_store)
        auth.refresh_page()
        warehouse_page = WarehousePage(driver)
        assert warehouse_page.get_page_name() == "Quản lý sản phẩm", \
            "Expected 'Quản lý sản phẩm' page to be loaded after setting token, but got '{}'".format(warehouse_page.get_page_name())