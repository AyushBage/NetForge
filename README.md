# NetForge

NetForge is a lightweight Python command-line tool for reviewing firewall policies before they are deployed. It parses ordered firewall rules, compares their source networks, ports, protocols, and actions, and identifies relationships that may make a policy difficult to reason about.

The project is intended for security engineering education, policy review, and experimentation with deterministic rule analysis. It does not change firewall configurations or apply rules to a production system.

## Capabilities

NetForge currently reports:

- **Overlapping rules:** rules that match some of the same traffic.
- **Conflicting rules:** overlapping rules with different actions, such as `ALLOW` and `DENY`.
- **Shadowed rules:** a later, more specific source network is covered by an earlier rule with the same port and protocol.
- **Redundant rules:** overlapping rules with the same source network, port, protocol, and action.

The analyzer evaluates every rule pair and prints a summary followed by the detected relationships. The result is intended to help an engineer decide whether a policy needs clarification or reordering.

## How It Works

```text
rules.txt
    |
    v
Parser loads and normalizes each rule
    |
    v
Analyzer compares source networks, ports, and protocols
    |
    v
Reporter prints overlaps, conflicts, shadowing, and redundancy
```

IP networks are normalized with Python's standard `ipaddress` library. Two rules overlap only when their source networks overlap and their ports and protocols match. A conflict is an overlap where the actions differ.

## Requirements

- Python 3.8 or later
- No third-party packages

## Quick Start

1. Clone or download the repository.
2. Open a terminal in the project directory.
3. Run the analyzer:

   ```bash
   python main.py
   ```

NetForge reads `rules.txt` from the current directory and writes the analysis to standard output. Run the command from the project root, or update the input path in `main.py` before running it.

## Rule File Format

Each non-empty line in `rules.txt` must contain four comma-separated fields in this order:

```text
source_network,port,protocol,action
```

Example:

```text
192.168.1.0/24,80,TCP,ALLOW
192.168.1.50/32,80,TCP,DENY
10.0.0.0/24,443,TCP,ALLOW
```

Field definitions:

| Field | Description | Example |
| --- | --- | --- |
| `source_network` | IPv4 or IPv6 network in CIDR notation | `192.168.1.0/24` |
| `port` | Destination port represented as an integer | `443` |
| `protocol` | Protocol identifier used for comparison | `TCP` |
| `action` | Policy action used for comparison | `ALLOW` or `DENY` |

The parser skips blank lines. Values are not automatically validated against a fixed protocol or action list, so use consistent uppercase values in policy files.

## Example Analysis

Given these rules:

```text
192.168.1.0/24,80,TCP,ALLOW
192.168.1.50/32,80,TCP,DENY
```

The second source network is contained within the first. Because both rules use port `80` and protocol `TCP`, they overlap. Their different actions make the pair a conflict, and the later rule is reported as shadowed by the earlier broader rule.

The console summary has this general form:

```text
Rules analyzed : 2
Overlaps       : 1
Conflicts      : 1
Shadowed       : 1
Redundant      : 0
```

## Project Structure

```text
NetForge/
|-- analyzer.py   # Compares rules and classifies relationships
|-- main.py       # Command-line entry point
|-- parser.py     # Loads rules from the input file
|-- reporter.py   # Formats individual conflict details
|-- rules.py      # FirewallRule model and network matching logic
|-- rules.txt     # Sample policy input
`-- README.md     # Project documentation
```

## Design Notes

The analyzer uses a pairwise comparison, so its runtime grows approximately with the square of the number of rules. This is appropriate for small and medium policy reviews. Large production policy sets may require indexing or a specialized policy-analysis engine before this tool is used operationally.

NetForge is a review aid, not a complete firewall policy validator. It does not currently parse vendor-specific formats, evaluate stateful firewall behavior, calculate risk scores, or modify policy files. Always validate findings against the semantics of the target firewall and test approved changes in a controlled environment.

## Development

The project has no build step or dependency installation process. A basic smoke test is:

```bash
python main.py
```

When extending the analyzer, keep parsing, rule comparison, and output formatting separated so that each layer can be tested independently.

## License and Use

This project is provided for educational and cybersecurity research purposes. Review and adapt the licensing terms before distributing it as part of a commercial product.