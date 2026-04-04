import allure
from selenium.webdriver.common.by import By

from pages.mPointShop.base_page import BasePage
from pages.mPointShop.login_page import LoginPage
from pages.mPointShop.store_manage_page import StoreManage
from pages.mPointShop.voucher_partner_page import VoucherPartnerPage
from pages.mPointShop.warehouse_page import WarehousePage


class MenuPage(BasePage):
    MENU_STORE_MANAGE = (By.CSS_SELECTOR, "div.dashboard-container > div:nth-child(1)")
    MENU_VOUCHER_MANAGE = (By.CSS_SELECTOR, "div.dashboard-container > div:nth-child(4)")
    MENU_WAREHOUSE = (By.CSS_SELECTOR, "div.dashboard-container > div:nth-child(3)")

    BTN_LOG_OUT = (By.XPATH, "//span[text()='Đăng xuất']")
    USER_BLOCK = (By.CSS_SELECTOR, "#cheader > section > div > div.c-header__right > div > a > div")

    @allure.step("Navigate to Store Manager")
    def navigate_to_store_manage(self):
        self.click(self.MENU_STORE_MANAGE)
        return StoreManage(self.driver)

    @allure.step("Navigate to Voucher Manager")
    def navigate_to_voucher_manage(self):
        self.click(self.MENU_VOUCHER_MANAGE)
        return VoucherPartnerPage(self.driver)

    @allure.step("Navigate to Warehouse")
    def navigate_to_warehouse(self):
        self.click(self.MENU_WAREHOUSE)
        return WarehousePage(self.driver)

    @allure.step("Log out")
    def log_out(self):
        self.click(self.USER_BLOCK)
        self.click(self.BTN_LOG_OUT)
        return LoginPage(self.driver)
