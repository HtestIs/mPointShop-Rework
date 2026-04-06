import json
import os

import allure
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    StaleElementReferenceException,
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)
        self.actions = ActionChains(driver)
        self.base_url = getattr(driver, "base_url", "")

    def open(self, path=None):
        target = path or self.base_url
        if not target:
            raise ValueError("No URL was provided and driver.base_url is not set.")

        if isinstance(target, str) and target.startswith(("http://", "https://")):
            self.driver.get(target)
            return

        if not self.base_url:
            raise ValueError("driver.base_url is not set. Use an absolute URL or configure base_url.")

        if not path:
            self.driver.get(self.base_url)
            return

        self.driver.get(f"{self.base_url.rstrip('/')}/{path.lstrip('/')}")

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_presence_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_until(self, condition):
        return self.wait.until(lambda driver: condition())

    def wait_stale(self, old):
        return self.wait.until(EC.staleness_of(old))

    def wait_attribute_change(self, locator, attribute, old_value):
        def condition(driver):
            try:
                element = driver.find_element(*locator)
                return element.get_attribute(attribute) != old_value
            except StaleElementReferenceException:
                return False

        return self.wait.until(condition)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def finds(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Click element")
    def click(self, locator, retries=3):
        for attempt in range(retries):
            try:
                element = self.wait_clickable(locator)
                element.click()
                return element
            except (
                StaleElementReferenceException,
                ElementClickInterceptedException,
                ElementNotInteractableException,
            ):
                self.scroll_into_view(locator)
                if attempt == retries - 1:
                    raise

    def scroll_into_view(self, locator):
        element = locator if hasattr(locator, "is_displayed") else self.find(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element,
        )

    @allure.step("Type text: {text}")
    def type_text(self, locator, text):
        self.wait_visible(locator)
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
        return element

    def type(self, locator, text):
        return self.type_text(locator, text)

    @allure.step("Clear field")
    def clear(self, locator):
        self.find(locator).clear()

    @allure.step("Get current URL")
    def get_current_url(self):
        return self.driver.current_url

    def wait_url_contains(self, text):
        return self.wait.until(EC.url_contains(text))

    @allure.step("Get text")
    def get_text(self, locator):
        element = self.wait_visible(locator)
        return element.text

    @allure.step("Refresh page")
    def refresh_page(self):
        self.driver.get(self.driver.current_url)

    def get_attribute_status(self, locator, attribute):
        element = locator if hasattr(locator, "get_attribute") else self.wait_presence(locator)
        return element.get_attribute(attribute)

    @allure.step("Hover over element")
    def hover(self, locator):
        element = locator if hasattr(locator, "is_displayed") else self.wait_clickable(locator)
        self.actions.move_to_element(element).perform()

    @allure.step("Upload image: {file_path}")
    def upload_image(self, locator, file_path):
        absolute_path = os.path.abspath(file_path)
        element = self.find(locator)
        element.send_keys(absolute_path)

    def is_visible(self, locator):
        try:
            self.wait_visible(locator)
            return True
        except Exception:
            return False

    @allure.step("Inject auth token")
    def dump_token(self, token):
        self.driver.execute_script(
            "window.localStorage.setItem(arguments[0], arguments[1]);",
            "authStore",
            json.dumps(token),
        )
