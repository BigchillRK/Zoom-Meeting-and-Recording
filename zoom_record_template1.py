## Code to Automatically open Zoom program to join a meeting and record meeting is required

#####################################

## Please read through the read me to understand how this works to implement it for your set up

#####################################

## You need the pyautogui library, best way to install is using 'pip install pyautogui'
## in essence this script uses your keyboard and mouse to automatically open zoom from start menu and click and enter meeting id
## some settings of zoom itself needs to be changed for this script to work correctly

## documentation for pyautogui

########################################################

## https://pyautogui.readthedocs.io/en/latest/index.html

########################################################

## Created by Rohit Kannachel
## Not liable if this causes any issues.
## thank you to Tanushi De Silva for giving me the inspiration to make this

# importing libraries
import pyautogui 
import time


#####   Joining Zoom Meeting   ###################

#######################################################################################
#Enter the meeting id as a string here *important that it is in string format
meet_id = '123456789'
#esc clicked to ensure that the win key will open up correctly in the next step
pyautogui.press('esc',interval=0.1)

time.sleep(0.2)

#these lines are simulating starting up zoom by pressing windows key and typing zoom to open program
pyautogui.press('win',interval=0.1)
pyautogui.write('zoom')
pyautogui.press('enter',interval=0.5)


#time delay to factor for zoom app to load up, good buffer is like 10 sec but its case specific
time.sleep(10)

#this part is important and may need to be altered to your needs according
#this part simulates clicking join meeting, entering meeting id and pressing enter to join
##Make sure the joinButton.png file is located in the same folder as the python file or else it will not work
##this tells the script where to click to join the meeting

x,y = pyautogui.locateCenterOnScreen('joinButton.png')
pyautogui.click(x,y)


pyautogui.press('enter',interval=1)
## the interval of 1 second is important, if not there, then the meeting id will not be inputted
pyautogui.write(meet_id)
pyautogui.press('enter',interval=1)


###### password OPTIONAL!!! #####
# if your meeting has a password then uncomment the code below and enter it here


# change the value of the variable to your password
password = 'password'

#pyautogui.write(password)
#pyautogui.press('enter',interval = 10)
##### IF YOUR MEETING HAS NO PASSWORD PLEASE LEAVE THIS SECTION AS IS AND DONT UNCOMMENT



##################################################################################


###### Recording meeting using Windows Game Bar  #############################


#######################################################################################


## this time buffer is added so that it accounts for the time taken to load into the meeting 
## a good buffer time is around 10-20 seconds before recording starts to ensure you're in the meeting


time.sleep(5)


## opening up windows game bar overlay
pyautogui.hotkey('win','g')
time.sleep(1)
## commencing screen recording
pyautogui.hotkey('win','alt','r')
time.sleep(1)
## closing windows game bar overlay
pyautogui.hotkey('win','g')


#### recording time amount
## however long you want, enter the time here in seconds, e.g. 30 minutes is 60*30 = 1800 seconds
## in windows game bar the default setting for time limit for recording is 2 hours,
## make sure to change this as you need
time.sleep(25)


## ending screen recording
pyautogui.hotkey('win','alt','r')
time.sleep(2)
## By default, screen captures are sent to a folder called captures in "videos" in "this PC"

## closing Zoom
pyautogui.hotkey('alt','f4')
time.sleep(0.5)
pyautogui.hotkey('alt','f4')

############################################################################################