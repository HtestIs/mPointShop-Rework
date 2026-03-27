import pytest
@pytest.mark.api
@pytest.mark.parametrize("method,send_payload, status_code, code, message", [
    ("post",True,200, 0, "Thành công"),
    ("get", False, 422, 422, "Tham số đầu vào không hợp lệ!"),
    ("get",True,200,0,"Thành công")
    ], ids=["POST method with payload", "GET method without payload", "GET method with payload"])
def test_invalid_contract_login_api(auth_api, method, send_payload, status_code, code, message, env_config):
    creds = env_config["users"]["partner"]
    payload = {
        "username": creds["username"],
        "password": creds["password"]
    }
    actual_payload = payload if send_payload else None
    response = auth_api.login_request(payload=actual_payload, method=method) 
    data = response.json()
    auth_api.client.debug_response(response)
    assert response.request.method == method.upper()
    assert response.status_code == status_code
    assert data["code"] == code
    assert data["message"] == message