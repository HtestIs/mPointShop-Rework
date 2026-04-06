from mExchange.pages.base_page import BasePage


class MenuPage(BasePage):
    URL = "/#/dashboard"

    def wait_url(self):
        self.wait_url_contains(self.URL)
