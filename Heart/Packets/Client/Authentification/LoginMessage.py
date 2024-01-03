from Heart.Messaging import Messaging
from DB.DatabaseHandler import DatabaseHandler
from Heart.Packets.PiranhaMessage import PiranhaMessage
import json
from Heart.Utils.ClientsManager import ClientsManager

class LoginMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["AccountID"] = self.readLong()
        fields["PassToken"] = self.readString()
        fields["ClientMajor"] = self.readInt()
        fields["ClientMinor"] = self.readInt()
        fields["ClientBuild"] = self.readInt()
        fields["ResourceSha"] = self.readString()
        fields["Device"] = self.readString()
        fields["PreferredLanguage"] = self.readDataReference()
        fields["PreferredDeviceLanguage"] = self.readString()
        fields["OSVersion"] = self.readString()
        fields["isAndroid"] = self.readBoolean()
        fields["IMEI"] = self.readString()
        fields["AndroidID"] = self.readString()
        fields["isAdvertisingEnabled"] = self.readBoolean()
        fields["AppleIFV"] = self.readString()
        fields["RndKey"] = self.readInt()
        fields["AppStore"] = self.readVInt()
        fields["ClientVersion"] = self.readString()
        fields["TencentOpenId"] = self.readString()
        fields["TencentToken"] = self.readString()
        fields["TencentPlatform"] = self.readVInt()
        fields["DeviceVerifierResponse"] = self.readString()
        fields["AppLicensingSignature"] = self.readString()
        fields["DeviceVerifierResponse"] = self.readString()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        if fields["ClientMajor"]==53:
            calling_instance.player.ClientVersion = f'{str(fields["ClientMajor"])}.{str(fields["ClientBuild"])}.{str(fields["ClientMinor"])}'
            fields["Socket"] = calling_instance.client
            db_instance = DatabaseHandler()
            if db_instance.playerExist(fields["PassToken"], fields["AccountID"]):
                player_data = json.loads(db_instance.getPlayerEntry(fields["AccountID"])[2])
                db_instance.loadAccount(calling_instance.player, fields["AccountID"])
            else:
                db_instance.createAccount(calling_instance.player.getDataTemplate(fields["AccountID"][0], fields["AccountID"][1], fields["PassToken"]))
            ClientsManager.AddPlayer(calling_instance.player.ID, calling_instance.client)
            Messaging.sendMessage(20104, fields, cryptoInit, calling_instance.player)
            Messaging.sendMessage(24101, fields, cryptoInit, calling_instance.player)
            Messaging.sendMessage(24399, fields, cryptoInit, calling_instance.player)

    def getMessageType(self):
        return 10101

    def getMessageVersion(self):
        return self.messageVersion