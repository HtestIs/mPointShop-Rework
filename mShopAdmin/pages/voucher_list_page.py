from mShopAdmin.pages.basepage import BasePage
from selenium.webdriver.common.by import By

class VoucherListPage(BasePage):
    #TOGGLE
    SEARCH_EXPAND_BUTTON = (By.XPATH, "//a[normalize-space()='Mở rộng']")
    
    #SEARCH INPUTS
    SEARCH_ALT_ID = (By.ID,"voucherId")

    #SEARCH BUTTON
    SEARCH_BUTTON = (By.XPATH,"//button[@type='submit' and contains(@class,'ant-btn-primary')]")
    def expand_search(self):
        self.click(self.SEARCH_EXPAND_BUTTON)
    def search(self):
        self.click(self.SEARCH_BUTTON)
        
    def search_input(self,locator,text):
        self.type_text(locator, text)

    def search_by_alt_id(self, alt_id):
        self.search_input(self.SEARCH_ALT_ID, alt_id)
