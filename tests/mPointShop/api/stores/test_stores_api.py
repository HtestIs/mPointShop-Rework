import pytest
from api.mPointShop.endpoints.store_api import StoreAPI
from api.mPointShop.api_assertions.store_assertions import assert_code_response, assert_valid_post_response, assert_validation_error_type, assert_store_page_response, assert_store_response
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

@pytest.mark.api
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
@pytest.mark.api
@pytest.mark.parametrize("missing_field", [
    "address", "district", "image", "lat", "lng", "nameStore", 
    "password", "phoneStore", "province", 
    "storeOwnerName", "storeOwnerPhone", "username","ward"
    ], ids=[
    "missing_address", "missing_district", "missing_image", "missing_lat", "missing_lng", "missing_nameStore", 
    "missing_password", "missing_phoneStore", "missing_province", 
    "missing_storeOwnerName", "missing_storeOwnerPhone", "missing_username", "missing_ward"
    ])
def test_create_store_missing_required_fields(logged_in_client_partner, store_api_data, missing_field):
    store_api = StoreAPI(client=logged_in_client_partner)
    payload = store_api_data.copy()
    payload.pop(missing_field)  # Remove the required field to test missing field validation
    response = store_api.create_store(payload=payload)
    # store_api.client.debug_response(response)
    assert_code_response(response=response, status_code=422, expected_code=422, expected_message="Tham số đầu vào không hợp lệ!")

@pytest.mark.api
@pytest.mark.parametrize("payload", [
    {"skip": 0, "limit": 10, "name": "Craft Store", "phone": "0393704472"},
    {"skip": 0, "limit": 10, "name": "Craft Store"},
    {"skip": 0, "limit": 10, "phone": "0393704472"},
    {"skip": 0, "limit": 10}
], ids=["full_payload", "name_only", "phone_only", "pagination_only"])
def test_search_store_valid_payload(logged_in_client_partner, payload):
    store_api = StoreAPI(client=logged_in_client_partner)
    response = store_api.search_store(payload=payload)
    assert_code_response(response=response, status_code=200, expected_code=0)

@pytest.mark.api
@pytest.mark.parametrize("payload", [
    {"skip": 0, "limit": 10, "name": "", "phone": ""},
    {"skip": 0, "limit": 10, "name": ""},
    {"skip": 0, "limit": 10, "phone": ""}  
], ids=["empty_field", "empty_name_no_phone", "empty_phone_no_name"])
def test_search_store_empty_fields(logged_in_client_partner, payload):
    store_api = StoreAPI(client=logged_in_client_partner)
    response = store_api.search_store(payload=payload)
    assert_code_response(response=response, status_code=422, expected_code=422, expected_message="Tham số đầu vào không hợp lệ!")

@pytest.mark.api
@pytest.mark.parametrize("payload,response_code",[
    ({"skip": -1, "limit": 10, "name": "Craft Store", "phone": "0393704472"}, 200),
    ({"limit": 10, "name": "Craft Store", "phone": "0393704472"}, 422),
    ({"skip": 0, "limit": -10, "name": "Craft Store", "phone": "0393704472"}, 200),
    ({"skip": 0, "name": "Craft Store", "phone": "0393704472"}, 422),
    ({"skip": 0, "limit": 10, "name": ["Craft Store"], "phone": "0393704472"}, 422),
    ({"skip": 0, "limit": 10, "name": "Craft Store", "phone": ["0393704472"]}, 422),
]
, ids=["negative_skip", "missing_skip", "negative_limit", "missing_limit", "invalid_name_type", "invalid_phone_type"]
)
def test_search_store_invalid_payload(logged_in_client_partner, payload, response_code):
    store_api = StoreAPI(client=logged_in_client_partner)
    response = store_api.search_store(payload=payload)
    # store_api.client.debug_response(response)
    assert_code_response(response=response, status_code=response_code, expected_code=422)   