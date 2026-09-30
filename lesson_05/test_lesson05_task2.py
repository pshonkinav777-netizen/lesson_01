from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    # Ваш код здесь [name="custname"]
    driver.find_element(By.CSS_SELECTOR, value='[name="custname"]').send_keys(
        'Алексей Владимирович')
    sleep(3)

    driver.find_element(By.CSS_SELECTOR, value='[type="submit"]').click()
    assert driver.current_url.endswith('/post')
    sleep(2)

    driver.quit()
