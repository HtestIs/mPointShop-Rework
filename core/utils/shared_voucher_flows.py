from mExchange.api.flows.voucher_flow import find_and_commit_voucher_pool_in_mexchange, sync_voucher_to_partner
from mPointShop.api.flows.voucher_flow import create_and_sync_voucher_to_mexchange
from mShopAdmin.api.endpoints.customer_voucher_api import CustomerVoucherAPI
from mShopAdmin.api.endpoints.voucher_api import VoucherAPI
from mShopAdmin.api.helpers.voucher_helpers import create_approve_params, create_find_params, wait_for_voucher


def create_commit_and_sync_voucher_to_partner(
    mpointshop_client,
    voucher_response,
    mexchange_client,
    partner_id="$mpoint",
):
    result = create_and_sync_voucher_to_mexchange(mpointshop_client, voucher_response)
    commit_result = find_and_commit_voucher_pool_in_mexchange(
        mexchange_client,
        result["voucher_id"],
    )

    partner_sync_payload = {
        "type": "SYNC_ONE_PARTNER",
        "ids": [commit_result["payload"]["voucher_id"]],
        "partner_id": partner_id,
        "includes": "partner,voucher,total,stores",
    }
    partner_sync_response = commit_result["voucher_api"].post_sync_voucher_to_partner(
        payload=partner_sync_payload
    )

    return {
        **result,
        "commit_result": commit_result,
        "partner_sync_payload": partner_sync_payload,
        "partner_sync_response": partner_sync_response,
        "mexchange_voucher_id": commit_result["payload"]["voucher_id"],
    }


def get_synced_partner_voucher_alt_id(
    mpointshop_client,
    voucher_response,
    mexchange_client,
    partner_id="$mpoint",
):
    result = create_commit_and_sync_voucher_to_partner(
        mpointshop_client,
        voucher_response,
        mexchange_client,
        partner_id=partner_id,
    )

    assert result["add_store_response"].status_code == 200, "Failed to add store to voucher"
    assert result["sync_response"].status_code == 200, "Failed to sync voucher to mExchange"
    assert result["commit_result"]["find_response"].status_code == 200, "Voucher not found in mExchange"
    assert result["commit_result"]["commit_response"].status_code == 200, "Failed to commit voucher in mExchange"
    assert result["partner_sync_response"].status_code == 200, "Failed to sync voucher to partner"

    return result["voucher_id"]

def get_code(response,partner_client,exchange_client,mshopadmin_client,app_client):
    result = create_and_sync_voucher_to_mexchange(partner_client, response)
    commit_result = find_and_commit_voucher_pool_in_mexchange(exchange_client, result["voucher_id"])
    sync_voucher_to_partner(commit_result["voucher_api"], commit_result["payload"]["voucher_id"])
    voucher_id = commit_result["payload"]["voucher_id"]
    params = create_find_params(page=308, api="find", voucher_id=voucher_id)
    voucher_page = VoucherAPI(mshopadmin_client)
    find_response = wait_for_voucher(voucher_page,params)
    params_approve = create_approve_params(page=308)
    admin_portal_voucher_id = find_response.json()["data"][0]["id"]
    payload ={
        "id": admin_portal_voucher_id,
        "isApprove": True,
    }
    approve_response = voucher_page.update_voucher(voucher_id=admin_portal_voucher_id,payload=payload ,params=params_approve)
    data_approve = approve_response.json()
    voucher_app_id = data_approve["data"]["id"]
    voucher_app = CustomerVoucherAPI(app_client)
    payload_order = {
    "listOrderItems": [
    {
      "type": "voucher",
      "typeId": voucher_app_id,
      "quantity": 1
        }
    ]
    }
    response = voucher_app.create_order(payload = payload_order)
    data = response.json()
    code = data["orderItemInfos"][0]["code"]["code"]
    return code