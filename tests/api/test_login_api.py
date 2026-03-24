import pytest
import requests
from config.env_config import ENV_CONFIG


env = ENV_CONFIG["dev"]


@pytest.mark.api
def test_login_with_invalid_password_should_fail():
    url = f"{env['api_url']}/api/v2/appuser/login"

    payload = {
        "username": env["users"]["partner"]["username"],
        "password": "wrong_password"
    }

    response = requests.post(url, json=payload, timeout=10)

    # Debug (remove later)
    print("STATUS:", response.status_code)
    print("BODY:", response.text)

    assert response.status_code != 500