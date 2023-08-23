from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import unittest

link = "http://suninjuly.github.io/registration1.html"
driver = webdriver.Chrome()
driver.get(link)

try:
    input1 = driver.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.NAME, "email")
    input3.send_keys("test@mail.ru")

    button = driver.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()
    driver.close()

# не забываем оставить пустую строку в конце файла