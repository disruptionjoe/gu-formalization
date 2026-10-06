#!/usr/bin/env python3
"""Hostile mutations for K1252."""

EXPECTED = ((4, 2), (16, 2, 2, 2, 2, 2, 2), 7, 1024, -2, True)

def accepts(row):
    if len(row) != 6:
        return False
    degrees, diagonal, rank, determinant, minimum, unique = row
    product = 1
    for value in diagonal:
        product *= value
    return (row == EXPECTED and len(set(degrees)) == 2
            and len(diagonal) == rank == 7 and all(value > 0 for value in diagonal)
            and product == determinant and minimum == -2 and unique)

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
mutations.extend([EXPECTED[:-1], EXPECTED + ("source",), ((4,4),EXPECTED[1],7,1024,-2,True), ((4,2),(16,2,2,2,2,2,0),6,0,-2,False)])
assert accepts(EXPECTED) and all(not accepts(row) for row in mutations)
print(f"PASS hostile mutations {len(mutations)}/{len(mutations)}")
