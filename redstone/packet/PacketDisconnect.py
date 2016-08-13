from redstone.packet.IPacketMessage import IPacketMessage

class PacketDisconnect(IPacketMessage):
    """
    A packet handler that sends disconnect to the client as a chat message
    """

    PACKET_ID = 0x00

    def __init__(self):
        IPacketMessage.__init__(self)

    def serialize(self):
        pass

    def deserialize(self, protocol, data_buffer):
        pass