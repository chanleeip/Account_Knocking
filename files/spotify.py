from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Firefox()

driver.get("https://www.spotify.com/in-en/signup")

driver.implicitly_wait(2)



email_feild=driver.find_element(By.XPATH,'//*[@id="username"]')
email_feild.send_keys("nithinnmanickam@hotmail.com")

email_feild_button=driver.find_element(By.XPATH,'//*[@id="__next"]/main/main/section/div/div/form/button')
email_feild_button.click()

try:
    time.sleep(5)
    not_found_log = driver.find_element(By.XPATH, '//*[@id="__next"]/main/main/section/div/div/form/div/div/div/div/div[2]/div[1]/span/span')
    not_found_log_text = not_found_log.text
    print(not_found_log_text)
    
    if not_found_log_text == 'This address is already linked to an existing account. To continue, log in.':
        print("Account Exists")
    else:
        print("Account not exists")
except NoSuchElementException:
    print("Account  not exists.")
