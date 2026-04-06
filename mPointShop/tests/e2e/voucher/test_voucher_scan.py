from mPointShop.pages.voucher_scan_page import VoucherScan
import pytest
import allure

@pytest.mark.smoke
@allure.story("Voucher scanning")
@allure.title("Merchant can enter voucher code")
@allure.severity(allure.severity_level.NORMAL)
def t_enter_voucher(login_merchant_success):
    menu = login_merchant_success
    voucher_scan = menu.navigate_to_voucher_scan()
    voucher_scan.enter_voucher("abc")