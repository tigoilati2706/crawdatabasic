#imports here
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.chrome.options import Options
import Account
import datetime
import csv
import numpy as np
import json
import time
import pandas as pd
# import test_get_list_id

#disable alerts chrome driver
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-software-rasterizer")

prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='./chromedriver')
 
# access to facebook.com
driver.get('https://www.facebook.com/')

# target username and password
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

#enter username and password
username.clear()
username.send_keys(Account.GetUsername())
password.clear()
password.send_keys(Account.GetPassWord())

#target the login button and click it
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
sleep(0.5)

# declare list url
list_url= []

# read data from csv file and create url then append to list_url
with open('list_user123.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for lines in csv_reader:
        for id in lines:
            base_url = 'https://www.facebook.com/{}/about'
            url = base_url.format(id)
            list_url.append(url)

# start time
# start_time = time.time()

# declare list PROFILE            
PROFILE = []            

not_found = "Null"

# loop to get data from profile user
for url_user in list_url[:1706]:
    try:
        # get url to profile user
        driver.get(url_user)
        sleep(8)
        # sleep(100)
        id = url_user[-21:-6]

        # scroll profile
        scroll_profile = driver.execute_script("window.scrollTo(0,350);")

        # target and get username
        user_name =driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/span/div/h1').text

        # target and get user work
        try:
            user_work = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[2]/div/span/a/span/span').text
        except:
            user_work = not_found 

        # target and get user education
        try:
            user_education = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/span/a/span/span').text
        except:
            user_education = not_found

        # target and get user live
        try:
            user_live = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div[2]/div/span/a/span/span').text
        except:
            user_live = not_found

        # target and get user hometown
        try:
            user_hometown = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[4]/div/div/div[2]/div/span/a/span/span').text
        except:
            user_hometown = not_found

        date_stay = datetime.datetime.now()

        # declare dict
        data = {
            "id":id,
            "name": user_name,
            "work": user_work,
            "education": user_education,
            "live in": user_live,
            "hometown": user_hometown,
            "time stay": date_stay,
            "name group": "Cộng đồng Marketing & Advertising",
            "link group": "https://www.facebook.com/groups/advertisingvietnam/members"
        }
    
        # append dict to list
        PROFILE.append(data)

    except:
        #continue if user not about
        continue


# close chrome driver
driver.close()

#export to csv
df = pd.DataFrame(PROFILE).to_csv('profile_user.csv', index=False)

#delete column index
# np.savetxt('profile_user.csv', PROFILE, fmt='%s')

# cal time
# end_time = time.time()
# elapsed_time = end_time - start_time
# print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

    

