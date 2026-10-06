#!/usr/bin/env python3
"""Hostile mutations for the K1236 all-comm causal census."""

EXPECTED = {
    "nonnull": (114687, 122878, 106498),
    "null": (114687, 114688, 114688),
    "jump": 8190,
    "edges": ((1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14)),
}


def accepts(candidate):
    return (candidate["nonnull"] == EXPECTED["nonnull"]
            and candidate["null"] == EXPECTED["null"]
            and candidate["jump"] == candidate["null"][2] - candidate["nonnull"][2] == EXPECTED["jump"]
            and tuple(candidate["edges"]) == EXPECTED["edges"])


base = dict(EXPECTED)
mutations = []
for key, index, delta in (("nonnull", 0, 1), ("nonnull", 1, -1), ("nonnull", 2, 1),
                          ("null", 0, -1), ("null", 1, 1), ("null", 2, -1)):
    item = dict(base)
    values = list(item[key])
    values[index] += delta
    item[key] = tuple(values)
    mutations.append(item)
item = dict(base); item["jump"] = 8166; mutations.append(item)
item = dict(base); item["edges"] = base["edges"][:-1]; mutations.append(item)

assert accepts(base)
assert all(not accepts(item) for item in mutations)
print(f"PASS hostile mutations {len(mutations)}/{len(mutations)}")
