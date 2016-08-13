from redstone.packet.IPacketMessage import IPacketMessage

class PacketEncryptionRequest(IPacketMessage):
    """
    A packet handler that recieves the response in which the client responds with
    """

    PACKET_ID = 0x01

    def __init__(self):
        IPacketMessage.__init__(self)
    
    def serialize(self):
        pass

    def deserialize(self, protocol, data_buffer):
        pass