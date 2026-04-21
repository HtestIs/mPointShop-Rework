from mPointShop.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure
class VoucherScan(BasePage):
    URL = "/merchant-scan/voucher"
    TEXT_VOUCHER = (By.XPATH, "//input[@placeholder='Nhập mã Voucher']")
    CONFIRM_BTN = (By.XPATH, "//input[@placeholder='Nhập mã Voucher']/following-sibling::button")
    VOUCHER_NAME = (By.XPATH, "//li[span[1][normalize-space()='Tên voucher:']]/span[2]")
    VOUCHER_STATUS = (By.XPATH, "//li[span[1][normalize-space()='Tình trạng sử dụng:']]/span[2]")
    TOTAL_BILL = (By.XPATH, "//input[@placeholder='Nhập giá trị hóa đơn']")
    CONTINUE_BTN = (By.XPATH, "//button[span[normalize-space()='Tiếp tục']]")
    @allure.step("Check voucher scan page is loaded")
    def is_loaded(self):
        return self.wait_url_contains(self.URL)
    @allure.step("Enter voucher code: {text}")
    def enter_voucher(self,text):
        self.type_text(self.TEXT_VOUCHER,text)
    @allure.step("Click confirm button")
    def click_confirm(self):
        self.click(self.CONFIRM_BTN)
    def get_voucher_name(self):
        return self.get_text(self.VOUCHER_NAME)
    def get_voucher_status(self):
        return self.get_text(self.VOUCHER_STATUS)
    
    @allure.step("Enter total bill: {amount}")
    def enter_total_bill(self, amount):
        self.type_text(self.TOTAL_BILL, str(amount))
    @allure.step("Click continue button")
    def click_continue(self):
        self.click(self.CONTINUE_BTN)