from api.mExchange.endpoints.voucher_api import mExchangeVoucherAPI


def find_voucher_pool_in_mexchange(client, alt_voucher_id):
    voucher_api = mExchangeVoucherAPI(client=client)
    find_response = voucher_api.get_find_voucher_pools(params={"alt_voucher_id": alt_voucher_id})
    data = find_response.json()
    voucher_pools = data.get("voucher_pools", [])
    voucher_id = voucher_pools[0].get("voucher_id") if voucher_pools else None

    return {
        "alt_voucher_id": alt_voucher_id,
        "find_response": find_response,
        "data": data,
        "voucher_pools": voucher_pools,
        "voucher_id": voucher_id,
        "voucher_api": voucher_api
    }


def find_and_commit_voucher_pool_in_mexchange(client, alt_voucher_id, state="accepted"):
    result = find_voucher_pool_in_mexchange(client, alt_voucher_id)

    if result["voucher_id"] is None:
        raise ValueError(f"Voucher pool not found in mExchange for alt_voucher_id={alt_voucher_id}")

    payload = {
        "voucher_id": result["voucher_id"],
        "state": state,
    }

    voucher_api = mExchangeVoucherAPI(client=client)
    commit_response = voucher_api.post_commit_voucher_pool(payload=payload)

    return {
        **result,
        "payload": payload,
        "commit_response": commit_response,
        "voucher_api": voucher_api
    }
