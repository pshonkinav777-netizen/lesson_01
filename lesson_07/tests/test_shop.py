from pages.shop_page import LoginPage
from pages.shop_page import MainPage
from pages.shop_page import CartPage
from pages.shop_page import CheckoutPage
from pages.shop_page import InformationPage

from selenium import webdriver


def test_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.delete_all_cookies()
    login = LoginPage(driver, url='https://www.saucedemo.com/')
    login.open_shop_page()
    login.log_in("standard_user", "secret_sauce")
    # login.log_in()
    main = MainPage(driver)
    main.add_to_cart()
    cart = CartPage(driver)
    cart.click_cart()
    checkout = CheckoutPage(driver)
    checkout.click_checkout()
    information = InformationPage(driver)
    information.information('Alex', 'P', '123123')
    result = information.get_total()

    driver.quit()

    assert result == 'Total: $58.29'
