import pytest
@pytest.mark.api
@pytest.mark.parametrize("role,expected_role_descriptions", [
    ("partner", "Cửa hàng của đối tác"),
    ("merchant", "Cửa hàng")
] ,ids=["Login as partner", "Login as merchant"])
def test_valid_login(auth_api, role, expected_role_descriptions,env_config):
    creds = env_config["users"][role]
    payload = {
        "username": creds["username"],
        "password": creds["password"]
    }
    response, data = auth_api.get_data(payload)
    assert response.status_code == 200
    assert data["data"]["token"] is not None
    assert data["data"]["roleDescription"] == expected_role_descriptions
@pytest.mark.api
@pytest.mark.parametrize("payload,expected_status,expected_code,expected_error_message", [
    (
        {"username": "invalid_user", "password": "invalid_pass"},
        200,
        1,
        "Cửa hàng không tồn tại!"
    ),
    (
        {"username": "", "password": ""},
        200,
        1,
        "Cửa hàng không tồn tại!"
    ),
    (
        {"username": "valid_user"},
        422,
        422,
        "Tham số đầu vào không hợp lệ!"
    ),
    (
        {"password": "valid_pass"},
        422,
        422,
        "Tham số đầu vào không hợp lệ!"
    ),
    (
        {},
        422,
        422,
        "Tham số đầu vào không hợp lệ!"
    ),
    (
        {"username": "craftmbeer_1", "password": "123124124"},
        200,
        1,
        "Thông tin đăng nhập tài khoản không đúng. Xin vui lòng thử lại sau !")
],ids=[
    "Invalid credentials",
    "Empty credentials",
    "Missing password in body",
    "Missing username in body",
    "Missing both fields in body",
    "Incorrect password"
])
def test_invalid_login(auth_api, payload, expected_status, expected_code, expected_error_message):
    response = auth_api.login(payload)
    assert response.status_code == expected_status
    data = response.json()
    assert data["code"] == expected_code
    assert data["message"] == expected_error_message