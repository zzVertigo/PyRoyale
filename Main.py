import os
import socket
import argparse

from threading import *
from Networking import *

width = os.get_terminal_size().columns

parser = argparse.ArgumentParser()

parser.add_argument('-d', '--debug', action='store_true', help='Will display DEBUG log messages.')

args = parser.parse_args()

print('Starting PyRoyale v1.0!'.center(width))

Networking = Networking(args).start()
