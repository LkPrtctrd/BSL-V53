from Logic.Data.DataManager import Writer

class ListBrawlTvChannelsMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24700
        self.client = client
        self.player = player

    def encode(self):
        self.writeVint(1) # count
        
        self.writeVint(1)
        self.writeString("hacc")
        self.writeString("hacc2")

