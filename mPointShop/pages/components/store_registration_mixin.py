import random

import allure
from selenium.webdriver.common.by import By


class StoreRegistrationMixin:
    @allure.step("Confirm user modal")
    def click_confirm_button_user_modal(self):
        self.click(self.MODAL_CONFIRM_BUTTON)

    @allure.step("Upload store image")
    def upload_store_image(self, image_path):
        self.upload_image(self.MODAL_UPLOAD_INPUT, image_path)

    @allure.step("Get first store username from edit modal")
    def get_first_store_username_from_edit_modal(self):
        self.click(self.FIRST_STORE_EDIT)
        username = self.get_attribute_status(self.FIRST_STORE_USERNAME, "value")
        self.click(self.MODAL_CANCEL)
        return username

    @allure.step("Fill field: {field_name}")
    def fill_field(self, field_name, value):
        locator = self.FORM_FIELDS[field_name]
        self.type_text(locator, value)

    @allure.step("Choose option for {field_name}: {value}")
    def choose_option(self, field_name, value):
        dropdown = self.COMBO_FIELDS[field_name]
        self.click(dropdown)

        self.wait.until(
            lambda d: self.finds(self.MODAL_OPTION_LIST) or self.is_visible(self.MODAL_NO_RESULT)
        )
        options = self.finds(self.MODAL_OPTION_LIST)
        if not options:
            raise Exception(f"No options available for {field_name}")

        for option in options:
            if option.text.strip() == value:
                option.click()
                break
        else:
            raise Exception(f"Option '{value}' not found for {field_name}")

        self.wait.until(lambda d: self.get_selected_text(field_name) == value)

    @allure.step("Get selected text for {field_name}")
    def get_selected_text(self, field_name):
        dropdown = self.COMBO_FIELDS[field_name]
        return self.find(dropdown).text.strip()

    @allure.step("Select location options")
    def select_option(self, data):
        city = data.get("city_old")
        district = data.get("district_old")
        ward = data.get("ward_old")
        city_new = data.get("city_new")
        ward_new = data.get("ward_new")

        if city:
            self.choose_option("city_old", city)
            if district:
                self.choose_option("district_old", district)
                if ward:
                    self.choose_option("ward_old", ward)

        if city_new:
            self.choose_option("city_new", city_new)
            if ward_new:
                self.choose_option("ward_new", ward_new)

    @allure.step("Setup location: {setup}")
    def setup_location(self, setup, storedata):
        if setup == "missing_city":
            return
        if setup == "missing_district":
            self.choose_option("city_old", storedata["city_old"])
        elif setup == "missing_city_new":
            return

    @allure.step("Check if selectable option exists")
    def has_selectable_option(self):
        self.wait.until(
            lambda d: self.finds(self.MODAL_OPTION_LIST) or self.is_visible(self.MODAL_NO_RESULT)
        )
        return len(self.finds(self.MODAL_OPTION_LIST)) > 0

    @allure.step("Choose date")
    def choose_date(self):
        self.click(self.MODAL_DATE_PICKER)
        months_to_add = random.randint(1, 48)
        for _ in range(months_to_add):
            self.click(self.MODAL_NEXT_MONTH_BUTTON)
        days = self.finds(self.MODAL_CHOOSE_DATE)
        random.choice(days).click()
        self.click(self.MODAL_DATE_PICKER_CONFIRM)

    @allure.step("Fill store form fields")
    def fill_store_form_fields(self, storedata):
        for field in self.FORM_FIELDS:
            value = storedata.get(field)
            if value:
                if field == "image_path":
                    self.upload_store_image(value)
                else:
                    self.fill_field(field, value)

    @allure.step("Select store location fields")
    def select_store_location_fields(self, storedata):
        for field in self.COMBO_FIELDS:
            value = storedata.get(field)
            if value:
                self.choose_option(field, value)

    @allure.step("Register new store")
    def register_new_store(self, storedata):
        self.click_add_new_store()
        self.fill_store_form_fields(storedata)
        self.select_store_location_fields(storedata)
        self.choose_date()
        self.click_confirm_button_user_modal()

    @allure.step("Get field error for: {field_name}")
    def get_field_error(self, field_name):
        locator = (By.XPATH, f"//b[contains(text(),'{field_name}')]/following-sibling::span")
        return self.find(locator).text
