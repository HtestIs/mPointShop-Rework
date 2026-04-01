from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure

class WarehousePage(BasePage):
    URL = '/manager/warehouse-manager'
    PAGE_NAME = (By.CLASS_NAME, "title")
    @allure.step("Open warehouse page")
    def open_url(self,base_url):
        self.open(base_url + self.URL)
    @allure.step("Get page name")
    def get_page_name(self):
        self.wait_visible(self.PAGE_NAME)
        return self.get_text(self.PAGE_NAME)