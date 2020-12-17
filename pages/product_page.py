from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_button(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_button.click()
        self.solve_quiz_and_get_code()

    def should_be_success_message(self):
        assert self.browser.find_element(*ProductPageLocators.ADDING_SUCCESSFUL), "No success message"

    def should_be_right_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        cart_name = self.browser.find_element(*ProductPageLocators.CART_NAME_PRODUCT)
        assert product_name.text == cart_name.text, "Wrong cart name"

    def should_be_message_with_sum(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE), "No sum message"

    def should_be_right_sum(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE_PRODUCT)
        assert product_price.text == cart_price.text, "Wrong cart price"
