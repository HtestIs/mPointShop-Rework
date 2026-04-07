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
    FIRST_STORE = (By.XPATH, "(//div[contains(@class,'branchmanagement-container')])[1]")
    FIRST_STORE_NAME = (By.XPATH, "((//div[contains(@class,'branchmanagement-container')])[1]//div[contains(@class,'branchmanagement-form-content')]//b)[1]")
    FIRST_STORE_BUTTON = (By.XPATH, "((//div[contains(@class,'branchmanagement-container')])[1]//button[normalize-space()='Đổi mật khẩu'])[1]")
    FIRST_STORE_EDIT = (By.XPATH, "((//div[contains(@class,'branchmanagement-container')])[1]//button[normalize-space()='Chỉnh sửa'])[1]")
    FIRST_SWITCH_BUTTON = (By.XPATH, "((//div[contains(@class,'branchmanagement-container')])[1]//label[contains(@class,'rs-toggle')])[1]")
    FIRST_STORE_USERNAME = (By.XPATH, "//b[contains(text(),'Tên đăng nhập')]/following-sibling::input")
    FIRST_SWITCH = (By.XPATH, "((//div[contains(@class,'branchmanagement-container')])[1]//input[@role='switch'])[1]")
    FIRST_PHONE_NUMBER = (By.XPATH, "((//div[contains(@class,'branchmanagement-container')])[1]//span[contains(normalize-space(.), 'Số điện thoại:')])[1]")
# STORE INFO MODAL
    MODAL_FULL = (By.XPATH, "//div[@class='rs-modal-content']")
    MODAL_UPLOAD_IMAGE_BUTTON = (By.XPATH,"//span[contains(text(),'Cần tải ảnh cửa hàng lên')]/ancestor::button")
    MODAL_UPLOAD_INPUT = (By.XPATH,"(//input[@type='file'])[1]")
    MODAL_STORE_NAME = (By.XPATH,"//div[@role='row'][.//b[contains(text(),'Tên cửa hàng')]]//input")
    MODAL_USER_NAME = (By.XPATH,"//b[contains(text(),'Tên đăng nhập')]/following::input[1]")
    MODAL_ADDRESS = (By.XPATH,"//b[contains(text(),'Địa chỉ')]/following::textarea[1]")
    MODAL_GPS = (By.XPATH, "//div[contains(@class,'abm-textarea')][.//b[contains(normalize-space(.), 'GPS')]]//input")
    MODAL_MANAGER_NAME = (By.XPATH, "//div[contains(@class,'abm-textarea')][.//b[contains(normalize-space(.), 'Tên người phụ trách')]]//input")
    MODAL_MANAGER_PHONE = (By.XPATH, "//div[contains(@class,'abm-textarea')][.//b[contains(normalize-space(.), 'Số điện thoại người phụ trách')]]//input")
    MODAL_CUSTOMER_SERVICE_PHONE = (By.XPATH, "//div[contains(@class,'abm-textarea')][.//b[contains(normalize-space(.), 'Số điện thoại chăm sóc khách hàng')]]//input")
    MODAL_SALES_CODE = (By.XPATH, "//div[contains(@class,'abm-textarea')][.//b[contains(normalize-space(.), 'Mã nhân viên kinh doanh')]]//input")
    MODAL_PASSWORD = (By.XPATH, "//div[contains(@class,'abm-select')][.//b[contains(normalize-space(.), 'Mật khẩu')]]//input[@type='password']")
    MODAL_CONFIRM_PASSWORD = (By.XPATH, "//div[contains(@class,'abm-select')][.//b[contains(normalize-space(.), 'Nhập lại mật khẩu')]]//input[@type='password']")
    MODAL_COMMISSION = (By.XPATH, "//div[contains(@class,'abm-textarea')][.//b[contains(normalize-space(.), 'Hoa hồng')]]//input")
    MODAL_TRANSFER_LIMIT = (By.XPATH, "//div[contains(@class,'abm-textarea')][.//b[contains(normalize-space(.), 'Giới hạn mức chuyển điểm')]]//input")
    MODAL_MIN_WALLET_BALANCE = (By.XPATH, "//div[contains(@class,'abm-textarea')][.//b[contains(normalize-space(.), 'Số dư tối thiểu')]]//input")
    MODAL_POINT_RATE = (By.XPATH, "//div[contains(@class,'abm-textarea')][.//b[contains(normalize-space(.), 'Tỷ lệ tích điểm')]]//input")
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
