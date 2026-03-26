import pytest
from api.client import APIClient
from api.endpoints.auth_api import AuthAPI

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