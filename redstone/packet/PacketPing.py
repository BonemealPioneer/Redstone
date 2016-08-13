from redstone.packet.IPacketMessage import IPacketMessage
from redstone.packet.PacketPong import PacketPong
from callbacks import supports_callbacks

class PacketPing(IPacketMessage):
    """
    A packet handler that handles ping and pong, server latency
    """

    PACKET_ID = 0x01

    def __init__(self):
        IPacketMessage.__init__(self)

    def serialize(self):
        pass

    def deserialize(self, protocol, data_buffer):
        timestamp = data_buffer.read_long()

        if not timestamp:
            return

        protocol.append_send_packet(
            *PacketPong().serialize(timestamp))

        # done, close the connection.
        protocol.disconnect()