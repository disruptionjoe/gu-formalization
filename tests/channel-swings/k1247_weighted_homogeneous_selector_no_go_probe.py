#!/usr/bin/env python3
"""Hostile mutations for K1247."""

EXPECTED = {"weights":(2,4,6,7,8,10,12), "critical_radial_kernel":True,
            "rank_upper":6, "required_rank":7, "inhomogeneous_excluded":False}

def accepts(item):
    return (item == EXPECTED and len(item["weights"]) == 7
            and item["critical_radial_kernel"] and item["rank_upper"] < item["required_rank"]
            and not item["inhomogeneous_excluded"])

mutations = []
for key in EXPECTED:
    item = dict(EXPECTED)
    value = item[key]
    if isinstance(value, bool): item[key] = not value
    elif isinstance(value, int): item[key] += 1
    else: values=list(value); values[3]+=1; item[key]=tuple(values)
    mutations.append(item)
for index in range(5):
    item = dict(EXPECTED); item.pop(list(EXPECTED)[index]); mutations.append(item)
assert accepts(EXPECTED) and all(not accepts(item) for item in mutations)
print(f"PASS hostile mutations {len(mutations)}/{len(mutations)}")
