from utils.data_helpers import apply_field_value
from data.test_data import DATA_CASES
import pytest
import allure



@pytest.mark.registration
@allure.story("Registering stores")
@allure.title("Register store")
@allure.severity(allure.severity_level.CRITICAL)
def test_new_store_registration(login_partner_success,storedata):
    menu = login_partner_success
    page = menu.navigate_to_store_manage()
    page.register_new_store(storedata)
    assert "Thành công" in page.get_toast_msg()



@pytest.mark.registration
@allure.story("Registering stores")
@allure.title("Register store with missing required fields")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("field, field_name",[
    # ("image_path", "THÊM CỬA HÀNG")
    ("name", "Tên cửa hàng"),
    ("username", "Tên đăng nhập"),
    ("address", "Địa chỉ"),
    ("gps", "GPS"),
    ("manager_name", "Tên người phụ trách"),
    ("manager_phone", "Số điện thoại người phụ trách"),
    ("customer_service_phone", "Số điện thoại chăm sóc khách hàng"),
    ("password", "Mật khẩu"),
    ("confirm_password", "Nhập lại mật khẩu")
])
def test_missing_field_store_registration(login_partner_success,storedata,field,field_name):
    menu = login_partner_success
    page = menu.navigate_to_store_manage()
    data = storedata.copy()
    data[field] = ""
    page.register_new_store(data)
    assert "bắt buộc" in page.get_field_error(field_name)

@pytest.mark.registration
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
    menu = login_partner_success
    page = menu.navigate_to_store_manage()
    data = storedata.copy()
    data[field] = ""
    page.click_add_new_store()
    page.fill_store_form_fields(storedata)
    page.select_option(data)
    page.choose_date()
    page.click_confirm_button_user_modal()
    assert "bắt buộc" in page.get_field_error(field_name)

@pytest.mark.registration
@allure.story("Registering stores")
@allure.title("Register store with invalid input fields shows field error")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("field,invalid_value,location,error_msg",[
    ("gps","abc","GPS","lat/lng"),
    ("confirm_password","abcd","Nhập lại mật khẩu","không khớp"),
    ("min_wallet","1000","Số dư tối thiểu của ví điểm","lớn hơn hoặc bằng 1,000,000"),
])
def test_invalid_field_span_error(login_partner_success,storedata,field,invalid_value,location,error_msg):
    menu = login_partner_success
    page = menu.navigate_to_store_manage()
    data = storedata.copy()
    data[field] = invalid_value
    page.register_new_store(data)
    assert error_msg in page.get_field_error(location), f"Expected error message for {field} was not displayed"

@pytest.mark.registration
@allure.story("Registering stores")
@allure.title("Register store with oversized input fields")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("field,error_msg",[
    ("name", "Tham số đầu vào không hợp lệ!"),
    ("username", "Tham số đầu vào không hợp lệ!"),
    ("manager_name","Tham số đầu vào không hợp lệ!"),
    ("manager_phone","Tham số đầu vào không hợp lệ!"),
    ("customer_service_phone","Tham số đầu vào không hợp lệ!")
])
def test_register_store_shows_toast_for_oversized_input(login_partner_success,storedata,field,error_msg):
    menu = login_partner_success
    page = menu.navigate_to_store_manage()
    data = storedata.copy()
    data[field] = DATA_CASES["max_255"]()
    page.register_new_store(data)
    assert error_msg in page.get_toast_msg(), f"Expected toast error message for {field} was not displayed"

@pytest.mark.registration
@allure.story("Registering stores")
@allure.title("Register store with invalid input fields shows toast error")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("field,invalid_value,error_msg",[
    ("username","duplicate_user","Tên đăng nhập đã tồn tại trên hệ thống. Xin vui lòng thử lại !"),
    ("password", "short", "Mật khẩu từ 6-20 ký tự, ít nhất 1 chữ viết hoa, 1 kí tự đặc biệt."),
    ("password", "noupper", "Mật khẩu từ 6-20 ký tự, ít nhất 1 chữ viết hoa, 1 kí tự đặc biệt."),
    ("password", "nolower", "Mật khẩu từ 6-20 ký tự, ít nhất 1 chữ viết hoa, 1 kí tự đặc biệt."),
    ("password", "nodigit", "Mật khẩu từ 6-20 ký tự, ít nhất 1 chữ viết hoa, 1 kí tự đặc biệt."),
    ("password", "no_special", "Mật khẩu từ 6-20 ký tự, ít nhất 1 chữ viết hoa, 1 kí tự đặc biệt.")
])
def test_invalid_field_toast_error(login_partner_success,storedata,field,invalid_value,error_msg,get_dup_username):
    menu = login_partner_success
    page = menu.navigate_to_store_manage()
    data = storedata.copy()
    if invalid_value == "duplicate_user":
        value = get_dup_username
    else:
        value = DATA_CASES[invalid_value]()
    data = apply_field_value(data, field, value)
    page.register_new_store(data)
    assert error_msg in page.get_toast_msg(), f"Expected toast error message for {field} was not displayed,data used: {data['password']} / {data['username']}"
