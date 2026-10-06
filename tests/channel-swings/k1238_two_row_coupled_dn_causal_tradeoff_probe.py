#!/usr/bin/env python3
"""Hostile mutations for K1238 coupled causal ranks."""

EXPECTED = {"ranks": (131070, 131070, 122880), "radicals": (98316, 98316, 106506), "gains": (158, 158, 132), "common_null": 11}


def accepts(item):
    return (item == EXPECTED
            and all(r + k == 229386 for r, k in zip(item["ranks"], item["radicals"]))
            and item["radicals"][2] - item["radicals"][0] == 8190)


mutations = []
for key in ("ranks", "radicals", "gains"):
    for index in range(3):
        item = dict(EXPECTED); values = list(item[key]); values[index] += 1; item[key] = tuple(values); mutations.append(item)
item = dict(EXPECTED); item["common_null"] = 24; mutations.append(item)
assert accepts(EXPECTED)
assert all(not accepts(item) for item in mutations)
print(f"PASS hostile mutations {len(mutations)}/{len(mutations)}")
