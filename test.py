import random
import string
import os
import urllib.request
import urllib.parse
import time
import sys

def maker_close():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
		rr

let = 0

Bule="\033[1;36;40m"
Dark="\033[0;37;40m"


text = string.ascii_lowercase + string.digits
number = string.digits
email2 = string.ascii_lowercase


maker_close()
print("""
 ██╗     ██╗███████╗████████╗              ███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗ 
 ██║     ██║██╔════╝╚══██╔══╝              ████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
 ██║     ██║███████╗   ██║       █████╗    ██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝
 ██║     ██║╚════██║   ██║       ╚════╝    ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
 ███████╗██║███████║   ██║                 ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║
 ╚══════╝╚═╝╚══════╝   ╚═╝                 ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
 ════════════════════════════════════════════════════════════════════════════════════
  The programmer is not responsible for any wrong event
  TikTok: @l.7a
  GitHub: WHITE71wolf
""")

o = input('''
 (1) - List Text or username
 (2) - List Number
 (3) - List email
 (4) - Exit tool
-> ''')


if o =="1":
  beginning = input('[-] Beginning: ')
  ending = input('[-] Ending: ')
  lengit = int(input('[+] Length: '))
  count = int(input('[+] Count: '))
  for x in range(count):
    pasb = ''.join(random.choice(text) for x in range(lengit))
    with open('user.txt', 'a') as file:
      file.write(beginning + pasb + ending + '\n')
      let += 1
      print(f'Done {let}\{count}')   


if o =="2":
  lengit1 = int(input('[+] Length Number: '))
  count1 = int(input("[+] Count Number: "))
  for i in range(count1):
    resesor = ''.join(random.choice(number) for i in range(lengit1))
    with open('user.txt', 'a') as file:
      file.write(resesor + '\n')


if o =="3":
  maker_close()
  email = input("[+] Enter Domain (@) : ")
  length2 = int(input("[+] Length Email: "))
  count2 = int(input("[+] Count Email: "))
  for r in range(count2):
    sourss = ''.join(random.choice(email2) for r in range(length2))
    with open('user.txt', 'a') as file:
      file.write(sourss + f'@{email}' + '\n')


if o =="4":
  os.system('exit')




def update():
  data = urllib.request.urlopen("https://raw.githubusercontent.com/WHITE71wolf/ListMaker-master/master/.update").read().decode('utf-8')
  stuff_to_update = data
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

  



        
