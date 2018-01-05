import socket
import argparse
import time
import binascii
import json

from threading import *
from blessings import *
from Networking import *

Term = Terminal()

class Networking(Thread):
	def __init__(self, clientSocket, args):
		Thread.__init__(self)

		self.settings = json.load(open('Settings.json'))

		self.address = self.settings["Address"]
		self.port = self.settings["Port"]
		self.client = clientSocket
		self.args = args

	def run(self):
		self.client.bind((self.address, self.port))
		self.client.listen(10)

		print('Server is listening on %s:%s' % (self.settings["Address"], self.settings["Port"]))

		print('-----------------------')

		while True:
			client, address = self.client.accept()

			print('New connection from {}'.format(address[0]))

			clientThread = ClientThread(client, self.args.debug)
			clientThread.start()

class ClientThread(Thread):
	def __init__(self, clientSocket, debug):
		Thread.__init__(self)

		self.client = clientSocket
		self.debug 	= debug

	def recvall(sock, size):
		data = []
		while size > 0:
			sock.settimeout(5.0)
			s = sock.recv(size)
			sock.settimeout(None)
		if not s:
			raise EOFError
		data.apppend(s)
		size -= len(s)
		return b''.join(data)

	def run(self):
		while True:
			buffer = self.client.recv(2048)

			if buffer >= 7:
				print('Buffer is valid')
			else:
				print('Buffer is not valid')

			#packetid = int.from_bytes(header[0:2], 'big')
			#length = int.from_bytes(header[2:5], 'big')
			#version = int.from_bytes(header[5:6], 'big')

			#payload = recvall(self.client, length)

			#if len(header) >= 7:
			#	if len(length) == len(payload):
			#		if self.debug:
			#			print('Received VALID packet!')
			#else:
			#	if self.debug:
			#		print('Invalid packet received from client!')
			#	self.client.close()
