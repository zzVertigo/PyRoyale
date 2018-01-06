import os
import socket
import argparse

from threading import *
from Networking import *

width = os.get_terminal_size().columns

parser = argparse.ArgumentParser()

parser.add_argument('-d', '--debug', action='store_true', help='Will display DEBUG log messages.')

args = parser.parse_args()

print('''

			  __________         __________                         .__           
			  \______   \ ___.__.\______   \  ____   ___.__._____   |  |    ____  
			   |     ___/<   |  | |       _/ /  _ \ <   |  |\__  \  |  |  _/ __ \ 
			   |    |     \___  | |    |   \(  <_> ) \___  | / __ \_|  |__\  ___/ 
			   |____|     / ____| |____|_  / \____/  / ____|(____  /|____/ \___  >
			              \/             \/          \/          \/            \/ 
						  
''')
print('Starting PyRoyale v1.0...'.center(width))

Networking = Networking(args).start()
