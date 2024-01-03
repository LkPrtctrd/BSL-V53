from Heart.Packets.PiranhaMessage import PiranhaMessage

class BattleEndMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeLong(0, 0) # Battle UUID High
        self.writeLong(0, 0) # Battle UUID Low
        self.writeVInt(2) # Battle End Game Mode (gametype)
        self.writeVInt(fields["Rank"]) # Result (Victory/Defeat/Draw/Rank Score)
        self.writeVInt(0) # Tokens Gained (Gained Keys)
        self.writeVInt(0) # Trophies Result (Metascore change)
        self.writeVInt(0) # Power Play Points Gained (Pro League Points)
        self.writeVInt(0) # Doubled Tokens (Double Keys)
        self.writeVInt(0) # Double Token Event (Double Event Keys)
        self.writeVInt(0) # Token Doubler Remaining (Double Keys Remaining)
        self.writeVInt(0) # game Lenght In Seconds
        self.writeVInt(0) # Epic Win Power Play Points Gained (op Win Points)
        self.writeVInt(0) # Championship Level Reached (CC Wins)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(True)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)

        self.writeVInt(fields["HeroesCount"])
        for heroEntry in fields["Heroes"]:
            self.writeBoolean(heroEntry["IsPlayer"])
            self.writeBoolean(bool(heroEntry["Team"]))
            self.writeBoolean(bool(heroEntry["Team"]))
            self.writeByte(1)
            for i in range(1):
                self.writeDataReference(heroEntry["Brawler"]["ID"][0], heroEntry["Brawler"]["ID"][1])
            self.writeByte(1)
            for i in range(1):
                if (heroEntry["Brawler"]["SkinID"] is None):
                    self.writeVInt(0)
                else:
                    self.writeDataReference(heroEntry["Brawler"]["SkinID"][0], heroEntry["Brawler"]["SkinID"][1])
            self.writeByte(1)
            for i in range(1):
                self.writeVInt(1250)
            self.writeByte(1)
            for i in range(1):
                self.writeVInt(11)
            self.writeByte(1)
            for i in range(1):
                self.writeVInt(0)

            self.writeVInt(0)
            self.writeVInt(0)

            self.writeBoolean(heroEntry["IsPlayer"])
            if heroEntry["IsPlayer"]:
                self.writeLong(player.ID[0], player.ID[1])
            self.writeString(heroEntry["PlayerName"])
            self.writeVInt(100)
            self.writeVInt(28000000)
            self.writeVInt(43000000)
            self.writeVInt(-2)
            if heroEntry["IsPlayer"]:
                self.writeBoolean(True)
                self.writeVLong(5, 4181497)
                self.writeString('haccer club')
                self.writeDataReference(8, 16)
            else:
                self.writeBoolean(False)

            self.writeInt8(1)
            self.writeVInt(5978)
            self.writeInt8(1)
            self.writeVInt(0)

            self.writeInt16(5)
            self.writeInt16(3)
            self.writeInt(27328)
            self.writeInt(25659)

            self.writeDataReference(0)

        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # 0x0
        self.writeBoolean(False) # 0x0
        self.writeBoolean(False) # 0x0
        self.writeBoolean(False) # 0x0
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # 0x0
        self.writeVInt(0)
        self.writeBoolean(False) # 0x0
        self.writeVInt(0)
        self.writeBoolean(False) # 0x0
        self.writeBoolean(False) # 0x0
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # 0x0
        self.writeBoolean(False) # 0x0
        self.writeBoolean(False) # 0x0

    def decode(self):
        fields = {}
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 23456

    def getMessageVersion(self):
        return self.messageVersion