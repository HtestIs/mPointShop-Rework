"""Shared API fixtures available to all systems via the top-level pytest plugin list."""

import pytest

from mPointShop.api.client import MPointShopClient
from mPointShop.api.endpoints.auth_api import AuthAPI
from mExchange.api.client import MExchangeClient

@pytest.fixture
def mpointshop_valid_login_payload_partner(env_config):
    creds = env_config["users"]["partner"]
    return {
        "username": creds["username"],
        "password": creds["password"],
    }


@pytest.fixture
def mpointshop_valid_login_payload_merchant(env_config):
    creds = env_config["users"]["merchant"]
    return {
        "username": creds["username"],
        "password": creds["password"],
    }

@pytest.fixture
def mpointshop_api_client(env_config):
    return MPointShopClient(base_url=env_config["api_url"])

@pytest.fixture
def mpointshop_fresh_api_client(env_config):
    return MPointShopClient(base_url=env_config["api_url"])


@pytest.fixture
def mpointshop_auth_api(mpointshop_api_client):
    return AuthAPI(mpointshop_api_client)


@pytest.fixture
def mpointshop_logged_in_client_merchant(mpointshop_api_client, mpointshop_auth_api, mpointshop_valid_login_payload_merchant):
    response = mpointshop_auth_api.login(mpointshop_valid_login_payload_merchant)
    data = response.json()
    token = data["data"]["token"] if data["data"] else None
    if token:
        mpointshop_api_client.set_token(token)
    return mpointshop_api_client


@pytest.fixture
def mpointshop_logged_in_client_partner(mpointshop_api_client, mpointshop_auth_api, mpointshop_valid_login_payload_partner):
    response = mpointshop_auth_api.login(mpointshop_valid_login_payload_partner)
    data = response.json()
    token = data["data"]["token"] if data["data"] else None
    if token:
        mpointshop_api_client.set_token(token)
    return mpointshop_api_client

@pytest.fixture
def mexchange_client_ui(env_config, mexchange_token_from_ui):
    client = MExchangeClient(base_url=env_config["mexchange_api_url"])
    client.set_x_access_token(mexchange_token_from_ui)
    return client
