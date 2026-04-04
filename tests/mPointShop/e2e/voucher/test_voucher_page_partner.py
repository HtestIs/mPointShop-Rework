from time import sleep

import pytest
import allure

from api.mPointShop.endpoints.store_api import StoreAPI
from api.mPointShop.endpoints.voucher_api import VoucherAPI
from api.mPointShop.helpers.store_helpers import add_store_to_voucher_payload, get_stores_names


@pytest.mark.e2e
@pytest.mark.api
@allure.story("Voucher page")
@allure.title("Partner can create voucher")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("voucher_type",[
    "cash_multiple", 
    "discount_percentage", 
    "discount_constant", 
    "gift"],ids=["Pre-paid voucher","Percentage discount voucher","Constant discount voucher","Gift voucher"])
def test_partner_create_voucher_page(voucher_data, logged_in_client_partner,login_partner_success,voucher_type): ## <--- delete this
    # Step 1: Create voucher page
    voucher_page = VoucherAPI(client = logged_in_client_partner)
    payload = voucher_data(vouchertype=voucher_type)
    response = voucher_page.create_voucher(payload=payload)
    assert response.status_code == 200
    menu = login_partner_success
    voucher_ui = menu.navigate_to_voucher_manage()
    voucher_ui.search_voucher_and_wait(payload["name"])
    first_voucher_name = voucher_ui.get_first_voucher_name()
    assert payload["name"] == first_voucher_name, "Voucher name on UI does not match created voucher name"

@pytest.mark.e2e
@pytest.mark.api
@pytest.mark.slow
def test_sync_voucher_to_mExchange(logged_in_client_partner,create_cash_multiple_voucher,login_partner_success):
# API Magic
# 1. Create voucher via api
    response = create_cash_multiple_voucher
# 2. Get voucher ID from response
    voucher_id = response.json()["data"]["id"]
# 3. Get list of stores
    store_api = StoreAPI(client=logged_in_client_partner)
    store_response = store_api.get_store_list(params={"page": 1, "pageSize": 100})
    assert store_response.status_code == 200, f"Failed to get store list"
# 4. Create payload to add store(s) to voucher
    payload = add_store_to_voucher_payload(store_response.json(),voucher_id)
# 5. Move to Voucher Client and add store(s) to voucher using the sync endpoint
    voucher_api = VoucherAPI(client=logged_in_client_partner)
    add_store_response = voucher_api.add_store_to_voucher(payload=payload)
    assert add_store_response.status_code == 200, f"Failed to add store(s) to voucher"
# 6. Sync voucher to mExchange
    sync_response = voucher_api.sync_voucher_to_mexchange(payload={"id": voucher_id})
    assert sync_response.status_code == 200, f"Failed to sync voucher to mExchange"
# E2E Lame thingy
    menu = login_partner_success
    voucher_ui = menu.navigate_to_voucher_manage()
    # voucher_ui.hover_store_span()
    tooltip_names = voucher_ui.get_tooltip_stores_names()
    assert tooltip_names == get_stores_names(store_response.json(),payload), "Store names in tooltip do not match the store names added to voucher"
    voucher_ui.wait_until_synced()
    assert voucher_ui.get_status_store_text() == "Đã được đồng bộ", "Voucher status is not Active after syncing to mExchange"
