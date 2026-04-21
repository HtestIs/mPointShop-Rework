import pytest
import allure
from time import sleep

pytestmark = [
    pytest.mark.mpointshop,
    allure.parent_suite("mPointShop"),
    allure.suite("E2E"),
    allure.sub_suite("Warehouse"),
]

@pytest.mark.e2e
@allure.feature("Warehouse Management")
@allure.story("Product management")
@allure.title("Navigate to product creation page")
@allure.severity(allure.severity_level.NORMAL)
def test_navigate_to_product_creating(login_partner_success):
    menu = login_partner_success
    page = menu.navigate_to_warehouse()
    create_product_page = page.click_add_product()
    # sleep(5)
    # page.test_debug_add_product()
