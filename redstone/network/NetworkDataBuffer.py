from struct import pack, unpack_from, calcsize
from json import dumps, loads

class NetworkDataBuffer(object):
    """
    A class that manages and stores data in ram and is non-persistant
    """

    def __init__(self, data=None):
        super(NetworkDataBuffer, self).__init__()

        if not data:
            self._buffer = b''
        else:
            self._buffer = data

        self._offset = 0

    def add_raw_bytes(self, bytes):
        self._buffer += bytes

    def add_offset(self, offset):
        self._offset += offset

    def get_buffer(self):
        return self._buffer

    def set_buffer(self, buffer):
        self._buffer = buffer

    def get_offset(self):
        return self._offset

    def set_offset(self, offset):
        self._offset = offset

    def read_from(self, length=-1):
        return self.get_buffer()[self.get_offset():][:length]

    def write_bytes(self, fmt, *args):
        return pack('%s' % (fmt), *args)

    def read_bytes(self, fmt):
        unpacked_bytes = unpack_from('%s' % (fmt), self.get_buffer(), self.get_offset())
        self.add_offset(calcsize('%s' % fmt))
        return unpacked_bytes

    def get_length(self):
        return len(self.get_buffer())

    def get_remaining_size(self):
        return len(self.get_buffer()[self.get_offset():])

    def get_remaining_bytes(self):
        return self.get_buffer()[self.get_offset():]

    def write_boolean(self, value):
        self.add_raw_bytes(self.write_bytes('>?', value))

    def read_boolean(self):
        return self.read_bytes('>?')[0]

    def write_byte(self, value):
        self.add_raw_bytes(self.write_bytes('>b', value))

    def read_byte(self):
        return self.read_bytes('>b')[0]

    def write_ubyte(self, value):
        self.add_raw_bytes(self.write_bytes('>B', value))

    def read_ubyte(self):
        return self.read_bytes('>B')[0]

    def write_short(self, value):
        self.add_raw_bytes(self.write_bytes('>h', value))

    def read_short(self):
        return self.read_bytes('>h')[0]

    def write_ushort(self, value):
        self.add_raw_bytes(self.write_bytes('>H', value))

    def read_ushort(self):
        return self.read_bytes('>H')[0]

    def write_int(self, value):
        self.add_raw_bytes(self.write_bytes('>i', value))

    def read_int(self):
        return self.read_bytes('>i')[0]

    def write_long(self, value):
        self.add_raw_bytes(self.write_bytes('>q', value))

    def read_long(self):
        return self.read_bytes('>q')[0]

    def write_float(self, value):
        self.add_raw_bytes(self.write_bytes('>f', value))

    def read_float(self):
        return self.read_bytes('>f')[0]

    def write_double(self, value):
        self.add_raw_bytes(self.write_bytes('>d', value))

    def read_double(self):
        return self.read_bytes('>d')[0]

    def read_string(self):
        return ''.join([self.read_bytes('>s')[0] for _ in xrange(self.read_varint())])

    def write_string(self, string):
        self.add_raw_bytes(self.write_varint(len(string)) + string.encode('utf-8'))

    def write_json_object(self, json_object):
        self.write_string(dumps(json_object))

    def write_byte_array(self, byte_array):
        self.add_raw_bytes(self.write_varint(len(byte_array)) + bytes(byte_array))

    def read_byte_array(self):
        byte_array = []

        for _ in xrange(self.read_varint()):
            byte_array.append(self.read_from(self.get_offset() + 1))
            self.add_offset(self._offset + 1)

        return b''.join(byte_array)

    def write_varint(self, value):
        result = []
        
        while True:
            towrite = value & 0x7F
            value >>= 7

            if not value:
                result.append(self.write_bytes('<B', towrite))
                break
            
            result.append(self.write_bytes('<B', towrite | 0x80))

        return b''.join(result)

    def read_varint(self):
        shift = 0
        result = 0
        
        while True:
            i = self.read_bytes('<B')[0]
            result |= (i & 0x7F) << shift
            shift += 7
            
            if not (i & 0x80):
                break

        return result