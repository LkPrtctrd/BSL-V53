import json
import random
import string


class Player:
    ClientVersion = "0.0.0"

    ID = [0, 1]
    Token = ""
    Name = "Brawler"
    Registered = False
    Thumbnail = 0
    Namecolor = 0
    Region = "RU"
    ContentCreator = "BSL-V53"

    Coins = 99999
    Gems = 99999
    Blings = 0
    Trophies = 50000
    HighestTrophies = 50000
    TrophyRoadTier = 334
    Experience = 99999
    Level = 500
    Tokens = 200
    TokensDoubler = 1000

    SelectedSkins = {}
    SelectedBrawlers = [76, 76, 76]
    RandomizerSelectedSkins = []
    OwnedPins = []
    OwnedThumbnails = []
    OwnedSkins = []
    OwnedBrawlers = {
        0: {'CardID': 0, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        1: {'CardID': 4, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        2: {'CardID': 8, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        3: {'CardID': 12, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        4: {'CardID': 16, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        5: {'CardID': 20, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        6: {'CardID': 24, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        7: {'CardID': 28, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        8: {'CardID': 32, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        9: {'CardID': 36, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        10: {'CardID': 40, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        11: {'CardID': 44, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        12: {'CardID': 48, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        13: {'CardID': 52, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        14: {'CardID': 56, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        15: {'CardID': 60, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        16: {'CardID': 64, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        17: {'CardID': 68, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        18: {'CardID': 72, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        19: {'CardID': 95, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        20: {'CardID': 100, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        21: {'CardID': 105, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        22: {'CardID': 110, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        23: {'CardID': 115, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        24: {'CardID': 120, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        25: {'CardID': 125, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        26: {'CardID': 130, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        27: {'CardID': 177, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        28: {'CardID': 182, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        29: {'CardID': 188, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        30: {'CardID': 194, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        31: {'CardID': 200, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        32: {'CardID': 206, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        34: {'CardID': 218, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        35: {'CardID': 224, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        36: {'CardID': 230, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        37: {'CardID': 236, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        38: {'CardID': 279, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        39: {'CardID': 296, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        40: {'CardID': 303, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        41: {'CardID': 320, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        42: {'CardID': 327, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        43: {'CardID': 334, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        44: {'CardID': 341, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        45: {'CardID': 358, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        46: {'CardID': 365, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        47: {'CardID': 372, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        48: {'CardID': 379, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        49: {'CardID': 386, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        50: {'CardID': 393, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        51: {'CardID': 410, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        52: {'CardID': 417, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        53: {'CardID': 427, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        54: {'CardID': 434, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        56: {'CardID': 448, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        57: {'CardID': 466, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        58: {'CardID': 474, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        59: {'CardID': 491, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        60: {'CardID': 499, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        61: {'CardID': 507, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        62: {'CardID': 515, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        63: {'CardID': 523, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        64: {'CardID': 531, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        65: {'CardID': 539, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        66: {'CardID': 547, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        67: {'CardID': 557, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        68: {'CardID': 565, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        69: {'CardID': 573, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        70: {'CardID': 581, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        71: {'CardID': 589, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        72: {'CardID': 597, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        73: {'CardID': 605, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        74: {'CardID': 619, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        75: {'CardID': 633, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        76: {'CardID': 642, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
        77: {'CardID': 655, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 1},
    }

    def __init__(self):
        pass

    def getDataTemplate(self, highid, lowid, token):
        if highid == 0 or lowid == 0:
            self.ID[0] = int(''.join([str(random.randint(0, 9)) for _ in range(1)]))
            self.ID[1] = int(''.join([str(random.randint(0, 9)) for _ in range(8)]))
            self.Token = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(40))
        else:
            self.ID[0] = highid
            self.ID[1] = lowid
            self.Token = token

        DBData = {
            'ID': self.ID,
            'Token': self.Token,
            'Name': self.Name,
            'Registered': self.Registered,
            'Thumbnail': self.Thumbnail,
            'Namecolor': self.Namecolor,
            'Region': self.Region,
            'ContentCreator': self.ContentCreator,
            'Coins': self.Coins,
            'Gems': self.Gems,
            'Blings': self.Blings,
            'Trophies': self.Trophies,
            'HighestTrophies': self.HighestTrophies,
            'TrophyRoadTier': self.TrophyRoadTier,
            'Experience': self.Experience,
            'Level': self.Level,
            'Tokens': self.Tokens,
            'TokensDoubler': self.TokensDoubler,
            'SelectedBrawlers': self.SelectedBrawlers,
            'OwnedPins': self.OwnedPins,
            'OwnedThumbnails': self.OwnedThumbnails,
            'OwnedBrawlers': self.OwnedBrawlers,
            'OwnedSkins': self.OwnedSkins,
        }
        return DBData

    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4))