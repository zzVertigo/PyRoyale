# -*- coding: utf-8 -*-

import time
from Utils.Writer import Writer


class LoginOk(Writer):

    def __init__(self, device):
        self.id = 22280
        self.version = 1
        self.device = device
        super().__init__(self.device)

    def encode(self):

        timeStamp = str(round(time.time(), 3)).replace('.', '')

        self.writeInt(0)  # HighId
        self.writeInt(1)  # LowId

        self.writeInt(0)  # HighId
        self.writeInt(1)  # LowId

        self.writeString("ThisIsAToken")  # Token

        self.writeString()  # GameCenterId
        self.writeString()  # FacebookId

        self.writeVint(3)    # MajorVersion
        self.writeVint(830)  # Build
        self.writeVint(830)  # Build
        self.writeVint(7)    # MinorVersion

        self.writeString("prod")  # Environment

        self.writeVint(0)  # SessionCount
        self.writeVint(0)  # PlayTimeSeconds
        self.writeVint(0)  # DaySinceStartedPlaying

        self.writeString("1475268786112433")  # FacebookAppId
        self.writeString(timeStamp)  # ServerTime
        self.writeString("")  # AccountCreatedDate

        self.writeVint(0)

        self.writeString()  # GoogleServiceId
        self.writeString()
        self.writeString()

        self.writeString()  # Region
        self.writeString()  # City
        self.writeString()  # LocalRegion

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(2)

        self.writeString()  # Url Game Assets
        self.writeString()  # Url cdn

        self.writeVint(1)

        self.writeString()  # Url event assets
