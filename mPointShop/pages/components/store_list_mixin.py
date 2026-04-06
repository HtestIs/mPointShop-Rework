import allure


class StoreListMixin:
    @allure.step("Get page name")
    def get_page_name(self):
        return self.get_text(self.PAGE_NAME)

    @allure.step("Search store by name: {text}")
    def find_store_with_name(self, text):
        self.type_text(self.SEARCH_TEXT_FIND, text)

    @allure.step("Click add new store")
    def click_add_new_store(self):
        self.click(self.ADD_STORE_BUTTON)

    @allure.step("Search store by phone: {text}")
    def find_store_with_number(self, text):
        self.type_text(self.SEARCH_PHONE_SEARCH_INPUT, text)

    @allure.step("Get store name")
    def get_store_name(self):
        return self.get_text(self.FIRST_STORE_NAME)

    @allure.step("Get store phone")
    def get_store_phone(self):
        return self.get_text(self.FIRST_PHONE_NUMBER).replace("Số điện thoại:", "").strip()

    def wait_store_info_loaded(self, keyword=None):
        def condition():
            name = self.get_store_name()
            phone = self.get_store_phone()
            if keyword:
                return keyword in name or keyword in phone
            return bool(name) and bool(phone)

        self.wait_until(condition)
