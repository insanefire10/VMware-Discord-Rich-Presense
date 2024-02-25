from pypresence import Presence
import time
import psutil
import pyautogui
import random

#Enter Client ID here
client_id = ""

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
        vmstate = "Found your web server"
    elif OSlogo == "ubuntu":
        vmstate = "Deleting /etc/passwd"
    else:
        vmstate = detailJokeList[random.randint(0,len(detailJokeList)-1)]
    
    if OSlogo == "vmwarelogo":
        minilogo = " "
    else: 
        minilogo = "https://imgur.com/bXH4oFE.png"

    try:
        RPC.update(
            state=vmstate,
            large_image=OSlogo,
            details=OSString,
            small_image=minilogo,
            start=time.time()
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
    return "https://imgur.com/bXH4oFE.png"

#List Objects
OSDict = {"Windows 10":"https://imgur.com/kxO5E9i.png",
          "Windows 11":"https://imgur.com/o8kY5or.png",
          "Windows 8":"https://imgur.com/FvYjSTf.png",
          "Windows 7":"https://imgur.com/L77FPCt.png",
          "Windows Vista":"https://imgur.com/L77FPCt.png",
          "Windows XP":"https://imgur.com/L77FPCt.png",
          "Windows":"https://imgur.com/L77FPCt.png",
          "Kali":"https://imgur.com/R1WBgCS.png",
          "Ubuntu":"https://imgur.com/Woznh88.png"}

detailJokeList = ("Deleting System32",
                  "Messing with Registry Keys",
                  "Another Day another BSOD",
                  "Alt + F4", 
                  "Sending Microsoft my data",
                  "I have your SMB",
                  "Dodging OneDrive")

#main

time.sleep(25)

flagCon = False
flagIsUpdated = True
flagVMw = False
detectVMChange = " "

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
        if detectVMChange == getGuestOS():
            continue
        detectVMChange = getGuestOS()
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
