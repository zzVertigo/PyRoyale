import socket
import argparse

from Networking import *
from threading import *

parser = argparse.ArgumentParser()

parser.add_argument('-d', '--debug', action='store_true', help='Will display DEBUG log messages.')

args = parser.parse_args()

print('Starting PyRoyale v1.0!')

Networking = Networking(args).start()