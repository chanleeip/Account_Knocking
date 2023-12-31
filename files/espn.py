from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time

def check_account_espn(email):
    driver = webdriver.Firefox()
    driver.get("https://www.espn.in/")
    driver.implicitly_wait(10)
    login_button_hover=driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/header/div[2]/ul/li[2]/a')
    ActionChains(driver).move_to_element(login_button_hover).perform()
    login_button_hover.click()
    li_element = driver.find_element(By.XPATH,'//*[@id="global-viewport"]/div[3]/div/ul[2]/li/div/div/a')
    driver.execute_script("arguments[0].click();",li_element)
    driver.implicitly_wait(10)

    # email_feild_div=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[2]/div/div/form/label/div')
    # email_feild_div.location_once_scrolled_into_view()
    # email_feild=driver.find_element(By.XPATH,'//*[@id="InputIdentityFlowValue"]')
    # driver.execute_script("arguments[0].click();",email_feild)
    # email_feild.send_keys("nithinnmanickam@gmail.com")

    iframe_div=driver.find_element(By.XPATH,'//*[@id="oneid-iframe"]')
    driver.switch_to.frame(iframe_div)
    email_feild=driver.find_element(By.XPATH,'//*[@id="InputIdentityFlowValue"]')
    email_feild.send_keys(email)
    email_feild_submit=driver.find_element(By.XPATH,'//*[@id="BtnSubmit"]')
    email_feild_submit.click()
    try:
        time.sleep(5)
        not_found_log = driver.find_element(By.XPATH, '//*[@id="Title"]')
        not_found_log_text = not_found_log.text
        
        if not_found_log_text == 'Good news, you already have an account':
            return(True)
        else:
            return(False)
    except NoSuchElementException:
        return(False)



    driver.close()
