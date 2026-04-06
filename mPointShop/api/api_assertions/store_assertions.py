import math
def assert_store_response(page,pageSize,data):
    body = data.json()
    assert "data" in body, "Response should contain 'data' field"
    assert isinstance(body["data"], list), "'data' field should be a list"
    assert "total" in body, "Response should contain 'total' field"
    assert "page" in body, "Response should contain 'page' field"
    assert body["page"] == page, f"Expected page {page}, got {body['page']}"
    assert "pageSize" in body, "Response should contain 'pageSize' field"
    assert body["pageSize"] == pageSize, f"Expected pageSize {pageSize}, got {body['pageSize']}"
    assert "totalPages" in body, "Response should contain 'totalPages' field"
    assert body["totalPages"] == math.ceil(body["total"] / pageSize), f"Expected totalPages {math.ceil(body['total'] / pageSize)}, got {body['totalPages']}"
    for item in body["data"]:
        assert "id" in item, "Each menu item should contain 'id'"
        assert "mexchangeStoreId" in item, "Each menu item should contain 'mexchangeStoreId'"
        assert "name" in item, "Each menu item should contain 'name'"
        assert "mexchangePartnerId" in item, "Each menu item should contain 'mexchangePartnerId'"
        assert "partnerId" in item, "Each menu item should contain 'partnerId'"
        assert "merchantId" in item, "Each menu item should contain 'merchantId'"

def assert_code_response(response, status_code, expected_code, expected_message=None,expected_type=None):
    assert response.status_code == status_code, f"Expected status code {status_code}, got {response.status_code}"
    body = response.json()
    assert body["code"] == expected_code, f"Expected code {expected_code}, got {body['code']}"
    if expected_message is not None:
        assert body["message"] == expected_message, f"Expected message '{expected_message}', got '{body['message']}'"
    if expected_type is not None:
        assert body["type"] == expected_type, f"Expected type '{expected_type}', got '{body['type']}'"

def assert_store_page_response(data, expected_page = None, expected_pageSize = None):
    body = data.json()
    assert "data" in body, "Response body should contain 'data' key"
    if expected_page is not None:
        assert "page" in body, "Response body should contain 'page' key"
        assert body["page"] == expected_page, f"Expected page {expected_page}, got {body['page']}"
    if expected_pageSize is not None:
        assert "pageSize" in body, "Response body should contain 'pageSize' key"
        assert body["pageSize"] == expected_pageSize, f"Expected pageSize {expected_pageSize}, got {body['pageSize']}"

def assert_validation_error_type(response, expected_type):
    body = response.json()
    assert "data" in body, "Response body should contain 'data' key"
    assert isinstance(body["data"], list), "'data' should be a list"
    assert len(body["data"]) > 0, "'data' should contain at least one validation error"
    assert "type" in body["data"][0], "First validation error should contain 'type'"
    assert body["data"][0]["type"] == expected_type, (
        f"Expected validation type '{expected_type}', got '{body['data'][0]['type']}'"
    )
def assert_valid_post_response(response,payload):
    body = response.json()
    assert "code" in body, "Response should contain 'code' field"
    assert body["message"] == "Thành công", f"Expected message 'Thành công', got '{body['message']}'"
    assert "data" in body, "Response should contain 'data' field"
    assert isinstance(body["data"], dict), "'data' field should be a dictionary"  
    data = body["data"]
    lat_long_fields = f'{payload["lat"]}/{payload["lng"]}'
    assert "id" in data, "Response should contain 'id' field"
    assert "mexchangeStoreId" in data, "Response should contain 'mexchangeStoreId' field"
    assert "mexchangePartnerId" in data, "Response should contain 'mexchangePartnerId' field"
    assert "partnerId" in data, "Response should contain 'partnerId' field"
    assert "merchantId" in data, "Response should contain 'merchantId' field"
    assert data["address"] == payload["address"], f"Expected address '{payload['address']}', got '{data['address']}'"
    assert data["name"] == payload["nameStore"], f"Expected name '{payload['nameStore']}', got '{data['name']}'"
    assert data["gpsLocation"] == lat_long_fields, f"Expected GPS '{lat_long_fields}', got '{data['gpsLocation']}'"
    assert data["username"] == payload["username"], f"Expected username '{payload['username']}', got '{data['username']}'"