from Heart.Packets.PiranhaMessage import PiranhaMessage


class PlayerProfileMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVLong(fields["PlayerHighID"], fields["PlayerLowID"])
        self.writeDataReference(16,11) # 
        self.writeVInt(70)
        for i in range(70):
            self.writeDataReference(16, i)
            self.writeDataReference(0)
            self.writeVInt(500) # trophies
            self.writeVInt(1250) # highestTrophies
            self.writeVInt(11) #power level
        
        self.writeVInt(18)

        self.writeVInt(1) 
        self.writeVInt(1) # 3v3 victories

        self.writeVInt(2)
        self.writeVInt(528859) # total exp

        self.writeVInt(3)
        self.writeVInt(3) # current trophies

        self.writeVInt(4)
        self.writeVInt(4) # highest trophies

        self.writeVInt(5) 
        self.writeVInt(5) # unlocked brawler?

        self.writeVInt(8)
        self.writeVInt(6) # solo victories

        self.writeVInt(11) 
        self.writeVInt(7) # duo victories

        self.writeVInt(9) 
        self.writeVInt(8) # highest level robo rumble

        self.writeVInt(12) 
        self.writeVInt(9) # highest level boss fight

        self.writeVInt(13)
        self.writeVInt(10) # highest power league points

        self.writeVInt(14)
        self.writeVInt(11) # some power league stuff

        self.writeVInt(15)
        self.writeVInt(12) # most challenge win

        self.writeVInt(16) #highest level city rampage
        self.writeVInt(13)

        self.writeVInt(18) #highest solo power league rank
        self.writeVInt(14)

        self.writeVInt(17) #highest team power league rank
        self.writeVInt(15)

        self.writeVInt(19) # highest Club league rank
        self.writeVInt(16)

        self.writeVInt(20) # number fame
        self.writeVInt(1000)

        self.writeVInt(21)
        self.writeVInt(502052) #v50

        self.writeString(player.Name)  #PlayerInfo
        self.writeVInt(100)
        self.writeVInt(28000000 + player.Thumbnail)
        self.writeVInt(43000000 + player.Namecolor)
        self.writeVInt(14)

        self.writeBoolean(True)
        self.writeVInt(300)

        self.writeString("hello world")
        self.writeVInt(100)
        self.writeVInt(200)
        self.writeDataReference(29, 558)
        self.writeDataReference(0)
        self.writeDataReference(0)
        self.writeDataReference(0)
        self.writeDataReference(0)

        self.writeBoolean(True) #alliance
        self.writeLong(0,1) #alliance ID
        self.writeString("haccers") #alliance name
        self.writeDataReference(8,1) # alliance icon
        self.writeVInt(1) # type
        self.writeVInt(1) # member count
        self.writeVInt(10000) # total trophies
        self.writeVInt(1) # minimum trophies to enter
        self.writeDataReference(0)
        self.writeString("RU") #location
        self.writeVInt(4) # unknown
        self.writeBoolean(True) #is Family friendly
        self.writeVInt(0)
        

        self.writeDataReference(25, 1) #alliance role
        self.writeVInt(16)

    def decode(self):
        pass
        # fields = {}
        # fields["PlayerCount"] = self.readVInt()
        # fields["Text"] = self.readString()
        # fields["Unk1"] = self.readVInt()
        # super().decode(fields)
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24113

    def getMessageVersion(self):
        return self.messageVersion