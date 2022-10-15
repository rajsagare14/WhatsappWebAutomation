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
URL = 'https://web.whatsapp.com/'
WAITER_ELEMENT = "landing-title _3-XoE"
def logout():
	pass
def login():
	global driver
	global waiter
	driver = webdriver.Chrome('D:\\setup\\ChromeDriver\\chromedriver_win32\\chromedriver.exe')
	driver.implicitly_wait(10)
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
if __name__ == '__main__':
	login()
	print(art.text2art("WhatsApp Automation"))
	print(Fore.CYAN + "\nCreated By:" + Fore.RESET + " Rajwardhan Sagare\n")
	print(Fore.YELLOW + "GitHub: " + Fore.RESET + "   https://github.com/rajsagare14")
