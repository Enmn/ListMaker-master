import os
import urllib.request
import urllib.parse
import time
import sys



def update():
  stuff_to_update = ['test.py', '.version', 'start.bat' 'update.py']
  for fl in stuff_to_update:
    dat = urllib.request.urlopen("https://raw.githubusercontent.com/WHITE71wolf/ListMaker-master/master/" + fl).read()
    file = open(fl, 'wb')
    file.write(dat)
    file.close()
    print('\n\t\tUpdated Successfull !!!!')
    print('\tRun The Script Again...')
    exit()

try:
    urllib.request.urlopen('https://www.google.com')
except Exception:
    print("Error While Connecting To Internet!!!")
    print("\tPlease Connect To Internet To Continue...\n")
    input('Exiting....\n Press Enter To Exit....')
    exit()
print('\tChecking For Updates...')
ver = urllib.request.urlopen("https://raw.githubusercontent.com/WHITE71wolf/ListMaker-master/master/.version").read().decode('utf-8')
verl = ''
try:
    verl = open(".version", 'r').read()
except Exception:
    pass
if ver != verl:
    print('\n\t\tAn Update is Available....')
    print('\tUpdating Anon-SMS...')
    update()
