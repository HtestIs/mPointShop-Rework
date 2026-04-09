from mShopAdmin.pages.basepage import BasePage
from selenium.webdriver.common.by import By

class VoucherListPage(BasePage):
    #TOGGLE
    SEARCH_EXPAND_BUTTON = (By.XPATH, "//a[normalize-space()='Mở rộng']")
    
    #SEARCH INPUTS
    SEARCH_ALT_ID = (By.ID,"voucherId")

    #SEARCH BUTTON
    SEARCH_BUTTON = (By.XPATH,"//button[@type='submit' and contains(@class,'ant-btn-primary')]")

    #ROWS
    FIRST_ROW = (By.XPATH, "(//tbody[@class='ant-table-tbody']/tr[not(contains(@class,'ant-table-measure-row'))])[1]")
    FIRST_ROW_STATUS_TOGGLE = (By.XPATH, "(//tbody[@class='ant-table-tbody']/tr[not(contains(@class,'ant-table-measure-row'))])[1]/td[2]//button[@role='switch']")
    FIRST_ROW_APPROVE_TOGGLE = (By.XPATH, "(//tbody[@class='ant-table-tbody']/tr[not(contains(@class,'ant-table-measure-row'))])[1]/td[3]//button[@role='switch']")
    FIRST_ROW_IS_M1_TOGGLE = (By.XPATH, "(//tbody[@class='ant-table-tbody']/tr[not(contains(@class,'ant-table-measure-row'))])[1]/td[4]//button[@role='switch']")
    FIRST_ROW_HOME_TOGGLE = (By.XPATH, "(//tbody[@class='ant-table-tbody']/tr[not(contains(@class,'ant-table-measure-row'))])[1]/td[5]//button[@role='switch']")
    def expand_search(self):
        self.click(self.SEARCH_EXPAND_BUTTON)
    def search(self):
        self.click(self.SEARCH_BUTTON)
        
    def search_input(self,locator,text):
        self.type_text(locator, text)

    def search_by_alt_id(self, alt_id):
        self.search_input(self.SEARCH_ALT_ID, alt_id)
    
    def click_approve_toggle(self):
        self.click(self.FIRST_ROW_APPROVE_TOGGLE)