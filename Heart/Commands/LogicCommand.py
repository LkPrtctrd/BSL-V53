from Heart.Record.ByteStream import ByteStream

class LogicCommand(ByteStream):
    def __init__(self, commandData):
        super().__init__(commandData)
        self.messageBuffer = commandData
        self.messagePayload = commandData

    def encode(self, fields):
        self.writeVInt(-1)
        self.writeVInt(-1)
        self.writeVInt(0)
        self.writeVInt(0)
        #self.writeVLong(0, 0)

    def decode(calling_instance, fields, auto_decode=True):
        fields["TickWhenGiven"] = calling_instance.readVInt()
        fields["ExecuteTick"] = calling_instance.readVInt()
        fields["ExecutorAccountID"] = calling_instance.readVLong()
        if True:
            print()
            for typeName,value in fields.items():
                print(f"{typeName}: {value}")
            print()
        return fields

    def parseFields(fields):
        print()
        for typeName,value in fields.items():
            print(f"{typeName}: {value}")
        print()
