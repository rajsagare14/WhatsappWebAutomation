## Version 1

##Schedule A message Here
'''
import time
def search():
	key = input('Type to search...\n')
	# Code to search key in excel file here
	# do a try except block with exception as contact not found
	#
	id = input('Enter Contact Id: ')
	contact = '+919850099477'
	contact.replace(' ','')
	if contact.find('+') == -1:
		contact = f'+91{contact}'
	# contact = #phonenumber of the searched name
	return contact

def getMessage():
	message = input('Enter message: ')
	# message.replace() #replace all whitespaces and punctuations and return carriages here
	return message

def getTime():
	hh = input('At what hour(enter value between 0-23): ')
	mm = input('At what hour(enter value between 0-59): ')
	return hh,mm

def schedule():
	contact = search()
	message = getMessage()
	send_at = getTime()
	# get time here
	print('Message scheduled successfully') #print only if TRUE!!!!!
'''
##Schedule A message Here
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

# df = pd.read_excel('test_data.xlsx',['Sheet1'])
# '''
# Scheduled
# '''
# print('df=\n',df)
# print(type(df))

import time
##Initialising Lists
key_list = ['name','contact','message','hh','mm','dos','id']
id_list = [] 
contact_list = []
message_list = []
hh_list = []
mm_list = []
dos_list = []
name_list = []
t = []
def search():
	key = input('Type to search...\n')
	# Code to search key in excel file here
	# do a try except block with exception as contact not found
	#
	id = input('Enter Contact Id: ')
	contact = '9850099477'
	contact.replace(' ','')
	if contact.find('+') == -1:
		contact = f'+91{contact}'
	# contact = #phonenumber of the searched name
	return [id,contact]

def getMessage():
	message = input('Enter message: ')
	# message.replace() #replace all whitespaces and punctuations and return carriages here
	return message

def getTime():
	hh = input('At what hour(enter value between 0-23): ')
	mm = input('At what hour(enter value between 0-59): ')
	dos = input('Date of sending(DD:MM:YYYY): ')  #Or or or or see if there is a get date function
	return hh,mm,dos


def schedule(id_list,contact_list,message_list,hh_list,mm_list,dos_list,name_list):
	
	id_contact = search()
	id_list.append(id_contact[0])
	contact_list.append(id_contact[1])
	
	message_list.append(getMessage())
	
	send_at = list(getTime())
	hh_list.append(int(send_at[0]))
	mm_list.append(int(send_at[1]))
	dos_list.append(send_at[2])
	name_list.append('getName Function here')

	# print(id_list)
	# print(contact_list)
	# print(message_list)
	# print(hh_list)
	# print(mm_list)
	# print(dos_list)
	# print(name_list)
	cols = dict.fromkeys(key_list)
	cols.update({'id' : id_list})
	cols.update({'name' : name_list})
	cols.update({'message' : message_list})
	cols.update({'hh' : hh_list})
	cols.update({'contact' : contact_list})
	cols.update({'mm' : mm_list})
	cols.update({'dos': dos_list})
	print('Message scheduled successfully') #print only if TRUE!!!!!
	return cols
#end Schedule
# df1 = pd.read_excel('test_data.xlsx')
# print('df1=\n',df1)
# df1.columns = ['name','contact','message','hh','mm','dos','id']
# print('df1=\n',df1)
def get():
	counter = 0
	while True:
		if counter == 0:
			print('1. Schedule a message\n2. Exit\n')
		else:
			print('1. Schedule another message\n2. Save and Exit\n3. Exit without Saving\n')
		loop = input()
		if loop == '1':
			t = schedule(id_list,contact_list,message_list,hh_list,mm_list,dos_list,name_list)
			counter = counter + 1
		elif loop == '2':
			# save progress code
			break
		elif loop == '2' and counter == 0:
			break
		elif loop == '3':
			break
		else:
			print('invalid choice')
	#endWhile
	if counter != 0:
		print('t=\n',t)
		print(type(t))
		# converting Dict to A Data Frame
		df1 = pd.DataFrame(t)
		print('df1=\n',df1)
		print(type(df1))
	counter = 0
#endGet()
#uncomment when running alone
# get()