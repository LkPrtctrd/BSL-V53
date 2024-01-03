from Heart.Messaging import Messaging

from Heart.Packets.PiranhaMessage import PiranhaMessage


class AskForAllianceDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["id"] = self.readVLong()
        fields["isInAlliance"] = self.readBoolean()
        if fields["isInAlliance"] == True:
            fields["anotherIDHigh"] = self.readVInt()
            fields["anotherIDLow"] = self.readVInt()
        super().decode(fields)

        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(24301, fields, cryptoInit, calling_instance.player)

    def getMessageType(self):
        return 14302

    def getMessageVersion(self):
        return self.messageVersion