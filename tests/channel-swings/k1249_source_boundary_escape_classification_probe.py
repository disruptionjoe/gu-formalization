#!/usr/bin/env python3
"""Hostile mutations for K1249."""

EXPECTED = (6, "sufficient_unowned", "wrong_algebra", "rank_le_6", "seven_free", "open_rank_7", "outside_finite", False, False)

def accepts(row):
    return row == EXPECTED and row[0] == 6 and row[1:7] == EXPECTED[1:7] and not row[7] and not row[8]

mutations = []
for index, value in enumerate(EXPECTED):
    row = list(EXPECTED)
    if isinstance(value, bool): row[index] = not value
    elif isinstance(value, int): row[index] += 1
    else: row[index] = value + "_mutated"
    mutations.append(tuple(row))
assert accepts(EXPECTED) and all(not accepts(row) for row in mutations)
print(f"PASS hostile mutations {len(mutations)}/{len(mutations)}")
