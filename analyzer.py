def analyze_rules(rules):

    conflicts = []
    overlaps = []
    shadowed = []
    redundant = []

    for i in range(len(rules)):

        for j in range(i + 1, len(rules)):

            rule1 = rules[i]
            rule2 = rules[j]

            if rule1.overlaps_with(rule2):

                overlaps.append((i, j))

                if rule1.action != rule2.action:

                    conflicts.append((i, j))

                else:

                    if rule1.source == rule2.source:
                        redundant.append((i, j))

                if is_shadowed(rule1, rule2):

                    shadowed.append((i, j))

    return conflicts, overlaps, shadowed, redundant

def is_shadowed(previous_rule, current_rule):

    source_covered = current_rule.source.subnet_of(previous_rule.source)

    same_port = current_rule.port == previous_rule.port
    same_protocol = current_rule.protocol == previous_rule.protocol

    return source_covered and same_port and same_protocol