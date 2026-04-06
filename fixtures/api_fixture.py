import pytest
from core.base.client import APIClient
from mExchange.api.endpoints.user_api import ExchangeAuthAPI
from mPointShop.api.client import MPointShopClient
from mExchange.api.client import MExchangeClient
from mPointShop.api.endpoints.auth_api import AuthAPI
@pytest.fixture
def valid_login_payload_partner(env_config):
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
def api_client(env_config):
    return MPointShopClient(base_url=env_config["api_url"])

@pytest.fixture
def fresh_api_client(env_config):
    return MPointShopClient(base_url=env_config["api_url"])

@pytest.fixture
def mexchange_client(env_config):
    return MExchangeClient(base_url=env_config["mexchange_api_url"])

@pytest.fixture
def auth_api(api_client):
    return AuthAPI(api_client)

@pytest.fixture
def logged_in_client_merchant(api_client, auth_api, valid_login_payload_merchant):
    response = auth_api.login(valid_login_payload_merchant)
    data = response.json()
    token = data["data"]["token"] if data["data"] else None
    if token:
        api_client.set_token(token)
    return api_client

@pytest.fixture
def logged_in_client_partner(api_client, auth_api, valid_login_payload_partner):
    response = auth_api.login(valid_login_payload_partner)
    data = response.json()
    token = data["data"]["token"] if data["data"] else None
    if token:
        api_client.set_token(token)
    return api_client

@pytest.fixture
def mexchange_auth_api(mexchange_client_ui):
    return ExchangeAuthAPI(mexchange_client_ui)

@pytest.fixture
def mexchange_client_ui(env_config, mexchange_token_from_ui):
    client = MExchangeClient(base_url=env_config["mexchange_api_url"])
    client.set_x_access_token(mexchange_token_from_ui)
    return client
