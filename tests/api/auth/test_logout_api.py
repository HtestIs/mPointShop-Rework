import pytest
from api.endpoints.auth_api import AuthAPI
from api.endpoints.store_api import StoreAPI

@pytest.mark.ongoing
def test_logout(logged_in_client_partner, auth_api,env_config):
    creds = env_config["users"]["partner"]
    payload = {
        "username": creds["username"],
        "password": creds["password"]
    }
    login, data = auth_api.get_data(payload)
    old_token = data["data"]["token"]
    response = auth_api.logout()
    auth_api.client.debug_response(response)
    data_logout = response.json()
    assert response.status_code == 200
    assert data_logout["code"] == 0, f"Expected code 0 for successful logout, got {data['code']}"
    login_2 = StoreAPI(client = logged_in_client_partner)
    login_2.client.set_token(old_token)
    response_2 = login_2.get_store_list()
    auth_api.client.debug_response(response_2)
