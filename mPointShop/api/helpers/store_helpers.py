import random


def add_store_to_voucher_payload(data,voucher_id):
#Get the list of stores from the response
    stores = data["data"]
#Extract the store IDs from the list of stores
    store_ids = [store["id"] for store in stores]
# Get the total number of stores available
    max_store = len(data["data"]) 
# Randomly select how many stores to add to the voucher
    number_of_stores_to_add = random.randint(1, max_store)
# Randomly select the store IDs to add to the voucher
    ids_to_add = random.sample(store_ids, number_of_stores_to_add)
    ids_to_add.append("stoe49bab985300f815f4fa")
# Get the remaining store IDs
    remaining_ids = [store_id for store_id in store_ids if store_id not in ids_to_add] 
# Create the payload
    payload = {
        "voucherId": voucher_id,
        "storeIdsApply": ids_to_add,
        "storeIdsRemove": remaining_ids
    }
    return payload

def get_stores_names(data,payload):
    stores = data["data"]
    id = payload["storeIdsApply"]
    store_names = [store["name"] for store in stores if store["id"] in id]
    return store_names