from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.options import Options
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)
options.page_load_strategy = 'eager'

driver.get('https://citaty.info/random')
text = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/main/div/div/div/div/div[2]/article/div[1]/div[1]/div/div/p')
print(text.text)
print('################################')
spisok = driver.find_elements(By.CLASS_NAME, 'field-items')
for s in spisok:
    try:
        a = s.find_element(By.TAG_NAME, 'a')
        if a.get_attribute('title') != '':
            print(a.get_attribute('title'), a.text)
            print('***************************')
    except:
        pass
driver.close()
