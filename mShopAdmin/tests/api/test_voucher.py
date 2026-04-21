import json

import pytest
import allure
from time import sleep

from core.utils.shared_voucher_flows import get_synced_partner_voucher_alt_id
from mExchange.api.flows.voucher_flow import find_and_commit_voucher_pool_in_mexchange, sync_voucher_to_partner
from mPointShop.api.flows.voucher_flow import create_and_sync_voucher_to_mexchange
from mShopAdmin.api.endpoints.voucher_api import VoucherAPI
from mShopAdmin.api.helpers.voucher_helpers import create_approve_params, create_find_params, wait_for_voucher

pytestmark = [
    pytest.mark.mshopadmin,
    allure.parent_suite("mShopAdmin"),
    allure.suite("API"),
    allure.sub_suite("Voucher Management"),
]

@pytest.mark.api
@allure.story("Voucher searching")
@allure.title("Find voucher with alternative ID")
@allure.severity(allure.severity_level.NORMAL)
def test_finding_voucher_with_alt_id(mshopadmin_api_client_with_token):
    voucher_page = VoucherAPI(mshopadmin_api_client_with_token)
    params = create_find_params(page=308, api="find", voucher_id="voud7dr8b50bemc73d6nsi0")
    response = voucher_page.find_voucher(params=params)
    data = response.json()
    # voucher_page.client.debug_response(response)
    assert response.status_code == 200, "Expected status code 200"
    assert data["count"] > 0, "Expected at least one voucher to be found"

def test_approve_voucher(mshopadmin_api_client_with_token):
    voucher_page = VoucherAPI(mshopadmin_api_client_with_token)
    params = create_approve_params(page=308)
    payload ={
        "id": 128,
        "isApprove": True,
}
    response = voucher_page.update_voucher(voucher_id=128,payload=payload ,params=params)
    data = response.json()
    voucher_page.client.debug_response(response)
    assert response.status_code == 200
    assert data["code"] == 0, "Expected code 0 for successful approval"

@pytest.mark.api
@pytest.mark.mpointshop
@pytest.mark.mexchange
@allure.story("Voucher approval workflow")
@allure.title("Approve synced voucher across systems")
@allure.severity(allure.severity_level.CRITICAL)
def test_approve_synced_voucher(mshopadmin_api_client_with_token, create_cash_multiple_voucher, mpointshop_logged_in_client_partner, mexchange_client_ui):
#1: mPointShop: Create voucher and sync to mExchange
    response = create_cash_multiple_voucher
    result = create_and_sync_voucher_to_mexchange(mpointshop_logged_in_client_partner, response)
#2: mExchange: Find and commit the voucher pool
    commit_result = find_and_commit_voucher_pool_in_mexchange(mexchange_client_ui, result["voucher_id"])
    sync_voucher_to_partner(commit_result["voucher_api"], commit_result["payload"]["voucher_id"])
    voucher_id = commit_result["payload"]["voucher_id"]
#3: mShopAdmin: Find the synced voucher using alt_id and approve it
    params = create_find_params(page=308, api="find", voucher_id=voucher_id)
    voucher_page = VoucherAPI(mshopadmin_api_client_with_token)
    find_response = wait_for_voucher(voucher_page,params)
    # voucher_page.client.debug_response(find_response)
    assert find_response.status_code == 200, "Expected status code 200 when finding voucher"
    params_approve = create_approve_params(page=308)
    admin_portal_voucher_id = find_response.json()["data"][0]["id"]
    payload ={
        "id": admin_portal_voucher_id,
        "isApprove": True,
    }
#4: Approve the voucher in mShopAdmin and verify the response
    approve_response = voucher_page.update_voucher(voucher_id=admin_portal_voucher_id,payload=payload ,params=params_approve)
    voucher_page.client.debug_response(approve_response)
    assert approve_response.status_code == 200, "Expected status code 200 when approving voucher"
    assert approve_response.json()["code"] == 0, "Expected code 0 for successful approval"
    assert approve_response.json()["message"] == "Update voucher successfully", "Expected success message for voucher approval"