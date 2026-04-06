import pytest
import allure

from mPointShop.api.endpoints.store_api import StoreAPI

@pytest.mark.search
@allure.story("Finding stores")
@allure.title("Find store with name")
@allure.severity(allure.severity_level.NORMAL)
def test_find_store_with_name(login_partner_success,store_api_data,logged_in_client_partner):
#API Magic
#1 : Create store via API
    store_api = StoreAPI(client=logged_in_client_partner)
    store_api.create_store(payload=store_api_data)
#2: Get store name from created store response
    keyword = store_api_data["nameStore"]
#Lame E2E thingy
#3: Navigate to store management page
    menu = login_partner_success
    page = menu.navigate_to_store_manage()
#4: Search store with name keyword and wait for results to load
    page.find_store_with_name(keyword)
    page.wait_store_info_loaded(keyword)
    assert keyword in page.get_store_name(), "Store name in search result does not match searched keyword"



@pytest.mark.search
@allure.story("Finding stores")
@allure.title("Find store with phone number")
@allure.severity(allure.severity_level.NORMAL)
def test_find_store_with_phone(login_partner_success,store_api_data,logged_in_client_partner):
#API Magic
#1 : Create store via API
    store_api = StoreAPI(client=logged_in_client_partner)
    store_api.create_store(payload=store_api_data)
#2: Get store phone number from created store response
    keyword = store_api_data["phoneStore"]
#Lame E2E thingy
#3: Navigate to store management page
    menu = login_partner_success
    page = menu.navigate_to_store_manage()
#4: Search store with phone number keyword and wait for results to load
    page.find_store_with_number(keyword)
    page.wait_store_info_loaded(keyword)
    assert keyword in page.get_store_phone(), "Store phone number in search result does not match searched keyword"