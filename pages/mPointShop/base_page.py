import json
import os
import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException,ElementClickInterceptedException,ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        self.actions = ActionChains(driver)
    @allure.step("Open URL: {base_url}")
    def open(self,base_url):
        self.driver.get(base_url)
    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    def wait_invisible(self,locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))
    def wait_clickable(self,locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    def wait_presence(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    def wait_presence_all(self,locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    #Superior Wait/ ONE WAIT TO RULE THEM ALL
    def wait_until(self,condition):
        self.wait.until(lambda d: condition())
    def wait_stale(self,old):
        self.wait.until(EC.staleness_of(old))
    def wait_attribute_change(self,locator,attribute,old_value):
    #     self.wait.until(
    #     lambda d: d.find_element(*locator).get_attribute(attribute) != old_value
    # )
        def condition(driver):
            try:
                element = driver.find_element(*locator)
                return element.get_attribute(attribute) != old_value
            except StaleElementReferenceException:
                return False

        self.wait.until(condition)
    def find(self,locator):
        return self.driver.find_element(*locator)
    def finds(self,locator):
        return self.driver.find_elements(*locator)
    @allure.step("Click element")
    def click(self,locator,step_desc="", retries=3):
        for attempts in range(retries):
            try:
                element = self.wait_clickable(locator)
                element.click()
                return
            except (
            StaleElementReferenceException,
            ElementClickInterceptedException,
            ElementNotInteractableException
        ):
                self.scroll_into_view(locator)
                if attempts == retries - 1:
                    raise
    def scroll_into_view(self,locator):
        element = self.find(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )
    @allure.step("Type text: {text}")
    def type_text(self,locator,text):
        self.wait_visible(locator)
        self.find(locator).send_keys(text)
    @allure.step("Clear field")
    def clear(self,locator):
        self.find(locator).clear()
    @allure.step("Get current URL")
    def get_current_url(self):
        return self.driver.current_url
    def wait_url_contains(self,text):
        return self.wait.until(EC.url_contains(text))
    @allure.step("Get text")
    def get_text(self,locator):
        location = self.wait_visible(locator)
        return location.text
    @allure.step("Refresh page")
    def refresh_page(self):
        self.driver.get(self.driver.current_url)
    def get_attribute_status(self,location,attribute):
        element = self.wait_presence(location)
        return element.get_attribute(attribute)
    @allure.step("Hover over element")
    def hover(self,location):
        element = self.wait_clickable(location)
        self.actions.move_to_element(element).perform()
    @allure.step("Upload image: {file_path}")
    def upload_image(self, locator, file_path):
        absolute_path = os.path.abspath(file_path)
        element = self.find(locator)
        element.send_keys(absolute_path)
    def is_visible(self,locator):
        try:
            self.wait_visible(locator)
            return True
        except:
            return False
    
    @allure.step("Inject auth token")
    def dump_token(self,token):
        self.driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", "authStore",
                              json.dumps(token))