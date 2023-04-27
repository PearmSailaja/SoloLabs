
import time
from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
@given(u'I am on the Demo Login Page of scenario2')
def launch_browser(context):
    context.driver=webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get("https://www.saucedemo.com/")
    context.driver.maximize_window()
    time.sleep(10)

@when(u'I fill the account information for account LockedOutUser into the Username field and the Password field')
def fill_lockedOut_info(context):
    user_name = context.driver.find_element(By.XPATH, '//*[@id="user-name"]')
    user_name.send_keys("locked_out_user")
    user_pwd = context.driver.find_element(By.XPATH, '//*[@id="password"]')
    user_pwd.send_keys('secret_sauce')


@when(u'I click the Login Button of scenario2')
def step_impl(context):
    login_btn = context.driver.find_element(By.XPATH, '//*[@id="login-button"]')
    login_btn.click()
    time.sleep(5)

@then(u'I verify the Error Message contains the text "Sorry, this user has been banned. "')
def step_impl(context):
    msg = context.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    expected_text = "Sorry, this user has been locked out."
    if expected_text in msg:
        print("Error Message contains the text",expected_text)
    else:
        print("Error Message does not  contains the text",expected_text)
    time.sleep(10)
    context.driver.close()