def print_header():

    print("=" * 60)
    print("                    NETFORGE")
    print("        Firewall Rule Analysis System")
    print("=" * 60)
    print()


def print_summary(rules, results):

    print(f"Rules analyzed : {len(rules)}")
    print(f"Overlaps       : {len(results['overlaps'])}")
    print(f"Conflicts      : {len(results['conflicts'])}")
    print(f"Shadowed       : {len(results['shadowed'])}")
    print(f"Redundant      : {len(results['redundant'])}")
    print()


def print_relationship(title, pairs, rules):

    print(f"--- {title} ---")

    if not pairs:
        print("None detected.")
        print()
        return

    for i, j in pairs:

        print(f"Rule {i + 1} <-> Rule {j + 1}")
        print(f"  Rule {i + 1}: {rules[i]}")
        print(f"  Rule {j + 1}: {rules[j]}")
        print()


def print_report(rules, results):

    print_header()
    print_summary(rules, results)

    print_relationship(
        "CONFLICTS",
        results["conflicts"],
        rules
    )

    print_relationship(
        "SHADOWED RULES",
        results["shadowed"],
        rules
    )

    print_relationship(
        "REDUNDANT RULES",
        results["redundant"],
        rules
    )