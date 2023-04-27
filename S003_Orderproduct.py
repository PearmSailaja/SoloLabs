import time

from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
@given(u'I am on the inventory page')
def navigate_to_inventoryPage(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get("https://www.saucedemo.com/")
    context.driver.maximize_window()
    user_name = context.driver.find_element(By.XPATH, '//*[@id="user-name"]')
    user_name.send_keys("standard_user")
    user_pwd = context.driver.find_element(By.XPATH, '//*[@id="password"]')
    user_pwd.send_keys('secret_sauce')
    login_btn = context.driver.find_element(By.XPATH, '//*[@id="login-button"]')
    login_btn.click()
    time.sleep(5)

@when(u'user sorts products from low price to high price')
def Sort_lowToHigh(context):
    dd=Select(context.driver.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/div/span/select'))
    dd.select_by_visible_text("Price (low to high)")
    time.sleep(3)
@when(u'user adds lowest priced product')
def add_to_cart(context):
    add_item=context.driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-onesie"]')
    add_item.click()
    time.sleep(3)
@when(u'user clicks on cart')
def Click_On_Cart(context):
    cart= context.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart.click()
    time.sleep(3)
@when(u'user clicks on checkout')
def Click_On_Checkout(context):
    cart= context.driver.find_element(By.ID, "checkout")
    cart.click()
    time.sleep(3)

@when(u'user enters first name John')
def send_FirstName(context):
    FirstName=context.driver.find_element(By.ID,"first-name")
    FirstName.send_keys("John")

@when(u'user enters last name Doe')
def send_LastName(context):
    lastName = context.driver.find_element(By.ID, 'last-name')
    lastName.send_keys("Doe")

@when(u'user enters zip code 123')
def send_ZipCode(context):
    zip = context.driver.find_element(By.ID, 'postal-code')
    zip.send_keys("123")
    time.sleep(5)

@when(u'user clicks Continue button')
def click_continue(context):
    continue_btn= context.driver.find_element(By.ID, 'continue')
    continue_btn.click()
    time.sleep(2)


@then(u'I verify in Checkout overview page if the total amount for the added item is $8.63')
def verify_cost(context):
    cost=context.driver.find_element(By.XPATH,'//*[@id="checkout_summary_container"]/div/div[2]/div[8]').text
    assert cost == "Total: $8.63"

@when(u'user clicks Finish button')
def click_finish(context):
    finish_btn = context.driver.find_element(By.ID, 'finish')
    finish_btn.click()
    time.sleep(2)


@then(u'Thank You header is shown in Checkout Complete page')
def Verifying_ThankyouText(context):
    element=context.driver.find_element(By.XPATH,'//*[@id="checkout_complete_container"]/h2').text
    assert element=="Thank you for your order!"