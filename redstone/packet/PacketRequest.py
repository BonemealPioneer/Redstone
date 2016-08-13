from redstone.packet.IPacketMessage import IPacketMessage
from redstone.packet.PacketResponse import PacketResponse

class PacketRequest(IPacketMessage):
    """
    A packet handler that handles server status query
    """

    PACKET_ID = 0x00

    def __init__(self):
        IPacketMessage.__init__(self)

    def serialize(self):
        pass

    def deserialize(self, protocol, data_buffer):
        protocol.append_send_packet(
            *PacketResponse().serialize())