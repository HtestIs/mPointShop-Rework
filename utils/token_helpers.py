def get_local_storage_token(driver, key="token"):
    return driver.execute_script(f"return window.localStorage.getItem('{key}');")