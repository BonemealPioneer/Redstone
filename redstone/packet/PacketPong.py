from redstone.packet.IPacketMessage import IPacketMessage
from redstone.network.NetworkDataBuffer import NetworkDataBuffer

class PacketPong(IPacketMessage):
    """
    A packet handler that handles ping and pong, server latency
    """

    PACKET_ID = 0x01

    def __init__(self):
        IPacketMessage.__init__(self)

    def serialize(self, timestamp):
        data_buffer = NetworkDataBuffer()
        data_buffer.write_long(timestamp)
        return (self.PACKET_ID, data_buffer)

    def deserialize(self, protocol, data_buffer):
        pass