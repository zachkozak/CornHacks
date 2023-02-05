from time import sleep
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

login = open("login.txt","r")
myUsername = login.readline().strip()
myPassword = login.readline().strip()


headless_option = Options()
#headless_option.add_argument("--headless")
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=headless_option)

#Canvas:
webPath = "https://canvas.unl.edu/"
browser.get(webPath)
sleep(1)
username = browser.find_element(by=By.XPATH, value='//*[@id="username"]')
username.send_keys(myUsername)
password = browser.find_element(by=By.XPATH, value='//*[@id="password"]')
password.send_keys(myPassword)
login_button = browser.find_element(by=By.XPATH, value='//*[@id="login-main"]/form/div/button')
login_button.click()
while(browser.title != "Dashboard"):
    try:
        browser.find_element(by=By.XPATH, value='//*[@id="trust-browser-button"]').click()
    except:
        sleep(.1)
        if browser.title == "Universal Prompt":
            os.system('clear')
            print("Waiting for authenicator...")

#MYRED:
webPath = "https://myred.nebraska.edu"
browser.get(webPath)
while(browser.title != "MyRED"):
    try:
        browser.find_element(by=By.XPATH, value='//*[@id="trust-browser-button"]').click()
    except:
        sleep(.1)
        if browser.title == "Universal Prompt":
            os.system('clear')
            print("Waiting for authenicator...")
            
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


browser.close()