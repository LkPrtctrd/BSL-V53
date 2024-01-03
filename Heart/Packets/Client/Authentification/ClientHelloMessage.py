from Heart.Messaging import Messaging

from Heart.Packets.PiranhaMessage import PiranhaMessage


class ClientHelloMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["Protocol"] = self.readInt()
        fields["KeyVersion"] = self.readInt()
        fields["MajorVersion"] = self.readInt()
        fields["MinorVersion"] = self.readInt()
        fields["Build"] = self.readInt()
        fields["ContentHash"] = self.readString()
        fields["DeviceType"] = self.readInt()
        fields["AppStore"] = self.readInt()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(20100, fields, cryptoInit)

    def getMessageType(self):
        return 10100

    def getMessageVersion(self):
        return self.messageVersion