## Version 3

##Schedule A message Here
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

# df = pd.read_excel('test_data.xlsx','Sheet1')
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
counter = 0
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
def purge():
	#Empty all Lists
	pass

# global read_df #checking
read_df = pd.read_excel('test_data.xlsx','Sheet1')
def schedule(id_list,contact_list,message_list,hh_list,mm_list,dos_list,name_list):
	# dict(read_df)
	print(type(read_df))
	print(read_df)

	id_contact = search()
	id_list.append(id_contact[0])
	contact_list.append(id_contact[1])
	message = getMessage()
	message_list.append(message)
	
	send_at = list(getTime())
	hh_list.append(int(send_at[0]))
	mm_list.append(int(send_at[1]))
	dos_list.append(send_at[2])
	name_list.append('getName Function here')
	# Single variable list for rows to append directly to df
	# id_contact = search()
	id = id_contact[0]
	contact = id_contact[1]
	
	# message = getMessage()
	
	# send_at = list(getTime())
	hh = int(send_at[0])
	mm = int(send_at[1])
	dos = send_at[2]
	name = 'getName Function here'

	new_row = [read_df.shape[0],f'{name}',f'{contact}',f'{message}',hh,mm,f'{dos}',f'{id}'] 
	read_df.loc[read_df.shape[0]] = new_row #adds row to df and not to excel file
	print(read_df)
	# print(id_list)
	# print(contact_list)
	# print(message_list)
	# print(hh_list)
	# print(mm_list)
	# print(dos_list)
	# print(name_list)
	# cols = dict.fromkeys(key_list)
	# cols.update({'id' : id_list})
	# cols.update({'name' : name_list})
	# cols.update({'message' : message_list})
	# cols.update({'hh' : hh_list})
	# cols.update({'contact' : contact_list})
	# cols.update({'mm' : mm_list})
	# cols.update({'dos': dos_list})
	# print('Message scheduled successfully') #print only if TRUE!!!!!
	# print('\nDatatype of cols is \n',type(cols))
	# return cols
#end Schedule
# df1 = pd.read_excel('test_data.xlsx')
# print('df1=\n',df1)
# df1.columns = ['name','contact','message','hh','mm','dos','id']
# print('df1=\n',df1)
def get():
	counter = 0
	disp_t = 0

	while True:
		if counter == 0:
			print('1. Schedule a message\n2. Exit\n')
		else:
			print('1. Schedule another message\n2. Save and Exit\n3. Exit without Saving\n')
		choice = input()
		if choice == '1':
			# t = schedule(id_list,contact_list,message_list,hh_list,mm_list,dos_list,name_list)
			schedule(id_list,contact_list,message_list,hh_list,mm_list,dos_list,name_list)
			disp_t = pd.DataFrame(t)
			counter = counter + 1
		elif choice == '2':
			# save progress code
			# disp_t.to_excel('test_data.xlsx',sheet_name='Sheet1',index_label='Message_ID')
			read_df.to_excel('test_data.xlsx',sheet_name='Sheet1',index=False)
			if counter == 1:
				print('Message Scheduled Successfully...')
			else:
				print('Messages Scheduled Successfully...')
			break
		# Save and Exit
		elif choice == '2' and counter == 0:
			break
		# Exit Without Saving
		elif choice == '3':
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
		print('disp_t=\n',disp_t)
	counter = 0
#endGet()
#uncomment when running alone
get()