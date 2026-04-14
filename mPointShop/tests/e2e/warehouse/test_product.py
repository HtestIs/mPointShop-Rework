import pytest
import allure
from time import sleep

def test_navigate_to_product_creating(login_partner_success):
    menu = login_partner_success
    page = menu.navigate_to_warehouse()
    create_product_page = page.click_add_product()
    sleep(5)
    # page.test_debug_add_product()
    