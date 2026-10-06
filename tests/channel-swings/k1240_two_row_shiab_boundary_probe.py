#!/usr/bin/env python3
"""Hostile mutations for K1240 integration."""

EXPECTED = {"gains": (158, 158, 132), "radicals": (98316, 98316, 106506), "k1150": 0, "source_selected": False}


def accepts(item):
    return (item == EXPECTED and item["radicals"][2] - item["radicals"][0] == 8190
            and item["k1150"] == 0 and not item["source_selected"])


mutations = []
for key in ("gains", "radicals"):
    for index in range(3):
        item = dict(EXPECTED); values = list(item[key]); values[index] += 1; item[key] = tuple(values); mutations.append(item)
item = dict(EXPECTED); item["k1150"] = 1; mutations.append(item)
item = dict(EXPECTED); item["source_selected"] = True; mutations.append(item)
assert accepts(EXPECTED)
assert all(not accepts(item) for item in mutations)
print(f"PASS hostile mutations {len(mutations)}/{len(mutations)}")
