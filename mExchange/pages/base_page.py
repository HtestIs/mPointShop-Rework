import json

import allure
from core.base.base_page import BasePage as CoreBasePage


class BasePage(CoreBasePage):
    """mExchange page objects extend the shared Selenium base here."""

    @allure.step("Inject auth token")
    def dump_token(self, token):
        self.driver.execute_script(
            "window.localStorage.setItem(arguments[0], arguments[1]);",
            "authStore",
            json.dumps(token),
        )