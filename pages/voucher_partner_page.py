import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from datetime import datetime

class VoucherPartnerPage(BasePage):
    URL = "/manager/voucher-manager"
    
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Tên voucher']")
    ROW = (By.XPATH, "//table//tbody//tr")
    ROW_VOUCHER_NAME = (By.XPATH, ".//td[2]")
    @allure.step("Open voucher manager page")
    def open_url(self, base_url):
        self.open(base_url + self.URL)
    @allure.step("Search voucher: {name}")
    def search_voucher(self, name):
        self.wait_clickable(self.SEARCH_INPUT)
        self.type_text(self.SEARCH_INPUT, name)
    @allure.step("Get first voucher name")
    def get_first_voucher_name(self):
        rows = self.finds(self.ROW)
        first_row = rows[0]
        first_row_voucher_name = first_row.find_element(*self.ROW_VOUCHER_NAME).text
        return first_row_voucher_name
    def wait_store_info_loaded(self,keyword=None):
        def condition():
            name = self.get_first_voucher_name()
            if keyword:
                return keyword in name
        self.wait_until(condition)
    @allure.step("Search voucher and wait: {name}")
    def search_voucher_and_wait(self,name):
        self.search_voucher(name)
        self.wait_store_info_loaded(keyword=name)