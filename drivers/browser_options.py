from selenium import webdriver


def get_chrome_options():
    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-infobars")
    options.add_argument("--guest")
    prefs = {
        "translate_enabled": False,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.media_stream_camera": 2
    }

    options.add_experimental_option("prefs", prefs)

    return options