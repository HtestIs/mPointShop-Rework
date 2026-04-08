"""Shared voucher fixtures backed by the mPointShop API client."""

import pytest

from mPointShop.api.endpoints.voucher_api import VoucherAPI


@pytest.fixture
def create_voucher_discount_percentage(logged_in_client_partner, voucher_data):
    voucher_page = VoucherAPI(client=logged_in_client_partner)
    payload = voucher_data(vouchertype="discount_percentage")
    return voucher_page.create_voucher(payload=payload)


@pytest.fixture
def create_voucher_discount_constant(logged_in_client_partner, voucher_data):
    voucher_page = VoucherAPI(client=logged_in_client_partner)
    payload = voucher_data(vouchertype="discount_constant")
    return voucher_page.create_voucher(payload=payload)


@pytest.fixture
def create_gift_voucher(logged_in_client_partner, voucher_data):
    voucher_page = VoucherAPI(client=logged_in_client_partner)
    payload = voucher_data(vouchertype="gift")
    return voucher_page.create_voucher(payload=payload)


@pytest.fixture
def create_cash_multiple_voucher(logged_in_client_partner, voucher_data):
    voucher_page = VoucherAPI(client=logged_in_client_partner)
    payload = voucher_data(vouchertype="cash_multiple")
    return voucher_page.create_voucher(payload=payload)
