import pandas as pd
def search():
	df = pd.read_excel('contacts.xlsx')
	key = input('Type to search...\n')
	# Code to search key in excel file here
	# do a try except block with exception as contact not found
	#
	search_results = df.loc[df['names'].str.contains(key, case=False)]
	pd.set_option("display.max_rows", None)
	print(search_results)
	id = input('Enter Contact Id: ')
	contact = '91 985 00 99 477'
	contact.replace(' ','')
	if contact.find('+') == -1:
		contact = f'+91{contact}'
	# contact = #phonenumber of the searched name
	return [id,contact]
if __name__ == "__main__":
	search()