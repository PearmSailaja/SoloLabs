import time

from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

@given(u'I am on the Demo Login Page')
def launch_browser(context):
    context.driver=webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get("https://www.saucedemo.com/")
    context.driver.maximize_window()
    time.sleep(10)

@when(u'I fill the account information for account StandardUser into the Username field and the Password field')
def fill_Userinfo(context):
    user_name=context.driver.find_element(By.XPATH,'//*[@id="user-name"]')
    user_name.send_keys("standard_user")
    user_pwd = context.driver.find_element(By.XPATH, '//*[@id="password"]')
    user_pwd.send_keys('secret_sauce')

@when(u'I click the Login Button')
def click_login(context):
    login_btn=context.driver.find_element(By.XPATH,'//*[@id="login-button"]')
    login_btn.click()
    time.sleep(5)

@then(u'I am redirected to the Demo Main Page')
def  Directing_to_MainPage(context):
    get_title = context.driver.title
    print(get_title)

@then(u'I verify the App Logo exists')
def Verify_Logo(context):
    app_logo=context.driver.find_element(By.XPATH,'//*[@id="header_container"]/div[1]/div[2]/div')
    status=app_logo.is_displayed()
    assert status==True
    # closing browser
    context.driver.close()

