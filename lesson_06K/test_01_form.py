from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 20)
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    driver.maximize_window()
    first_name = wait.until(EC.presence_of_element_located(
        (By.NAME, 'first-name')))
    first_name.send_keys('Иван')
    last_name = wait.until(EC.presence_of_element_located(
            (By.NAME, 'last-name')))
    last_name.send_keys('Петров')
    address = wait.until(EC.presence_of_element_located(
            (By.NAME, 'address')))
    address.send_keys('Ленина, 55-3')
    email = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[wfd-id="id6"]')))
    email.send_keys('test@skypro.com')
    phone = wait.until(EC.presence_of_element_located(
            (By.NAME, 'phone')))
    phone.send_keys('+7985899998787')
    zip_code = wait.until(EC.presence_of_element_located(
            (By.NAME, 'zip-code')))
    zip_code.send_keys('')
    city = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[wfd-id="id4"]')))
    city.send_keys('Москва')
    country = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[wfd-id="id5"]')))
    country.send_keys('Россия')
    job_position = wait.until(EC.presence_of_element_located(
                (By.NAME, 'job-position')))
    job_position.send_keys('QA')
    company = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[wfd-id="id9"]')))
    company.send_keys('SkyPro')
    submit_button = wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, 'btn.btn-outline-primary.mt-3')))
    submit_button.click()
    zip_code_field = driver.find_element(
        By.CLASS_NAME, 'alert.py-2.alert-danger')
    background_color = zip_code_field.value_of_css_property('background-color')
    assert background_color == 'rgba(248, 215, 218, 1)', \
        f"Поле {zip_code_field} не подсвечено красным цветом"
    print(background_color)
    list_of_fields = ['first_name', 'last_name', 'address', 'email',
                      'phone', 'city', 'country', 'job_position', 'company']
    for fields in list_of_fields:
        list_element = driver.find_element(By.CLASS_NAME,
                                           'alert.py-2.alert-success')
    border_color = list_element.value_of_css_property("background-color")
    assert border_color == "rgba(209, 231, 221, 1)", \
        f"Поле {fields} неподсвечено зеленым"

    driver.quit()
