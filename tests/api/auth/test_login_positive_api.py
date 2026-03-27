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