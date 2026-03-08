from pages.voucher_scan_page import VoucherScan

def test_enter_voucher(login_merchant_success):
    login_merchant_success.enter_voucher("abc")