# -*- coding: utf-8 -*-
from Utils.Reader import ByteStream
from Packets.Messages.Server.LoginOk import LoginOk


class Login(ByteStream):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):
        print("HighID: {}".format(self.ReadUint32()))
        print("LowID: {}".format(self.ReadUint32()))
        print("Token: {}".format(self.ReadString()))
        print("Major: {}".format(self.ReadVint()))
        print("Minor: {}".format(self.ReadVint()))
        print("Revision: {}".format(self.ReadVint()))
        print("Masterhash: {}".format(self.ReadString()))
        print("Unknown: {}".format(self.ReadUint32()))
        print("AndroidID: {}".format(self.ReadString()))
        print("Unknown: {}".format(self.ReadString()))
        print("Device Model: {}".format(self.ReadString()))
        print("OpenUDID: {}".format(self.ReadString()))
        print("OS Version: {}".format(self.ReadString()))
        print("IsAndroid: {}".format(self.ReadBool()))
        print("Unknown: {}".format(self.ReadUint32()))
        print("AndroidID: {}".format(self.ReadString()))
        print("Language: {}".format(self.ReadString()))

    def process(self):
        LoginOk(self.device).Send()
        # Todo : Process stuff (implement OHD)
