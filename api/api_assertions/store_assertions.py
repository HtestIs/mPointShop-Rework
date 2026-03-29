import math
def assert_store_response(page,pageSize,body: dict):
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