from twisted.internet import reactor
from twisted.internet.protocol import Factory
from redstone.network.NetworkProtocol import NetworkProtocol
from callbacks import supports_callbacks

class NetworkFactory(Factory):
    """
    Class as the server factory repository
    """

    reactor = reactor
    protocol = NetworkProtocol

    def __init__(self):
        self.protocols = []

    @supports_callbacks
    def startFactory(self):
        self.startFactory.add_callback(self.startupDone)
        systemLogger.log_info('Starting Redstone minecraft server...')

    def startupDone(self):
        systemLogger.log_info('Server initialized, waiting for connections.')

    def stopFactory(self):
        pass

    def register_protocol(self, protocol):
        if protocol not in self.protocols:
            self.protocols.append(protocol)

    def unregister_protocol(self, protocol):
        if protocol in self.protocols:
            self.protocols.remove(protocol)

    def broadcast_packet(self, packet_id, data_buffer):
        for protocol in self.protocols:

            # ensure the client is capable of recieving other updates.
            if not protocol.get_is_authenicated():
                return

            # make sure the client can actually send this packet, before sending it.
            protocol.append_send_packet(packet_id, data_buffer)

    def run_forever(self, port_address):
        self.reactor.listenTCP(port_address, self)
        self.reactor.run()