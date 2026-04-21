"""Shared API fixtures available to all systems via the top-level pytest plugin list."""

import pytest

from mPointShop.api.client import MPointShopClient
from mPointShop.api.endpoints.auth_api import AuthAPI
from mExchange.api.client import MExchangeClient
from mShopAdmin.api.client import MSHopAdminClient
from mShopAdmin.api.endpoints.customer_auth_api import CustomerLoginAPI

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

@pytest.fixture
def app_api_client(env_config):
    return MSHopAdminClient(base_url=env_config["aap_base_url"])

@pytest.fixture
def app_logged_in_client(app_api_client, env_config):
    client = app_api_client
    client.set_key_app()
    login_client = CustomerLoginAPI(client)
    login_payload = {
        "phone": env_config["app_username"],
        "password": env_config["app_password"]
    }
    response = login_client.login(payload=login_payload)
    data = response.json()
    token = data["accessToken"] if data else None
    if token:
        app_api_client.set_token(token)
    return app_api_client

@pytest.fixture
def mshopadmin_api_client(env_config):
    return MSHopAdminClient(base_url=env_config["aap_base_url"])

##Mshop Admin API client with token fixture, it using captcha, so we need to 
# set token in env file and use it in this fixture, not ideal but we can use
#  it for now until we find a better solution to handle captcha in tests.

@pytest.fixture
def mshopadmin_api_client_with_token(env_config, mshopadmin_api_client):
    token = env_config["aap_token"]
    if token:
        mshopadmin_api_client.set_token(token)
    return mshopadmin_api_client