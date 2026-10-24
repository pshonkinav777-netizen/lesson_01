from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    INPUT_FIELD = (By.ID, 'delay')
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_SUM = (By.XPATH, "//span[text()='+']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_EQUALS = (By.XPATH, "//span[text()='=']")
    RESULT_ELEMENT = (By.XPATH, "//div[text()='15']")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 50)

    def open_calc_page(self):
        self.driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java'
            '/slow-calculator.html')

    def enter_value(self):
        input_field = self.wait.until(
            EC.presence_of_element_located(self.INPUT_FIELD))
        input_field.clear()
        input_field.send_keys(45)

    def press_buttons(self):
        button_7 = self.wait.until(EC.presence_of_element_located(
                self.BUTTON_7))
        button_7.click()
        button_sum = self.wait.until(EC.presence_of_element_located(
                self.BUTTON_SUM))
        button_sum.click()
        button_8 = self.wait.until(EC.presence_of_element_located(
                self.BUTTON_8))
        button_8.click()
        button_equals = self.wait.until(EC.presence_of_element_located(
                self.BUTTON_EQUALS))
        button_equals.click()

    def get_result(self):
        result_element = self.wait.until(EC.visibility_of_element_located(
                self.RESULT_ELEMENT))
        result_text = result_element.text
        return result_text
