from selenium.webdriver.common.by import By

from mPointShop.pages.base_page import BasePage
from mPointShop.pages.components.store_list_mixin import StoreListMixin
from mPointShop.pages.components.store_registration_mixin import StoreRegistrationMixin
from mPointShop.pages.components.store_security_mixin import StoreSecurityMixin


class StoreManage(StoreListMixin, StoreSecurityMixin, StoreRegistrationMixin, BasePage):
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
    FIRST_PHONE_NUMBER = (By.XPATH,"//div[contains(@class,'branchmanagement-form-content')]//span[contains(normalize-space(.), 'Số điện thoại:')]")
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
        "ward_new": MODAL_WARD_NEW_SELECT,
    }
