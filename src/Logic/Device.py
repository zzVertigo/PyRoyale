# -*- coding: utf-8 -*-
from CryptoRC4.Crypto import CryptoRc4


class Device:
    AndroidID = None
    DeviceModel = None
    OpenUDID = None
    OSVersion = None  
    IsAndroid = False
    Language = None

    def __init__(self, socket):
        self.socket = socket
        self.crypto = CryptoRc4()

    def SendData(self, ID, data, version=None):

        encrypted = self.crypto.encrypt(data)
        packetID   = ID.to_bytes(2, 'big')

        if version:
            packetVersion = version.to_bytes(2, 'big')

        else:
            packetVersion = (0).to_bytes(2, 'big')

        self.socket.send(packetID + len(encrypted).to_bytes(3, 'big') + packetVersion + encrypted)
        print('[*] {} sent'.format(ID))

    def decrypt(self, data):
        return self.crypto.decrypt(data)
