from Heart.Messaging import Messaging

from Heart.Packets.PiranhaMessage import PiranhaMessage


class SinglePlayerMatchRequestMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(23456, fields, cryptoInit, calling_instance.player)

    def getMessageType(self):
        return 14118

    def getMessageVersion(self):
        return self.messageVersion
