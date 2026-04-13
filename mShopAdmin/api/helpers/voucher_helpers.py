import time
import json

from mShopAdmin.api.endpoints.voucher_api import VoucherAPI


def create_find_params(page, api, voucher_id):
    params = {
            "page": page,
            "api": api,
            "queryInput": json.dumps({
                "voucherId": {
                    "contains": voucher_id
                }
            }),
            "limit": 10,
            "skip": 0,
            "sort": json.dumps([
                {"id": "desc"}
            ])
    }
    return params

def create_approve_params(page):
    params = {
        "page": page,
        "api": "toggleApprove"
    }
    return params

#TODO: Clean this mess later, this is just to get the test working for now. 
# We should have a more robust way of waiting for the voucher to be available in the system
#  instead of just sleeping for a fixed amount of time. ahahaha
def wait_for_voucher(voucher_api, params, timeout=20, interval=2):
    end_time = time.time() + timeout

    while time.time() < end_time:
        response = voucher_api.find_voucher(params=params)
        if response.status_code == 200 and response.json().get("count", 0) > 0:
            return response
        time.sleep(interval)

    raise AssertionError(f"Voucher not found. Params: {params}")