import pytest
from api.endpoints.store_api import StoreAPI
from api.api_assertions.store_assertions import assert_code_response, assert_valid_post_response, assert_validation_error_type, assert_store_page_response, assert_store_response
@pytest.mark.api
@pytest.mark.parametrize("page,pageSize", [
    (1, 10),
    (2, 5),
    (3, 20),
    (4, 15),
    (5, 30)
])
def test_get_store_list_api(logged_in_client_partner, page, pageSize):
    store_api = StoreAPI(client=logged_in_client_partner)
    params = {"page": page, "pageSize": pageSize}
    response = store_api.get_store_list(params=params)
    # store_api.client.debug_response(response)
    assert_code_response(response, status_code=200, expected_code=0)
    assert_store_response(page=page, pageSize=pageSize, data=response) 
@pytest.mark.api
def test_get_store_list_unauthorized(api_client):
    store_api = StoreAPI(client=api_client)
    response = store_api.get_store_list()
    # store_api.client.debug_response(response)
    assert_code_response(response=response, status_code=401, expected_code=401, expected_message="Token này đã hết hạn", expected_type="ERR_TOKEN_EXPIRED")
@pytest.mark.api
def test_get_store_list_invalid_token(api_client):
    store_api = StoreAPI(client=api_client)
    api_client.set_token("invalid_token")
    response = store_api.get_store_list()
    # store_api.client.debug_response(response)
    assert_code_response(response=response, status_code=401, expected_code=401, expected_message="Token này đã hết hạn", expected_type="ERR_TOKEN_EXPIRED")
@pytest.mark.api
@pytest.mark.parametrize("page,pageSize,type_text", [
    (-1, 10,"numberMin"),
    (1, -5,"numberMin"),
    (0, 20,"numberMin"),
    ("abc", 15,"number"),
    (1, "abc","number"),
    (1.5, 10,"numberInteger"),
    (1, 10.5,"numberInteger"),
],ids=["negative_page", "negative_pageSize", "zero_page", "non_numeric_page", "non_numeric_pageSize", "float_page", "float_pageSize"])
def test_get_store_list_invalid_page_params(logged_in_client_partner,page,pageSize,type_text):
    store_api = StoreAPI(client=logged_in_client_partner)
    params = {"page": page, "pageSize": pageSize}
    response = store_api.get_store_list(params=params)
    # store_api.client.debug_response(response)
    assert_code_response(response=response, status_code=422, expected_code=422, expected_message="Tham số đầu vào không hợp lệ!")
    assert_validation_error_type(response=response, expected_type=type_text) 
@pytest.mark.api
@pytest.mark.parametrize("page,pageSize,expectedPageSize", [
    (1, 1000,100),
    (10, 0,10),
],ids=["pageSize_too_big","pageSize_too_small"])
def test_get_store_list_pageSize_edge_cases(logged_in_client_partner, page, pageSize, expectedPageSize):
    store_api = StoreAPI(client=logged_in_client_partner)
    params = {"page": page, "pageSize": pageSize}
    response = store_api.get_store_list(params=params)
    # store_api.client.debug_response(response)
    assert_code_response(response=response, status_code=200, expected_code=0)
    assert_store_page_response(data =response, expected_pageSize = expectedPageSize)
@pytest.mark.api
def test_get_store_list_exceeds_max_page(logged_in_client_partner):
    store_api = StoreAPI(client=logged_in_client_partner)
    params_prerequisite = {"page": 1, "pageSize": 10}
    response_prerequisite = store_api.get_store_list(params=params_prerequisite)
    body_prerequisite = response_prerequisite.json()
    exceed_page = body_prerequisite["totalPages"] + 1
    params = {"page": exceed_page, "pageSize": 10}
    response = store_api.get_store_list(params=params)
    # store_api.client.debug_response(response)
    body = response.json()
    assert_code_response(response=response, status_code=200, expected_code=0)
    assert isinstance(body["data"], list), f"Expected data to be a list, got {type(body['data'])}"
    assert len(body["data"]) == 0, f"Expected data list to be empty for page exceeding totalPages, got {len(body['data'])}"
@pytest.mark.api
def test_post_store_list_not_allowed(logged_in_client_partner):
    store_api = StoreAPI(client=logged_in_client_partner)
    response = store_api.post_store_list()
    # store_api.client.debug_response(response)
    assert_code_response(response=response, status_code=404, expected_code=404, expected_type="SERVICE_NOT_FOUND")

@pytest.mark.api
@pytest.mark.parametrize("params", [
    {"page": 1},
    {"pageSize": 10},
    {"unexpectedParam": "value"},
    {},
    {"page": None, "pageSize": None}
], ids=["no_pageSize", "no_page", "unexpected_param", "empty_dict", "null_params"])
def test_missing_or_unexpected_params_get_store_list(logged_in_client_partner, params):
    store_api = StoreAPI(client=logged_in_client_partner)
    response = store_api.get_store_list(params=params)
    # store_api.client.debug_response(response)
    assert_code_response(response=response, status_code=200, expected_code=0)
    assert_store_page_response(data=response, expected_page=params.get("page"), expected_pageSize=params.get("pageSize"))

@pytest.mark.api
def test_create_store_no_payload(logged_in_client_partner):
    store_api = StoreAPI(client=logged_in_client_partner)
    response = store_api.create_store(payload=None)
    store_api.client.debug_response(response)
    assert_code_response(response=response, status_code=422, expected_code=422, expected_type="VALIDATION_ERROR")

@pytest.mark.ongoing
def test_create_store_valid_payload(logged_in_client_partner,store_api_data):
    store_api = StoreAPI(client=logged_in_client_partner)
    
    payload = store_api_data.copy()
    response = store_api.create_store(payload=payload)
    store_api.client.debug_response(response)
    assert_code_response(response=response, status_code=200, expected_code=0)
    assert_valid_post_response(response=response, payload=payload)
# TODO: Add more test cases for create_store endpoint, such as invalid payload, missing required fields, etc.
# yo mf, put a parametrize here for different invalid payloads to test the validation of the create_store endpoint
@pytest.mark.api
def test_create_store_invalid_payload(logged_in_client_partner,store_api_data):
    store_api = StoreAPI(client=logged_in_client_partner)
    # Create a copy of the valid payload and remove a required field to make it invalid
    payload = store_api_data.copy()
    payload["nameStore"] = ""  # Assuming 'name' is a required field, setting it to empty string to make it invalid
    response = store_api.create_store(payload=payload)
    store_api.client.debug_response(response)
    assert_code_response(response=response, status_code=200, expected_code=1, expected_message="not_found_name")

# TODO 2: yo mf, pop the payload to test the missing required field validation, and add more cases for other required fields and invalid values