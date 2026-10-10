from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    # wait = WebDriverWait(driver, 30)
    driver.maximize_window()
    driver.get('https://gitflic.ru/')
    driver.add_cookie({
      "name": "SESSION",
      "value": "YTc2NjI3ZWQtMzQ3Zi00N2RhLTkzMmMtZGM5Yjk4NzgwZTY3",
      "domain": "gitflic.ru"})
    driver.refresh()
    driver.get('https://gitflic.ru/user/pavel_sky')
    # wait.until(EC.presence_of_element_located(
    #      (By.CLASS_NAME, 'header-username')))
    current_url1 = driver.current_url

    driver.delete_all_cookies()
    driver.refresh()
    driver.add_cookie({
          "name": "SESSION",
          "value": "YWQ4ZDBmZjYtZTBiYi00MWM0LWE4ODAtNmJjYzg2YzVhNDVk",
          "domain": "gitflic.ru"
       })
    driver.refresh()
    driver.get('https://gitflic.ru/user/alex_skypro')
    current_url2 = driver.current_url
    assert current_url1 != current_url2

    driver.quit()
