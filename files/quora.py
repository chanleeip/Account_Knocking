from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def check_account_quora(email):
    driver = webdriver.Firefox()
    driver.get("https://www.quora.com/login")
    driver.implicitly_wait(10)
    email_feild=driver.find_element(By.XPATH,'//*[@id="email"]')
    email_feild.send_keys(email)

    try:
        time.sleep(5)
        not_found_log = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[3]/div')
        not_found_log_text = not_found_log.text
        if not_found_log_text == 'No account found for this email. Retry, or Sign up for Quora.':
            return(False)
        else:
            return(True)
    except NoSuchElementException:
        return(True)
    