import random, string
from time import sleep
import requests
import json
from colorama import init,Style,Fore
import sys
import sys as n
import time as un

let = 0

Bule="\033[1;36;40m"
Dark="\033[0;37;40m"


def slow(M):
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        un.sleep(1. / 200)



 
print("""

  ▄▄▌  ▪  .▄▄ · ▄▄▄▄▄    • ▌ ▄ ·.  ▄▄▄· ▄ •▄ ▄▄▄ .▄▄▄  
  ██•  ██ ▐█ ▀. •██      ·██ ▐███▪▐█ ▀█ █▌▄▌▪▀▄.▀·▀▄ █·
  ██▪  ▐█·▄▀▀▀█▄ ▐█.▪    ▐█ ▌▐▌▐█·▄█▀▀█ ▐▀▀▄·▐▀▀▪▄▐▀▀▄ 
  ▐█▌▐▌▐█▌▐█▄▪▐█ ▐█▌·    ██ ██▌▐█▌▐█ ▪▐▌▐█.█▌▐█▄▄▌▐█•█▌
  . ▀▀▀ ▀▀▀ ▀▀▀▀  ▀▀▀     ▀▀  █▪▀▀▀ ▀  ▀ ·▀  ▀ ▀▀▀ .▀  ▀
 ═════════════════════════════════════════════════════

  The programmer is not responsible for any wrong event
  TikTok: @l.7a'

""")

text = string.ascii_lowercase + string.digits
additions = input('additions: ')
lengit = int(input('length: '))
count = int(input('count: '))
for x in range(count):
    pasb = ''.join(random.choice(text) for x in range(lengit))
    with open('list.txt', 'a') as file:
        file.write(additions + pasb + '\n')

        
        



        
        

        
        
