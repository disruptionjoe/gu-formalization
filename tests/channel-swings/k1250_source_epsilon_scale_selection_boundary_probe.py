#!/usr/bin/env python3
"""Hostile mutations for K1250."""

EXPECTED = (9, 1, 3, 5, 0, 0, True, True, True)

def accepts(row):
    return row == EXPECTED and sum(row[1:4]) == row[0] and row[4:6] == (0,0) and all(row[6:])

mutations = []
for index, value in enumerate(EXPECTED):
    row = list(EXPECTED); row[index] = (not value) if isinstance(value, bool) else value + 1; mutations.append(tuple(row))
assert accepts(EXPECTED) and all(not accepts(row) for row in mutations)
print(f"PASS hostile mutations {len(mutations)}/{len(mutations)}")
