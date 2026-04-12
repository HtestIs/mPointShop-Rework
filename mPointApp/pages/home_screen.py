from mPointApp.pages.base_screen import BaseScreen
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

class AppHomePage(BaseScreen):
    HOMEPAGE_NAV_BAR = (AppiumBy.ACCESSIBILITY_ID,"Trang Chủ")
    SEE_MORE_VOUCHER_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Xem thêm").instance(0)')
    def is_homepage_displayed(self):
        return self.is_visible(self.HOMEPAGE_NAV_BAR)
    def is_navigated_to_homepage(self):
        home_page_icon = self.find(self.HOMEPAGE_NAV_BAR)
        return home_page_icon.get_attribute("selected") == "true"
    def click_see_more_voucher(self):
        self.tap(self.SEE_MORE_VOUCHER_BUTTON)