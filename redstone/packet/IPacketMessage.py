from zope.interface import Interface
from zope.interface.declarations import implements
from redstone.network.NetworkDataBuffer import NetworkDataBuffer

class IPacketMessage(object):
    """
    Base class of every packet handler
    """

    implements(Interface)

    PACKET_ID = None

    def __init__(self):
        pass

    def serialize(self):
        pass

    def deserialize(self, protocol, data_buffer):
        pass