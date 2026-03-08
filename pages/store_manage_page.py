from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
class StoreManage(BasePage):
    URL="/manager/store-manager"
    PAGE_NAME = (By.CLASS_NAME,"title")
    TEXT_FIND = (By.CSS_SELECTOR,"input[placeholder='Tìm cửa hàng']")
    FIRST_STORE = (By.XPATH,"(//div[contains(@class,'branchmanagement-container')])[1]")
    FIRST_STORE_NAME =(By.XPATH,"(//div[contains(@class,'branchmanagement-form-content')]//b)[1]")
    FIRST_STORE_BUTTON=(By.XPATH,"(//button[normalize-space()='Đổi mật khẩu'])[1]")
    FIRST_SWITCH_BUTTON = (By.CSS_SELECTOR, ".branchmanagement-container:first-of-type .rs-toggle")
    FIRST_SWITCH = (By.CSS_SELECTOR,".branchmanagement-container:first-of-type input[aria-checked]")
    TEXT_PASSWORD_MODAL=(By.XPATH,"//div[contains(@class,'rs-modal-content')]//b[contains(text(),'Mật khẩu mới')]/ancestor::div[@role='row']//input")
    CONFIRM_BUTTON =(By.XPATH,"//div[@role='dialog']//button[.//span[normalize-space()='Xác nhận']]")
    TOAST_MESSAGE =(By.XPATH,"//div[@role='alert']/div[2]")
    BTN_LOG_OUT = (By.XPATH,"//span[text()='Đăng xuất']")
    USER_BLOCK = (By.CSS_SELECTOR,"#cheader > section > div > div.c-header__right > div > a > div")
    def get_page_name(self):
        return self.get_text(self.PAGE_NAME)
    def find_store(self,text):
        self.type_text(self.TEXT_FIND,text)
    def get_store_name(self):
        return self.get_text(self.FIRST_STORE_NAME)
    def click_change_password(self):
        self.click(self.FIRST_STORE_BUTTON)
    def enter_password(self,text):
        self.type_text(self.TEXT_PASSWORD_MODAL,text)
    def click_confirm_button(self):
        self.click(self.CONFIRM_BUTTON)
    def change_password(self,new_password):
        self.click_change_password()
        self.enter_password(new_password)
        self.click_confirm_button()
    def get_toast_msg(self):
        return self.get_text(self.TOAST_MESSAGE)
    def toggle_store(self):
        old = self.find(self.FIRST_SWITCH_BUTTON)
        current = self.get_lock_status()
        self.click(self.FIRST_SWITCH_BUTTON)
        self.wait_stale(old)
        self.wait_clickable(self.FIRST_SWITCH_BUTTON)
        self.wait_attribute_change(self.FIRST_SWITCH,"aria-checked",current)
    def click_logout(self):
        self.click(self.BTN_LOG_OUT)
    def hover_user(self):
        self.hover(self.USER_BLOCK)
    def get_lock_status(self):
        return self.get_attribute_status(self.FIRST_SWITCH,"aria-checked")