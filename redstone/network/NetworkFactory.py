from twisted.internet import reactor
from twisted.internet.protocol import Factory
from redstone.network.NetworkProtocol import NetworkProtocol
from redstone.util.ObjectListRegistry import ObjectListRegistry

class NetworkFactory(Factory):
    """
    Class as the server factory repository
    """

    protocol = NetworkProtocol

    def __init__(self):
        self.protocols = ObjectListRegistry()

    def startFactory(self):
        pass

    def stopFactory(self):
        pass

    def register_protocol(self, protocol):
        self.protocols.register_object(protocol)

    def unregister_protocol(self, protocol):
        self.protocols.unregister_object(protocol)

    def run_forever(self, port_address):
        reactor.listenTCP(port_address, self)
        reactor.run()