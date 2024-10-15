#Created by InsaneFire. This program is free to use and improve on if you wish. Please leave this line as a way to give credit to me, the original author :)

from pypresence import Presence
from osaliases import OSDict
import time
import pyautogui
import wmi
import win32gui
import psutil

#Enter Client ID here
client_id = "1201392534656647238"

#Enter current Github
githuburl = 'https://github.com/insanefire10/VMware-Discord-Rich-Presense'

#detect if VMware/Discord is active
def vmdetect():
    global flagVMw
    global vmwarePID
    if(flagVMw):
        if psutil.pid_exists(vmwarePID):
            return True
        vmwarePID = 0
        return False
    for process in c.Win32_Process(name="vmware.exe"):
        vmwarePID = process.processId
        return True
    return False

def discorddetect():
    global flagCon
    global discordPID
    if(flagCon):
        if psutil.pid_exists(discordPID):
            return True
        discordPID = 0
        return False
    for process in c.Win32_Process(name="Discord.exe"):
        discordPID = process.processId
        return True
    return False

#Update Discord Status
def update(newVM):
    OSString = newVM
    OSlogo = OSimage(OSString)
    
    if OSlogo == "https://imgur.com/bXH4oFE.png":
        minilogo = " "
    else: 
        minilogo = "https://imgur.com/bXH4oFE.png"

    try:
        RPC.update(
            state=OSString,
            large_image=OSlogo,
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
#main

#Waits 15 seconds upon system startup to start the process to ensure Discord starts up
time.sleep(15)

#flags/vars:
flagCon = False #Global flag to determine if RPC session is connected
flagVMw = False #Global flag to determine if VMware is running, and if so, turns true and starts RPC session
currentVM = " " #Holds name of current working VM. Runs the Update function if user switches to another VM
currentStatus = False #Holds if VMware is in the foreground
pollTime = 10
vmwarePID = 0
discordPID = 0
global timeVar
c = wmi.WMI()

print("Running")
while True:
    time.sleep(pollTime) #Script will check if Discord and VMware are running every 2 seconds (Vmware is running) or 5 seconds (VMware is not running)

    
    if vmdetect():
        if not discorddetect():
            print("Discord Not Detected")
            pollTime = 5
            if flagCon == True:
                RPC.close()
            flagCon = False
            continue

        pollVM = getGuestOS()

        if (currentVM == pollVM):
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
            pollTime = 2
            timeVar = time.time()
        update(pollVM)
        print("Detected")

    else:
        if flagVMw == True:
            currentVM = " "
            flagVMw = False
            flagCon = False
            pollTime = 10
            RPC.clear()
            RPC.close()
        flagVMw = False
        flagCon = False

print("Exited")
