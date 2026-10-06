#!/usr/bin/env python3
"""Hostile mutations for K1255."""

EXPECTED = (10, 3, 1, 6, 0, 0, False)

def accepts(row):
    if len(row) != 7:
        return False
    total, satisfied, excluded, missing, k1145, k1150, source_owned = row
    return (row == EXPECTED and satisfied + excluded + missing == total
            and k1145 == k1150 == 0 and not source_owned)

mutations = []
for index in range(len(EXPECTED)):
    row = list(EXPECTED)
    if isinstance(row[index], bool):
        row[index] = not row[index]
    else:
        row[index] += 1
    mutations.append(tuple(row))
mutations.extend([EXPECTED[:-1], EXPECTED + ("physical",), (10,4,1,5,0,0,False)])
assert accepts(EXPECTED) and all(not accepts(row) for row in mutations)
print(f"PASS hostile mutations {len(mutations)}/{len(mutations)}")
