#!/usr/bin/env python3
"""Hostile mutations for K1246."""

EXPECTED = ("D7", 91, 7, (1,3,5,6,7,9,11), (2,4,6,7,8,10,12), 84, 7)

def accepts(row):
    if len(row) != 7:
        return False
    kind, dim, rank, exponents, degrees, orbit, quotient = row
    return (row == EXPECTED and dim == rank * (2 * rank - 1)
            and degrees == tuple(sorted(x + 1 for x in exponents))
            and orbit == dim - rank and quotient == rank)

mutations = []
for index in range(len(EXPECTED)):
    row = list(EXPECTED)
    if isinstance(row[index], int):
        row[index] += 1
    elif isinstance(row[index], tuple):
        values = list(row[index]); values[0] += 1; row[index] = tuple(values)
    else:
        row[index] = "D6"
    mutations.append(tuple(row))
mutations.extend([EXPECTED[:-1], EXPECTED + (True,)])
assert accepts(EXPECTED) and all(not accepts(row) for row in mutations)
print(f"PASS hostile mutations {len(mutations)}/{len(mutations)}")
