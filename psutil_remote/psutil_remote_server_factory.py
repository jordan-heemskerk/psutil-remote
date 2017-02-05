from autobahn.twisted.websocket import WebSocketServerFactory
from twisted.internet import reactor
from psutil_json_wrapper import PsutilJsonWrapper

import logging

logger = logging.getLogger(__name__)


class PsutilRemoteServerFactory(WebSocketServerFactory):

    def __init__(self, *args, **kwargs):

        super(PsutilRemoteServerFactory, self).__init__(*args, **kwargs)
        self.clients = []
        self.tickcount = 0
        self.psutil_json_wrapper = PsutilJsonWrapper()

        self.tick()

    def tick(self):
        self.tickcount += 1
        self.broadcast(self.psutil_json_wrapper.dumps())
        reactor.callLater(1, self.tick)

    def register(self, client):
        if client not in self.clients:
            logger.info("Register client: {}".format(client.peer))
            self.clients.append(client)

    def unregister(self, client):
        if client in self.clients:
            logger.info("Unregister client: ".format(client.peer))
            self.clients.remove(client)

    def broadcast(self, msg):
        if len(self.clients) > 0:
            logger.debug("broadcasting... {}".format(msg))
            for c in self.clients:
                c.sendMessage(msg.encode('utf-8'))
                logger.info("sent message to {}".format(c.peer))
