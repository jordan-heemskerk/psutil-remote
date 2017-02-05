import time
import threading
import logging

from autobahn.twisted.websocket import WebSocketServerProtocol

logger = logging.getLogger(__name__)


class PsutilRemoteServerProtocol(WebSocketServerProtocol):

    def onConnect(self, request):
        logger.info("Client connecting: {}".format(request.peer))

    def onOpen(self):
        logger.info("Opening connection")

        def worker(proto):
            import psutil
            while not proto.signal_worker_stop:
                usage = psutil.cpu_percent(interval=0.1).__repr__()
                proto.sendMessage(usage, isBinary=False)
                time.sleep(1)

        self.signal_worker_stop = False
        self.worker_thread = threading.Thread(target=worker, args=(self,))
        self.worker_thread.start()

    def onClose(self, wasClean, code, reason):
        logger.info("Closing connection: {}".format(reason))
        self.signal_worker_stop = True
        self.worker_thread.join()
