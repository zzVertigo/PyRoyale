# -*- coding: utf-8 -*-
from Utils.Writer import Writer


class LoginOk(Writer):

    def __init__(self, device):
        self.id = 22280
        self.device = device
        super().__init__(self.device)

    def encode(self):
        self.writeString("Test")
