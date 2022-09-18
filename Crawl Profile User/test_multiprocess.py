#imports here
from ast import arguments
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
from multiprocessing import process

capa = DesiredCapabilities().CHROME
capa["pageLoadStrategy"] = "normal"

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

driver = webdriver.Chrome(chrome_options=chrome_options, desired_capabilities=capa, executable_path='./chromedriver')

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

start_time = time.time()

# scroll to bottom page
def scroll_page(i_start, i_end):
    for i in range(i_start, i_end):
        print(i)
        last_height = driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
        sleep(3)
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
def main():
    p1 = process(target = scroll_page, args = (0,100,))
    p2 = process(target = scroll_page, args = (100,200,))
    p3 = process(target = scroll_page, args = (200,300,))
    p4 = process(target = scroll_page, args = (300,400,))

    p1.start()
    # p2.start()
    # p3.start()
    # p4.start()

    p1.join()
    # p2.join()
    # p3.join()
    # p4.join()

if __name__ == '__main__':
    main()
    
end_time = time.time(0)
elapsed_time = end_time - start_time
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

# declare list_id
list_id = []

# target and get all the <a> elements
users = driver.find_element(By.CLASS_NAME,'obtkqiv7').find_elements(By.TAG_NAME, 'a')

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
df = pd.DataFrame(data).to_csv('list_user.csv')

# delete column index
np.savetxt('list_user.csv', list_id, fmt='%s')



