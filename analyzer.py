def analyze_rules(rules):

    results = {
        "overlaps": [],
        "conflicts": [],
        "shadowed": [],
        "redundant": []
    }

    for i in range(len(rules)):

        for j in range(i + 1, len(rules)):

            earlier = rules[i]
            later = rules[j]

            # 1. Check whether rules affect the same traffic
            if earlier.overlaps_with(later):

                results["overlaps"].append((i, j))

                # 2. Different actions = conflict
                if earlier.action != later.action:
                    results["conflicts"].append((i, j))

                # 3. Same behavior = redundant
                elif earlier.is_identical_to(later):
                    results["redundant"].append((i, j))

                # 4. Earlier broader rule completely covers later rule
                if earlier.contains(later):
                    results["shadowed"].append((i, j))

    return results