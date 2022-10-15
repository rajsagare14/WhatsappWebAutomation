## Edit searchd Message here 
import search,getMessage,getTime
def getID():
	print('---Edit Records---')
	key = input('Type to search...\n')
	# Code to search key in excel file here
	# do a try except block with exception as contact not found
	#
	id = '1'
	return id
def edit():
	id = getID()
	# code to display record here
	# 
	# 
	# 
	print('Do you want to edit this record?\n1. Yes\n2. No')
	flag = input()
	if flag == '1':
		while True:
			choice = input("What do you want to Edit?\n1. Name\n2. Message\n3. Time\n4. Update Record\n5. Exit\nEnter your choice: ")
			if choice == '1':
				contact = search.search()
			elif choice == '2':
				message = getMessage.getMessage()
			elif choice == '3':
				send_at = getTime.getTime()
			elif choice == '4':
				#code to update/save changes made to a record in excel
				#
				#
				#
				break
			elif choice == '5':
				break
			else:
				print('Enter a Valid Choice Please')
			print('record edited sucessfully') #print this only if it is TRUE!!!!
if __name__ == "__main__":
	edit()