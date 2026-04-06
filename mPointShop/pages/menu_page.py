import allure
from selenium.webdriver.common.by import By

from mPointShop.pages.base_page import BasePage
from mPointShop.pages.login_page import LoginPage
from mPointShop.pages.store_manage_page import StoreManage
from mPointShop.pages.voucher_partner_page import VoucherPartnerPage
from mPointShop.pages.warehouse_page import WarehousePage


class MenuPage(BasePage):
# URL (this one is required, admin can change the default menu, but the URL should remain the same for each page)
    STORE_URL = "/manager/store-manager"
    VOUCHER_URL = "/manager/voucher-manager"
    WAREHOUSE_URL = "/manager/warehouse-manager"
# LOCATORS
    MENU_STORE_MANAGE = (By.CSS_SELECTOR, "div.dashboard-container > div:nth-child(1)")
    MENU_VOUCHER_MANAGE = (By.CSS_SELECTOR, "div.dashboard-container > div:nth-child(4)")
    MENU_WAREHOUSE = (By.CSS_SELECTOR, "div.dashboard-container > div:nth-child(3)")
    BTN_LOG_OUT = (By.XPATH, "//span[text()='Đăng xuất']")
    USER_BLOCK = (By.CSS_SELECTOR, "#cheader > section > div > div.c-header__right > div > a > div")
    @allure.step("Navigate to Store Manager")
    def navigate_to_store_manage(self):
        self.open(self.STORE_URL)
        return StoreManage(self.driver)

    @allure.step("Navigate to Voucher Manager")
    def navigate_to_voucher_manage(self):
        self.open(self.VOUCHER_URL)
        return VoucherPartnerPage(self.driver)

    @allure.step("Navigate to Warehouse")
    def navigate_to_warehouse(self):
        self.open(self.WAREHOUSE_URL)
        return WarehousePage(self.driver)

    @allure.step("Log out")
    def log_out(self):
        self.click(self.USER_BLOCK)
        self.click(self.BTN_LOG_OUT)
        return LoginPage(self.driver)
