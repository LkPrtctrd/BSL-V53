from Heart.Commands.Client.PurchaseOfferCommand import PurchaseOfferCommand
from Heart.Commands.Server.ChangeAvatarNameCommand import ChangeAvatarNameCommand
from Heart.Commands.Client.SetPlayerThumbnailCommand import SetPlayerThumbnailCommand
from Heart.Commands.Client.SetPlayerNameColorCommand import SetPlayerNameColorCommand

class LogicCommandManager:
    commandsList = {
        201: ChangeAvatarNameCommand,
        202: 'DiamondsAddedCommand',
        203: 'GiveDeliveryItemsCommand',
        204: 'DayChangedCommand',
        205: 'DecreaseHeroScoreCommand',
        206: 'AddNotificationCommand',
        207: 'ChangeResourcesCommand',
        208: 'TransactionsRevokedCommand',
        209: 'KeyPoolChangedCommand',
        210: 'IAPChangedCommand',
        211: 'OffersChangedCommand',
        212: 'PlayerDataChangedCommand',
        213: 'InviteBlockingChangedCommand',
        214: 'GemNameChangeStateChangedCommand',
        215: 'SetSupportedCreatorCommand',
        216: 'CooldownExpiredCommand',
        217: 'ProLeagueSeasonChangedCommand',
        218: 'BrawlPassSeasonChangedCommand',
        219: 'BrawlPassUnlockedCommand',
        220: 'HerowinQuestsChangedCommand',
        221: 'TeamChatMuteStateChangedCommand',
        222: 'RankedSeasonChangedCommand',
        223: 'CooldownAddedCommand',
        224: 'SetESportsHubNotificationCommand',
        228: 'RefreshRandomRewardsCommand',
        500: 'GatchaCommand',
        503: 'ClaimDailyRewardCommand',
        504: 'SendAllianceMailCommand',
        505: SetPlayerThumbnailCommand,
        506: 'SelectSkinCommand',
        507: 'UnlockSkinCommand',
        508: 'ChangeControlModeCommand',
        509: 'PurchaseDoubleCoinsCommand',
        511: 'HelpOpenedCommand',
        512: 'ToggleInGameHintsCommand',
        514: 'DeleteNotificationCommand',
        515: 'ClearShopTickersCommand',
        517: 'ClaimRankUpRewardCommand',
        518: 'PurchaseTicketsCommand',
        519: PurchaseOfferCommand,
        520: 'LevelUpCommand',
        521: 'PurchaseHeroLvlUpMaterialCommand',
        522: 'HeroSeenCommand',
        523: 'ClaimAdRewardCommand',
        524: 'VideoStartedCommand',
        525: 'SelectCharacterCommand',
        526: 'UnlockFreeSkinsCommand',
        527: SetPlayerNameColorCommand,
        528: 'ViewInboxNotificationCommand',
        529: 'SelectStarPowerCommand',
        530: 'SetPlayerAgeCommand',
        531: 'CancelPurchaseOfferCommand',
        532: 'ItemSeenCommand',
        533: 'QuestSeenCommand',
        534: 'PurchaseBrawlPassCommand',
        535: 'ClaimTailRewardCommand',
        536: 'PurchaseBrawlpassProgressCommand',
        537: 'VanityItemSeenCommand',
        538: 'SelectEmoteCommand',
        539: 'BrawlPassAutoCollectWarningSeenCommand',
        540: 'PurchaseChallengeLivesCommand',
        541: 'ClearESportsHubNotificationCommand',
        542: 'SelectGroupSkinCommand',
        571: 'OpenRandomCommand'
    }

    def getCommandsName(commandType):
        try:
            command = LogicCommandManager.commandsList[commandType]
        except KeyError:
            command = str(commandType)
        if type(command) == str:
            return command
        else:
            return command.__name__

    def commandExist(commandType):
        return (commandType in LogicCommandManager.commandsList.keys())

    def createCommand(commandType, commandPayload=b''):
        commandList = LogicCommandManager.commandsList
        if LogicCommandManager.commandExist(commandType):
            print(LogicCommandManager.getCommandsName(commandType), "created")
            if type(commandList[commandType]) == str:
                pass
            else:
                return commandList[commandType](commandPayload)
        else:
            print(commandType, "skipped")
            return None

    def isServerToClient(commandType):
        if 200 <= commandType < 500:
            return True
        elif 500 <= commandType:
            return False
