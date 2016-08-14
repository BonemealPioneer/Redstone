from redstone.packet.IPacketMessage import IPacketMessage

class PacketLoginStart(IPacketMessage):
    """
    A packet handler that recieves the login start; contains the players username
    """

    PACKET_ID = 0x00

    def __init__(self):
        IPacketMessage.__init__(self)

    def serialize(self):
        pass

    def deserialize(self, protocol, data_buffer):
        if data_buffer.get_remaining_size() == 0:
            return

        player_username = data_buffer.read_string()
        print player_username