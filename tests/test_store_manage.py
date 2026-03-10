from pages.store_manage_page import StoreManage
from pages.login_page import LoginPage
import pytest
from time import sleep

def test_find_store_with_name(login_partner_success):
    keyword = "Craft Mbeer"
    login_partner_success.find_store_with_name(keyword)
    login_partner_success.wait_loading_overlay()
    assert keyword in login_partner_success.get_store_name()

def test_find_store_with_phone(login_partner_success):
    keyword = "0393254477"
    login_partner_success.find_store_with_number(keyword)
    login_partner_success.wait_loading_overlay()
    assert keyword in login_partner_success.get_store_name()

@pytest.mark.parametrize("password,toast",[
    ("123456789","Thành công"),
    ("","Vui")
    ])
def test_change_store_password(login_partner_success,password,toast):
    login_partner_success.change_password(password)
    assert toast in login_partner_success.get_toast_msg()

def test_lock_store(login_partner_success):
    login_partner_success.ensure_locked()
    login_partner_success.toggle_store()
    assert login_partner_success.get_lock_status() == "false"
    locked_username = login_partner_success.get_store_username()
    login_partner_success.hover_user()
    login = login_partner_success.click_logout()
    print(locked_username)
    login.fill_login(locked_username,"1")
    assert "Tài khoản đang bị khóa!" in login.get_toast_message()
    assert "/login" in login.get_current_url()

@pytest.mark.parametrize("storedata", [
    {"name": "Store", 
     "username": "store", 
     "address": "somewhere", 
     "gps": "9.814872168201843/105.61238136803532", 
     "manager_name": "Mr. D", 
     "manager_phone": "0393049828", 
     "customer_service_phone": "12002302", 
     "sale_code": "1", 
     "password": "Abc@1234", 
     "confirm_password": "Abc@1234", 
     "commission": "1", 
     "min_wallet": "1", 
     "transfer_limit": "1", 
     "point_rate": "1"}
])
def test_register_new_store(login_partner_success,storedata):
    login_partner_success.fill_form_store_register(storedata)