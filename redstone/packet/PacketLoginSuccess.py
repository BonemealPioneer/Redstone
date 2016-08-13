from redstone.packet.IPacketMessage import IPacketMessage

class PacketLoginSuccess(IPacketMessage):
    """
    A packet handler that handles login success; user authenicated
    """

    PACKET_ID = 0x02

    def __init__(self):
        IPacketMessage.__init__(self)

    def serialize(self):
        pass

    def deserialize(self, protocol, data_buffer):
        pass