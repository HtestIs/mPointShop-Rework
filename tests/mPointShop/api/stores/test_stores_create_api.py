import allure
import pytest

from api.mPointShop.api_assertions.store_assertions import assert_code_response, assert_valid_post_response
from api.mPointShop.endpoints.store_api import StoreAPI


@pytest.mark.api
@allure.story("Store creation")
@allure.title("Create store without payload returns validation error")
@allure.severity(allure.severity_level.NORMAL)
def test_create_store_no_payload(logged_in_client_partner):
    store_api = StoreAPI(client=logged_in_client_partner)
    response = store_api.create_store(payload=None)
    # store_api.client.debug_response(response)
    assert_code_response(response=response, status_code=422, expected_code=422, expected_type="VALIDATION_ERROR")


@pytest.mark.api
@allure.story("Store creation")
@allure.title("Create store with valid payload succeeds")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_store_valid_payload(logged_in_client_partner, store_api_data):
    store_api = StoreAPI(client=logged_in_client_partner)
    payload = store_api_data.copy()
    response = store_api.create_store(payload=payload)
    # store_api.client.debug_response(response)
    assert_code_response(response=response, status_code=200, expected_code=0)
    assert_valid_post_response(response=response, payload=payload)


@pytest.mark.api
@allure.story("Store creation")
@allure.title("Create store with invalid payload returns business error")
@allure.severity(allure.severity_level.NORMAL)
def test_create_store_invalid_payload(logged_in_client_partner, store_api_data):
    store_api = StoreAPI(client=logged_in_client_partner)
    payload = store_api_data.copy()
    payload["nameStore"] = ""
    response = store_api.create_store(payload=payload)
    # store_api.client.debug_response(response)
    assert_code_response(response=response, status_code=200, expected_code=1, expected_message="not_found_name")


@pytest.mark.api
@pytest.mark.parametrize(
    "missing_field",
    [
        "address",
        "district",
        "image",
        "lat",
        "lng",
        "nameStore",
        "password",
        "phoneStore",
        "province",
        "storeOwnerName",
        "storeOwnerPhone",
        "username",
        "ward",
    ],
    ids=[
        "missing_address",
        "missing_district",
        "missing_image",
        "missing_lat",
        "missing_lng",
        "missing_nameStore",
        "missing_password",
        "missing_phoneStore",
        "missing_province",
        "missing_storeOwnerName",
        "missing_storeOwnerPhone",
        "missing_username",
        "missing_ward",
    ],
)
@allure.story("Store creation")
@allure.title("Create store validates missing required fields")
@allure.severity(allure.severity_level.NORMAL)
def test_create_store_missing_required_fields(logged_in_client_partner, store_api_data, missing_field):
    store_api = StoreAPI(client=logged_in_client_partner)
    payload = store_api_data.copy()
    payload.pop(missing_field)
    response = store_api.create_store(payload=payload)
    assert_code_response(
        response=response,
        status_code=422,
        expected_code=422,
        expected_message="Tham số đầu vào không hợp lệ!",
    )
