
class IPacketState(object):
    """
    This serves as an enum for connection state
    """

    CONNECTION_STATE_HANDSHAKING = 0
    CONNECTION_STATE_STATUS = 1
    CONNECTION_STATE_PLAY = 2
    CONNECTION_STATE_LOGIN = 3