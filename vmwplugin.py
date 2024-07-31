#Created by InsaneFire. This program is free to use and improve on if you wish. Please leave this line as a way to give credit to me, the original author :)

from pypresence import Presence
from osaliases import OSDict
import time
import pyautogui
import wmi
import win32gui

global timeVar
c = wmi.WMI()

#Enter Client ID here
client_id = "1201392534656647238"

#detect if VMware/Discord is active
def vmdetect():
    for process in c.Win32_Process(name="vmware.exe"):
        return True
    return False

def discorddetect():
    for process in c.Win32_Process(name="Discord.exe"):
        return True
    return False

#Update Discord Status
def update(newVM, newState):
    OSString = newVM
    OSlogo = OSimage(OSString)
    if(newState):
        vmstate = "Currently Working"
    else:
        vmstate = "Running in background"
    
    if OSlogo == "https://imgur.com/bXH4oFE.png":
        minilogo = " "
    else: 
        minilogo = "https://imgur.com/bXH4oFE.png"

    try:
        RPC.update(
            state=vmstate,
            large_image=OSlogo,
            details=OSString,
            small_image=minilogo,
            start=timeVar,
            buttons=[{"label":"Get Rich Presence for VMware","url":"https://github.com/insanefire10/VMware-Discord-Rich-Presense"}]
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
    osname = osname.lower()
    for key, value in OSDict.items():
        if key in osname:
            return value
    return "https://imgur.com/bXH4oFE.png"

def isForeground():
    w=win32gui
    if "VMware Workstation" in w.GetWindowText(w.GetForegroundWindow()):
        return True
    return False



#main

#Waits 15 seconds upon system startup to start the process to ensure Discord starts up
time.sleep(15)

#flags:
flagCon = False #Global flag to determine if RPC session is connected
flagVMw = False #Global flag to determine if VMware is running, and if so, turns true and starts RPC session
currentVM = " " #Holds name of current working VM. Runs the Update function if user switches to another VM
currentStatus = False #Holds if VMware is in the foreground
pollTime = 5

print("Running")
while True:
    time.sleep(pollTime) #Script will check if Discord and VMware are running every 2/5 seconds

    
    if vmdetect():
        if not discorddetect():
            print("Discord Not Detected")
            pollTime = 5
            if flagCon == True:
                RPC.close()
            flagCon = False
            continue

        pollVM = getGuestOS()
        pollStatus = isForeground()

        if (currentVM == pollVM) and (currentStatus == pollStatus):
            continue
        currentVM = pollVM
        currentStatus = pollStatus


        if flagVMw == False:
            RPC = Presence(client_id)
            try:
                RPC.connect()
            except:
                print("Connection Error")
                continue
            flagVMw = True
            flagCon = True
            pollTime = 2
            timeVar = time.time()
        update(pollVM, pollStatus)
        print("Detected")

    else:
        if flagVMw == True:
            currentVM = " "
            flagVMw = False
            flagCon = False
            pollTime = 5
            RPC.clear()
            RPC.close()
        flagVMw = False
        flagCon = False

print("Exited")
