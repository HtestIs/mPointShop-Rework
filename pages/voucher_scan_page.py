from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure
class VoucherScan(BasePage):
    URL = "/merchant-scan/voucher"
    TEXT_VOUCHER = (By.XPATH, "//input[@placeholder='Nhập mã Voucher']")
    @allure.step("Check voucher scan page is loaded")
    def is_loaded(self):
        return self.wait_url_contains(self.URL)
    @allure.step("Enter voucher code: {text}")
    def enter_voucher(self,text):
        self.type_text(self.TEXT_VOUCHER,text)
    