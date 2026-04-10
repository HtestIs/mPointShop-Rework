from mPointApp.pages.login_screen import LoginScreen
import pytest

@pytest.mark.defect
def test_open_app(mobile_driver):
    open_app = LoginScreen(mobile_driver)
    open_app.login("0123456789", "password123")
    print(open_app.message())