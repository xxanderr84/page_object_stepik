from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    NAME_PRODUCT = (By.TAG_NAME, "h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    ADDING_SUCCESSFUL = (By.CSS_SELECTOR, "div.alert-success")
    PRICE_MESSAGE = (By.CSS_SELECTOR, "div.alert-info")
    CART_PRICE_PRODUCT = (By.CSS_SELECTOR, "div.alert-info div p strong")
    CART_NAME_PRODUCT = (By.CSS_SELECTOR, "div.alert-success div strong")


