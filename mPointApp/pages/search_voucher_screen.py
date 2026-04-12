from mPointApp.pages.base_screen import BaseScreen
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SearchVoucherScreen(BaseScreen):
    SEARCH_BAR_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Nhập từ khóa ...")')
    def is_search_voucher_page_displayed(self):
        return self.is_visible(self.SEARCH_BAR_INPUT)
    def enter_search_keyword(self, keyword):
        self.type_text(self.SEARCH_BAR_INPUT, keyword)
        self.driver.press_keycode(66)  # Keycode 66 corresponds to the Enter key on Android