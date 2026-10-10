from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 50)
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    driver.maximize_window()
    input_field = wait.until(EC.presence_of_element_located((By.ID, 'delay')))
    input_field.clear()
    input_field.send_keys(45)
    button_7 = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//span[text()='7']")))
    button_7.click()
    button_sum = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//span[text()='+']")))
    button_sum.click()
    button_8 = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//span[text()='8']")))
    button_8.click()
    button_equals = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//span[text()='=']")))
    button_equals.click()
    result_element = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[text()='15']")))
    result_text = result_element.text
    assert result_text == '15', "Результат не равен 15"

    driver.quit()
