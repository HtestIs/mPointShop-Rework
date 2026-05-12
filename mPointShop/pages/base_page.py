import re

from core.base.base_page import BasePage as CoreBasePage


class BasePage(CoreBasePage):
    """mPointShop page objects extend the shared Selenium base here."""

    def money_to_int(self, text):
    # Keep digits and minus sign only
        return int(re.sub(r"[^\d-]", "", text))