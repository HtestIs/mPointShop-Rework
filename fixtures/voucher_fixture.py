import pytest

from api.mPointShop.endpoints.voucher_api import VoucherAPI

@pytest.fixture
def create_voucher_discount_percentage(logged_in_client_partner, voucher_data):
    voucher_page = VoucherAPI(client = logged_in_client_partner)
    payload = voucher_data(vouchertype="discount_percentage")
    response = voucher_page.create_voucher(payload=payload)
    return response

@pytest.fixture
def create_voucher_discount_constant(logged_in_client_partner, voucher_data):
    voucher_page = VoucherAPI(client = logged_in_client_partner)
    payload = voucher_data(vouchertype="discount_constant")
    response = voucher_page.create_voucher(payload=payload)
    return response

@pytest.fixture
def create_gift_voucher(logged_in_client_partner, voucher_data):
    voucher_page = VoucherAPI(client = logged_in_client_partner)
    payload = voucher_data(vouchertype="gift")
    response = voucher_page.create_voucher(payload=payload)
    return response

@pytest.fixture
def create_cash_multiple_voucher(logged_in_client_partner, voucher_data):
    voucher_page = VoucherAPI(client = logged_in_client_partner)
    payload = voucher_data(vouchertype="cash_multiple")
    response = voucher_page.create_voucher(payload=payload)
    return response