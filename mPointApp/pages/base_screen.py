from selenium.common import NoSuchElementException

from core.base.base_page import BasePage


class BaseScreen(BasePage):
    """Shared mobile screen helpers for Appium page objects."""

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def has_error_message(self, expected_message: str) -> bool:
        try:
            return bool(self.wait_until(lambda: expected_message in self.driver.page_source))
        except Exception:
            return False

    def swipe_up(self, duration=600):
        size = self.driver.get_window_size()
        start_x = size['width'] // 2
        start_y = size['height'] * 0.8
        end_y = size['height'] * 0.3
        self.driver.swipe(start_x, start_y, start_x, end_y, duration)

    def swipe_to_element(self, locator, max_swipes=5):
        for _ in range(max_swipes):
            if self.is_visible(locator, timeout=1):
                return self.find(locator)
            self.swipe_up()

        if self.is_visible(locator, timeout=1):
            return self.find(locator)

        raise NoSuchElementException(
            f"Element with locator {locator} not found after {max_swipes} swipes."
        )

    def scroll_into_view(self, locator, max_swipes=5):
        return self.swipe_to_element(locator, max_swipes)

    def tap(self, locator, max_swipes=5):
        element = self.swipe_to_element(locator, max_swipes)
        element.click()
        return element