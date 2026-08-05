#!/usr/bin/env sage
"""Independent exact product-basis rank check for the K77 Shiab channels.

The main probe computes the full real-Cl(7,7) maps.  This Sage route checks a
different algebraic layer: before Clifford/Hodge identities are imposed, the
three binary commutator/i-anticommutator choices form an invertible Walsh
transform on the eight ordered-word choices.  It is an independent exact
rank engine and deliberately does not claim to reconstruct the full K77 map.
"""

K.<ii> = QuadraticField(-1)

from itertools import product


def local_row(kind):
    if kind == "comm":
        return vector(K, [1, -1])
    if kind == "symi":
        return vector(K, [ii, ii])
    raise ValueError(kind)


channels = product(["comm", "symi"], repeat=3)
rows = []
for channel in channels:
    row = local_row(channel[0])
    row = vector(K, [a * b for a in row for b in local_row(channel[1])])
    row = vector(K, [a * b for a in row for b in local_row(channel[2])])
    rows.append(row)

M = Matrix(K, rows)
assert M.nrows() == 8 and M.ncols() == 8
assert M.rank() == 8
assert M.det() != 0

# Removing either half of one local binary product destroys invertibility.
M_bad = copy(M)
M_bad[7] = M_bad[6]
assert M_bad.rank() == 7

print("SAGE_EXACT_PRODUCT_TRANSFORM_RANK=8")
print("SAGE_EXACT_PRODUCT_TRANSFORM_DETERMINANT=", M.det())
print("SAGE_PLANTED_DUPLICATE_RANK=7")
print("PASS: independent Sage exact product-basis transform is invertible; full K77 channel-map rank remains owned by the main probe.")
