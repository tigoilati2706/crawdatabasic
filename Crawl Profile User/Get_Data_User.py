#imports here
from selenium import webdriver
from selenium.webdriver.common.by import By
import GetXpath

#disable alerts chrome driver
def GetUserName():
    user_name = driver.find_element(By.XPATH, GetXpath.GetXpathUserName()).text
    print(f'user name: {user_name}')
    return user_name    

def GetUserWork():   
    try:
        user_work = driver.find_element(By.XPATH,GetXpath.GetXpathUserWork()).text
        print(f'user work: {user_work}')
    except:
        user_work = None
        print(f'user work: {user_work}')
    return user_work
    
def GetUserEducation(): 
    try:
        user_education = driver.find_element(By.XPATH, GetXpath.GetXpathUserEducation()).text
        print(f'user education: {user_education}')
    except:
        user_education = None
        print(f'user education: {user_education}')
        return user_education

def GetUserLive(): 
    try:
        user_live = driver.find_element(By.XPATH, GetXpath.GetXpathUserLive()).text
        print(f'user live in: {user_live}')
    except:
        user_live = None
        print(f'user live in: {user_live}')
    return user_live

def GetUserHometown(): 
    try:
        user_hometown = driver.find_element(By.XPATH, GetXpath.GetXpathUserHometown()).text
        print(f'user hometown: {user_hometown}')
    except:
        user_hometown = None
        print(f'user hometown: {user_hometown}')
    return user_hometown

def GetUserRelationship(): 
    try:
        user_relationship = driver.find_element(By.XPATH, GetXpath.GetXpathUserRelationship()).text
        print(f'user relationship: {user_relationship}')
    except:
        user_relationship = None
        print(f'user relationship: {user_relationship}')
    return user_relationship
