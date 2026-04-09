from selenium import webdriver


def get_chrome_options(headless=False):
    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-infobars")
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

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