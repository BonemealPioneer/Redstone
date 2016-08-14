from zope.interface import Interface
from zope.interface.declarations import implements

from redstone.packet.IPacketDirection import IPacketDirection
from redstone.packet.IPacketState import IPacketState
from redstone.packet.PacketHandshaking import PacketHandshaking
from redstone.packet.PacketRequest import PacketRequest
from redstone.packet.PacketResponse import PacketResponse
from redstone.packet.PacketPing import PacketPing
from redstone.packet.PacketPong import PacketPong
from redstone.packet.PacketDisconnect import PacketDisconnect
from redstone.packet.PacketLoginStart import PacketLoginStart
from redstone.packet.PacketEncryptionRequest import PacketEncryptionRequest
from redstone.packet.PacketEncryptionResponse import PacketEncryptionResponse
from redstone.packet.PacketLoginSuccess import PacketLoginSuccess
from redstone.packet.PacketSetCompression import PacketSetCompression

class IPacketDispatcher(object):
    """
    Dispatches packets acording to their packet_id and the handler interface
    """

    implements(Interface)

    # call init on the classes to pre-load the handlers.
    packet_handlers = {
        IPacketDirection.downstream: {
            IPacketState.CONNECTION_STATE_HANDSHAKING: {
                PacketHandshaking.PACKET_ID: PacketHandshaking(),
            },
            IPacketState.CONNECTION_STATE_STATUS: {
                PacketRequest.PACKET_ID: PacketRequest(),
                PacketPing.PACKET_ID: PacketPing(),
            },
            IPacketState.CONNECTION_STATE_PLAY: {
            },
            IPacketState.CONNECTION_STATE_LOGIN: {
                PacketLoginStart.PACKET_ID: PacketLoginStart(),
                PacketEncryptionResponse.PACKET_ID: PacketEncryptionResponse(),
            },
        },
        IPacketDirection.upstream: {
            IPacketState.CONNECTION_STATE_HANDSHAKING: {
            },
            IPacketState.CONNECTION_STATE_STATUS: {
                PacketResponse.PACKET_ID: PacketResponse(),
                PacketPong.PACKET_ID: PacketPong(),
            },
            IPacketState.CONNECTION_STATE_PLAY: {
            },
            IPacketState.CONNECTION_STATE_LOGIN: {
                PacketDisconnect.PACKET_ID: PacketDisconnect(),
                PacketEncryptionRequest.PACKET_ID: PacketEncryptionRequest(),
                PacketLoginSuccess.PACKET_ID: PacketLoginSuccess(),
                PacketSetCompression.PACKET_ID: PacketSetCompression(),
            },
        }
    }

    def __init__(self, protocol):
        super(IPacketDispatcher, self).__init__()

        self.protocol = protocol

    def packet_handle_exists(self, packet_id, direction, connection_state):
        """
        Checks if the packet_id exists in packet_handlers
        """

        if packet_id in self.packet_handlers[direction][connection_state].keys():
            return True

        return False

    def dispatch_packet(self, direction, connection_state, packet_id, data_buffer):
        """
        Dispatches packet acording to packet_handlers
        """

        if connection_state not in self.packet_handlers[direction]:
            self.discard_packet(packet_id)
            return

        if not self.packet_handle_exists(packet_id, direction, connection_state):
            self.discard_packet(packet_id)
            return

        # custom handle for handshaking connection state including the packet_id.
        if connection_state is IPacketState.CONNECTION_STATE_HANDSHAKING:
            self.packet_handlers[direction][connection_state][packet_id].deserialize( \
                self.protocol, packet_id, data_buffer)
            
            return

        self.packet_handlers[direction][connection_state][packet_id].deserialize( \
            self.protocol, data_buffer)

    def discard_packet(self, packet_id):
        """
        Discards unused packets by packet_id
        """

        systemLogger.log_debug('Failed to handle packet with id: %d!' % packet_id)