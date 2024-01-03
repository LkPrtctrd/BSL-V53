from Heart.Commands.LogicCommand import LogicCommand
from Heart.Messaging import Messaging

class PurchaseOfferCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        self.writeVInt(0)
        self.writeDataReference(0)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["OfferIndex"] = calling_instance.readVInt()
        fields["Unk2"] = calling_instance.readDataReference()
        fields["Unk3"] = calling_instance.readDataReference()
        fields["Unk4"] = calling_instance.readVInt()
        
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields, cryptoInit):
        if fields["OfferIndex"] == 0:
            pass

    def getCommandType(self):
        return 519