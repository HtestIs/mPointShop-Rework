import pytest
from api.endpoints.store_api import StoreAPI
from api.api_assertions.store_assertions import assert_store_response
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
    data = response.json()
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert data["code"] == 0, f"Expected code 0, got {data['code']}"
    assert_store_response(page=page, pageSize=pageSize, body=data) 
@pytest.mark.api
def test_get_store_list_unauthorized(api_client):
    store_api = StoreAPI(client=api_client)
    response = store_api.get_store_list()
    # store_api.client.debug_response(response)
    body = response.json()
    assert response.status_code == 401, f"Expected status code 401 for unauthorized access, got {response.status_code}"
    assert body["code"] == 401, f"Expected code 401 for unauthorized access, got {body['code']}"
    assert body["message"] == "Token này đã hết hạn", f"Expected message 'Token này đã hết hạn' for unauthorized access, got {body['message']}"
    assert body["type"] == "ERR_TOKEN_EXPIRED", f"Expected type 'ERR_TOKEN_EXPIRED' for unauthorized access, got {body['type']}"
@pytest.mark.api
def test_get_store_list_invalid_token(api_client):
    store_api = StoreAPI(client=api_client)
    api_client.set_token("invalid_token")
    response = store_api.get_store_list()
    # store_api.client.debug_response(response)
    body = response.json()
    assert response.status_code == 401, f"Expected status code 401 for unauthorized access, got {response.status_code}"
    assert body["code"] == 401, f"Expected code 401 for unauthorized access, got {body['code']}"
    assert body["message"] == "Token này đã hết hạn", f"Expected message 'Token này đã hết hạn' for unauthorized access, got {body['message']}"
    assert body["type"] == "ERR_TOKEN_EXPIRED", f"Expected type 'ERR_TOKEN_EXPIRED' for unauthorized access, got {body['type']}"
@pytest.mark.api
@pytest.mark.parametrize("page,pageSize,type_text", [
    (-1, 10,"numberMin"),
    (1, -5,"numberMin"),
    (0, 20,"numberMin"),
    ("abc", 15,"number"),
    (1, "abc","number"),
    (1.5, 10,"numberInteger"),
    (1, 10.5,"numberInteger")
],ids=["negative_page", "negative_pageSize", "zero_page", "non_numeric_page", "non_numeric_pageSize", "float_page", "float_pageSize"])
def test_get_store_list_invalid_page_params(logged_in_client_partner,page,pageSize,type_text):
    store_api = StoreAPI(client=logged_in_client_partner)
    params = {"page": page, "pageSize": pageSize}
    response = store_api.get_store_list(params=params)
    # store_api.client.debug_response(response)
    body = response.json()
    assert response.status_code == 422, f"Expected status code 422 for invalid page parameter, got {response.status_code}"
    assert body["code"] == 422, f"Expected code 422 for invalid page parameter, got {body['code']}"
    assert body["message"] == "Tham số đầu vào không hợp lệ!", f"Expected message 'Tham số đầu vào không hợp lệ!' for invalid page parameter, got {body['message']}"
    assert body["data"][0]["type"] == type_text, f"Expected type '{type_text}' for invalid page parameter, got {body['data']['type']}"
@pytest.mark.api
def test_get_store_list_edge_case_page_exceeds_total(logged_in_client_partner):
    store_api = StoreAPI(client=logged_in_client_partner)
    params = {"page": 1000, "pageSize": 10}
    response = store_api.get_store_list(params=params)
    # store_api.client.debug_response(response)
    body = response.json()
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert body["code"] == 0, f"Expected code 0, got {body['code']}"
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
    body = response.json()
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert body["code"] == 0, f"Expected code 0, got {body['code']}"
    assert body["code"] == 0, f"Expected code 0, got {body['code']}"
    assert body["pageSize"] == expectedPageSize, f"Expected pageSize {expectedPageSize}, got {body['pageSize']}"
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
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert body["code"] == 0, f"Expected code 0, got {body['code']}"
    assert isinstance(body["data"], list), f"Expected data to be a list, got {type(body['data'])}"
    assert len(body["data"]) == 0, f"Expected data list to be empty for page exceeding totalPages, got {len(body['data'])}"
@pytest.mark.api
def test_post_store_list_not_allowed(logged_in_client_partner):
    store_api = StoreAPI(client=logged_in_client_partner)
    response = store_api.post_store_list()
    # store_api.client.debug_response(response)
    body = response.json()
    assert response.status_code == 404, f"Expected status code 404 for method not allowed, got {response.status_code}"
    assert body["code"] == 404, f"Expected code 404 for method not allowed, got {body['code']}"
    assert body["type"] == "SERVICE_NOT_FOUND", f"Expected type 'SERVICE_NOT_FOUND' for method not allowed, got {body['type']}"