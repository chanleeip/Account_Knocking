from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Firefox()

driver.get("https://www.quora.com/login")

driver.implicitly_wait(10)


email_feild=driver.find_element(By.XPATH,'//*[@id="email"]')
email_feild.send_keys("nithinnmanickam@gmail.com")


try:
    time.sleep(5)
    not_found_log = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[3]/div')
    not_found_log_text = not_found_log.text
    
    if not_found_log_text == 'No account found for this email. Retry, or Sign up for Quora.':
        print("Account not  Exists")
    else:
        print("Account exists")
except NoSuchElementException:
    print("Account exist.")