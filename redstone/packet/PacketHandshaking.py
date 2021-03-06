from redstone.packet.IPacketMessage import IPacketMessage
from redstone.packet.IPacketState import IPacketState
from redstone.packet.IPacketDirection import IPacketDirection

class PacketHandshaking(IPacketMessage):
    """
    A packet handler that sends disconnect to the client as a chat message
    """

    PACKET_ID = 0x00

    def __init__(self):
        IPacketMessage.__init__(self)

    def serialize(self):
        pass

    def deserialize(self, protocol, packet_id, data_buffer):
        try:
            protocol_version = data_buffer.read_varint()
            server_address = data_buffer.read_string()
            server_port = data_buffer.read_ushort()
            next_state = data_buffer.read_varint()
        except:
            protocol.disconnect()
            return

        connection_states = [IPacketState.CONNECTION_STATE_HANDSHAKING, IPacketState.CONNECTION_STATE_STATUS, IPacketState.CONNECTION_STATE_PLAY, \
            IPacketState.CONNECTION_STATE_LOGIN]

        if next_state not in connection_states:
            # recieved an invalid state, don't switch target states.
            return
        
        if next_state is IPacketState.CONNECTION_STATE_PLAY:
            if not protocol.get_is_authenicated():
                protocol.CONNECTION_STATE = IPacketState.CONNECTION_STATE_LOGIN

                # sometimes the packets, handshake and login start are as one packet, we need to check and if so
                # just handle the packet normally.
                if not data_buffer.get_remaining_size():
                    return
                
                # works for now...
                protocol.handle_data_recieved(
                    data_buffer.get_remaining_bytes())
                
                return

        protocol.CONNECTION_STATE = next_state

        # handle the indicated packet_id, if one is specified.
        self.dispatched_handle_packet(protocol, packet_id, data_buffer)

    def dispatched_handle_packet(self, protocol, packet_id, data_buffer):
        protocol.handle_packet(IPacketDirection.downstream, protocol.CONNECTION_STATE, packet_id, data_buffer)