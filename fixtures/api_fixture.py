import pytest
from api.client import APIClient
from api.endpoints.auth_api import AuthAPI
from api.endpoints.menu_api import MenuAPI
from api.endpoints.store_api import StoreAPI
@pytest.fixture
def api_url(env_config):
    return env_config["api_url"]
@pytest.fixture
def valid_login_payload(env_config):
    creds = env_config["users"]["partner"]
    return {
        "username": creds["username"],
        "password": creds["password"]}
@pytest.fixture
def valid_login_payload_merchant(env_config):
    creds = env_config["users"]["merchant"]
    return {
        "username": creds["username"],
        "password": creds["password"]}
@pytest.fixture
def api_client(api_url):
    client = APIClient(base_url=api_url)
    return client
@pytest.fixture
def auth_api(api_client):
    return AuthAPI(client=api_client)
@pytest.fixture
def menu_api(api_client):
    return MenuAPI(client=api_client)
@pytest.fixture
def store_api(api_client):
    return StoreAPI(client=api_client)
@pytest.fixture
def logged_in_client_merchant(api_client, auth_api, valid_login_payload_merchant):
    response = auth_api.login(valid_login_payload_merchant)
    assert response.status_code == 200, f"Login failed {response.text}"
    data = response.json()
    token = data["data"]["token"] if data["code"] == 0 else None
    if token:
        api_client.set_token(token)
    return api_client
@pytest.fixture
def logged_in_client_partner(api_client, auth_api, valid_login_payload):
    response = auth_api.login(valid_login_payload)
    assert response.status_code == 200, f"Login failed {response.text}"
    data = response.json()
    token = data["data"]["token"] if data["code"] == 0 else None
    if token:
        api_client.set_token(token)
    return api_client
@pytest.fixture
def logged_in_partner_menu_api(logged_in_client_partner):
    return MenuAPI(client=logged_in_client_partner)

@pytest.fixture
def logged_in_merchant_menu_api(logged_in_client_merchant):
    return MenuAPI(client=logged_in_client_merchant)
@pytest.fixture
def fresh_api_client(api_url):
    return APIClient(base_url=api_url)