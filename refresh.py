import art, time, os, platform
from colorama import init, Fore
import pandas as pd
import pandas as pd
import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import *
import pyautogui

login_status = False
st=time()
def eta(seconds):
    sec=seconds-st
    return "ETA: "+str(datetime.timedelta(seconds=sec))
def scroll():
    for i in range(8):
        pyautogui.press('down')
        sleep(0.125)

FILE_LOC = "contact.xlsx"
URL = 'https://web.whatsapp.com/'
WAITER_ELEMENT = "landing-title _3-XoE"
NEW_CHAT = '//*[@id="app"]/div/div/div[3]/header/div[2]/div/span/div[2]/div/span'
BACK_BUTTON_NEW_CHAT = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/header/div/div[1]/button/span'
PROFILE_IMAGE = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[2]/div/div/div[5]/div/div/div[1]/div/div/img'
THREE_DOTS = '//*[@id="app"]/div/div/div[3]/header/div[2]/div/span/div[3]/div/span'
LOGOUT_BUTTON = '//*[@id="app"]/div/div/div[3]/header/div[2]/div/span/div[3]/span/div/ul/li[4]/div[1]'

def login():
    global driver
    driver = webdriver.Chrome('D:\\setup\\ChromeDriver\\chromedriver_win32\\chromedriver.exe')
    driver.implicitly_wait(10)
    global waiter
    waiter = WebDriverWait(driver, 10)
    driver.get(URL)
    print("Loading site...")
    waiter.until(EC.title_is("WhatsApp"))
    print("Site loaded successfully...")
    print("Waiting for user to log in using WhatsApp Web")
    waitCounter = 0
    while 1:
        try:
            waiter.until(EC.presence_of_element_located((By.XPATH, "//canvas[@aria-label='Scan me!']")))
            waitCounter+=1
            if waitCounter%1000 == 0:
                print("Waiting for user to log in...")
        except:
            print("Logged in to WhatsApp")
            break
    global login_status
    login_status = True
    
def refresh_contact_list():
    driver.find_element_by_xpath(NEW_CHAT).click()
    sleep(0.6)
    pyautogui.press('tab')
    sleep(0.6)
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')

    mycon=set()
    while(True):
        contacts = driver.find_elements_by_class_name('_3OvU8')
        newcon=set([j.text for j in contacts])
        if len(newcon|mycon)==len(mycon):
            break
        else:
            mycon=newcon|mycon
        scroll()
    contact=sorted(list(mycon),key=str.casefold)
    rotate=dict()
    print(len(contact),"contacts has been retrieved",eta(time()))
    # print(contact)
    df = {'names':contact}
    print(df)
    df = pd.DataFrame(df)
    print(df)
    cols = ['names'] 
    df.to_excel('contacts.xlsx',sheet_name='Sheet1',index_label='id')
    # Logout Functionality
    # driver.find_element_by_xpath(BACK_BUTTON_NEW_CHAT).click()
    # sleep(0.6)
    # driver.find_element_by_xpath(THREE_DOTS).click()
    # sleep(0.5)
    # driver.find_element_by_xpath(LOGOUT_BUTTON).click()
    # sleep(3)
    # pyautogui.hotkey('alt','f4')

# if __name__ != '__main__':
#     try:
#         # pyautogui.hotkey('alt','tab')
#         refresh_contact_list()
#     except:
#         login()
#         login_status = True
#         refresh_contact_list()
if __name__ == '__main__':
    
    print(art.text2art("WhatsApp Automation"))
    print(Fore.CYAN + "\nCreated By:" + Fore.RESET + " Rajwardhan Sagare\n")
    print(Fore.YELLOW + "GitHub: " + Fore.RESET + "   https://github.com/rajsagare14")
    try:
        refresh_contact_list()
    except:
        login()
        login_status = True
        refresh_contact_list()
