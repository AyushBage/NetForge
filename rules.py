import ipaddress


class FirewallRule:

    def __init__(self, source, port, protocol, action):
        self.source = ipaddress.ip_network(source)
        self.port = int(port)
        self.protocol = protocol.upper()
        self.action = action.upper()

    def overlaps_with(self, other):
        return (
            self.source.overlaps(other.source)
            and self.port == other.port
            and self.protocol == other.protocol
        )

    def contains(self, other):
        return (
            other.source.subnet_of(self.source)
            and self.port == other.port
            and self.protocol == other.protocol
        )

    def is_identical_to(self, other):
        return (
            self.source == other.source
            and self.port == other.port
            and self.protocol == other.protocol
            and self.action == other.action
        )

    def __str__(self):
        return (
            f"{self.source} | "
            f"{self.port} | "
            f"{self.protocol} | "
            f"{self.action}"
        )