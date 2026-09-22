import sys

from parser import load_rules
from analyzer import analyze_rules
from reporter import print_report


def main():

    if len(sys.argv) < 2:

        print("Usage:")
        print("  python main.py <rules_file>")
        return

    filename = sys.argv[1]

    rules = load_rules(filename)

    if not rules:

        print("No valid firewall rules found.")
        return

    results = analyze_rules(rules)

    print_report(rules, results)


if __name__ == "__main__":
    main()