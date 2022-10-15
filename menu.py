from typing import final
import edit, delete,excel3,refresh,pyautogui
from time import sleep
def menu():# Displays Main Menu
	while True:# Keep Displaying Main Menu
		print("\n1. Schedule Message\n2. Edit Scheduled Message\n3. Delete Scheduled Message\n4. Login to WhatsApp\n5. Refresh Contact List\n6. Exit\n")
		choice = input('Enter Your Choice: ')
		if choice == '1':#Schedule a Message
			excel3.schedule()
		elif choice == '2':# Edit Scheduled Message
			edit.edit()
		elif choice == '3':# Delete Scheduled Message
			delete.delete()
		elif choice == '4':# Login to Whatsapp
			if refresh.login_status == True:
				print('You are Already logged in')
			else:
				refresh.login()
				pyautogui.hotkey('alt','tab')
		elif choice == '5':# Refreshes the contact list
			if refresh.login_status == True:
				sleep(1)
				pyautogui.hotkey('alt','tab')
				refresh.refresh_contact_list()
				pyautogui.hotkey('esc')
				pyautogui.hotkey('esc')
				pyautogui.hotkey('alt','tab')
			else:
				try:
					refresh.refresh_contact_list()
				except:
					refresh.login()
					refresh.login_status = True
					refresh.refresh_contact_list()
				finally:
					pyautogui.hotkey('esc')
					pyautogui.hotkey('esc')
					pyautogui.hotkey('alt','tab')
		elif choice == '6':# Exit Program
			print('logging out')
			# try:
			# 	login.logout()
			# except Exception as e:
			# 	print(f'error logging out\n{e}')
			# 	print('Exiting...\nThank You for using our Services')
			# 	exit()
			break
		else:
			print('Enter a Valid Choice Please')
if __name__ == "__main__":
	menu()