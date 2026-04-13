from mExchange.api.flows.voucher_flow import find_and_commit_voucher_pool_in_mexchange
from mPointShop.api.flows.voucher_flow import create_and_sync_voucher_to_mexchange


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
