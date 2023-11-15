from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd

import time
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

PATH = r"C:\Program Files (x86)\msedgedriver"
service = Service(PATH)

driver = webdriver.Edge(service=service)


driver.get("https://soccerguru.live/dashboard")
time.sleep(10)
try:
    container = driver.find_element(By.XPATH,'//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div/div/div/form')
except:
    print("container not found")
try:

    email_box = container.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/input')
    email_box.send_keys(os.getenv("login"))
    mdp_box = container.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/div[2]/div/input')
    mdp_box.send_keys(os.getenv("password"))
    email_box.submit()

except:
    print("inputs not found")

time.sleep(5)
try:
    button = driver.find_element(By.LINK_TEXT,'Autoriser')
    button.click()
except:
    print("button not found")


time.sleep(10)
# def Video_Ad_Reward ():
#     driver.get("https://www.allrecipes.com/ingredients-a-z-6740416")
#     load_more =WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.CLASS_NAME, "loadmorenow")))