## Version 4
##Schedule A message Here
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import time

from pip import main
import search
import getMessage
import getTime

# Variables
counter = 0
read_df = pd.read_excel('test_data.xlsx','Sheet1') #Reading ExcelFile
new_df_row = 0
def addRow(): #Adds New Row to the DataFrame
	#Get Contact
	id_contact = search.search()
	id = int(id_contact[0])
	contact = id_contact[1]
	#Get Message
	message = getMessage.getMessage()
	send_at = list(getTime.getTime())
	hh = int(send_at[0])
	mm = int(send_at[1])
	dos = send_at[2]
	name = 'getName Function here'
	# Adding all row data into a list
	new_row = [read_df.shape[0],f'{name}',f'{contact}',f'{message}',hh,mm,f'{dos}',f'{id}'] 

	read_df.loc[read_df.shape[0]] = new_row #adds row to df and not to excel file
	new_df_row = pd.DataFrame(new_row)
	# print(read_df)
	print(new_df_row)

def schedule():
	counter = 0
	while True:
		if counter == 0:#Display inner Menu
			print('1. Schedule a message\n2. Exit\n')
		else: #Display alternate inner Menu
			print('1. Schedule another message\n2. Save and Exit\n3. Exit without Saving\n4. Display Scheduled Messages\n')
		choice = input() #Selects a menu item
		if choice == '1': #Schedule a Message
			# schedule()
			addRow()
			counter = counter + 1
		elif choice == '2': # Save and Exit
			read_df.to_excel('test_data.xlsx',sheet_name='Sheet1',index=False) #Saving to excelfile
			if counter == 1:
				print('Message Scheduled Successfully...')
			else:
				print('Messages Scheduled Successfully...')
			break
		
		elif (choice == '2' and counter == 0) or choice == '3':# Exit Without Saving
			break
		elif (choice == '3' and counter == 0) or (choice == '4' and counter != '0'):# Display Scheduled messages
			print(new_df_row)
		else:
			print('invalid choice')
# Uncomment line below For testing this code alone
if __name__ == "__main__":
	schedule()