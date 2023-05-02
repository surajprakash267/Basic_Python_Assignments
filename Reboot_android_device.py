# Q11. Write a program to reboot the device once every two minutes.
# Ans.

import os,time  # importing OS module and time module

while True: # The code will run Infinitely
    adb_reboot = os.system("adb reboot")
    print(adb_reboot)
    print('Device Rebooted')
    time.sleep(120)  # The code will run after 120 sec.