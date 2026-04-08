import pytest
import allure
from time import sleep
@pytest.mark.mshopadmin
@pytest.mark.e2e
@pytest.mark.defect
def test_voucher_list_expand_search(login_aap_success):
    dashboard_page = login_aap_success
    voucher_list_page = dashboard_page.navigate_to_voucher_list()
    voucher_list_page.expand_search()
    voucher_list_page.search_by_alt_id("voud7ahk7t0bemc73d6nrt0")
    voucher_list_page.search()
    sleep(3)