#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.chrome.options import Options
import Account
import csv
import json
import time

start_time = time.time()

#disable alerts chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='./chromedriver')
 
driver.get('https://www.facebook.com/')
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

#enter username and password
username.clear()
username.send_keys(Account.GetUsername())
password.clear()
password.send_keys(Account.GetPassWord())

#target the login button and click it
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

list_url= []

with open('list_user.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for lines in csv_reader:
        for id in lines:
            base_url = 'https://www.facebook.com/{}/about'
            url = base_url.format(id)
            list_url.append(url)

print(list_url)

#define list PROFILE            
PROFILE = []            

for url_user in list_url[:20]:
    try:
        driver.get(url_user)
    
        #scroll profile
        scroll_profile = driver.execute_script("window.scrollTo(0,350);")

        user_name = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div/div/span/div/h1'))).text
        print(user_name)
        #target and print user work
        try:
            user_work = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[2]/div[1]/span/a/span/span'))).text
        except:
            user_work = None    

        #target and print user education
        try:
            user_education = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/span/a/span/span'))).text
        except:
            user_education = None

        #target and print user live
        try:
            user_live = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div[2]/div/span/a/span/span'))).text
        except:
            user_live = None

        #target and print user hometown
        try:
            user_hometown = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[4]/div/div/div[2]/div/span/a/span/span'))).text
        except:
            user_hometown = None

        # target and print user relationship
        try:
            user_relationship = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[5]/div/div/div[2]/span'))).text
        except:
            user_relationship = None

        data = {
            "name": user_name,
            "work": user_work,
            "education": user_education,
            "live in": user_live,
            "hometown": user_hometown,
            "relationship": user_relationship
        }

        PROFILE.append(data)

    except:
        continue

driver.close()

json_object = json.dumps(PROFILE, indent = 4, ensure_ascii=False) # UTF-8 fixed
print(json_object)

with open('profile_facebook.json', 'w', encoding='utf-8') as outfile:
    outfile.write(json_object)

end_time = time.time()
elapsed_time = end_time - start_time
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

    

