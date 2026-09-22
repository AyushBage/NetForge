# NetForge

## Intelligent Firewall Rule Analysis and Conflict Detection System

NetForge is a terminal-based cybersecurity tool designed to analyze firewall rules and identify logical relationships and potential policy issues within a firewall configuration.

The project focuses on detecting:

- Overlapping rules
- Conflicting rules
- Shadowed rules
- Redundant rules

NetForge uses IP network relationships, rule conditions, set-theoretic reasoning, and Boolean logic to analyze firewall policies.

---

## 1. Problem Statement

Firewall configurations can grow significantly over time. As rules are added, modified, or copied, administrators may unintentionally introduce rules that overlap, contradict existing policies, become unreachable due to rule ordering, or provide no additional functionality.

Manually reviewing large rule sets is time-consuming and error-prone.

NetForge addresses this problem by automatically comparing firewall rules and reporting potentially problematic relationships in a readable terminal-based report.

---

## 2. Project Objective

The primary objective of NetForge is to provide a lightweight analysis engine that can:

1. Read firewall rules from a configuration file.
2. Convert the rules into structured objects.
3. Compare rules based on their source network, port, protocol, and action.
4. Identify meaningful relationships between rules.
5. Report detected issues through the terminal.
6. Provide a foundation for future firewall policy optimization.

---

## 3. Current Scope

The current MVP uses the following simplified firewall rule format:

```text
SOURCE,PORT,PROTOCOL,ACTION
```

Example:

```text
192.168.1.0/24,80,TCP,ALLOW
192.168.1.50/32,80,TCP,DENY
```

Each rule contains:

| Field | Description |
|---|---|
| Source | IPv4 network or host represented using CIDR notation |
| Port | Network port associated with the rule |
| Protocol | Network protocol such as TCP or UDP |
| Action | Policy decision such as ALLOW or DENY |

The current version intentionally keeps the rule model simple so that the analysis logic remains easy to understand and extend.

---

## 4. Detection Capabilities

### 4.1 Overlap Detection

Two rules overlap when they apply to some of the same traffic conditions.

For example:

```text
Rule 1:
192.168.1.0/24,80,TCP,ALLOW

Rule 2:
192.168.1.50/32,80,TCP,DENY
```

The host `192.168.1.50` belongs to the `192.168.1.0/24` network, so the rules affect common traffic.

---

### 4.2 Conflict Detection

A conflict occurs when two overlapping rules apply to the same traffic but specify different actions.

Example:

```text
Rule 1 -> ALLOW
Rule 2 -> DENY
```

NetForge reports this relationship as a conflict.

---

### 4.3 Shadowed Rule Detection

For the MVP, NetForge assumes a first-match rule-processing model in which firewall rules are evaluated from top to bottom.

A later rule is considered shadowed when an earlier rule completely covers its relevant traffic conditions.

Example:

```text
Rule 1:
192.168.1.0/24,80,TCP,DENY

Rule 2:
192.168.1.50/32,80,TCP,ALLOW
```

Traffic from `192.168.1.50` matches Rule 1 before reaching Rule 2.

Therefore, Rule 2 may never be applied under the first-match assumption.

---

### 4.4 Redundant Rule Detection

A rule is considered redundant when another rule has the same source, port, protocol, and action.

Example:

```text
Rule 1:
192.168.10.0/24,80,TCP,ALLOW

Rule 2:
192.168.10.0/24,80,TCP,ALLOW
```

The second rule does not introduce new behavior and can therefore be flagged as redundant.

---

## 5. Core Concepts

NetForge applies concepts from discrete structures, networking, and programming.

### Set Theory

IP networks can be treated as sets of addresses.

For example:

```text
192.168.1.50/32 ⊆ 192.168.1.0/24
```

This relationship helps determine whether one firewall rule is contained within another.

### Set Intersection

If two rules apply to a common set of traffic:

```text
Rule A ∩ Rule B ≠ ∅
```

the rules overlap.

### Boolean Logic

A simplified firewall rule can be represented as a combination of conditions:

```text
Source AND Protocol AND Port
```

Two rules can be compared by evaluating whether their conditions describe common traffic.

### Rule Ordering

The order of firewall rules can affect the resulting policy when a first-match model is used.

This is particularly important for shadow detection.

---

## 6. System Architecture

```text
                 rules.txt
                     |
                     v
                +---------+
                | Parser  |
                +----+----+
                     |
                     v
              FirewallRule[]
                     |
                     v
               +----------+
               | Analyzer |
               +----+-----+
                    |
          +---------+---------+
          |         |         |
          v         v         v
       Overlap   Conflict   Shadow
          |         |         |
          +---------+---------+
                    |
                    v
                Redundant
                    |
                    v
               +----------+
               | Reporter |
               +----+-----+
                    |
                    v
              Terminal Report
```

---

## 7. Project Structure

```text
NetForge/
|
├── main.py
├── rules.py
├── parser.py
├── analyzer.py
├── reporter.py
├── rules.txt
├── README.md
|
└── tests/
    └── test_analyzer.py
```

### `main.py`

Application entry point. Loads the rule file, runs the analysis, and displays the report.

### `rules.py`

Contains the `FirewallRule` class and rule-level relationship methods.

### `parser.py`

Reads the firewall rule file and converts each valid line into a `FirewallRule` object.

### `analyzer.py`

Compares firewall rules and identifies overlaps, conflicts, shadowed rules, and redundant rules.

### `reporter.py`

Formats analysis results into a readable terminal report.

### `rules.txt`

Input file containing firewall rules.

### `tests/`

Contains automated tests for validating analysis behavior.

---

## 8. Requirements

NetForge currently requires:

- Python 3.10 or later
- No external Python packages for the core MVP

The project uses Python's built-in `ipaddress` module for IPv4 network handling.

---

## 9. Installation

Clone or download the project and navigate into the project directory:

```bash
cd NetForge
```

Verify Python:

```bash
python --version
```

No package installation is required for the current MVP.

---

## 10. Rule File Format

Rules are stored in `rules.txt`.

The format is:

```text
SOURCE,PORT,PROTOCOL,ACTION
```

Example:

```text
# Broad web access
192.168.1.0/24,80,TCP,ALLOW

# Specific host restriction
192.168.1.50/32,80,TCP,DENY

# HTTPS access
10.0.0.0/24,443,TCP,ALLOW
```

Lines beginning with `#` are treated as comments.

Blank lines are ignored.

---

## 11. Running NetForge

Run the analyzer using:

```bash
python main.py rules.txt
```

Example output:

```text
============================================================
                    NETFORGE
        Firewall Rule Analysis System
============================================================

Rules analyzed : 8
Overlaps       : 4
Conflicts      : 2
Shadowed       : 4
Redundant      : 0

--- CONFLICTS ---
Rule 1 <-> Rule 2
  Rule 1: 192.168.1.0/24 | 80 | TCP | ALLOW
  Rule 2: 192.168.1.50/32 | 80 | TCP | DENY
```

---

## 12. Analysis Workflow

NetForge processes rules in the following sequence:

```text
1. Read rule file
        |
2. Validate and parse rules
        |
3. Convert source addresses into IP networks
        |
4. Compare rule pairs
        |
5. Check source network relationships
        |
6. Check port and protocol conditions
        |
7. Identify overlaps
        |
8. Compare actions
        |
9. Identify conflicts
        |
10. Analyze rule ordering
        |
11. Identify shadowed rules
        |
12. Identify redundant rules
        |
13. Generate terminal report
```

---

## 13. Design Assumptions

The current MVP intentionally makes several assumptions:

1. Rules contain one source network, one port, one protocol, and one action.
2. IPv4 is supported.
3. The firewall uses a first-match rule-processing model for shadow analysis.
4. Port ranges are not currently supported.
5. Destination IP addresses are not currently modeled.
6. Source ports are not currently modeled.
7. `ANY` or wildcard values are not currently supported.
8. Vendor-specific firewall syntax is not currently supported.

These limitations define the scope of the MVP and provide clear directions for future development.

---

## 14. Future Scope

Potential improvements include:

### Rule Model

- Destination IP/network
- Source ports
- Destination ports
- Port ranges
- Multiple protocols
- Wildcard and `ANY` conditions
- IPv6 support
- Rule priorities

### Analysis Engine

- More precise shadow detection
- Advanced redundancy detection
- Rule reachability analysis
- Policy optimization
- Risk classification
- Detailed reasoning for each finding

### Input Support

Support for common firewall configuration formats such as:

- Linux iptables
- nftables
- Cisco ACLs
- Windows Firewall rules
- Other vendor-specific formats

### Visualization

A future version could represent relationships as a graph:

```text
Rule 1 ---- CONFLICT ---- Rule 5
  |
  |
SHADOWS
  |
  v
Rule 8
```

### Advanced Features

- Automatic rule-order recommendations
- Firewall policy cleanup suggestions
- Configuration comparison
- Security policy auditing
- AI-assisted explanations
- Exportable analysis reports

---

## 15. Testing Strategy

NetForge should be tested against known rule relationships.

Important test cases include:

| Scenario | Expected Result |
|---|---|
| Same source, port, protocol, different actions | Conflict |
| Contained network, same conditions | Overlap |
| Earlier broad rule covers later specific rule | Shadowed |
| Identical rules | Redundant |
| Same network but different ports | No overlap |
| Same network and port but different protocols | No overlap |
| Different networks | No overlap |

Automated tests should be added as the analysis engine becomes more sophisticated.

---

## 16. Security and Project Scope

NetForge is an analysis and research tool. It does not directly modify firewall configurations or block network traffic.

Its purpose is to inspect firewall policy logic and help identify potentially problematic relationships before an administrator applies or maintains a configuration.

The tool should therefore be treated as an analysis aid rather than a replacement for firewall testing, validation, or production security controls.

---

## 17. Educational Value

NetForge combines practical cybersecurity concepts with programming and discrete mathematics.

The project demonstrates how theoretical concepts can be applied to a real-world security problem:

```text
Set Theory
     +
Boolean Logic
     +
Computer Networking
     +
Object-Oriented Programming
     +
Rule-Based Analysis
     =
NetForge
```

This makes the project useful for understanding both the programming implementation and the reasoning behind firewall policy analysis.

---

## 18. Project Status

Current MVP capabilities:

- [x] Firewall rule representation
- [x] IPv4 network parsing
- [x] CIDR handling
- [x] Rule file parsing
- [x] Rule pair comparison
- [x] Overlap detection
- [x] Conflict detection
- [x] Shadow detection
- [x] Redundancy detection
- [x] Terminal reporting

Planned improvements:

- [ ] More precise rule semantics
- [ ] Destination network support
- [ ] Port ranges
- [ ] Wildcard conditions
- [ ] Automated test suite
- [ ] Risk classification
- [ ] Detailed recommendations
- [ ] Multi-format firewall support
- [ ] Rule optimization

---

## 19. License

This project is developed for educational and cybersecurity research purposes.

If distributed publicly, a formal open-source license such as MIT can be added to the repository.
