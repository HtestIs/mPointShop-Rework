from pages.voucher_scan_page import VoucherScan
import pytest
import allure

@pytest.mark.smoke
@allure.story("Voucher scanning")
@allure.title("Merchant can enter voucher code")
@allure.severity(allure.severity_level.NORMAL)
def test_enter_voucher(login_merchant_success):
    login_merchant_success.enter_voucher("abc")