from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage:
    LOGIN = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

    def __init__(self, driver, url):
        """
        Конструктор класса LoginPage

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Открытие страницы магазина")
    def open_shop_page(self) -> None:
        """
        Открывает страницу магазина и удаляет все куки.

        :return: None, так как метод ничего не возвращает.
        """
        with allure.step("Переход на страницу магазина"):
            self.driver.get('https://www.saucedemo.com/')
        with allure.step("Удаление куки"):
            self.driver.delete_all_cookies()

    @allure.step(
            "Авторизация пользователя заполняет поля {username} и {password}")
    def log_in(self, username: str, password: str) -> None:
        """
        Позволяет авторизироваться с помощью указанных
        имени пользователя и пароля.

        :param username: Имя пользователя, строка.
        :param password: Пароль пользователя, строка.
        :return: None, так как метод ничего не возвращает.
        """
        with allure.step("Вводит имя в поле Username"):
            self.driver.find_element(By.ID, "user-name").send_keys(username)
        with allure.step("Вводитт пароль в пое Password"):
            self.driver.find_element(By.ID, "password").send_keys(password)
        with allure.step("Кдикает по кнопке Login"):
            login_button = self.wait.until(
                EC.element_to_be_clickable(self.LOGIN_BUTTON))
            login_button.click()


class MainPage:
    ADD_BACKPACK = (By.ID, 'add-to-cart-sauce-labs-backpack')
    ADD_BOLT_T_SHIRT = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    ADD_ONSIE = (By.ID, 'add-to-cart-sauce-labs-onesie')

    def __init__(self, driver):
        """Конструктор класса MainPage

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Добавление товаров в корзину")
    def add_to_cart(self) -> None:
        """
        Добавляет указанные элементы в корзину: рюкзак, футболку и комбинезон.

        :return: None, так как метод ничего не возвращает.
        """
        with allure.step("Добавляет элемент backpack в корзину"):
            add_backpack = self.wait.until(EC.element_to_be_clickable(
                    self.ADD_BACKPACK))
            add_backpack.click()
        with allure.step("Добавляет элемент bolt_t_shirt в корзину"):
            add_bolt_t_shirt = self.wait.until(EC.element_to_be_clickable(
                    self.ADD_BOLT_T_SHIRT))
            add_bolt_t_shirt.click()
        with allure.step("Добавляет элемент onsie в корзину"):
            add_onsie = self.wait.until(EC.element_to_be_clickable(
                        self.ADD_ONSIE))
            add_onsie.click()


class CartPage:
    CART = (By.CLASS_NAME, 'shopping_cart_link')

    def __init__(self, driver):
        """
        Конструктор класса CartPage
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Переход на страницу корзины")
    def click_cart(self) -> None:
        """
        Кликает на кнопку перехода на страницу корзины.

        :return: None, так как метод ничего не возвращает.
        """
        cart = self.wait.until(EC.element_to_be_clickable(
            self.CART))
        cart.click()


class CheckoutPage:
    CHECKOUT_BUTTON = (
        By.CLASS_NAME, 'btn.btn_action.btn_medium.checkout_button ')

    def __init__(self, driver):
        """
        Конструктор класса CheckoutPage
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Подтверждает покупку товаров кликом на checkout_button ")
    def click_checkout(self) -> None:
        """
        Подтверждает покупку товаров, кликая на кнопку checkout.

        :return: None, так как метод ничего не возвращает.
        """
        checkout_button = self.wait.until(EC.element_to_be_clickable(
            self.CHECKOUT_BUTTON))
        checkout_button.click()


class InformationPage:
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    ZIP_CODE = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    TOTAL_TEXT = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        """
        Конструктор класса InformationPage
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Заполняет поля {firstname}, {lastname} и {zipcode}")
    def information(self, firstname: str, lastname: str, zipcode: str) -> str:
        """
        Заполняет информацию о покупателе: Имя, Фамилия и Индекс.
        Возвращает строку с подтверждением успешного выполнения.

        :param firstname: Имя покупателя, строка.
        :param lastname: Фамилия покупателя, строка.
        :param zipcode: Почтовый индекс покупателя, строка.
        :return: Строка, подтверждающая успешное заполнение информации.
        """
        with allure.step("Заполняет поле Имя"):
            self.wait.until(EC.presence_of_element_located(
                    self.FIRST_NAME)).send_keys(firstname)
        with allure.step("Заполняет поле Фамилия"):
            self.wait.until(EC.presence_of_element_located(
                    self.LAST_NAME)).send_keys(lastname)
        with allure.step("Заполняет поле Индекс"):
            self.wait.until(EC.presence_of_element_located(
                    self.ZIP_CODE)).send_keys(zipcode)
        with allure.step("Прокручивает страницу и кликает по кнопке continue"):
            continue_button = self.wait.until(EC.element_to_be_clickable(
                    self.CONTINUE_BUTTON))
            continue_button.click()
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Получает и сравнивает итоговый результат")
    def get_total(self) -> str:
        """
        Получает итоговую сумму с страницы и возвращает её в виде строки.

        :return: Итоговая сумма в виде строки,
        полученная с элемента на странице.
        """
        total_text = self.wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label")))
        total_result = total_text.text
        return total_result
