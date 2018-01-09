# -*- coding: utf-8 -*-
from Utils.Reader import ByteStream
from Packets.Messages.Server.LoginOk import LoginOk


class Login(ByteStream):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):
        self.ReadUint32()
        # Todo: Read Stuff

    def process(self):
        LoginOk(self.device).Send()
        # Todo : Process stuff (implement OHD)
