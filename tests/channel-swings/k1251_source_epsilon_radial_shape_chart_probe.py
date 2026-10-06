#!/usr/bin/env python3
"""Hostile mutations for K1251."""

EXPECTED = ((2, 4, 6, 7, 8, 10, 12), 7, 6, 48, True)

def accepts(row):
    if len(row) != 5:
        return False
    weights, dimension, shape_count, exponent, positive_horn = row
    return (row == EXPECTED and dimension == len(weights) == 7
            and shape_count == dimension - 1
            and exponent == 1 + sum(weights[1:])
            and positive_horn)

mutations = []
for index in range(len(EXPECTED)):
    row = list(EXPECTED)
    if isinstance(row[index], tuple):
        values = list(row[index]); values[-1] += 1; row[index] = tuple(values)
    elif isinstance(row[index], bool):
        row[index] = not row[index]
    else:
        row[index] += 1
    mutations.append(tuple(row))
mutations.extend([EXPECTED[:-1], EXPECTED + ("global",), ((2,4,6,7,8,10),6,5,36,True), ((2,4,6,8,10,12,14),7,6,49,True)])
assert accepts(EXPECTED) and all(not accepts(row) for row in mutations)
print(f"PASS hostile mutations {len(mutations)}/{len(mutations)}")
