import os
import sys
import random
from time import sleep

def clear():
	os.system('clear')

def getline(stream, delimiter="\n"):
  def _gen():
    while 1:
      line = stream.readline()
      if delimiter in line:
        yield line[0:line.index(delimiter)]
        break
      else:
        yield line
  return "".join(_gen())
getline(sys.stdin, ".")

health = int(100)
food = int(100)
player = int()
inventory[5] = string(["[1] Wooden Sword(s)", "[3] Water Bottle", "[12] Apple", "[64] Dark Oak Planks", "[4] Torch"]);
character = str()
loadStr = str([lsCs100_1, lsCs100_2, lsCa100_1, lsCa100_2])




Blue = "\033[0;34m"
Cyan = "\033[1;36m"
White = "\033[0;37m" 
Green = "\033[0;32m"
Orange ="\033[0;33m"
Pink = "\033[1;31m"
Black = "\033[0;30m"
Purple = "\033[0;35m"

login0 = '''
╔══════════════════════════════════════════════╗
║                                              ║
║                                              ║
║                                              ║
║ MPE: v1.14                                   ║
║ VPN:                                         ║
║                                              ║
║                                              ║
║                                              ║
╚══════════════════════════════════════════════╝
'''
login1 = '''
╔══════════════════════════════════════════════╗
║                                              ║
║                                              ║
║                                              ║
║ MPE: v1.14                                   ║
║ VPN: *                                       ║
║                                              ║
║                                              ║
║                                              ║
╚══════════════════════════════════════════════╝
'''
login2 = '''
╔══════════════════════════════════════════════╗
║                                              ║
║                                              ║
║                                              ║
║ MPE: v1.14                                   ║
║ VPN: **                                      ║
║                                              ║
║                                              ║
║                                              ║
╚══════════════════════════════════════════════╝
'''
login3 = '''
╔══════════════════════════════════════════════╗
║                                              ║
║                                              ║
║                                              ║
║ MPE: v1.14                                   ║
║ VPN: ***                                     ║
║                                              ║
║                                              ║
║                                              ║
╚══════════════════════════════════════════════╝
'''
login4 = '''
╔══════════════════════════════════════════════╗
║                                              ║
║                                              ║
║                                              ║
║ MPE: v1.14                                   ║
║ VPN: ****                                    ║
║                                              ║
║                                              ║
║                                              ║
╚══════════════════════════════════════════════╝
'''
login5 = '''
╔══════════════════════════════════════════════╗
║                                              ║
║                                              ║
║                                              ║
║ MPE: v1.14                                   ║
║ VPN: *****                                   ║
║                                              ║
║                                              ║
║                                              ║
╚══════════════════════════════════════════════╝
'''
login6 = '''
╔══════════════════════════════════════════════╗
║                                              ║
║                                              ║
║                                              ║
║ MPE: v1.14                                   ║
║ VPN: *****                                   ║
║                                              ║
║                                              ║
║                                              ║
╚══════════════════════════════════════════════╝
'''
login7 = '''
╔══════════════════════════════════════════════╗
║                                              ║
║                                              ║
║                                              ║
║                   LOGIN                      ║
║                 SUCCESSFUL                   ║
║                                              ║
║                                              ║
║                                              ║
╚══════════════════════════════════════════════╝
'''
login8 = '''
╔══════════════════════════════════════════════╗
║                                              ║
║                                              ║
║                                              ║
║                   WELCOME                    ║
║                                              ║
║                                              ║
║                                              ║
║                                              ║
╚══════════════════════════════════════════════╝
'''

intlz = '''
╔══════════════════════════════════════════════╗
║                                              ║
║                                              ║
║                                              ║
║               INITIALIZING...                ║
║                                              ║
║                                              ║
║                                              ║
║                                              ║
╚══════════════════════════════════════════════╝
'''

hndl0 = '''
╔══════════════════════════════════════════════╗
║                                              ║
║                                              ║
║                  MINECRAFT                   ║
║                  PYTHON/SQL                  ║ 
║                   EDITION                    ║
║                                              ║
║                                     NEXT >   ║
║                                              ║
╚══════════════════════════════════════════════╝
'''

hndl1 = '''
╔══════════════════════════════════════════════╗
║                                              ║
║                                              ║
║                  MINECRAFT                   ║
║                  PYTHON/SQL                  ║ 
║                   EDITION                    ║
║                                              ║
║                                     NEXT >   ║
║                                              ║
╚══════════════════════════════════════════════╝
'''

SCRN = '''
╔══════════════════════════════════════════════╗
║                                              ║
║                                              ║
║                 SINGLEPLAYER                 ║
║                 MULTIPLAYER                  ║ 
║                   REALMS                     ║
║                                              ║
║                                              ║
║                                              ║
╚══════════════════════════════════════════════╝
'''

flscrn = print(White + "YOU HAVE NOW ENTERED FULLSCREEN MODE")

def login():
	clear()
	print(login0)
	sleep(1)
	clear()
	print(login1)
	sleep(0.5)
	clear()
	print(login2)
	sleep(0.5)
	clear()
	print(login3)
	sleep(0.5)
	clear()
	print(login4)
	sleep(0.5)
	clear()
	print(login5)
	sleep(0.5)
	clear()
	print(login6)
	sleep(0.5)
	clear()
	print(login7)
	sleep(1)
	clear()
	print(login8)
	sleep(1.7)
	clear()

def intro():
	for i in range(31):
		clear()
		print(intlz)
		

login()
intro()
print("\n")
sleep(3)
clear()
print(hndl0)
sleep(5)
clear()
print(hndl1)
sleep(3)

clear()
print("")
MVN0 = input()
clear()

if MVN0 == "":
	GaMode = input(SCRN)
	if GaMode == "SINGLEPLAYER":
		clear()
    print(flscrn)
	if GaMode == "MULTIPLAYER":
		clear()
    print(flscrn)
	if GaMode == "REALMS":
		clear()
    print(flscrn)

if MVN0 != "":
	print(Pink + "ERROR - OUTPUT NOT AVAILABLE")
