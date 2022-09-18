#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import json
from selenium.webdriver.chrome.options import Options
import Account
import Get_Data_User
import GetXpath

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
scroll_page = driver.execute_script("window.scrollTo(0,1280);")

#define scroll height
scroll_height=1200

#define list PROFILE
PROFILE = []

#define list link user
list_link_user = []

#user in group
members = 5

#get user information
for member in range(members):
    try:
        #target user name
        name_user = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div[9]/div/div[2]/div/div['+str(member)+']/div/div/div[2]/div[1]/div/div/div[1]/span/span/span/a')))
        
        #get link profile user
        link_user = name_user.get_attribute('href')
        list_link_user.append(link_user)

        print(link_user)
        name_user.click()
        sleep(1.5)
        
        #click view main profile
        try: 
            view_main_profile = driver.find_element(By.XPATH,"//span[text()='View Main Profile']").click()
        except:
             #target the three-dot button
            three_dot_button= driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[2]/div/div').click()
            sleep(0.5)
            view_main_profile_in_three_dot_button = driver.find_element(By.XPATH,"//span[text()='View Main Profile']").click()
            sleep(1)
        
        #click about user
        try:
            about_user = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[2]'))).click()
            sleep(1.5)

            #scroll profile
            scroll_profile = driver.execute_script("window.scrollTo(0,350);")
            sleep(1)

            # user_name = data_user.GetUserName()
            # user_work = data_user.GetUserWork()
            # user_education = data_user.GetUserEducation()
            # user_live = data_user.GetUserLive()
            # user_hometown = data_user.GetUserHometown()
            # user_relationship = data_user.GetUserRelationship()

            user_name =driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div/div/span/div/h1').text
            print(f'user name: {user_name}')

            #target and print user work
            try:
                user_work = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[2]/div[1]/span/a/span/span').text
                print(f'user work: {user_work}')
            except:

                user_work = None 
                print(f'user work: {user_work}')    

            #target and print user education
            try:
                user_education = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/span/a/span/span').text
                print(f'user education: {user_education}')
            except:
                user_education = None
                print(f'user education: {user_education}')

            #target and print user live
            try:
                user_live = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div[2]/div/span/a/span/span').text
                print(f'user live in: {user_live}')
            except:
                user_live = None
                print(f'user live in: {user_live}')

            #target and print user hometown
            try:
                user_hometown = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[4]/div/div/div[2]/div/span/a/span/span').text
                print(f'user hometown: {user_hometown}')
            except:
                user_hometown = None
                print(f'user hometown: {user_hometown}')

            # target and print user relationship
            try:
                user_relationship = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[5]/div/div/div[2]/span').text
                print(f'user relationship: {user_relationship}')
            except:
                user_relationship = None
                print(f'user relationship: {user_relationship}')

        except:
            continue

        #back to the previous page
        driver.execute_script("window.history.go(-1)")
        sleep(1)

        #back to the previous page
        driver.execute_script("window.history.go(-1)")
        sleep(1)

        #scroll page
        scroll_page = driver.execute_script("window.scrollTo(0,"+str(scroll_height)+");")

        # increase scroll height
        scroll_height+=100

        data = {
            "name": user_name,
            "work": user_work,
            "education": user_education,
            "live in": user_live,
            "hometown": user_hometown,
            "relationship": user_relationship
        }

        print(data)

        PROFILE.append(data)

    except Exception:
        print(Exception) 
        continue

json_object = json.dumps(PROFILE, indent = 4, ensure_ascii=False) # UTF-8 fixed
print(json_object)

with open('profile_facebook.json', 'w', encoding='utf-8') as outfile:
    outfile.write(json_object)

for user in list_link_user:

    print(user)

driver.close()

