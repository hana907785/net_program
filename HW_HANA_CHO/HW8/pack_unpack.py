import struct

class Udphdr:
    def __init__(self, srcPort, dstPort, length, checksum):
        self.srcPort = srcPort
        self.dstPort = dstPort
        self.length = length
        self.checksum = checksum

    def pack_Udphdr(self):
        packed = struct.pack('!HHHH', self.srcPort, self.dstPort, self.length, self.checksum)
        return packed

def unpack_Udphdr(buffer):
    unpacked = struct.unpack('!HHHH', buffer[:8])
    return unpacked

def getSrcPort(unpacked_udpheader):
    return unpacked_udpheader[0]

def getDstPort(unpacked_udpheader):
    return unpacked_udpheader[1]

def getLength(unpacked_udpheader):
    return unpacked_udpheader[2]

def getChecksum(unpacked_udpheader):
    return unpacked_udpheader[3]

# Test Code
if __name__ == "__main__":
    udp = Udphdr(5555, 80, 1000, 0xFFFF)
    packed_udp = udp.pack_Udphdr()
    print(packed_udp)
    
    unpacked_udp = unpack_Udphdr(packed_udp)
    print(unpacked_udp)
    
    print("Source Port:{} Destination Port:{} Length:{} Checksum:{}".format(
        getSrcPort(unpacked_udp),
        getDstPort(unpacked_udp),
        getLength(unpacked_udp),
        getChecksum(unpacked_udp)
    ))
