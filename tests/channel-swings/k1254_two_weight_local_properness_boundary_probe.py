#!/usr/bin/env python3
"""Hostile mutations for K1254."""

EXPECTED = (-2, True, True, False, False, False, False)

def accepts(row):
    if len(row) != 7:
        return False
    floor, unique, boundary_noncompact, open_horn_proper, functional_domain, green, cohomology = row
    return (row == EXPECTED and floor == -2 and unique and boundary_noncompact
            and not open_horn_proper and not functional_domain and not green and not cohomology)

mutations = []
for index in range(len(EXPECTED)):
    row = list(EXPECTED)
    if isinstance(row[index], bool):
        row[index] = not row[index]
    else:
        row[index] += 1
    mutations.append(tuple(row))
mutations.extend([EXPECTED[:-1], EXPECTED + ("source",), (-2,True,False,True,False,False,False), (-2,True,True,False,True,True,True)])
assert accepts(EXPECTED) and all(not accepts(row) for row in mutations)
print(f"PASS hostile mutations {len(mutations)}/{len(mutations)}")
