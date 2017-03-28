########################
####### FunnyCat #######
########################
import win32api
import time
import os
__author__ = ('Olivier-Pascal BAKASANDA')
__version__=('python 3.5')

#os.spawnl(os.P_DETACH, 'some_long_running_command')

#Select 
button = win32api.GetKeyState(0x04) #Capture the click of the middle mouse button 

#Listening for the mouse actions
while True:
    a = win32api.GetKeyState(0x04)  
    if a != button:
        button = a   
        if a < 0:
			#Relocate mouse position at the top left corner of the screen
            win32api.SetCursorPos((14,14))
			#Simulate CTRL four times on the keyboard 
            for i in range(4):
                win32api.keybd_event(0x11, 0, 0, 0) #ctrl button down
                win32api.keybd_event(0x11, 0, 2, 0) #ctrl button up
				#sleep 1 seconde between keyboard event
                time.sleep(1)
			
    time.sleep(0.002)