import robobrowser
from selenium import webdriver
import re
import json
import os
import random
from time import sleep

MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; U; en-gb; KFTHWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.16 Safari/535.19"
FB_AUTH = "https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&client_id=464891386855067&ret=login&fallback_redirect_uri=221e1158-f2e9-1452-1a05-8983f99f7d6e&ext=1556057433&hash=Aea6jWwMP_tDMQ9y"


def get_access_token_test(email,password):
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(FB_AUTH)

    email_input = driver.find_element_by_xpath('//*[@id="email"]')
    email_input.send_keys(email)
    password_input = driver.find_element_by_xpath('//*[@id="pass"]')
    password_input.send_keys(password)
    login_btn = driver.find_element_by_xpath('//*[@id="loginbutton"]')
    login_btn.click()
    ok_btn = driver.find_element_by_xpath('//*[@id="platformDialogForm"]/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td[2]/button[2]')
    ok_btn.click()

    

def get_access_token(email, password):
    s = robobrowser.RoboBrowser(user_agent=MOBILE_USER_AGENT, parser = "lxml")
    s.open(FB_AUTH)
    ##submit login form##
    f = s.get_form()
    f["pass"] = password
    f["email"] = email
    s.submit_form(f)
    ##click the 'ok' button on the dialog informing you that you have already authenticated with the Tinder app
    f = s.get_form()
    ##get access token from the html response##
    access_token = re.search(r"access_token=([\w\d]+)", s.response.content.decode()).groups()[0]
    # print s.response.content.decode()
    return access_token

def get_login_credentials():
    print("Checking for credentials..")
    if os.path.exists('auth.json'):
        print("Auth.json existed..")
        with open("auth.json") as data_file:
            data = json.load(data_file)
            if "email" in data and "password" in data and "FBID" in data:
                return (data["email"], data["password"], data["FBID"])
            else:
                print ("Invalid auth.json file")

    print ("Auth.json missing or invalid. Please enter your credentials.")
    return (input("Enter email ..\n"), input("Enter password..\n"))
