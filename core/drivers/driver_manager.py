from selenium import webdriver

from core.drivers.browser_options import get_chrome_options


class DriverManager:
    @staticmethod
    def get_driver(browser):
        if browser == "chrome":
            return webdriver.Chrome(options=get_chrome_options())
        if browser == "firefox":
            return webdriver.Firefox()
        if browser == "edge":
            return webdriver.Edge()
        raise Exception("Unsupported Browser")