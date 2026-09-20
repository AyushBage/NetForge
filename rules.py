import ipaddress

class FirewallRule:
    def __init__(self, source, port, protocol, action):
        # self.source = source
        self.source = ipaddress.ip_network(source)
        self.port = port
        self.protocol = protocol
        self.action = action

    def overlaps_with(self, other):
        same_source = self.source.overlaps(other.source)
        same_port = self.port == other.port
        same_protocol = self.protocol == other.protocol

        return same_source and same_port and same_protocol