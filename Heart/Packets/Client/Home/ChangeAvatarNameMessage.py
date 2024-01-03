from Heart.Messaging import Messaging
from DB.DatabaseHandler import DatabaseHandler
from Heart.Packets.PiranhaMessage import PiranhaMessage


class ChangeAvatarNameMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        self.writeString(fields["Name"])
        self.writeBoolean(fields["NameSetByUser"])

    def decode(self):
        fields = {}
        fields["Name"] = self.readString()
        fields["NameSetByUser"] = self.readBoolean()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        db_instance = DatabaseHandler()
        playerData = db_instance.getPlayer(calling_instance.player.ID)
        playerData["Name"] = fields["Name"]
        playerData["Registered"] = True
        db_instance.updatePlayerData(playerData, calling_instance)
        fields["Socket"] = calling_instance.client
        fields["Command"] = {"ID": 201}
        Messaging.sendMessage(24111, fields, cryptoInit, calling_instance.player)

    def getMessageType(self):
        return 10212

    def getMessageVersion(self):
        return self.messageVersion