import socket
import argparse
import time
import os
import binascii
import json

from threading import *


clientSocket = socket.socket()
width = os.get_terminal_size().columns


class Networking(Thread):
    def __init__(self, args):
        Thread.__init__(self)

        self.settings = json.load(open('Settings.json'))

        self.address = self.settings["Address"]
        self.port = self.settings["Port"]
        self.client = clientSocket
        self.args = args

    def run(self):
        self.client.bind((self.address, self.port))
        self.client.listen(10)

        print('Server is listening on {}:{}'.format(self.address, self.port).center(width))

        print('{}'.format('-' * (width // 2)).center(width))

        while True:
            client, address = self.client.accept()

            print('New connection from {}'.format(address[0]))

            clientThread = ClientThread(client, self.args.debug).start()


class ClientThread(Thread):
    def __init__(self, clientSocket, debug):
        Thread.__init__(self)

        self.client = clientSocket
        self.debug  = debug

    def recvall(self, size):
        data = []
        while size > 0:
            self.client.settimeout(5.0)
            s = self.client.recv(size)
            self.client.settimeout(None)
            if not s:
                raise EOFError
            data.append(s)
            size -= len(s)
        return b''.join(data)

    def run(self):
        while True:
            header   = self.client.recv(7)
            packetid = int.from_bytes(header[:2], 'big')
            length   = int.from_bytes(header[2:5], 'big')
            version  = int.from_bytes(header[5:], 'big')
            data     = self.recvall(length)

            '''
            if len(header) >= 7:
                print('Buffer is valid')
            else:
                print('Buffer is not valid')
            '''
            if len(header) >= 7:
                if length == len(data):
                    if self.debug:
                        print('{} received'.format(packetid))

            else:
                if self.debug:
                    print('Received an invalid packet from client')
                self.client.close()

            '''
            packetid = int.from_bytes(header[0:2], 'big')
            length = int.from_bytes(header[2:5], 'big')
            version = int.from_bytes(header[5:6], 'big')

            payload = recvall(self.client, length)

            if len(header) >= 7:
                if len(length) == len(payload):
                    if self.debug:
                        print('Received VALID packet!')
            else:
                if self.debug:
                    print('Invalid packet received from client!')
                self.client.close()
            '''
