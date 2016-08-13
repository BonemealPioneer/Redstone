from redstone.packet.IPacketMessage import IPacketMessage

class PacketSetCompression(IPacketMessage):
    """
    A packet handler that handles set compression for a compressed buffer
    """

    PACKET_ID = 0x03

    def __init__(self):
        IPacketMessage.__init__(self)

    def serialize(self):
        pass

    def deserialize(self, protocol, data_buffer):
        pass