from redstone.packet.IPacketMessage import IPacketMessage
from redstone.network.NetworkDataBuffer import NetworkDataBuffer

class PacketResponse(IPacketMessage):
    """
    A packet handler that handles server status query
    """

    PACKET_ID = 0x00

    def __init__(self):
        IPacketMessage.__init__(self)

    def serialize(self):
        response = {}
        response['version'] = {}
        response['version']['name'] = '1.10.2'
        response['version']['protocol'] = 210
        response['players'] = {}
        response['players']['max'] = 50
        response['players']['online'] = 0
        response['players']['sample'] = []
        response['description'] = {}
        response['description']['text'] = 'A Redstone Minecraft Server!'

        data_buffer = NetworkDataBuffer()
        data_buffer.write_json_object(response)
        return (self.PACKET_ID, data_buffer)

    def deserialize(self, protocol, data_buffer):
        pass