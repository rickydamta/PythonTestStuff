import platform
import os
import time
import sys
from colorama import init
init()

from colorama import Fore, Back, Style

#Todos
    #TODO: ARRAY GLYPH RICORDATI




#Resize the window...
os.system('mode con: cols=120 lines=30')

print("                      ")
print("                      ")
print("                      ")
print("                      ")

print (Fore.RED +"                                     ")
print("                                           /  ___|                   | | ")
print("                                           \ `--. _ __   ___  ___ ___| | ")
print("                                            `--. \ '_ \ / _ \/ __/ __| | ")
print("                                           /\__/ / |_) |  __/ (__\__ \_| ")
print("                                           \____/| .__/ \___|\___|___(_)  ")
print("                                                 | |                      ")
print("                                                 |_|                      ")

print("                                                                           ")
print("                                                                           ")
print("                                                                           ")

print("                 ###########################################################################                     ")
print("                                               MADE BY RICKYDAMTA                   ")
print("                                                     0.0.1                 ")
print("                                               VERSION NAME: DEV   ")
print("                 ###########################################################################                      ")

print(Style.RESET_ALL)

print("[!]Loading..............................")
time.sleep( 2 )
print("[!]Loading..............................")
time.sleep( 2  )

print(Style.RESET_ALL)

print("[ 1 ]   Scan Computer Specs!............                 " )
print("[ 2 ]   Exit the program................                 " )


choose = input("Enter the number you want:   ")

if choose == "1":

    print(Fore.GREEN + "[!]Loading..............................")
    time.sleep( 2 )

    print(Style.RESET_ALL)

    print (Fore.RED + 'Version      : ', platform.python_version())
    print ('Version tuple: ', platform.python_version_tuple())
    print ('Compiler     : ', platform.python_compiler())
    print ('Build        : ', platform.python_build())
    print ('64 bit or 32bit: ', platform.machine())
    #print ('uname:', platform.uname())
    print ('system   :', platform.system())
    print ('node     :', platform.node())
    print ('release  :', platform.release())
    print ('version  :', platform.version())

    print ('processor:', platform.processor())

else:
    sys.exit()
