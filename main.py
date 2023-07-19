from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get('https://www.youtube.com/')
driver.find_element(By.TAG_NAME, 'input').send_keys('смешные видео про котов')
driver.find_element(By.TAG_NAME, 'input').submit()
# driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]')


results = driver.find_elements(By.CLASS_NAME, 'yt-simple-endpoint')
results[0].click()

