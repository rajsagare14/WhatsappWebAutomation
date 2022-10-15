import art,time,os,platform
import pandas as pd
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver

DRIVER_PATH = 'D:\\setup\\ChromeDriver\\chromedriver_win32\\chromedriver.exe'
BRAVE_PATH = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
WHATSAPP_WEB = 'https://web.whatsapp.com/'
NEW_CHAT = '//*[@id="side"]/header/div[2]/div/span/div[2]/div/span' #whatsapp web new chat option
# Xpaths
span_contact_name_class = 'ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr'

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
option = webdriver.ChromeOptions()
option.binary_location = BRAVE_PATH
# browser = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=option)
# browser.get(WHATSAPP_WEB)
driver.get(WHATSAPP_WEB)
def login():
	# If logged out login
	pass
def close():
	# Close the Driver when Everything is done
	pass
