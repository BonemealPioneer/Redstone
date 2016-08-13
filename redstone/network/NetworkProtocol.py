from twisted.internet.protocol import Protocol
from redstone.network.NetworkDataBuffer import NetworkDataBuffer
from redstone.packet.IPacketDispatcher import IPacketDispatcher
from redstone.packet.IPacketDirection import IPacketDirection
from redstone.packet.IPacketState import IPacketState

class NetworkProtocol(Protocol):
    """
    Class for operating to the client using the protocol
    """

    CONNECTION_STATE = IPacketState.CONNECTION_STATE_HANDSHAKING

    def __init__(self):
        self.packet_interface = IPacketDispatcher(self)
        self.is_authenicated = False

    def set_is_authenicated(self, is_authenicated):
        self.is_authenicated = is_authenicated

    def get_is_authenicated(self):
        return self.is_authenicated

    def append_send_packet(self, packet_id, data_buffer):
        if not data_buffer.get_remaining_size():
            return

        # check if the packet_id is actually sendable in the current state.
        if packet_id not in self.packet_interface.packet_handlers[IPacketDirection.upstream][ \
            self.CONNECTION_STATE].keys():

            return

        self.send_packet(packet_id, data_buffer)

    def send_packet(self, packet_id, _data_buffer):
        data_buffer = NetworkDataBuffer()
        data_buffer.write_varint(_data_buffer.get_length() + 1)
        data_buffer.write_varint(packet_id)
        data_buffer.set_buffer(data_buffer.get_buffer() + _data_buffer.get_buffer())
        self.transport.write(data_buffer.get_buffer())

    def connectionMade(self):
        self.factory.register_protocol(self)

    def dataReceived(self, data):
        data_buffer = NetworkDataBuffer(data)

        if data_buffer.get_remaining_size() == 0:
            self.disconnect()
            return

        try:
            packet_length = data_buffer.read_varint()
        except:
            self.disconnect()
            return

        if not packet_length:
            self.disconnect()
            return

        # construct a new data buffer with the contents acording to packet_length.
        data_buffer = NetworkDataBuffer(
            data_buffer.read_from(packet_length))

        if data_buffer.get_remaining_size() == 0:
            self.disconnect()
            return

        try:
            packet_id = data_buffer.read_varint()
        except:
            self.disconnect()
            return

        if data_buffer.get_remaining_size() == 0:
            self.disconnect()
            return

        # handle the packet acording to the packet_id.
        self.handle_packet(IPacketDirection.downstream, self.CONNECTION_STATE, 
            packet_id, data_buffer)

    def handle_packet(self, direction, connection_state, packet_id, data_buffer):
        self.packet_interface.dispatch_packet(direction, connection_state, packet_id, data_buffer)

    def disconnect(self):
        self.transport.loseConnection()

    def connectionLost(self, reason):
        self.factory.unregister_protocol(self)