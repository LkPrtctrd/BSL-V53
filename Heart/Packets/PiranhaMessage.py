from Heart.Record.ByteStream import ByteStream

class PiranhaMessage(ByteStream):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageBuffer = messageData
        self.fields = {}

    def decode(self, fields):
        if True:
            print()
            for typeName,value in fields.items():
                print(f"{typeName}: {value}")
            print()

    def getLength(self):
        return len(self.messageBuffer)

    def isServerToClient(self):
        messageType = self.getMessageType()
        if 20000 <= messageType < 30000 or messageType == 40000:
            return True
        elif 10000 <= messageType < 20000 or messageType == 30000:
            return False
