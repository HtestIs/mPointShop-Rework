from mPointShop.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure

class CreateProductPage(BasePage):
    INPUT_IMAGE_UPLOAD = (By.CSS_SELECTOR, 'input[type="file"][accept="image/*"]')
    INPUT_NAME_PRODUCT = (By.ID, 'name')
    INPUT_CATEGORY = (By.ID, 'categoryId')
    INPUT_VISIBLE_PICKER = (By.XPATH, '//label[@id="categoryId-control-label"]/following-sibling::div//div[@role="combobox"]')
    INPUT_SEQUENCE = (By.ID, 'sequence')
    INPUT_URL_VIDEO = (By.ID, 'videoUrl')
    INPUT_HASHTAG = (By.CSS_SELECTOR, 'button.tag-add-btn')
    INPUT_ITEM_PROPERTY_BUTTON = (By.XPATH, '//b[contains(.,"Đặc điểm sản phẩm")]/ancestor::div[@role="row"]//button')
    TYPE = (By.XPATH, '//b[contains(.,"Chủng loại")]')
    