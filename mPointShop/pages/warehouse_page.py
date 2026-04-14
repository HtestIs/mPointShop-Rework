from mPointShop.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure
from mPointShop.pages.product_create_page import CreateProductPage

class WarehousePage(BasePage):
    URL = '/manager/warehouse-manager'
    PAGE_NAME = (By.CLASS_NAME, "title")
    ADD_NEW_PRODUCT_BTN = (
    By.XPATH,
    "//div[contains(@class,'status-white-container')]//div[@role='toolbar']//button[.//span[normalize-space()='Thêm sản phẩm mới']]"
)
    @allure.step("Open warehouse page")
    def open_url(self):
        self.open(self.URL)
    @allure.step("Get page name")
    def get_page_name(self):
        self.wait_visible(self.PAGE_NAME)
        return self.get_text(self.PAGE_NAME)

    def click_add_product(self):
        self.wait_clickable(self.ADD_NEW_PRODUCT_BTN)
        self.click(self.ADD_NEW_PRODUCT_BTN)
        return CreateProductPage(self.driver)
    def test_debug_add_product(self):
        print(f"found: {len(self.finds(self.ADD_NEW_PRODUCT_BTN))}")