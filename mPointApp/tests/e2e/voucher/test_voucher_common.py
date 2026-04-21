import allure
import pytest

pytestmark = [
    pytest.mark.mpointapp,
    allure.parent_suite("mPointApp"),
    allure.suite("E2E"),
    allure.sub_suite("Voucher"),
]

@pytest.mark.e2e
@pytest.mark.defect
@allure.feature("Voucher")
@allure.story("Voucher navigation")
@allure.title("Navigate to voucher section from home screen")
@allure.severity(allure.severity_level.NORMAL)
def test_navigate_to_voucher_section(login_valid_user):
    pass