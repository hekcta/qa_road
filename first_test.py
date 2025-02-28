import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


url = "http://95.182.122.183/sign_up"

def test_positive_registration():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    time.sleep(2)

    driver.find_element(By.ID, "name").send_keys("user22")
    driver.find_element(By.ID, "pass1").send_keys("qwerty1234")
    driver.find_element(By.ID, "pass2").send_keys("qwerty1234")
    driver.find_element(By.ID, "email").send_keys("myuser1@mail.ru")
    driver.find_element(By.CSS_SELECTOR, ".ui.button.blue").click()
    time.sleep(2)

    assert driver.current_url == "http://95.182.122.183/login"
    time.sleep(2)

    alert = driver.find_element(By.CSS_SELECTOR, "div.Toastify__toast-body")
    # alert = driver.find_element(By.CSS_SELECTOR, "div[class ='Toastify__toast-body']")
    assert alert.get_attribute("textContent") == "Вы успешно зарегистрировались"
    driver.quit()