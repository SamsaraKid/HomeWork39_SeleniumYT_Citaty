from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.firefox.options import Options
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(options=options)
options.page_load_strategy = 'eager'

driver.get('https://www.youtube.com/')
driver.implicitly_wait(5)
print('open site')
yt = driver.find_element(By.TAG_NAME, 'input')
yt.send_keys('смешные видео про котов')
print('write to search')
time.sleep(2)
yt1 = driver.find_element(By.ID, 'search-icon-legacy')
yt1.click()
print('click search')
time.sleep(5)
spisok = driver.find_elements(By.TAG_NAME, 'ytd-video-renderer')
print('list of vids', len(spisok))

r = random.randint(0, len(spisok) - 1)
link = spisok[r].find_element(By.TAG_NAME, 'yt-formatted-string')
# action = ActionChains(driver)
# action.move_to_element(link)
# action.click(link).perform()
link.click()
print('vid click', r)

time.sleep(3)
like = driver.find_element(By.XPATH, '//*[@id="segmented-like-button"]')
like.click()
print('click like')

time.sleep(3)
driver.close()
print('end')