"""Shared API fixtures available to all systems via the top-level pytest plugin list."""

import pytest

from mPointShop.api.client import MPointShopClient
from mPointShop.api.endpoints.auth_api import AuthAPI


@pytest.fixture
def valid_login_payload_partner(env_config):
    creds = env_config["users"]["partner"]
    return {
        "username": creds["username"],
        "password": creds["password"],
    }


@pytest.fixture
def valid_login_payload_merchant(env_config):
    creds = env_config["users"]["merchant"]
    return {
        "username": creds["username"],
        "password": creds["password"],
    }


@pytest.fixture
def api_client(env_config):
    return MPointShopClient(base_url=env_config["api_url"])


@pytest.fixture
def fresh_api_client(env_config):
    return MPointShopClient(base_url=env_config["api_url"])


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
