#!/usr/bin/env sage
"""Independent exact certificate for the K77 Bianchi/target gate.

This route uses Sage's exact rational matrices and free associative algebra.
It shares no exterior/Clifford implementation with the main Python probe.
"""

from sage.all import FreeAlgebra, Matrix, QQ, vector


# Eight maps decompose into two first-term and four nested-term coordinates.
rows = []
for first in range(2):
    for inner in range(2):
        for outer in range(2):
            row = [QQ(0)] * 6
            row[first] = QQ(1)
            row[2 + 2 * inner + outer] = QQ(1)
            rows.append(row)

incidence = Matrix(QQ, rows)
assert incidence.rank() == 5
assert incidence.left_kernel().dimension() == 3

r1 = vector(QQ, [1, -1, 0, 0, -1, 1, 0, 0])
r2 = vector(QQ, [1, 0, -1, 0, -1, 0, 1, 0])
r3 = vector(QQ, [1, 0, 0, -1, -1, 0, 0, 1])
assert r1 * incidence == 0
assert r2 * incidence == 0
assert r3 * incidence == 0
assert Matrix(QQ, [r1, r2, r3]).rank() == 3


# Independent free-algebra reconstruction of the path-average curvature from
# the two-connection square's Delta F and T blocks.
A = FreeAlgebra(QQ, 4, names=("B", "T", "dB", "dT"))
B, T, dB, dT = A.gens()
F_B = dB + B * B
D_B_T = dT + B * T + T * B
T2 = T * T
F_A = F_B + D_B_T + T2
delta_F = F_A - F_B
average = F_B + QQ(1) / 2 * D_B_T + QQ(1) / 3 * T2
from_square = F_B + QQ(1) / 2 * delta_F - QQ(1) / 6 * T2

assert delta_F == D_B_T + T2
assert from_square == average
assert -T * F_B != 0

print("FULL_ADJOINT_PRODUCT_INCIDENCE_RANK=5")
print("UNIVERSAL_RELATION_DIMENSION=3")
print("TWO_CONNECTION_PATH_AVERAGE_RECONSTRUCTION=EXACT")
print("MIXED_TWO_CONNECTION_DEFECT=NONZERO")
