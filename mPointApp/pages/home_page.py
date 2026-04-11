from mPointApp.pages.base_screen import BaseScreen
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

class AppHomePage(BaseScreen):
    HOMEPAGE_NAV_BAR = (AppiumBy.ACCESSIBILITY_ID,"Trang Chủ")
    def is_homepage_displayed(self):
        return self.is_visible(self.HOMEPAGE_NAV_BAR)
    def is_navigated_to_homepage(self):
        home_page_icon = self.find(self.HOMEPAGE_NAV_BAR)
        return home_page_icon.get_attribute("selected") == "true"