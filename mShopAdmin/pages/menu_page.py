from mShopAdmin.pages.basepage import BasePage
from selenium.webdriver.common.by import By

class MenuPage(BasePage):
    
    def get_menu_items(self):
        return self.find_elements(self.menu_items_locator)