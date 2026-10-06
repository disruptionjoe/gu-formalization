#!/usr/bin/env python3
"""Hostile mutations for the K1237 bounded pencil screen."""

EXPECTED = {
    "-1": (40954, 40954),
    "-1/2": (131068, 122878),
    "1": (131068, 121888),
    "2": (131068, 122438),
    "3": (131068, 122878),
}


def accepts(candidate):
    return candidate == EXPECTED and candidate["3"][0] - 130912 == 156 and candidate["3"][1] - 122746 == 132


mutations = []
for key in EXPECTED:
    for coordinate in (0, 1):
        item = dict(EXPECTED)
        value = list(item[key])
        value[coordinate] += 1
        item[key] = tuple(value)
        mutations.append(item)
item = dict(EXPECTED); item.pop("3"); mutations.append(item)
assert accepts(EXPECTED)
assert all(not accepts(item) for item in mutations)
print(f"PASS hostile mutations {len(mutations)}/{len(mutations)}")
