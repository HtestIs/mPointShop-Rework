import allure
from pages.mPointShop.base_page import BasePage
from selenium.webdriver.common.by import By
from datetime import datetime

class VoucherPartnerPage(BasePage):
    URL = "/manager/voucher-manager"
    
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Tên voucher']")
    ROW = (By.XPATH, "//table//tbody//tr")
    ROW_VOUCHER_NAME = (By.XPATH, ".//td[2]")
    ROW_STORE_SPAN = (By.XPATH, ".//td[8]//div//span")
    TOOLTIP_STORES_NAMES = (By.XPATH, "//div[@role='tooltip' and contains(@class,'rs-tooltip')]")
    STATUS_STORE = (By.XPATH, ".//td[9]")
    @allure.step("Open voucher manager page")
    def open_url(self, base_url):
        self.open(base_url + self.URL)
    @allure.step("Search voucher: {name}")
    def search_voucher(self, name):
        self.wait_clickable(self.SEARCH_INPUT)
        self.type_text(self.SEARCH_INPUT, name)

    @allure.step("Wait for voucher info to load with keyword: {keyword}")
    def wait_voucher_info_loaded(self, keyword=None):
        def condition():
            rows = self.finds(self.ROW)
            if not rows:
                return False

            try:
                name = rows[0].find_element(*self.ROW_VOUCHER_NAME).text
                if keyword:
                    return keyword in name
                return bool(name.strip())
            except Exception:
                return False
        self.wait_until(condition)


    def search_voucher_and_wait(self,name):
        self.search_voucher(name)
        self.wait_voucher_info_loaded(keyword=name)

    @allure.step("Hover store span to display tooltip")
    def hover_store_span(self):
        def condition():
            rows = self.finds(self.ROW)
            if not rows:
                return False
            
            try:
                span = rows[0].find_element(*self.ROW_STORE_SPAN)
                return span.is_displayed()
            except:
                return False
        self.wait_until(condition)
        rows = self.finds(self.ROW)
        span = rows[0].find_element(*self.ROW_STORE_SPAN)
        self.hover(span)

    @allure.step("Get text from tooltip stores")
    def get_text_from_tooltips(self):
        tooltip = self.wait_visible(self.TOOLTIP_STORES_NAMES)
        tooltip_text = tooltip.get_attribute("textContent")
        stores_names = [name.strip() for name in tooltip_text.split(",") if name.strip()]
        return stores_names

    def wait_status_store_loaded(self):
        def condition():
            rows = self.finds(self.ROW)
            if not rows:
                return False

            try:
                status_text = rows[0].find_element(*self.STATUS_STORE).text.strip()
                return bool(status_text)
            except Exception:
                return False

        self.wait_until(condition)

    @allure.step("Get status store text")
    def get_status_store_text(self):
        self.wait_status_store_loaded()
        rows = self.finds(self.ROW)
        return rows[0].find_element(*self.STATUS_STORE).text.strip()
    
    def get_tooltip_stores_names(self):
        self.hover_store_span()
        return self.get_text_from_tooltips()