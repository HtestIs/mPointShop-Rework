from selenium.common import TimeoutException

from mPointApp.pages.base_screen import BaseScreen
from appium.webdriver.common.appiumby import AppiumBy

from mPointApp.pages.home_screen import AppHomePage

class AndroidPermissionDialog(BaseScreen):
    ALLOW_WHILE_USING_APP = (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
    def allow_permission(self):
        try:
            self.click(self.ALLOW_WHILE_USING_APP)
            return AppHomePage(self.driver)
        except TimeoutException:
            raise TimeoutException("Permission dialog not found")