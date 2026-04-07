import pytest
from mExchange.api.flows.voucher_flow import (
    find_and_commit_voucher_pool_in_mexchange,
    find_voucher_pool_in_mexchange,
    sync_voucher_to_partner,
)
from mPointShop.api.flows.voucher_flow import create_and_sync_voucher_to_mexchange


@pytest.mark.api
@pytest.mark.e2e
def test_pending_voucher(logged_in_client_partner,create_voucher_discount_constant,mexchange_client_ui):
    response = create_voucher_discount_constant
    result = create_and_sync_voucher_to_mexchange(logged_in_client_partner, response)
    voucher_result = find_voucher_pool_in_mexchange(mexchange_client_ui, result["voucher_id"])

    mexchange_client_ui.debug_response(voucher_result["find_response"])
    assert voucher_result["find_response"].status_code == 200
    assert voucher_result["data"]["total"] == 1, "Voucher pool not found in mExchange"

@pytest.mark.api
@pytest.mark.e2e
def test_commit_voucher(logged_in_client_partner,create_cash_multiple_voucher,mexchange_client_ui):
    response = create_cash_multiple_voucher
    result = create_and_sync_voucher_to_mexchange(logged_in_client_partner, response)
    commit_result = find_and_commit_voucher_pool_in_mexchange(mexchange_client_ui, result["voucher_id"])

    assert commit_result["find_response"].status_code == 200
    assert commit_result["commit_response"].status_code == 200, "Failed to commit voucher pool in mExchange"

@pytest.mark.api
@pytest.mark.e2e
def test_sync_voucher_to_partner(logged_in_client_partner,create_voucher_discount_constant,mexchange_client_ui):
    response = create_voucher_discount_constant
    result = create_and_sync_voucher_to_mexchange(logged_in_client_partner, response)
    commit_result = find_and_commit_voucher_pool_in_mexchange(mexchange_client_ui, result["voucher_id"])
    id_voucher = commit_result["payload"]["voucher_id"]
    payload = {
        "type": "SYNC_ONE_PARTNER",
        "ids": [id_voucher],
        "partner_id": "$mpoint",
        "includes": "partner,voucher,total,stores"
    }
    voucher_api = commit_result["voucher_api"]
    sync_response = voucher_api.post_sync_voucher_to_partner(payload=payload)
    assert sync_response.status_code == 200, "Failed to sync voucher to partner"