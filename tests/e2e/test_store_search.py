import pytest
import allure

@pytest.mark.search
@allure.story("Finding stores")
@allure.title("Find store with name")
@allure.severity(allure.severity_level.NORMAL)
def test_find_store_with_name(login_partner_success):
    keyword = "Craft Mbeer"
    login_partner_success.find_store_with_name(keyword)
    login_partner_success.wait_store_info_loaded(keyword)
    assert keyword in login_partner_success.get_store_name()



@pytest.mark.search
@allure.story("Finding stores")
@allure.title("Find store with phone number")
@allure.severity(allure.severity_level.NORMAL)
def test_find_store_with_phone(login_partner_success):
    keyword = "0393254477"
    login_partner_success.find_store_with_number(keyword)
    login_partner_success.wait_store_info_loaded(keyword)
    assert keyword in login_partner_success.get_store_phone()