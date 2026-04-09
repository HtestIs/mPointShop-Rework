import allure
import pytest

from core.utils.shared_voucher_flows import get_synced_partner_voucher_alt_id
from mExchange.conftest import mexchange_client_ui, mexchange_token_from_ui  # noqa: F401


@pytest.mark.mshopadmin
@pytest.mark.e2e
@pytest.mark.defect
def test_voucher_list_expand_search(
    login_aap_success,
    logged_in_client_partner,
    create_voucher_discount_constant,
    mexchange_client_ui,
):
    synced_partner_voucher_alt_id = get_synced_partner_voucher_alt_id(
        logged_in_client_partner,
        create_voucher_discount_constant,
        mexchange_client_ui,
    )
    allure.attach(
        synced_partner_voucher_alt_id,
        name="voucher_alt_id",
        attachment_type=allure.attachment_type.TEXT,
    )

    dashboard_page = login_aap_success
    voucher_list_page = dashboard_page.navigate_to_voucher_list()
    voucher_list_page.expand_search()
    voucher_list_page.search_by_alt_id(synced_partner_voucher_alt_id)
    voucher_list_page.search()
    voucher_list_page.wait_visible(voucher_list_page.FIRST_ROW)


@pytest.mark.mpointshop
@pytest.mark.mexchange
@pytest.mark.mshopadmin
@pytest.mark.e2e
@pytest.mark.api
@pytest.mark.defect
def test_voucher_list_approve(
    login_aap_success,
    logged_in_client_partner,
    create_voucher_discount_constant,
    mexchange_client_ui,
):
    synced_partner_voucher_alt_id = get_synced_partner_voucher_alt_id(
        logged_in_client_partner,
        create_voucher_discount_constant,
        mexchange_client_ui,
    )
    allure.attach(
        synced_partner_voucher_alt_id,
        name="voucher_alt_id",
        attachment_type=allure.attachment_type.TEXT,
    )

    dashboard_page = login_aap_success
    voucher_list_page = dashboard_page.navigate_to_voucher_list()
    voucher_list_page.expand_search()
    voucher_list_page.search_by_alt_id(synced_partner_voucher_alt_id)
    voucher_list_page.search()
    voucher_list_page.wait_visible(voucher_list_page.FIRST_ROW)
    voucher_list_page.click_approve_toggle()