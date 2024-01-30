from pypresence import Presence
import time
import psutil
import pyautogui
import random


def update():
    OSString = getGuestOS()
    OSlogo = OSimage(OSString)
    if OSlogo == "kali":
        vmstate = "Hacking🤓" 
    else:
        vmstate = detailJokeList[random.randint(0,len(detailJokeList)-1)]
    RPC.update(
        state=vmstate,
        large_image=OSlogo,
        details=OSString
    )

def vmdetect():
    return "vmware.exe" in (i.name() for i in psutil.process_iter()) 

def getGuestOS():
    windows = pyautogui.getAllWindows()
    for window in windows:
        if "VMware Workstation" in window.title:
            return window.title.split('-')[0]

def OSimage(osname):
    for key, value in OSDict.items():
        if key in osname:
            return value
    return "vmwarelogo"

#List Objects
OSDict = {"Windows 10":"win10",
          "Windows 11":"win11",
          "Kali":"kali",
          "Ubuntu":"ubuntu",
          "Windows 7":"win7",
          "Windows Vista":"winvista",
          "Windows XP":"winxp"}

detailJokeList = ("Deleting System32", "Messing with Registry Keys", "Another Day another BSOD", "Alt + F4", "Sending Microsoft my data", "I have your SMB")

#main

#Checking if Discord is running
if not "Discord.exe" in (i.name() for i in psutil.process_iter()):
    print("Discord is not connected")
    exit()

#Creating connection
client_id = "1201392534656647238"
RPC = Presence(client_id)
RPC.connect()

flagOff = True
print("Running")
while True:
    if not "Discord.exe" in (i.name() for i in psutil.process_iter()):
        print("Discord Not Detected")
        exit()
    time.sleep(4)
    if vmdetect():
        update()
        print("Detected")
        flagOff = False
    else:
        print("VMW not detect")
        if flagOff:
            continue
        else:
            RPC.clear()
            flagOff = True
    
print("Exited")