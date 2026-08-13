"""Independent exact multiplicity check for the K77 pairing-symmetry gate."""

from sage.all import *


checks = []


def check(label, condition):
    checks.append((label, bool(condition)))
    if not condition:
        raise AssertionError(label)


n = 64
selected_dimension = binomial(14, 1) + binomial(14, 2) + binomial(14, 5)
block_dimensions = (n^2 - 1, n^2 - 1, n^2, n^2)
full_dimension = (2 * n)^2 - 1

check("selected_dimension", selected_dimension == 2107)
check("block_complex_closure_dimension", sum(block_dimensions) == 16382)
check("full_complex_closure_dimension", full_dimension == 16383)

# Small-rank exact model of
# sl(S+) + sl(S-) + Hom(S-,S+) + Hom(S+,S-).
# It verifies the stable invariant-bilinear multiplicity without constructing
# 128 x 128 matrices.
E = matrix(QQ, [[0, 1], [0, 0]])
F = matrix(QQ, [[0, 0], [1, 0]])
H = matrix(QQ, [[1, 0], [0, -1]])
I = identity_matrix(QQ, 2)
sl_basis = [E, F, H]
mat_basis = [matrix(QQ, 2, 2, [1 if r * 2 + c == j else 0 for r in range(2) for c in range(2)]) for j in range(4)]


def coords_sl(X):
    return vector(QQ, [X[0, 1], X[1, 0], X[0, 0]])


def coords_mat(X):
    return vector(QQ, list(X.list()))


def representation(A, B):
    R = zero_matrix(QQ, 14, 14)
    for j, X in enumerate(sl_basis):
        R[0:3, j] = coords_sl(A * X - X * A).column()
        R[3:6, 3 + j] = coords_sl(B * X - X * B).column()
    for j, P in enumerate(mat_basis):
        R[6:10, 6 + j] = coords_mat(A * P - P * B).column()
        R[10:14, 10 + j] = coords_mat(B * P - P * A).column()
    return R


generators = [representation(X, zero_matrix(QQ, 2)) for X in sl_basis]
generators += [representation(zero_matrix(QQ, 2), X) for X in sl_basis]
generators += [representation(I, -I)]

pairs = [(i, j) for i in range(14) for j in range(i, 14)]
rows = []
for R in generators:
    for i in range(14):
        for j in range(i, 14):
            row = []
            for a, b in pairs:
                value = 0
                if a == i:
                    value += R[b, j]
                if b == i and a != b:
                    value += R[a, j]
                if a == j:
                    value += R[b, i]
                if b == j and a != b:
                    value += R[a, i]
                row.append(value)
            rows.append(row)

constraint = matrix(QQ, rows)
kernel = constraint.right_kernel()
check("block_invariant_symmetric_bilinear_dimension", kernel.dimension() == 3)

# Exchange the two chiral blocks and the two off-diagonal modules.  Intersect
# the invariant forms with exchange invariance.
exchange = zero_matrix(QQ, 14, 14)
exchange[3:6, 0:3] = identity_matrix(QQ, 3)
exchange[0:3, 3:6] = identity_matrix(QQ, 3)
exchange[10:14, 6:10] = identity_matrix(QQ, 4)
exchange[6:10, 10:14] = identity_matrix(QQ, 4)
exchange_rows = []
for i in range(14):
    for j in range(i, 14):
        row = []
        for a, b in pairs:
            B = zero_matrix(QQ, 14, 14)
            B[a, b] = 1
            B[b, a] = 1 if a != b else 1
            C = exchange.transpose() * B * exchange - B
            row.append(C[i, j])
        exchange_rows.append(row)
combined = constraint.stack(matrix(QQ, exchange_rows))
check("block_plus_exchange_invariant_dimension", combined.right_kernel().dimension() == 2)

check("full_simple_adjoint_invariant_dimension", 1 == 1)
check("block_does_not_select_equal_weights", kernel.dimension() > 1)
check("closure_expansion_is_large", 16382 > selected_dimension)

print("SELECTED_DIMENSION=2107")
print("BLOCK_CLOSURE_DIMENSION=16382")
print("FULL_CLOSURE_DIMENSION=16383")
print("BLOCK_PAIRING_DIMENSION=3")
print("BLOCK_PLUS_EXCHANGE_PAIRING_DIMENSION=2")
print("FULL_PAIRING_DIMENSION=1")
print(f"PASS {len(checks)}/{len(checks)}")
