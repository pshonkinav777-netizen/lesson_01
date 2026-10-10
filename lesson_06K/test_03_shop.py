from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 20)
    driver.get(
        'https://www.saucedemo.com/')
    driver.maximize_window()
    driver.delete_all_cookies()
    login = wait.until(EC.presence_of_element_located((By.ID, 'user-name')))
    login.send_keys('standard_user')
    password = wait.until(EC.presence_of_element_located((By.ID, 'password')))
    password.send_keys('secret_sauce')
    login_button = wait.until(EC.presence_of_element_located(
        (By.ID, 'login-button')))
    login_button.click()
    add_backpack = wait.until(EC.presence_of_element_located(
        (By.ID, 'add-to-cart-sauce-labs-backpack')))
    add_backpack.click()
    add_bolt_t_shirt = wait.until(EC.presence_of_element_located(
        (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')))
    add_bolt_t_shirt.click()
    add_onsie = wait.until(EC.presence_of_element_located(
        (By.ID, 'add-to-cart-sauce-labs-onesie')))
    add_onsie.click()
    cart = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, 'shopping_cart_link')))
    cart.click()
    checkout_button = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, 'btn.btn_action.btn_medium.checkout_button ')))
    checkout_button.click()
    first_name = wait.until(EC.presence_of_element_located(
        (By.ID, 'first-name')))
    first_name.send_keys('Alex')
    last_name = wait.until(EC.presence_of_element_located(
        (By.ID, 'last-name')))
    last_name.send_keys('P')
    zip_code = wait.until(EC.presence_of_element_located(
        (By.ID, 'postal-code')))
    zip_code.send_keys('123124')
    continue_button = wait.until(EC.presence_of_element_located(
        (By.ID, 'continue')))
    continue_button.click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    total_text = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "summary_total_label"))).text
    assert '58.29' in total_text
    sum_value = total_text

    driver.quit()

    assert '58.29' in sum_value
