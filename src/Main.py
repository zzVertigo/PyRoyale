import os
import socket
import argparse

from threading import *
from colorama import Fore, Style, init
from Networking import *
from TwistedNetworking import *

width = os.get_terminal_size().columns

parser = argparse.ArgumentParser()

parser.add_argument('-d', '--debug', action='store_true', help='Will display DEBUG log messages.')
parser.add_argument('-t', '--twisted', action='store_true', help='Will use twisted framework instead of classic thread')

args = parser.parse_args()

init()

print(Fore.YELLOW + '''

              __________         __________                         .__           
              \______   \ ___.__.\______   \  ____   ___.__._____   |  |    ____  
               |     ___/<   |  | |       _/ /  _ \ <   |  |\__  \  |  |  _/ __ \ 
               |    |     \___  | |    |   \(  <_> ) \___  | / __ \_|  |__\  ___/ 
               |____|     / ____| |____|_  / \____/  / ____|(____  /|____/ \___  >
                          \/             \/          \/          \/            \/ 

''')
print(Style.RESET_ALL)
print('Starting PyRoyale v1.0...'.center(width))

if args.twisted:
    startTwistedFactory()

else:
    Networking(args).start()
