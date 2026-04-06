import allure

from mPointShop.pages.login_page import LoginPage


class StoreSecurityMixin:
    @allure.step("Toggle store status")
    def toggle_store(self):
        old = self.find(self.FIRST_SWITCH_BUTTON)
        current = self.get_lock_status()
        self.click(self.FIRST_SWITCH_BUTTON)
        self.wait_stale(old)
        self.wait_clickable(self.FIRST_SWITCH_BUTTON)
        self.wait_attribute_change(self.FIRST_SWITCH, "aria-checked", current)

    @allure.step("Get store lock status")
    def get_lock_status(self):
        return self.get_attribute_status(self.FIRST_SWITCH, "aria-checked")

    @allure.step("Ensure store is locked")
    def ensure_locked(self):
        if self.get_lock_status() == "false":
            self.toggle_store()

    @allure.step("Click change password")
    def click_change_password(self):
        self.click(self.FIRST_STORE_BUTTON)

    @allure.step("Enter new password")
    def enter_password_update(self, text):
        self.type_text(self.TEXT_PASSWORD_MODAL, text)

    @allure.step("Confirm password change")
    def click_confirm_button_password_modal(self):
        self.click(self.CONFIRM_BUTTON)

    @allure.step("Change store password")
    def change_password(self, new_password):
        self.click_change_password()
        self.enter_password_update(new_password)
        self.click_confirm_button_password_modal()

    @allure.step("Get toast message")
    def get_toast_msg(self):
        return self.get_text(self.TOAST_MESSAGE)

    @allure.step("Click logout")
    def click_logout(self):
        self.click(self.BTN_LOG_OUT)
        return LoginPage(self.driver)

    @allure.step("Hover over user block")
    def hover_user(self):
        self.hover(self.USER_BLOCK)
