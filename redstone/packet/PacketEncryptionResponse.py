from redstone.packet.IPacketMessage import IPacketMessage

class PacketEncryptionResponse(IPacketMessage):
    """
    A packet handler that recieves encryption response from the client
    """

    PACKET_ID = 0x01

    def __init__(self):
        IPacketMessage.__init__(self)

    def serialize(self):
        pass

    def deserialize(self, protocol, data_buffer):
        pass