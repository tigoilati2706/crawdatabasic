#imports here
from email import header
from importlib.resources import path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.chrome.options import Options
import Account

#disable alerts chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='./chromedriver')

driver.get('https://www.facebook.com/groups/advertisingvietnam/members')

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

#enter username and password
username.clear()
username.send_keys(Account.GetUsername())
password.clear()
password.send_keys(Account.GetPassWord())

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
sleep(5)

#scroll page
scroll_page = driver.execute_script("window.scrollTo(0,1200);")
sleep(1)

list_id = []

members = 5000

#define scroll height
scroll_height=1200

for member in range(members):
    try:
        name_user = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div[9]/div/div[2]/div/div['+str(member)+']/div/div/div[2]/div[1]/div/div/div[1]/span/span/span/a')))
        
        #get link profile user
        link_user = name_user.get_attribute('href')

        id = link_user[-16:-1]
    
        list_id.append(id)
        sleep(0.2)
        
        #scroll page
        scroll_page = driver.execute_script("window.scrollTo(0,"+str(scroll_height)+");")

        # increase scroll height
        scroll_height+=100

    except Exception:
        continue

driver.close()

import pandas as pd

data  ={
    "id": list_id
}

df = pd.DataFrame(data).to_csv('list_user.csv')


import numpy as np

np.savetxt('list_user.csv', list_id, fmt='%s')



