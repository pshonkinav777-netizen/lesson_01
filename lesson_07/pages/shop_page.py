from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    LOGIN = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)

    def open_shop_page(self):
        self.driver.get('https://www.saucedemo.com/')
        self.driver.delete_all_cookies()

    def log_in(self):
        login = self.wait.until(EC.presence_of_element_located(self.LOGIN))
        login.send_keys('standard_user')
        password = self.wait.until(
            EC.presence_of_element_located(self.PASSWORD))
        password.send_keys('secret_sauce')
        login_button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_button.click()


class MainPage:
    ADD_BACKPACK = (By.ID, 'add-to-cart-sauce-labs-backpack')
    ADD_BOLT_T_SHIRT = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    ADD_ONSIE = (By.ID, 'add-to-cart-sauce-labs-onesie')

    def add_to_cart(self):
        add_backpack = self.wait.until(EC.element_to_be_clickable(
                self.ADD_BACKPACK))
        add_backpack.click()
        add_bolt_t_shirt = self.wait.until(EC.element_to_be_clickable(
                self.ADD_BOLT_T_SHIRT))
        add_bolt_t_shirt.click()
        add_onsie = self.wait.until(EC.element_to_be_clickable(
                    self.ADD_ONSIE))
        add_onsie.click()


class CartPage:
    CART = (By.CLASS_NAME, 'shopping_cart_link')

    def click_cart(self):
        cart = self.wait.until(EC.element_to_be_clickable(
            self.CART))
        cart.click()


class CheckoutPage:
    CHECKOUT_BUTTON = (
        By.CLASS_NAME, 'btn.btn_action.btn_medium.checkout_button ')

    def click_checkout(self):
        checkout_button = self.wait.until(EC.element_to_be_clickable(
            self.CHECKOUT_BUTTON))
        checkout_button.click()


class InformationPage:
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    ZIP_CODE = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    TOTAL_TEXT = (By.CLASS_NAME, "summary_total_label")

    def information(self):
        first_name = self.wait.until(EC.presence_of_element_located(
                self.FIRST_NAME))
        first_name.send_keys('Alex')
        last_name = self.wait.until(EC.presence_of_element_located(
                self.LAST_NAME))
        last_name.send_keys('P')
        zip_code = self.wait.until(EC.presence_of_element_located(
                self.ZIP_CODE))
        zip_code.send_keys('123124')
        continue_button = self.wait.until(EC.element_to_be_clickable(
                self.CONTINUE_BUTTON))
        continue_button.click()
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

    def get_total(self):
        total_text = self.wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label")))
        total_result = total_text.text
        return total_result


# class ShopObject:
    # LOGIN = (By.ID, 'user-name')
    # PASSWORD = (By.ID, 'password')
    # LOGIN_BUTTON = (By.ID, 'login-button')
    # ADD_BACKPACK = (By.ID, 'add-to-cart-sauce-labs-backpack')
    # ADD_BOLT_T_SHIRT = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    # ADD_ONSIE = (By.ID, 'add-to-cart-sauce-labs-onesie')
    # CART = (By.CLASS_NAME, 'shopping_cart_link')
    # CHECKOUT_BUTTON = (
    #     By.CLASS_NAME, 'btn.btn_action.btn_medium.checkout_button ')
    # FIRST_NAME = (By.ID, 'first-name')
    # LAST_NAME = (By.ID, 'last-name')
    # ZIP_CODE = (By.ID, 'postal-code')
    # CONTINUE_BUTTON = (By.ID, 'continue')
    # TOTAL_TEXT = (By.CLASS_NAME, "summary_total_label")

    # def __init__(self, driver):
    #     self.driver = driver
    #     self.wait = WebDriverWait(self.driver, 50)

    # def open_shop_page(self):
    #     self.driver.get('https://www.saucedemo.com/')
    #     self.driver.delete_all_cookies()

    # def log_in(self):
    #     login = self.wait.until(EC.presence_of_element_located(self.LOGIN))
    #     login.send_keys('standard_user')
    #     password = self.wait.until(
    #         EC.presence_of_element_located(self.PASSWORD))
    #     password.send_keys('secret_sauce')
    #     login_button = self.wait.until(
    #         EC.presence_of_element_located(self.LOGIN_BUTTON))
    #     login_button.click()

    # def add_to_cart(self):
    #     add_backpack = self.wait.until(EC.presence_of_element_located(
    #             self.ADD_BACKPACK))
    #     add_backpack.click()
    #     add_bolt_t_shirt = self.wait.until(EC.presence_of_element_located(
    #             self.ADD_BOLT_T_SHIRT))
    #     add_bolt_t_shirt.click()
    #     add_onsie = self.wait.until(EC.presence_of_element_located(
    #             self.ADD_ONSIE))
    #     add_onsie.click()

    # def click_cart(self):
    #     cart = self.wait.until(EC.presence_of_element_located(
    #         self.CART))
    #     cart.click()

    # def click_checkout(self):
    #     checkout_button = self.wait.until(EC.presence_of_element_located(
    #         self.CHECKOUT_BUTTON))
    #     checkout_button.click()

    # def information(self):
    #     first_name = self.wait.until(EC.presence_of_element_located(
    #             self.FIRST_NAME))
    #     first_name.send_keys('Alex')
    #     last_name = self.wait.until(EC.presence_of_element_located(
    #             self.LAST_NAME))
    #     last_name.send_keys('P')
    #     zip_code = self.wait.until(EC.presence_of_element_located(
    #             self.ZIP_CODE))
    #     zip_code.send_keys('123124')
    #     continue_button = self.wait.until(EC.presence_of_element_located(
    #             self.CONTINUE_BUTTON))
    #     continue_button.click()
    #     self.driver.execute_script(
    #         "window.scrollTo(0, document.body.scrollHeight);")

    # def get_total(self):
    #     total_text = self.wait.until(EC.presence_of_element_located(
    #             (By.CLASS_NAME, "summary_total_label")))
    #     total_result = total_text.text
    #     return total_result
        # assert  '58.29' in total_text
