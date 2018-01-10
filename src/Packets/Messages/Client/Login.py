# -*- coding: utf-8 -*-

from Utils.Reader import ByteStream
from Packets.Messages.Server.LoginOk import LoginOk
from Logic.Player import Player

class Login(ByteStream):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)

    def decode(self):
        self.player.HighID = self.ReadUint32()
        self.player.LowID = self.ReadUint32()
        self.player.Token = self.ReadString()

        self.ReadVint()
        self.ReadVint()
        self.ReadVint()
        self.ReadString()
        self.ReadUint32()

        self.device.AndroidID = self.ReadString()

        self.ReadString()

        self.device.DeviceModel = self.ReadString()
        self.device.OpenUDID = self.ReadString()
        self.device.OSVersion = self.ReadString()
        self.device.IsAndroid = self.ReadBool()

        self.ReadUint32()
        self.ReadString()

        self.device.Language = self.ReadString()

    def process(self):
        LoginOk(self.device).Send()
        # Todo : Process stuff (implement OHD)
