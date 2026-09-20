# from rules import FirewallRule
from parser import load_rules
from reporter import print_conflict
from analyzer import analyze_rules

# rule1 = FirewallRule(
#     "192.168.1.0/24",
#     80,
#     "TCP",
#     "ALLOW"
# )

# rule2 = FirewallRule(
#     "192.168.1.50/32",
#     80,
#     "TCP",
#     "DENY"
# )

rules = load_rules("rules.txt")


# if rule1.overlaps_with(rule2):

#     print("Rules overlap!")

#     if rule1.action != rule2.action:
#         print("Conflict detected!")
#     else:
#         print("No conflict.")

# else:

#     print("Rules do not overlap.")

conflicts, overlaps, shadowed, redundant = analyze_rules(rules)

print("=" * 50)
print("                 NETFORGE")
print("       Firewall Rule Analysis System")
print("=" * 50)
print()

print(f"Rules analyzed : {len(rules)}")
print(f"Overlaps       : {len(overlaps)}")
print(f"Conflicts      : {len(conflicts)}")
print(f"Shadowed       : {len(shadowed)}")
print(f"Redundant      : {len(redundant)}")

print()

print("\n--- CONFLICTS ---")

for i, j in conflicts:

    print(f"Rule {i + 1} <-> Rule {j + 1}")

    print(f"  Rule {i + 1}: {rules[i].action}")
    print(f"  Rule {j + 1}: {rules[j].action}")

    print()

print("\n--- SHADOWED RULES ---")

for i, j in shadowed:

    print(f"Rule {j + 1} is shadowed by Rule {i + 1}")

print("\n--- REDUNDANT RULES ---")

for i, j in redundant:

    print(f"Rule {j + 1} is redundant with Rule {i + 1}")

# for i in range(len(rules)):

#     for j in range(i + 1, len(rules)):

#         rule1 = rules[i]
#         rule2 = rules[j]

#         if rule1.overlaps_with(rule2):

#             if rule1.action != rule2.action:

#                 print_conflict(
#                     i + 1,
#                     j + 1,
#                     rule1,
#                     rule2
#                 )