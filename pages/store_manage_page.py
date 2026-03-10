from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from datetime import datetime
class StoreManage(BasePage):
    URL="/manager/store-manager"
    PAGE_NAME = (By.CLASS_NAME,"title")
    # LIST HEAD
    SEARCH_TEXT_FIND = (By.CSS_SELECTOR,"input[placeholder='Tìm cửa hàng']")
    SEARCH_PHONE_SEARCH_INPUT = (By.CSS_SELECTOR, "input[placeholder='Tìm theo số điện thoại']")
    ADD_STORE_BUTTON = (By.XPATH,"//button[.//span[text()='Thêm cửa hàng']]")
    # LIST
    FIRST_STORE = (By.XPATH,"(//div[contains(@class,'branchmanagement-container')])[1]")
    FIRST_STORE_NAME =(By.XPATH,"(//div[contains(@class,'branchmanagement-form-content')]//b)[1]")
    FIRST_STORE_BUTTON=(By.XPATH,"(//button[normalize-space()='Đổi mật khẩu'])[1]")
    FIRST_STORE_EDIT=(By.CSS_SELECTOR,".branchmanagement-container:first-of-type .branchmanagement-right button:nth-of-type(2)")
    FIRST_SWITCH_BUTTON = (By.CSS_SELECTOR, ".branchmanagement-container:first-of-type .rs-toggle")
    FIRST_STORE_USERNAME = (By.XPATH,"//b[contains(text(),'Tên đăng nhập')]/following-sibling::input")
    FIRST_SWITCH = (By.CSS_SELECTOR,".branchmanagement-container:first-of-type input[aria-checked]")
    # STORE INFO MODAL
    MODAL_STORE_NAME = (By.XPATH,"//div[@role='row'][.//b[contains(text(),'Tên cửa hàng')]]//input")
    MODAL_USER_NAME = (By.XPATH,"//b[contains(text(),'Tên đăng nhập')]/following::input[1]")
    MODAL_ADDRESS = (By.XPATH,"//b[contains(text(),'Địa chỉ')]/following::textarea[1]")
    MODAL_GPS = (By.XPATH,"//b[contains(text(),'GPS')]/following::input[1]")
    MODAL_MANAGER_NAME = (By.XPATH,"//b[contains(text(),'Tên người phụ trách')]/following::input[1]")
    MODAL_MANAGER_PHONE = (By.XPATH,"//b[contains(text(),'Số điện thoại người phụ trách')]/following::input[1]")
    MODAL_CUSTOMER_SERVICE_PHONE = (By.XPATH,"//b[contains(text(),'Số điện thoại chăm sóc khách hàng')]/following::input[1]")
    MODAL_SALES_CODE = (By.XPATH,"//b[contains(text(),'Mã nhân viên kinh doanh')]/following::input[1]")
    MODAL_PASSWORD = (By.XPATH,"//b[contains(text(),'Mật khẩu')]/following::input[@type='password'][1]")
    MODAL_CONFIRM_PASSWORD = (By.XPATH,"//b[contains(text(),'Nhập lại mật khẩu')]/following::input[@type='password'][1]")
    MODAL_COMMISSION = (By.XPATH,"//b[contains(text(),'Hoa hồng')]/following::input[1]")
    MODAL_TRANSFER_LIMIT = (By.XPATH,"//b[contains(text(),'Giới hạn mức chuyển điểm')]/following::input[1]")
    MODAL_MIN_WALLET_BALANCE = (By.XPATH,"//b[contains(text(),'Số dư tối thiểu')]/following::input[1]")
    MODAL_POINT_RATE = (By.XPATH,"//b[contains(text(),'Tỷ lệ tích điểm')]/following::input[1]")
    MODAL_CONFIRM_BUTTON = (By.XPATH,"//button[.//span[text()='Xác nhận']]")
    MODAL_CANCEL = (By.XPATH, "//button[normalize-space()='Hủy']")
    # STORE PASSWORD MODAL
    TEXT_PASSWORD_MODAL=(By.XPATH,"//div[contains(@class,'rs-modal-content')]//b[contains(text(),'Mật khẩu mới')]/ancestor::div[@role='row']//input")
    CONFIRM_BUTTON =(By.XPATH,"//div[@role='dialog']//button[.//span[normalize-space()='Xác nhận']]")
    # ETC
    TOAST_MESSAGE =(By.XPATH,"//div[@role='alert']/div[2]")
    BTN_LOG_OUT = (By.XPATH,"//span[text()='Đăng xuất']")
    USER_BLOCK = (By.CSS_SELECTOR,"#cheader > section > div > div.c-header__right > div > a > div")
    LOADING_OVERLAY = (By.CSS_SELECTOR, "div.c-loading-page")
    def get_page_name(self):
        return self.get_text(self.PAGE_NAME)
    # LIST HEAD INTERACT
    def find_store_with_name(self,text):
        self.type_text(self.SEARCH_TEXT_FIND,text)
    def click_add_new_store(self):
        self.click(self.ADD_STORE_BUTTON)
    def find_store_with_number(self,text):
        self.type_text(self.SEARCH_PHONE_SEARCH_INPUT,text)
    # LIST
    def get_store_name(self):
        return self.get_text(self.FIRST_STORE_NAME)
    def toggle_store(self):
        old = self.find(self.FIRST_SWITCH_BUTTON)
        current = self.get_lock_status()
        self.click(self.FIRST_SWITCH_BUTTON)
        self.wait_stale(old)
        self.wait_clickable(self.FIRST_SWITCH_BUTTON)
        self.wait_attribute_change(self.FIRST_SWITCH,"aria-checked",current)
    def get_lock_status(self):
        return self.get_attribute_status(self.FIRST_SWITCH,"aria-checked")
    def ensure_locked(self):
        if self.get_lock_status() == "false":
            self.toggle_store()
    # STORE PASSWORD
    def click_change_password(self):
        self.click(self.FIRST_STORE_BUTTON)
    def enter_password_update(self,text):
        self.type_text(self.TEXT_PASSWORD_MODAL,text)
    def click_confirm_button_password_modal(self):
        self.click(self.CONFIRM_BUTTON)
    def change_password(self,new_password):
        self.click_change_password()
        self.enter_password_update(new_password)
        self.click_confirm_button_password_modal()
    # ETC
    def get_toast_msg(self):
        return self.get_text(self.TOAST_MESSAGE)
    def click_logout(self):
        self.click(self.BTN_LOG_OUT)
        return LoginPage(self.driver)
    def hover_user(self):
        self.hover(self.USER_BLOCK)
    def wait_loading_overlay(self):
        self.wait_visible(self.LOADING_OVERLAY)
        self.wait_invisible(self.LOADING_OVERLAY)
    # USER MODAL INFO
    def get_store_username(self):
        self.click(self.FIRST_STORE_EDIT)
        username = self.get_attribute_status(self.FIRST_STORE_USERNAME,"value")
        self.click(self.MODAL_CANCEL)
        return username
    # USER MODAL INFO INTERACT
    FORM_FIELDS = {
        "name": MODAL_STORE_NAME,
        "username": MODAL_USER_NAME,
        "address": MODAL_ADDRESS,
        "gps": MODAL_GPS,
        "manager_name": MODAL_MANAGER_NAME,
        "manager_phone": MODAL_MANAGER_PHONE,
        "customer_service_phone": MODAL_CUSTOMER_SERVICE_PHONE,
        "sale_code": MODAL_SALES_CODE,
        "password": MODAL_PASSWORD,
        "confirm_password": MODAL_CONFIRM_PASSWORD,
        "commission": MODAL_COMMISSION,
        "transfer_limit": MODAL_TRANSFER_LIMIT,
        "min_wallet": MODAL_MIN_WALLET_BALANCE,
        "point_rate": MODAL_POINT_RATE
    }
    def fill_field(self,field_name,text):
        locator = self.FORM_FIELDS[field_name]
        self.type_text(locator,text)
    def fill_form_store_register(self,storedata):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        self.click_add_new_store()
        for field, value in storedata.items():
            if field in ["name","username"]:
                unique_value = f"{value}{timestamp}"
                self.fill_field(field, unique_value)
            else:
                self.fill_field(field, value)
        self.click_confirm_button_user_modal()