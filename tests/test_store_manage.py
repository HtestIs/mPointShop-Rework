from pages.store_manage_page import StoreManage
from pages.login_page import LoginPage
import pytest
import allure
from time import sleep
from faker import Faker

fake = Faker('vi_VN')
@allure.story("Finding stores")
@allure.title("Find store with name")
@allure.severity(allure.severity_level.NORMAL)
def test_find_store_with_name(login_partner_success):
    keyword = "Craft Mbeer"
    login_partner_success.find_store_with_name(keyword)
    login_partner_success.wait_loading_overlay()
    assert keyword in login_partner_success.get_store_name()
@allure.story("Finding stores")
@allure.title("Find store with phone number")
@allure.severity(allure.severity_level.NORMAL)
def test_find_store_with_phone(login_partner_success):
    keyword = "0393254477"
    login_partner_success.find_store_with_number(keyword)
    login_partner_success.wait_loading_overlay()
    assert keyword in login_partner_success.get_store_name()

@allure.story("Changing store password")
@allure.title("Change store password")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("password,toast",[
    ("123456789","Thành công"),
    ("","Vui")
    ])
def test_change_store_password(login_partner_success,password,toast):
    login_partner_success.change_password(password)
    assert toast in login_partner_success.get_toast_msg()

@allure.story("Locking stores")
@allure.title("Lock store")
@allure.severity(allure.severity_level.CRITICAL)
def test_lock_store(login_partner_success):
    login_partner_success.ensure_locked()
    locked_username = login_partner_success.get_store_username()
    login_partner_success.hover_user()
    login = login_partner_success.click_logout()
    login.fill_login(locked_username,"1")
    assert "Tài khoản đang bị khóa!" in login.get_toast_message()
    assert "/login" in login.get_current_url()
@allure.story("User choosing inferior location")
@allure.title("Options management")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.parametrize("setup,target_field",[
    ("missing_city", "district_old"),
    ("missing_city", "ward_old"),   
    ("missing_district", "ward_old"),
    ("missing_city_new", "ward_new")
])
def test_dropdown_location(login_partner_success,storedata,setup,target_field):
    page = login_partner_success
    page.click_add_new_store()
    page.setup_location(setup,storedata)
    page.click(page.FORM_FIELDS[target_field])
    options = page.has_selectable_option()
    assert options is False, f"Dropdown options for {target_field} should be empty when required location is missing"
    
@allure.story("Registering stores")
@allure.title("Register store")
@allure.severity(allure.severity_level.CRITICAL)
def test_new_store_registration(login_partner_success,storedata):
    login_partner_success.fill_form_store_register(storedata,with_dropdown=True)

@allure.story("Registering stores")
@allure.title("Register store with missing required fields")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("field, field_name",[
    ("name", "Tên cửa hàng"),
    ("username", "Tên đăng nhập"),
    ("address", "Địa chỉ"),
    ("gps", "GPS"),
    ("manager_name", "Tên người phụ trách"),
    ("manager_phone", "Số điện thoại người phụ trách"),
    ("customer_service_phone", "Số điện thoại chăm sóc khách hàng"),
    ("password", "Mật khẩu"),
    ("confirm_password", "Nhập lại mật khẩu"),
])
def test_missing_field_store_registration(login_partner_success,storedata,field,field_name):
    data = storedata.copy()
    data[field] = ""
    login_partner_success.fill_form_store_register(data,with_dropdown=True)
    assert "bắt buộc" in login_partner_success.get_field_error(field_name)

@allure.story("Registering stores")
@allure.title("Register store with missing dropdown fields")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("field, field_name",[
    ("city_old", "Tỉnh/TP"),
    ("district_old", "Quận/Huyện"),
    ("ward_old", "Xã/Phường"),
    ("city_new", "Tỉnh/TP (mới theo 2025)"),
    ("ward_new", "Xã/Phường (mới theo 2025)")
])
def test_missing_dropdown_store_registration(login_partner_success,storedata,field,field_name):
    data = storedata.copy()
    data[field] = ""
    login_partner_success.click_add_new_store()
    login_partner_success.enter_value(data)
    login_partner_success.choose_date()
    login_partner_success.click_confirm_button_user_modal()
    assert "bắt buộc" in login_partner_success.get_field_error(field_name)
