from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()

driver.get("https://in.pinterest.com/")

driver.implicitly_wait(2)
login_button=driver.find_element(By.XPATH,'//*[@id="mweb-unauth-container"]/div/div/div[1]/div/div[2]/div[2]/button')
login_button.click()

email_input_feild=driver.find_element(By.XPATH,'//*[@id="email"]')
passwrod_input_feild=driver.find_element(By.XPATH,'//*[@id="password"]')

email_input_feild.send_keys("nithinnmanickam@hotmail.com")
passwrod_input_feild.send_keys("Chunkymani@01")

submit_button=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[4]/form/div[7]/button')
submit_button.click()

try:
    not_found_log = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[4]/form/div[2]/fieldset/span/div[2]/div/span/div/div/div[2]')
    not_found_log_text = not_found_log.text
    
    if not_found_log_text == 'The email you entered does not belong to any account.':
        print("Account doesn't exist on Pinterest")
    else:
        print("Account exists")
except NoSuchElementException:
    print("Account may exist.")
driver.close()
