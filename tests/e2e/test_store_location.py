from data.builders import build_location_data, build_store_data
from data.fake_location import fake_new_location, fake_old_location
import pytest
import allure
@pytest.mark.registration
@allure.story("User choosing inferior location")
@allure.title("Options management")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.parametrize("location_setup,target_field",[
    ("missing_city", "district_old"),
    ("missing_city", "ward_old"),   
    ("missing_district", "ward_old"),
    ("missing_city_new", "ward_new")
])
def test_dropdown_options_should_be_empty_when_required_location_missing(login_partner_success,storedata,location_setup,target_field):
    page = login_partner_success
    page.click_add_new_store()
    page.setup_location(location_setup,storedata)
    page.click(page.FORM_FIELDS[target_field])
    options = page.has_selectable_option()
    assert options is False, f"Dropdown options for {target_field} should be empty when required location is missing"

@pytest.mark.registration
@allure.story("User changing location")
@allure.title("Dropdown options update")
@allure.severity(allure.severity_level.MINOR)
def test_update_dropdown_options(login_partner_success,storedata):
    
    page = login_partner_success
    data1 = storedata.copy()
    data2_old = fake_old_location(exclude_city=data1["city_old"])
    
    data2_new = fake_new_location(exclude_city=data1["city_new"])
    data2 = build_store_data(storedata, **data2_old, **data2_new)
    page.click_add_new_store()
    page.select_store_location_fields(data1)
    page.select_store_location_fields(data2)
    assert page.get_selected_text("city_old") == data2["city_old"], "City dropdown did not update to new selection"
    assert page.get_selected_text("district_old") == data2["district_old"], "District dropdown did not update based on new city selection"
    assert page.get_selected_text("ward_old") == data2["ward_old"], "Ward dropdown did not update based on new district selection"
    assert page.get_selected_text("city_new") == data2["city_new"], "New city dropdown did not update to new selection"
    assert page.get_selected_text("ward_new") == data2["ward_new"], "New ward dropdown did not update based on new city selection"

@pytest.mark.registration
@allure.story("User choosing superior location")
@allure.title("Dropdown superior options reset")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.parametrize("superior_field,target_field,dataset,expected",[
    ("city_old", "district_old","missing_city","Chọn Quận/Huyện"),
    ("city_old", "ward_old","missing_city","Chọn Xã/Phường"),
    ("district_old", "ward_old","missing_district","Chọn Xã/Phường"),
    ("city_new", "ward_new","missing_city","Chọn Xã/Phường")
])
def test_dependent_dropdown_behavior(login_partner_success,storedata,superior_field,target_field,dataset,expected):
    page = login_partner_success
    data1 = storedata.copy()
    data2 = build_location_data(data1, dataset)
    page.click_add_new_store()
    page.select_store_location_fields(data1)
    page.choose_option(superior_field, data2[superior_field])
    assert page.get_selected_text(target_field) == expected, f"{target_field} should reset when {superior_field} changes"

