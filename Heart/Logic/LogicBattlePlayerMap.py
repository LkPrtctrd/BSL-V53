from Heart.ByteStreamHelper import ByteStreamHelper
from Heart.Logic.LogicLong import LogicLong

class LogicBattlePlayerMap:
    def decode(bytestream, fields):
        battleMap = fields["Map"][0]
        fields["MapID"] = LogicLong()
        ByteStreamHelper.decodeLogicLong(self, fields["MapID"])
        #fields[""]