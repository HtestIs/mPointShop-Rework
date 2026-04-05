from api.mPointShop.endpoints.store_api import StoreAPI
from api.mPointShop.endpoints.voucher_api import VoucherAPI
from api.mPointShop.helpers.store_helpers import add_store_to_voucher_payload

def create_and_sync_voucher_to_mexchange(client, voucher_response):
    voucher_id = voucher_response.json()["data"]["id"]

    store_api = StoreAPI(client)
    store_response = store_api.get_store_list(params={"page": 1, "pageSize": 100})

    payload = add_store_to_voucher_payload(store_response.json(), voucher_id)

    voucher_api = VoucherAPI(client)
    add_store_response = voucher_api.add_store_to_voucher(payload=payload)
    response = voucher_api.sync_voucher_to_mexchange(payload={"id": voucher_id})
    return {
        "voucher_id": voucher_id,
        "store_response": store_response,
        "payload": payload,
        "add_store_response": add_store_response,
        "sync_response": response,
    }