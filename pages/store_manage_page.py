import allure

from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from datetime import datetime
import random
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
    MODAL_FULL = (By.XPATH, "//div[@class='rs-modal-content']")
    MODAL_UPLOAD_IMAGE_BUTTON = (By.XPATH,"//span[contains(text(),'Cần tải ảnh cửa hàng lên')]/ancestor::button")
    MODAL_UPLOAD_INPUT = (By.XPATH,"(//input[@type='file'])[1]")
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
    MODAL_CITY_SELECT = (By.XPATH,"//b[contains(text(),'Tỉnh/TP')]/following::div[@role='combobox'][1]")
    MODAL_DISTRICT_SELECT = (By.XPATH,"//b[contains(text(),'Quận/Huyện')]/following::div[@role='combobox'][1]")
    MODAL_WARD_SELECT = (By.XPATH,"(//b[contains(text(),'Xã/Phường')])[1]/following::div[@role='combobox'][1]")
    MODAL_CITY_NEW_SELECT = (By.XPATH,"//b[contains(text(),'Tỉnh/TP (mới theo 2025)')]/following::div[@role='combobox'][1]")
    MODAL_WARD_NEW_SELECT = (By.XPATH,"//b[contains(text(),'Xã/Phường (mới theo 2025)')]/following::div[@role='combobox'][1]")
    MODAL_OPTION_LIST = (By.CSS_SELECTOR,".rs-picker-select-menu.rs-anim-in div[role='option']")
    MODAL_SEARCH_OPTION =(By.XPATH, "//input[@class='rs-picker-search-bar-input']")
    MODAL_NO_RESULT =(By.CSS_SELECTOR,".rs-picker-none")
    MODAL_DATE_PICKER = (By.XPATH,"//b[contains(text(),'Ngày hết hạn giấy phép')]/following::div[@role='combobox'][1]")
    MODAL_NEXT_MONTH_BUTTON = (By.CSS_SELECTOR, ".rs-calendar-header-forward")
    MODAL_CHOOSE_DATE = (By.CSS_SELECTOR,".rs-calendar-table-cell:not(.rs-calendar-table-cell-disabled)"":not(.rs-calendar-table-cell-un-same-month) "".rs-calendar-table-cell-day")
    MODAL_DATE_PICKER_CONFIRM = (By.CSS_SELECTOR,".rs-picker-date-menu .rs-btn-primary")
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
# USER MODAL INTERACT
    def click_confirm_button_user_modal(self):
        self.click(self.MODAL_CONFIRM_BUTTON)
    def upload_store_image(self, image_path):
        self.upload_image(self.MODAL_UPLOAD_INPUT, image_path)
# USER MODAL INFO
    def get_store_username(self):
        self.click(self.FIRST_STORE_EDIT)
        username = self.get_attribute_status(self.FIRST_STORE_USERNAME,"value")
        self.click(self.MODAL_CANCEL)
        return username
# TYPE USER MODAL INFO INTERACT
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
        "point_rate": MODAL_POINT_RATE,
        "image_path": MODAL_UPLOAD_INPUT
    }
    COMBO_FIELDS = {
        "city_old": MODAL_CITY_SELECT,
        "district_old": MODAL_DISTRICT_SELECT,
        "ward_old": MODAL_WARD_SELECT,
        "city_new": MODAL_CITY_NEW_SELECT,
        "ward_new": MODAL_WARD_NEW_SELECT
    }
    def fill_field(self, field_name, value):
        locator = self.FORM_FIELDS[field_name]
        self.type_text(locator, value)
    def choose_option(self, field_name, value):
        dropdown = self.COMBO_FIELDS[field_name]

        self.click(dropdown)

        self.wait.until(
            lambda d: (
                self.finds(self.MODAL_OPTION_LIST)
                or self.is_visible(self.MODAL_NO_RESULT)
            )
        )
        options = self.finds(self.MODAL_OPTION_LIST)
        if not options:
            raise Exception(f"No options available for {field_name}")
        for option in options:
            if option.text.strip() == value:
                option.click()
                break
        else:
            raise Exception(f"Option '{value}' not found for {field_name}")
        
        self.wait.until(
            lambda d: self.get_selected_text(field_name) == value
        )
    def get_selected_text(self, field_name):
        dropdown = self.COMBO_FIELDS[field_name]
        return self.find(dropdown).text.strip()
#
#
#
# 
# 
#  add validate selection
# 
# 
# 
# 
#  
        # DROPDOWN INTERACTION
    # THIS ONE IS FOR SELECTING THE LOCATION OPTION,
    # IT'S CALLED BY select_option METHOD, 
    # IT WILL SELECT THE CITY, DISTRICT, WARD IN ORDER,
    # ADDITIONALLY, IF THE CITY IS NOT SELECTED, 
    # IT WILL NOT SELECT THE DISTRICT AND WARD,
    # IF THE DISTRICT IS NOT SELECTED, IT WILL NOT SELECT THE WARD.
    def select_option(self,data):
        city = data.get("city_old")
        district = data.get("district_old")
        ward = data.get("ward_old")
        city_new = data.get("city_new")
        ward_new = data.get("ward_new")
        if city:
            self.choose_option("city_old",city)
            if district:
                self.choose_option("district_old",district)
                if ward:
                    self.choose_option("ward_old",ward)
        if city_new:
            self.choose_option("city_new",city_new)
            if ward_new:
                self.choose_option("ward_new",ward_new)
    # THIS ONE IS FOR SELECTING INNER LOCATION OPTION,
    # CHECK IF USER CHOOSE BIGGER LOCATION YET
    def setup_location(self,setup,storedata):
        if setup == "missing_city":
            return
        elif setup == "missing_district":
            self.choose_option("city_old",storedata["city_old"])
        elif setup == "missing_city_new":
            return
    def has_selectable_option(self):
        self.wait.until(
        lambda d: (
            self.finds(self.MODAL_OPTION_LIST)
            or self.is_visible(self.MODAL_NO_RESULT)
        )
    )

        return len(self.finds(self.MODAL_OPTION_LIST)) > 0
# DATE CHOOSE
    def choose_date(self):
        self.click(self.MODAL_DATE_PICKER)
        months_to_add = random.randint(1, 48)
        for _ in range(months_to_add):
            self.click(self.MODAL_NEXT_MONTH_BUTTON)
        days = self.finds(self.MODAL_CHOOSE_DATE)
        random.choice(days).click()
        self.click(self.MODAL_DATE_PICKER_CONFIRM)

# STORE REGISTRATION
    # THIS AI HATES ME I THINK, 
    # IT KEPT GIVING ME THE SAME COMMENT FOR THIS METHOD, 
    # I HAD TO ASK IT TO STOP COMPLAINING AND JUST WRITE THE COMMENT, 
    # NOW IT'S WRITING A NORMAL COMMENT, I THINK IT'S FINE NOW
    def fill_all_fields(self, storedata):
        for field in self.FORM_FIELDS:
            value = storedata.get(field)
            if value:
                if field == "image_path":
                    self.upload_store_image(value)
                else:
                    self.fill_field(field, value)
    def select_all_dropdowns(self, storedata):
        for field in self.COMBO_FIELDS:
            value = storedata.get(field)
            if value:
                self.choose_option(field, value)
# ERROR HANDLING
    # THIS ONE FOR FIELDS ERROR
    # SELECTBOX MIGHT F THIS ONE UP
    def get_field_error(self,field_name):
        locator = (By.XPATH,f"//b[contains(text(),'{field_name}')]/following-sibling::span")
        return self.find(locator).text