from mPointApp.pages.base_screen import BaseScreen
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

from mPointApp.pages.search_voucher_screen import SearchVoucherScreen

class AppVoucherCommonPage(BaseScreen):
    SEARCH_BAR =(AppiumBy.ACCESSIBILITY_ID,", Tìm kiếm voucher...")

    def is_voucher_page_displayed(self):
        return self.is_visible(self.SEARCH_BAR)

    def click_search_bar(self):
        self.tap(self.SEARCH_BAR)
        return SearchVoucherScreen(self.driver)