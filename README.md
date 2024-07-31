Welcome to VMware Discord Rich Presense!
This application updates your Discord profile to show that you are using VMware Workstation as well as display which VM you are using!

Setup:
-Install Python on your machine
-Install the following packages with Python Pip: 
```
pypresence, pyautogui, wmi, win32gui
```
(alternatively, run the ModulesInstaller.py file with Python for easy install)
-Execute the vmwplugin.py file!

That is all the setup! you may now execute the script and your Discord status shall show you are Playing VMware Workstation, along with an icon and name of your VM. If you would like to add more Operating System Logos, you can modify the `osaliases.py` file

If you would like this script to start with Windows and run hidden:

1. Change the file name `vmwplugin.py` to `vmwplugin.pyw`
2. Right click the file and create a shortcut. navigate to `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup` and paste the shortcut file

