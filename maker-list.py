import random
import string
import os


def maker_close():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

let = 0

Bule="\033[1;36;40m"
Dark="\033[0;37;40m"





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

text = string.ascii_lowercase + string.digits 
additions = input('[+] Additions: ')
lengit = int(input('[+] Length: '))
count = int(input('[+] Count: '))
for x in range(count):
    pasb = ''.join(random.choice(text) for x in range(lengit))
    with open('user.txt', 'a') as file:
        file.write(additions + pasb + '\n')
        let += 1
        print(f'Done {let}\{count}')

        
