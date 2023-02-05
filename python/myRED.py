from time import sleep
import os
import my_utils

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

(myUsername, myPassword) = my_utils.credentials()
headless_option = Options()
#headless_option.add_argument("--headless")
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=headless_option)

#Nagivate to myRED:
webPath = "https://myred.nebraska.edu"
browser.get(webPath)
while(browser.title != "MyRED | University of Nebraska-Lincoln"):
    if browser.title == "MyRED":
        try:
            browser.switch_to.frame('content')
            browser.find_element(by=By.XPATH, value='//*[@id="login-nuid"]').click()
        except:
            print("MyRED Login Button not found")
    if browser.title == "University of Nebraska & State College Single Sign On":
        username = browser.find_element(by=By.XPATH, value='//*[@id="username"]')
        username.send_keys(myUsername)
        password = browser.find_element(by=By.XPATH, value='//*[@id="password"]')
        password.send_keys(myPassword)
        login_button = browser.find_element(by=By.XPATH, value='//*[@id="content-wrap"]/div/section[4]/div/div/form/div/button')
        login_button.click()
    if browser.title == "Universal Prompt":
        os.system('clear')
        try:
            browser.find_element(by=By.XPATH, value='//*[@id="trust-browser-button"]').click()
        except:
            print("Waiting for authenicator...")
            sleep(.5)

account_balance = None
due_date = None
due_now = None
while(account_balance == None or due_date == None or due_now == None):
    try:
        account_balance_strings = browser.find_element(by=By.XPATH, value = '//*[@id="student.hiobx.haccbal"]/div/strong').text.split(' ')
        account_balance = float(account_balance_strings[1])
    except:
        account_balance = None
    try:
        due_date = browser.find_element(by=By.XPATH, value = '//*[@id="student.hiobx.hiobxpc"]/div[1]/table/tbody/tr[2]/td').text
    except:
        due_date = None
    try:
        due_now_strings = browser.find_element(by=By.XPATH, value = '//*[@id="student.hiobx.hiobxpc"]/div[2]/strong').text.split(' ')
        due_now = float(due_now_strings[1])
    except:
        due_now = None

while(browser.title != 'Home | University Housing Portal'):
    try:
        browser.get('https://myred.nebraska.edu/psc/myred/NBL/HRMS/s/WEBLIB_NBA_SSO.ISCRIPT1.FieldFormula.IScript_Login?institution=NEUNL&setupid=STARREZUNL')
    except:
        print("Accessing UNL housing...")
        sleep(.1)
while(browser.title == 'Home | University Housing Portal'):
    try:
        href = browser.find_element(by=By.XPATH, value = '/html/body/div[1]/section[1]/div/article/div/div/div/section/div[1]/div[8]/div[2]/div/div/a')
        link = href.get_attribute('href')
        browser.get(link)
    except:
        sleep(.5)
        print("Accecssing meal plan information...")


meal_swipes_period = None
dining_dollars = None
herbies_gc_balance = None
meal_plan = None
while(meal_swipes_period == None or dining_dollars == None or herbies_gc_balance == None or meal_plan == None):
    try:
        meal_swipes_period = int(browser.find_element(by=By.XPATH, value = '/html/body/main/div[2]/form/strong[2]').text)
    except:
        meal_swipes_period = None
    try:
        dining_dollars = float(browser.find_element(by=By.XPATH, value = '/html/body/main/div[2]/form/strong[5]').text)
    except:
        dining_dollars = None
    try:
        herbies_gc_balance = float(browser.find_element(by=By.XPATH, value = '/html/body/main/div[2]/form/strong[6]').text)
    except:
        herbies_gc_balance = None
    try:
        meal_plan = browser.find_element(by=By.XPATH, value = '/html/body/main/div[2]/form/strong[7]').text
    except:
        meal_plan = None



print("Account balance: " + str(account_balance))
print("Due on " + due_date + ": " + str(due_now))
print("Meal swipes left this period: " + str(meal_swipes_period))
print("Dining dollars remaining: " + str(dining_dollars))
print("Herbie's Gift Card Balance: " + str(herbies_gc_balance))
print("Meal Plan: " + meal_plan)

sleep(100)