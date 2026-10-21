from pages.calc_page import PageObject
from selenium import webdriver


def test_calculator():
    driver = webdriver.Chrome()
    driver.maximize_window()
    calculator = PageObject(
        driver, url='https://bonigarcia.dev/selenium-webdriver-java'
        '/slow-calculator.html')
    calculator.open_calc_page()
    calculator.enter_value()
    calculator.press_buttons()
    result_text = calculator.get_result()
    assert result_text == '15', "Результат не равен 15"

    driver.quit()
