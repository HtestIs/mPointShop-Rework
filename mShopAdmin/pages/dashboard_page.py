from mShopAdmin.pages.basepage import BasePage
from selenium.webdriver.common.by import By
from mShopAdmin.pages.voucher_list_page import VoucherListPage

class DashboardPage(BasePage):
    #TOGGLE
    TOGGLE_MENU = (By.CSS_SELECTOR,"i.gx-icon-btn.icon.icon-menu-unfold")
    # PARRENT MENU
    SIDEBAR_DASHBOARD = (By.XPATH,"//ul[@role='menu']/li[contains(@class,'ant-menu-item')]//a[@href='#/dashboard']")
    SIDEBAR_REPORT = (By.XPATH,"//ul[@role='menu']/li[contains(@class,'ant-menu-submenu')]//div[contains(@class,'ant-menu-submenu-title')][.//span[normalize-space()='Báo cáo']]")
    SIDEBAR_VOUCHER_MANAGEMENT = (By.XPATH,"//ul[@role='menu']/li[contains(@class,'ant-menu-submenu')]//div[contains(@class,'ant-menu-submenu-title')][.//span[normalize-space()='Quản lý voucher']]")
    SIDEBAR_FLASHSALE = (By.XPATH,"//ul[@role='menu']/li[contains(@class,'ant-menu-submenu')]//div[contains(@class,'ant-menu-submenu-title')][.//span[normalize-space()='FlashSale']]")
    SIDEBAR_BANNER = (By.XPATH,"//ul[@role='menu']/li[contains(@class,'ant-menu-item')]//a[contains(@href,'#/list?page=315')]")
    SIDEBAR_LICENSE = (By.XPATH,"//ul[@role='menu']/li[contains(@class,'ant-menu-submenu')]//div[contains(@class,'ant-menu-submenu-title')][.//span[normalize-space()='Điều khoản']]")
    SIDEBAR_PRODUCT = (By.XPATH,"//ul[@role='menu']/li[contains(@class,'ant-menu-submenu')]//div[contains(@class,'ant-menu-submenu-title')][.//span[normalize-space()='Quản lý sản phẩm']]")

    #VOCHER MANAGEMENT
    SIDEBAR_VOUCHER_MANAGEMENT_LIST = (By.XPATH,"//ul[contains(@id,'162-popup')]//a[.//span[normalize-space()='Voucher']]")
    #PAGE ELEMENTS
    FIRST_ROW = (By.XPATH, "//table[@id='mywrapper']//tbody/tr[@data-row-key][1]")
    def navigate_to_parrent(self, parrent_locator):
        self.click(self.TOGGLE_MENU)
        self.wait_visible(parrent_locator)
        self.click(parrent_locator)
    def wait_spinner_invisible(self):
        self.wait_invisible(self.TABLE_LOADING_SPINNER)
    def navigate_to_voucher_management(self, child_menu):
        self.navigate_to_parrent(self.SIDEBAR_VOUCHER_MANAGEMENT)
        self.wait_visible(child_menu)
        self.click(child_menu)

    def navigate_to_voucher_list(self):
        self.navigate_to_voucher_management(self.SIDEBAR_VOUCHER_MANAGEMENT_LIST)
        self.wait_visible(self.FIRST_ROW)
        return VoucherListPage(self.driver)
