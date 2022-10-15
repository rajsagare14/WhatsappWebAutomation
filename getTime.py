def getTime():
	hh = input('At what hour(enter value between 0-23): ')
	mm = input('At what hour(enter value between 0-59): ')
	dos = input('Date of sending(DD:MM:YYYY): ')  #Or or or or see if there is a get date function
	return hh,mm,dos
if __name__ == "__main__":
	getTime()