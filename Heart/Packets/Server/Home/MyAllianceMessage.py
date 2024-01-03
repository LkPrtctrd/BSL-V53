from Heart.Packets.PiranhaMessage import PiranhaMessage


class MyAllianceMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVInt(1) # Online people in alliance
        self.writeBoolean(True) # isInAlliance
        self.writeDataReference(25, 4)
        self.writeLong(0, 1) # alliance ID
        self.writeString(player.ContentCreator) # alliance name
        self.writeDataReference(8, 37) # alliance icon
        self.writeVInt(3) # type
        self.writeVInt(1) # member count
        self.writeVInt(9500) # total trophies
        self.writeVInt(1) # minimum trophies to enter
        self.writeVInt(0) # 0
        self.writeString('RU') # location
        self.writeVInt(3) # unknown
        self.writeBoolean(True) # isFamilyFriendly
        self.writeVInt(0)

    def decode(self):
        fields = {}
        super().decode(fields)
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24399

    def getMessageVersion(self):
        return self.messageVersion