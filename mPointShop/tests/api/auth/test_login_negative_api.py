import pytest
import allure

pytestmark = [
    pytest.mark.mpointshop,
    allure.parent_suite("mPointShop"),
    allure.suite("API"),
    allure.sub_suite("Authentication"),
]

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
@allure.story("Authentication")
@allure.title("Login API validates invalid credentials and malformed payloads")
@allure.severity(allure.severity_level.CRITICAL)
def test_invalid_login(mpointshop_auth_api, payload, expected_status, expected_code, expected_error_message):
    
    response = mpointshop_auth_api.login(payload)
    assert response.status_code == expected_status
    data = response.json()
    assert data["code"] == expected_code
    assert data["message"] == expected_error_message