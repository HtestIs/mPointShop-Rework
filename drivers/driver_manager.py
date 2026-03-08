from selenium import webdriver
from drivers.browser_options import get_chrome_options

class DriverManager:
    @staticmethod
    def get_driver(browser):
        if browser == "chrome":
            return webdriver.Chrome(options=get_chrome_options())
        elif browser == "firefox":
            return webdriver.Firefox()
        elif browser == "edge":
            return webdriver.Edge()
        else:
            raise Exception("Unsupported Browser")