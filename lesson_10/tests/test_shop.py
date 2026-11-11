from pages.shop_page import LoginPage
from pages.shop_page import MainPage
from pages.shop_page import CartPage
from pages.shop_page import CheckoutPage
from pages.shop_page import InformationPage
import allure
from selenium import webdriver


@allure.feature("Магазин")
@allure.suite("Тестирование магазина")
@allure.title("Тестирование добавления и оплаты товаров")
@allure.description(
    "Тест проверяет корректность входа на страницу магазина, "
    "добавление товаров в корзину, оплату и проверки итоговой суммы")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    """Тест проверяет корректность входа,
    добавления товаров в корзину, оплаты и проверку итоговой суммы
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.delete_all_cookies()
    with allure.step("Переход на страницу магазина"):
        login = LoginPage(driver, url='https://www.saucedemo.com/')
        login.open_shop_page()
        login.log_in("standard_user", "secret_sauce")
        # login.log_in()
    with allure.step("Добавляет товары в корзину"):
        main = MainPage(driver)
        main.add_to_cart()
    with allure.step("Переходит в корзину"):
        cart = CartPage(driver)
        cart.click_cart()
    with allure.step("Кликает по кнопке checkout"):
        checkout = CheckoutPage(driver)
        checkout.click_checkout()
    with allure.step("Заполняет информацию"):
        information = InformationPage(driver)
        information.information('Alex', 'P', '123123')
    with allure.step("Получает результат"):
        result = information.get_total()
    with allure.step("Закрывает браузер"):
        driver.quit()
    with allure.step("Проверяет результат"):
        assert result == 'Total: $58.29'
