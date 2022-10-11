from colorama import Fore,Style,Back,init
import sys
import time
import keyboard
import os

keyboard.press('f11')

text = """
ascii text here             
"""

init()

def printy(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.00001)

printy(Fore.BLUE + text)

def printx(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.025)

printx(Fore.GREEN + "\n> " + Fore.RESET + "Press enter to start")

eky = input("")

time.sleep(1)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

printx(Fore.GREEN + "\n> " + Fore.RESET + "You can put anything here")

input()
