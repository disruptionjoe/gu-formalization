#!/usr/bin/env python3
"""Hostile mutations for K1253."""

EXPECTED = (1, 6, 7, True, 6, False)

def accepts(row):
    if len(row) != 6:
        return False
    scales, shapes, total, bijective, after_scale_grant, source_owned = row
    return (row == EXPECTED and scales + shapes == total == 7
            and after_scale_grant == shapes and bijective and not source_owned)

mutations = []
for index in range(len(EXPECTED)):
    row = list(EXPECTED)
    if isinstance(row[index], bool):
        row[index] = not row[index]
    else:
        row[index] += 1
    mutations.append(tuple(row))
mutations.extend([EXPECTED[:-1], EXPECTED + ("physical",), (1,5,6,True,5,False), (0,7,7,False,7,False)])
assert accepts(EXPECTED) and all(not accepts(row) for row in mutations)
print(f"PASS hostile mutations {len(mutations)}/{len(mutations)}")
