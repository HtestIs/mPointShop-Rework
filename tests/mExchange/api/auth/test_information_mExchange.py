import pytest

from api.mExchange.endpoints.user_api import ExchangeAuthAPI


@pytest.mark.ongoing
def test_mexchange_me(mexchange_client):
    login = ExchangeAuthAPI(client = mexchange_client)
    response = login.get_info()
    data = response.json()
    login.client.debug_response(response)

    assert response.status_code == 200
    assert data is not None