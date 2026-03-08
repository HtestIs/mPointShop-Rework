from pages.store_manage_page import StoreManage
import pytest
from time import sleep
@pytest.mark.parametrize("keyword",[
    "Craft Mbeer",""
    ])
def test_find_store(login_partner_success,keyword):
    login_partner_success.find_store(keyword)
    assert keyword in login_partner_success.get_store_name()

@pytest.mark.parametrize("password,toast",[
    ("123456789","Thành công"),
    ("","Vui")
    ])
def test_change_store_password(login_partner_success,password,toast):
    login_partner_success.change_password(password)
    assert toast in login_partner_success.get_toast_msg()

def test_lock_store(login_partner_success):
    if login_partner_success.get_lock_status() == "false":
        login_partner_success.toggle_store()
    login_partner_success.toggle_store()
    assert login_partner_success.get_lock_status() == "false"
    login_partner_success.hover_user()
    login_partner_success.click_logout()
    