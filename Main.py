import socket
import argparse

from threading import *
from Networking import *

Term = Terminal()
clientSocket = socket.socket()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	parser.add_argument('-d', '--debug', action='store_true', help='Will display DEBUG log messages.')

	args = parser.parse_args()

	print('Starting PyRoyale v1.0!')

	Networking = Networking(clientSocket, args).start()
