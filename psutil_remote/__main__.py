import sys
import logging

from psutil_remote_server_protocol import PsutilRemoteServerProtocol

from autobahn.twisted.websocket import WebSocketServerFactory


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main(args=None):
    """
    The main routine

    :param args: Command line arguments
    :type args: list(str)
    :return: None
    """
    if args is None:
        args = sys.argv[1:]

    logger.info("Initializing..")
    from twisted.internet import reactor

    factory = WebSocketServerFactory(u"ws://127.0.0.1:9000")
    factory.protocol = PsutilRemoteServerProtocol
    # factory.setProtocolOptions(maxConnections=2)

    # note to self: if using putChild, the child must be bytes...

    reactor.listenTCP(9000, factory)
    reactor.run()


if __name__ == "__main__":
    main()
