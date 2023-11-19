from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

import time
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

PATH = r"C:\Program Files (x86)\msedgedriver"
service = Service(PATH)

driver = webdriver.Edge(service=service)

# #login 
# login=os.getenv("login")
# password=os.getenv("password")

# driver.get("https://soccerguru.live/dashboard")

# try:
#     container = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div/div/div/form'))
#     )
# except:
#     print("container not found")
# try:
#     email_box = container.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/input')
#     email_box.send_keys(login)
#     mdp_box = container.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/div[2]/div/input')
#     mdp_box.send_keys(password)
#     email_box.submit()
#     time.sleep(7)

# except:
#     print("inputs not found")

# try:
#     button_container = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME,'authorize__4ddfc'))
#     )
# except:
#     print("container not find")
# try:
#     button = button_container.find_element(By.CSS_SELECTOR,'#app-mount > div.appAsidePanelWrapper__714a6 > div.notAppAsidePanel__9d124 > div.app_b1f720 > div > div > div > div > div > div.footer__04ee2 > button.button_afdfd9.lookFilled__19298.colorBrand_b2253e.sizeMedium_c6fa98.grow__4c8a4')
#     button.click()
# except:
#     print("button not found")

# time.sleep(5)


# actions = ActionChains(driver)

# #claiming ad reward
# try:
#     watch_ad = driver.find_element(By.CSS_SELECTOR,"#__nuxt > div > div.flex-grow > div > div > div.flex.flex-col.gap-4.px-4.md\:px-8 > div.flex.flex-col.gap-4.bg-blue-600.p-8.rounded.shadow > a")
#     actions.move_to_element(watch_ad).perform()
#     actions.click().perform()
#     time.sleep(30)
#     driver.quit
# except:
#     print("watch_ad not found")

# #claiming claim reward
# try:
#     claim= driver.find_element(By.CSS_SELECTOR,"#__nuxt > div > div.flex-grow > div > div > div.flex.flex-col.gap-4.px-4.md\:px-8 > div:nth-child(3) > div:nth-child(1) > a")
#     actions.move_to_element(claim).perform()
#     actions.click().perform()
#     time.sleep(5)
# except:
#     print("claim not found")


# #claiming daily reward
# try:
#     daily= driver.find_element(By.CSS_SELECTOR,"#__nuxt > div > div.flex-grow > div > div > div.flex.flex-col.gap-4.px-4.md\:px-8 > div:nth-child(3) > div:nth-child(2) > a")
#     actions.move_to_element(daily).perform()
#     actions.click().perform()
#     time.sleep(5)
# except:
#     print("daily not found")



# time.sleep(5)

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def login(driver, login, password):
    driver.get("https://soccerguru.live/dashboard")

    try:
        container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div/div/div/form'))
        )
    except:
        print("container not found")
    
    try:
        email_box = container.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/input')
        email_box.send_keys(login)
        mdp_box = container.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/div[2]/div/input')
        mdp_box.send_keys(password)
        email_box.submit()
        
        try:
            button_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME,'authorize__4ddfc'))
            )
        except:
            print("container not find")
        try:
            button = button_container.find_element(By.CSS_SELECTOR,'#app-mount > div.appAsidePanelWrapper__714a6 > div.notAppAsidePanel__9d124 > div.app_b1f720 > div > div > div > div > div > div.footer__04ee2 > button.button_afdfd9.lookFilled__19298.colorBrand_b2253e.sizeMedium_c6fa98.grow__4c8a4')
            button.click()
            
        except:
            print("button not found")
        time.sleep(10)   
    except:
        print("inputs not found")


def claim_reward(driver):
    try:
        
        
        claim = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"#__nuxt > div > div.flex-grow > div > div > div.flex.flex-col.gap-4.px-4.md\:px-8 > div:nth-child(3) > div:nth-child(1) > a"))
            )
        time.sleep(5)
        claim.click()
       
    except:
        print("claim not found")



def main():
    driver = webdriver.Edge()  # Make sure to replace with the appropriate WebDriver
    login(driver, os.getenv("login"), os.getenv("password"))

    claim_reward(driver)

    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    main()
