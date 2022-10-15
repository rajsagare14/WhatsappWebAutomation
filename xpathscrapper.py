import pandas as pd
from selenium import webdriver

DRIVER_PATH = 'D:\\setup\\ChromeDriver\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
book_name = ''
book_name = input()
url = f'https://www.google.com/search?q=author+of+{book_name}'
AUTHOR = '//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[1]/div/div[1]/div[2]/div/div[1]/a'
driver.get(url)
auths = []
try:
	auth = driver.find_element_by_xpath(AUTHOR)
	print(auth.text)
except:
	auths = driver.find_elements_by_class_name('bVj5Zb.FozYP')
	auths = driver.find_elements_by_class_name('uoFCfc')
	for i in auths:
		print(i.text)