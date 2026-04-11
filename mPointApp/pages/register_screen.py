
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from mPointApp.pages.base_screen import BaseScreen



class RegisterScreen(BaseScreen):
    # Define locators for registration screen elements here
    REGISTER_PHONE_NUMBER= (AppiumBy.UIAutomator, 'new UiSelector().text("Số điện thoại")')
    TOS_CHECKBOX = (AppiumBy.UIAutomator, 'new UiSelector().className("android.view.ViewGroup").instance(16)')
    ##DO LATER