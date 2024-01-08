from Heart.Record.ByteStreamHelper import ByteStreamHelper
from Heart.Packets.PiranhaMessage import PiranhaMessage

class OwnHomeDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVInt(1688816070)
        self.writeVInt(1191532375)
        self.writeVInt(2023189)
        self.writeVInt(73530)

        self.writeVInt(player.Trophies)
        self.writeVInt(player.HighestTrophies)
        self.writeVInt(player.HighestTrophies) 
        self.writeVInt(player.TrophyRoadTier)
        self.writeVInt(player.Experience)
        self.writeDataReference(28, player.Thumbnail)
        self.writeDataReference(43, player.Namecolor)

        self.writeVInt(26)
        for x in range(26):
            self.writeVInt(x)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)
        
        self.writeVInt(len(player.OwnedSkins))
        for x in player.OwnedSkins:
            self.writeDataReference(29, x)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(player.HighestTrophies)
        self.writeVInt(0)
        self.writeVInt(2)
        self.writeBoolean(True)
        self.writeVInt(0)
        self.writeVInt(115)
        self.writeVInt(335442)
        self.writeVInt(1001442)
        self.writeVInt(5778642) 

        self.writeVInt(120)
        self.writeVInt(200)
        self.writeVInt(0)

        self.writeBoolean(True)
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(1) # Shop Offers

        self.writeVInt(1) # RewardCount

        self.writeVInt(38)  # ItemType
        self.writeVInt(1337) # Amount
        self.writeDataReference(0)  # CsvID
        self.writeVInt(0) # SkinID

        self.writeVInt(0) # Currency(0-Gems, 1-Gold, 3-StarpoInts)
        self.writeVInt(0) # Cost
        self.writeVInt(0) # Time
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # Daily Offer
        self.writeVInt(0) # Old price
        self.writeString('Offer') # Text
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString("offer_xmas23") # Background
        self.writeVInt(0)
        self.writeBoolean(False) # This purchase is already being processed
        self.writeVInt(0) # Type Benefit
        self.writeVInt(0) # Benefit
        self.writeString()
        self.writeBoolean(False) # One time offer
        self.writeBoolean(False) # Claimed
        self.writeDataReference(0)
        self.writeDataReference(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeVInt(20)
        self.writeVInt(1428)

        self.writeVInt(0)

        self.writeVInt(1)
        self.writeVInt(30)

        self.writeByte(1) # count brawlers selected
        self.writeDataReference(16, player.SelectedBrawlers[0]) # selected brawler
        self.writeString(player.Region) # location
        self.writeString(player.ContentCreator) # supported creator

        self.writeVInt(6) 
        self.writeVInt(1) 
        self.writeVInt(9) 
        self.writeVInt(1) 
        self.writeVInt(22) 
        self.writeVInt(3) 
        self.writeVInt(25) 
        self.writeVInt(1) 
        self.writeVInt(24) 
        self.writeVInt(0)
        self.writeVInt(15)
        self.writeVInt(32447)
        self.writeVInt(28)


        self.writeVInt(0)

        self.writeVInt(1)
        for season in range(1):
            self.writeVInt(22-1)
            self.writeVInt(40000)
            self.writeBoolean(True)
            self.writeVInt(0)
            self.writeBoolean(False)
            self.writeBoolean(True)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
            self.writeBoolean(True)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
            self.writeBoolean(True)
            self.writeBoolean(True)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)

        self.writeVInt(0)

        self.writeBoolean(True)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(0) 

        self.writeBoolean(True) # Vanity items
        self.writeVInt(len(player.OwnedThumbnails)+len(player.OwnedPins))
        for x in player.OwnedThumbnails:
            self.writeVInt(28)
            self.writeVInt(x)
            self.writeVInt(0)
        for x in player.OwnedPins:
            self.writeVInt(52)
            self.writeVInt(x)
            self.writeVInt(0)


        self.writeBoolean(False) # Power league season data

        self.writeInt(0)
        self.writeVInt(0)
        self.writeVInt(16)
        self.writeVInt(76)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(2023189)

        self.writeVInt(35) # event slot id
        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(3)
        self.writeVInt(4)
        self.writeVInt(5)
        self.writeVInt(6)
        self.writeVInt(7)
        self.writeVInt(8)
        self.writeVInt(9)
        self.writeVInt(10)
        self.writeVInt(11)
        self.writeVInt(12)
        self.writeVInt(13) 
        self.writeVInt(14)
        self.writeVInt(15)
        self.writeVInt(16)
        self.writeVInt(17)
        self.writeVInt(18) 
        self.writeVInt(19)
        self.writeVInt(20)
        self.writeVInt(21) 
        self.writeVInt(22)
        self.writeVInt(23)
        self.writeVInt(24)
        self.writeVInt(25)
        self.writeVInt(26)
        self.writeVInt(27)
        self.writeVInt(28)
        self.writeVInt(29)
        self.writeVInt(30)
        self.writeVInt(31)
        self.writeVInt(32)
        self.writeVInt(33)
        self.writeVInt(34)
        self.writeVInt(35)

        self.writeVInt(1)

        self.writeVInt(4)
        self.writeVInt(7)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(72292)
        self.writeVInt(10) 
        self.writeDataReference(15, 21) # map id
        self.writeVInt(-1)
        self.writeVInt(2)
        self.writeString("")
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # MapMaker map structure array
        self.writeVInt(0)
        self.writeBoolean(False) # Power League array entry
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeVInt(0) 
        self.writeVInt(0) 
        self.writeVInt(0) 
        self.writeBoolean(False) 

        self.writeVInt(0)
       
        ByteStreamHelper.encodeIntList(self, [20, 35, 75, 140, 290, 480, 800, 1250, 1875, 2800])
        ByteStreamHelper.encodeIntList(self, [30, 80, 170, 360]) # Shop Coins Price
        ByteStreamHelper.encodeIntList(self, [300, 880, 2040, 4680]) # Shop Coins Amount

        self.writeVInt(0) 

        self.writeVInt(1)
        self.writeVInt(41000086) # theme
        self.writeVInt(1)

        self.writeVInt(0) 
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(2)
        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeVInt(1)
        self.writeVInt(-1)
        self.writeVInt(2)
        self.writeVInt(1)
        self.writeVInt(4)

        ByteStreamHelper.encodeIntList(self, [0, 29, 79, 169, 349, 699])
        ByteStreamHelper.encodeIntList(self, [0, 160, 450, 500, 1250, 2500])

        self.writeLong(0, 1) # Player ID

        self.writeVInt(0) # Notification factory
        
        self.writeVInt(1)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0) 
        self.writeVInt(0)
        self.writeBoolean(False) # Login Calendar
        self.writeVInt(0)
        self.writeBoolean(True) # Starr Road
        for i in range(7):
            self.writeVInt(0)

        self.writeVInt(0) # Mastery

        #BattleCard
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)

        self.writeVInt(0) #Brawler's BattleCards

        self.writeVInt(5)
        for i in range(5):
            self.writeDataReference(80, i)
            self.writeVInt(-1)
            self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeInt(0)
        self.writeVInt(0) 
        self.writeVInt(0)
        self.writeVInt(86400*24)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeBoolean(False)

        # end LogicClientHome

        self.writeVLong(player.ID[0], player.ID[1])
        self.writeVLong(player.ID[0], player.ID[1])
        self.writeVLong(player.ID[0], player.ID[1])
        self.writeStringReference(player.Name)
        self.writeBoolean(player.Registered)
        self.writeInt(-1)

        self.writeVInt(17)
        unlocked_brawler = [i['CardID'] for x,i in player.OwnedBrawlers.items()]
        self.writeVInt(len(unlocked_brawler) + 2)
        for x in unlocked_brawler:
            self.writeDataReference(23, x)
            self.writeVInt(-1)
            self.writeVInt(1)

        self.writeDataReference(5, 8)
        self.writeVInt(-1)
        self.writeVInt(player.Coins)

        self.writeDataReference(5, 23)
        self.writeVInt(-1)
        self.writeVInt(player.Blings)

        self.writeVInt(len(player.OwnedBrawlers)) # HeroScore
        for x,i in player.OwnedBrawlers.items():
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(i["Trophies"])

        self.writeVInt(len(player.OwnedBrawlers)) # HeroHighScore
        for x,i in player.OwnedBrawlers.items():
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(i["HighestTrophies"])

        self.writeVInt(0) # Array

        self.writeVInt(0) # HeroPower
        
        self.writeVInt(len(player.OwnedBrawlers)) # HeroLevel
        for x,i in player.OwnedBrawlers.items():
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(i["PowerLevel"]-1)

        self.writeVInt(0) # hero star power gadget and hypercharge

        self.writeVInt(len(player.OwnedBrawlers)) # HeroSeenState
        for x,i in player.OwnedBrawlers.items():
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(2)

        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array

        self.writeVInt(player.Gems) # Diamonds
        self.writeVInt(player.Gems) # Free Diamonds
        self.writeVInt(10) # Player Level
        self.writeVInt(100)
        self.writeVInt(0) # CumulativePurchasedDiamonds or Avatar User Level Tier | 10000 < Level Tier = 3 | 1000 < Level Tier = 2 | 0 < Level Tier = 1
        self.writeVInt(100) # Battle Count
        self.writeVInt(10) # WinCount
        self.writeVInt(80) # LoseCount
        self.writeVInt(50) # WinLooseStreak
        self.writeVInt(20) # NpcWinCount
        self.writeVInt(0) # NpcLoseCount
        self.writeVInt(2) # TutorialState | shouldGoToFirstTutorialBattle = State == 0
        self.writeVInt(12)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)

    def decode(self):
        fields = {}
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24101

    def getMessageVersion(self):
        return self.messageVersion
