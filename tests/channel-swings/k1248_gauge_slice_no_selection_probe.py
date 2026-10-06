#!/usr/bin/env python3
"""Hostile mutations for K1248."""

EXPECTED = (7, 7, True, False, False, False, False)

def accepts(row):
    if len(row) != 7:
        return False
    rank, free, rep, value, gauge_changes, canonical_charge, replaces_lock = row
    return row == EXPECTED and rank == free == 7 and rep and not any((value, gauge_changes, canonical_charge, replaces_lock))

mutations = []
for index, value in enumerate(EXPECTED):
    row = list(EXPECTED); row[index] = (not value) if isinstance(value, bool) else value + 1; mutations.append(tuple(row))
mutations.extend([EXPECTED[:-1], EXPECTED + (True,)])
assert accepts(EXPECTED) and all(not accepts(row) for row in mutations)
print(f"PASS hostile mutations {len(mutations)}/{len(mutations)}")
