import traceback

class Messaging:
    def writeHeader(message, payloadLen):
        message.messageBuffer += message.getMessageType().to_bytes(2, 'big', signed=True)
        message.messageBuffer += payloadLen.to_bytes(3, 'big', signed=True)
        message.messageBuffer += message.messageVersion.to_bytes(2, 'big', signed=True)

    def readHeader(headerBytes):
        headerData = []
        headerData.append(int.from_bytes(headerBytes[:2], 'big', signed=True))
        headerData.append(int.from_bytes(headerBytes[2:5], 'big', signed=True))
        return headerData

    def sendMessage(messageType, fields, cryptoInit,  player=None):
        from Heart.Logic.LogicLaserMessageFactory import LogicLaserMessageFactory
        message = LogicLaserMessageFactory.createMessageByType(messageType, b'')
        if player is not None:
            message.encode(fields, player)
        else:
            message.encode(fields)
        message.messagePayload = cryptoInit.encryptServer(message.getMessageType(), message.messagePayload)
        Messaging.writeHeader(message, len(message.messagePayload))
        message.messageBuffer += message.messagePayload
        try:
            fields["Socket"].send(message.messageBuffer)
        except Exception:
            print(traceback.format_exc())

class MessageManager:
    def receiveMessage(self, messageType, messagePayload, cryptoInit):
        from Heart.Logic.LogicLaserMessageFactory import LogicLaserMessageFactory
        message = LogicLaserMessageFactory.createMessageByType(messageType, messagePayload)
        if message is not None:
            try:
                if message.isServerToClient():
                    message.encode()
                else:
                    message.fields = message.decode()
                    message.execute(self, message.fields, cryptoInit)

            except Exception:
                print(traceback.format_exc())
        if messageType > 10100:
            Messaging.sendMessage(23457, {"Socket": self.client}, cryptoInit, self.player)