from Heart.Commands.LogicCommand import LogicCommand


class LogicServerCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def addCommand(self, fields):
        self.writeVInt(1)
        LogicCommand.encode(self, fields)

    def decode(calling_instance, fields):
        fields["ID"] = calling_instance.readVInt()
        return LogicCommand.decode(calling_instance, fields)
