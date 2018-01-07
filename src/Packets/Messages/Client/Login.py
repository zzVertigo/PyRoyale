# -*- coding: utf-8 -*-
from Utils.Reader import ByteStream


class Login(ByteStream):

    def __init__(self, data):
        super().__init__(data)

    def decode(self):
        self.ReadUint32()
        # Todo: Read Stuff and maybe create a parent instance of a Device Class

    def process(self):
        pass
        # Todo : Process LoginOK
