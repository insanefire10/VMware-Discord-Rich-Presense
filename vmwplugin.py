from pypresence import Presence
import time
import psutil
import pyautogui
import random

#detect if VMware/Discord is active
def vmdetect():
    return "vmware.exe" in (i.name() for i in psutil.process_iter()) 

def discorddetect():
    return "Discord.exe" in (i.name() for i in psutil.process_iter())

#Update Discord Status
def update():
    OSString = getGuestOS()
    OSlogo = OSimage(OSString)

    if OSlogo == "kali":
        vmstate = "Hacking🤓"
    elif OSlogo == "ubuntu":
        vmstate = "Deleting /etc/passwd"
    else:
        vmstate = detailJokeList[random.randint(0,len(detailJokeList)-1)]
    
    if OSlogo == "vmwarelogo":
        minilogo = " "
    else: 
        minilogo = "vmwarelogo"

    try:
        RPC.update(
            state=vmstate,
            large_image=OSlogo,
            details=OSString,
            small_image=minilogo
        )
    except:
        print("Connection Error: Cannot Update, API error")
        return
        

#Get VMware Data
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
          "Windows 8":"win8",
          "Windows 7":"win7",
          "Windows Vista":"winvista",
          "Windows XP":"winxp",
          "Windows":"win7",
          "Kali":"kali",
          "Ubuntu":"ubuntu"}

detailJokeList = ("Deleting System32",
                  "Messing with Registry Keys",
                  "Another Day another BSOD",
                  "Alt + F4", "Sending Microsoft my data",
                  "I have your SMB",
                  "Dodging OneDrive")

#main

#Enter Client ID here
client_id = ""
time.sleep(25)

flagCon = False
flagIsUpdated = True
flagVMw = False

print("Running")
while True:
    time.sleep(5)
    if not discorddetect():
        print("Discord Not Detected")
        if flagCon == True:
            RPC.close()
        flagCon = False
        continue
    
    if vmdetect():
        if flagVMw == False:
            RPC = Presence(client_id)
            try:
                RPC.connect()
            except:
                print("Connection Error")
                continue
            flagVMw = True
            flagCon = True
        update()
        print("Detected")

    else:
        print("VMW not detect")
        if flagVMw == True:
            flagVMw = False
            flagCon = False 
            RPC.clear()
            RPC.close()
        flagVMw = False
        flagCon = False

print("Exited")
