from rules import FirewallRule


def load_rules(filename):

    rules = []

    with open(filename, "r") as file:

        for line_number, line in enumerate(file, start=1):

            line = line.strip()

            if not line:
                continue

            if line.startswith("#"):
                continue

            parts = line.split(",")

            if len(parts) != 4:
                print(
                    f"Warning: Invalid rule on line {line_number}"
                )
                continue

            source, port, protocol, action = parts

            try:

                rule = FirewallRule(
                    source.strip(),
                    port.strip(),
                    protocol.strip(),
                    action.strip()
                )

                rules.append(rule)

            except ValueError:

                print(
                    f"Warning: Could not parse rule "
                    f"on line {line_number}"
                )

    return rules