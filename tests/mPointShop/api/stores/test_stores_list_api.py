import allure
import pytest

from api.mPointShop.api_assertions.store_assertions import (
    assert_code_response,
    assert_store_page_response,
    assert_store_response,
    assert_validation_error_type,
)
from api.mPointShop.endpoints.store_api import StoreAPI


@pytest.mark.api
@pytest.mark.parametrize(
    "page,pageSize",
    [
        (1, 10),
        (2, 5),
        (3, 20),
        (4, 15),
        (5, 30),
    ],
)
@allure.story("Store listing")
@allure.title("Get store list with valid pagination")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_store_list_api(logged_in_client_partner, page, pageSize):
    store_api = StoreAPI(client=logged_in_client_partner)
    params = {"page": page, "pageSize": pageSize}
    response = store_api.get_store_list(params=params)
    assert_code_response(response, status_code=200, expected_code=0)
    assert_store_response(page=page, pageSize=pageSize, data=response)


@pytest.mark.api
@allure.story("Store listing")
@allure.title("Get store list without token returns unauthorized")
@allure.severity(allure.severity_level.NORMAL)
def test_get_store_list_unauthorized(api_client):
    store_api = StoreAPI(client=api_client)
    response = store_api.get_store_list()
    assert_code_response(
        response=response,
        status_code=401,
        expected_code=401,
        expected_message="Token này đã hết hạn",
        expected_type="ERR_TOKEN_EXPIRED",
    )


@pytest.mark.api
@allure.story("Store listing")
@allure.title("Get store list with invalid token returns unauthorized")
@allure.severity(allure.severity_level.NORMAL)
def test_get_store_list_invalid_token(api_client):
    store_api = StoreAPI(client=api_client)
    api_client.set_token("invalid_token")
    response = store_api.get_store_list()
    assert_code_response(
        response=response,
        status_code=401,
        expected_code=401,
        expected_message="Token này đã hết hạn",
        expected_type="ERR_TOKEN_EXPIRED",
    )


@pytest.mark.api
@pytest.mark.parametrize(
    "page,pageSize,type_text",
    [
        (-1, 10, "numberMin"),
        (1, -5, "numberMin"),
        (0, 20, "numberMin"),
        ("abc", 15, "number"),
        (1, "abc", "number"),
        (1.5, 10, "numberInteger"),
        (1, 10.5, "numberInteger"),
    ],
    ids=[
        "negative_page",
        "negative_pageSize",
        "zero_page",
        "non_numeric_page",
        "non_numeric_pageSize",
        "float_page",
        "float_pageSize",
    ],
)
@allure.story("Store listing")
@allure.title("Get store list validates invalid page and pageSize values")
@allure.severity(allure.severity_level.NORMAL)
def test_get_store_list_invalid_page_params(logged_in_client_partner, page, pageSize, type_text):
    store_api = StoreAPI(client=logged_in_client_partner)
    params = {"page": page, "pageSize": pageSize}
    response = store_api.get_store_list(params=params)
    assert_code_response(
        response=response,
        status_code=422,
        expected_code=422,
        expected_message="Tham số đầu vào không hợp lệ!",
    )
    assert_validation_error_type(response=response, expected_type=type_text)


@pytest.mark.api
@pytest.mark.parametrize(
    "page,pageSize,expectedPageSize",
    [
        (1, 1000, 100),
        (10, 0, 10),
    ],
    ids=["pageSize_too_big", "pageSize_too_small"],
)
@allure.story("Store listing")
@allure.title("Get store list handles pageSize edge cases")
@allure.severity(allure.severity_level.NORMAL)
def test_get_store_list_pageSize_edge_cases(logged_in_client_partner, page, pageSize, expectedPageSize):
    store_api = StoreAPI(client=logged_in_client_partner)
    params = {"page": page, "pageSize": pageSize}
    response = store_api.get_store_list(params=params)
    assert_code_response(response=response, status_code=200, expected_code=0)
    assert_store_page_response(data=response, expected_pageSize=expectedPageSize)


@pytest.mark.api
@allure.story("Store listing")
@allure.title("Get store list returns empty data when page exceeds max")
@allure.severity(allure.severity_level.NORMAL)
def test_get_store_list_exceeds_max_page(logged_in_client_partner):
    store_api = StoreAPI(client=logged_in_client_partner)
    params_prerequisite = {"page": 1, "pageSize": 10}
    response_prerequisite = store_api.get_store_list(params=params_prerequisite)
    body_prerequisite = response_prerequisite.json()
    exceed_page = body_prerequisite["totalPages"] + 1

    params = {"page": exceed_page, "pageSize": 10}
    response = store_api.get_store_list(params=params)
    body = response.json()

    assert_code_response(response=response, status_code=200, expected_code=0)
    assert isinstance(body["data"], list), f"Expected data to be a list, got {type(body['data'])}"
    assert len(body["data"]) == 0, (
        f"Expected data list to be empty for page exceeding totalPages, got {len(body['data'])}"
    )


@pytest.mark.api
@allure.story("Store listing")
@allure.title("POST on store list endpoint is not allowed")
@allure.severity(allure.severity_level.MINOR)
def test_post_store_list_not_allowed(logged_in_client_partner):
    store_api = StoreAPI(client=logged_in_client_partner)
    response = store_api.post_store_list()
    assert_code_response(
        response=response,
        status_code=404,
        expected_code=404,
        expected_type="SERVICE_NOT_FOUND",
    )


@pytest.mark.api
@pytest.mark.parametrize(
    "params",
    [
        {"page": 1},
        {"pageSize": 10},
        {"unexpectedParam": "value"},
        {},
        {"page": None, "pageSize": None},
    ],
    ids=["no_pageSize", "no_page", "unexpected_param", "empty_dict", "null_params"],
)
@allure.story("Store listing")
@allure.title("Get store list handles missing and unexpected params")
@allure.severity(allure.severity_level.NORMAL)
def test_missing_or_unexpected_params_get_store_list(logged_in_client_partner, params):
    store_api = StoreAPI(client=logged_in_client_partner)
    response = store_api.get_store_list(params=params)
    assert_code_response(response=response, status_code=200, expected_code=0)
    assert_store_page_response(
        data=response,
        expected_page=params.get("page"),
        expected_pageSize=params.get("pageSize"),
    )
