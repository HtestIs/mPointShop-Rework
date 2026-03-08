from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        self.actions = ActionChains(driver)
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
    def click(self,locator,step_desc=""):
        for _ in range(3):
            try:
                element = self.wait_clickable(locator)
                element.click()
                return
            except StaleElementReferenceException:
                pass
        raise
    def type_text(self,locator,text):
        self.wait_visible(locator)
        self.find(locator).send_keys(text)
    def clear(self,locator):
        self.find(locator).clear()
    def get_current_url(self):
        return self.driver.current_url
    def wait_url_contains(self,text):
        return self.wait.until(EC.url_contains(text))
    def get_text(self,locator):
        location = self.wait_visible(locator)
        return location.text
    def refresh_page(self):
        self.driver.get(self.driver.current_url)
    def get_attribute_status(self,location,attribute):
        element = self.wait_presence(location)
        return element.get_attribute(attribute)
    def hover(self,location):
        self.actions.move_to_element(location).perform()