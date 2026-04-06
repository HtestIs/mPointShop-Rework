import pytest

from mExchange.api.endpoints.user_api import ExchangeAuthAPI


@pytest.mark.api
def test_mexchange_me(mexchange_client_ui):
    login = ExchangeAuthAPI(client = mexchange_client_ui)
    response = login.get_info()
    data = response.json()
    login.client.debug_response(response)

    assert response.status_code == 200
    assert data is not None