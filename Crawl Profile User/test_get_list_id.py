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
import numpy as np
import pandas as pd
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# capa = DesiredCapabilities().CHROME
# capa["pageLoadStrategy"] = "normal"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument("--disable-software-rasterizer")
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--incognito")
chrome_options.add_argument("enable-automation")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--dns-prefetch-disable")
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='./chromedriver')

# access to facebook.com
driver.get('https://www.facebook.com/groups/advertisingvietnam/members')

# target username and password
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

#enter username and password
username.clear()
username.send_keys(Account.GetUsername())
password.clear()
password.send_keys(Account.GetPassWord())

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
sleep(2)

# scroll to bottom page
for i in range(5):
    print(i)
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
    sleep(2)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# declare list_id
list_id = []

# target and get all the <a> elements
users = driver.find_element(By.CLASS_NAME,'kzdo7wvt').find_elements(By.TAG_NAME, 'a')

for user in users:
    # get link user from attribute href
    link_user = user.get_attribute('href') 

    # slice link_user to get id user
    id = link_user[-16:-1]
    
    # append id to list_id
    list_id.append(id)

# close chrome driver
driver.close()

#remove duplicate in list
sort_list = dict.fromkeys(list_id)
list_id = list(sort_list)

# declare dict to save list id user
data  ={
    "id": list_id
}

# export data to csv file
df = pd.DataFrame(data).to_csv('list_user12345.csv', index=False)

# delete column index
# np.savetxt('list_user12345.csv', list_id, fmt='%s')



