from pages.shop_page import ShopObject
from selenium import webdriver


def test_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.delete_all_cookies()
    shop = ShopObject(driver, url='https://www.saucedemo.com/')
    shop.open_shop_page()
    shop.log_in()
    shop.add_to_cart()
    shop.click_cart()
    shop.click_checkout()
    shop.information()
    result = shop.get_total()

    driver.quit()

    assert result == 'Total: $58.29'
