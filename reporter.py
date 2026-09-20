def print_conflict(rule1_number, rule2_number, rule1, rule2):

    print("----------------------------------------")
    print("CONFLICT DETECTED")
    print("----------------------------------------")

    print(f"Rule {rule1_number}:")
    print(f"  Source:   {rule1.source}")
    print(f"  Port:     {rule1.port}")
    print(f"  Protocol: {rule1.protocol}")
    print(f"  Action:   {rule1.action}")

    print()

    print(f"Rule {rule2_number}:")
    print(f"  Source:   {rule2.source}")
    print(f"  Port:     {rule2.port}")
    print(f"  Protocol: {rule2.protocol}")
    print(f"  Action:   {rule2.action}")

    print()