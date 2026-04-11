from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from core.base.base_page import BasePage


class BaseScreen(BasePage):
    """Shared mobile screen helpers for future Appium page objects."""

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def tap(self, locator):
        self.wait_for_visible(locator).click()

    def get_text(self, locator):
        return self.wait_for_visible(locator).text

    def is_visible(self, locator):
        try:
            return self.wait_for_visible(locator).is_displayed()
        except Exception:
            return False
    def has_error_message(self, expected_message: str) -> bool:
        try:
            return bool(
                self.wait_until(lambda : expected_message in self.driver.page_source)
            )
        except Exception:
            return False