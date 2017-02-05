import logging

from autobahn.twisted.websocket import WebSocketServerProtocol

logger = logging.getLogger(__name__)


class PsutilRemoteServerProtocol(WebSocketServerProtocol):

    def onConnect(self, request):
        logger.info("Client connecting: {}".format(request.peer))

    def onOpen(self):
        logger.info("Opening connection")
        self.factory.register(self)

    def onClose(self, wasClean, code, reason):
        logger.info("Closing connection: {}".format(reason))
        self.factory.unregister(self)
