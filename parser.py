from rules import FirewallRule

def load_rules(filename):
    rules = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            source, port, protocol, action = line.split(",")

            rule = FirewallRule(
                source,
                int(port),
                protocol,
                action
            )

            rules.append(rule)

    return rules