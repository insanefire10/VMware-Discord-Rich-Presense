#Created by InsaneFire. This program is free to use and improve on if you wish. Please leave this line as a way to give credit to me, the original author :)

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
def update(newVM):
    OSString = newVM
    OSlogo = OSimage(OSString)

    if OSlogo == "kali":
        vmstate = "Found your web server"
    elif OSlogo == "ubuntu":
        vmstate = "Deleting /etc/passwd"
    else:
        vmstate = detailJokeList[random.randint(0,len(detailJokeList)-1)]
    
    if OSlogo == "vmwarelogo":
        minilogo = None
    else: 
        minilogo = "https://imgur.com/bXH4oFE.png"

    try:
        RPC.update(
            state=vmstate,
            large_image=OSlogo,
            details=OSString,
            small_image=minilogo,
            start=time.time(),
            buttons=[{"label":"Get VMware RPC for Discord","url":"https://github.com/insanefire10/VMware-Discord-Rich-Presense"}]
        )
    except:
        print("Connection Error: Cannot Update, API error")
        return
        

#Get VMware Data
def getGuestOS():
    windows = pyautogui.getAllWindows()
    for window in windows:
        if "VMware Workstation" in window.title:
            return window.title.split('- VMware Workstation')[0]
    return "VMware Workstation"

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
          "Windows Server":"https://i.imgur.com/nVHdZcn.png",
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

#Waits 25 seconds upon system startup to start the process to ensure Discord starts up
time.sleep(2)

#flags:
flagCon = False #Global flag to determine if RPC session is connected
flagVMw = False #Global flag to determine if VMware is running, and if so, turns true and starts RPC session
currentVM = " " #Holds name of current working VM. Runs the Update function if user switches to another VM

print("Running")
while True:
    time.sleep(5) #Script will check if Discord and VMware are running every 5 seconds
    if not discorddetect():
        print("Discord Not Detected")
        if flagCon == True:
            RPC.close()
        flagCon = False
        continue
    
    if vmdetect():
        pollVM = getGuestOS()
        if currentVM == pollVM:
            continue
        currentVM = pollVM
        if flagVMw == False:
            RPC = Presence(client_id)
            try:
                RPC.connect()
            except:
                print("Connection Error")
                continue
            flagVMw = True
            flagCon = True
        update(pollVM)
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
