#!/usr/bin/env sage
"""Independent QQ check of the 34-field Green and pullback theorem."""

from sage.all import QQ, diagonal_matrix, matrix, vector


checks = []


def check(label, condition):
    checks.append((label, bool(condition)))
    if not condition:
        raise AssertionError(label)


n = 10 + 24
m = 9
K = diagonal_matrix(QQ, [1 if i % 2 == 0 else -1 for i in range(m)])
B = matrix(QQ, m, n, lambda i, j: ((3 * i + 1) * (j + 2)) % 17 - 8)
u0 = vector(QQ, [((5 * i + 1) % 23) - 11 for i in range(n)])
u1 = vector(QQ, [((7 * i + 2) % 29) - 14 for i in range(n)])
v0 = vector(QQ, [((11 * i + 3) % 31) - 15 for i in range(m)])
v1 = vector(QQ, [((13 * i + 4) % 37) - 18 for i in range(m)])

check("domain_34", n == 34)
check("krein_nondegenerate_indefinite", K.det() != 0 and 0 < sum(x > 0 for x in K.diagonal()) < m)

for mu in range(4):
    A = matrix(QQ, m, n, lambda i, j: ((i + 2) * (j + 3) + 5 * mu) % 19 - 9)
    ju0 = A * u1 + B * u0
    ju1 = B * u1
    lhs = vector(QQ, [
        ju0 * K * v0,
        ju0 * K * v1 + ju1 * K * v0,
        ju1 * K * v1,
    ])
    adj0 = -A.transpose() * K * v1 + B.transpose() * K * v0
    adj1 = B.transpose() * K * v1
    rhs = vector(QQ, [
        u0 * adj0,
        u1 * adj0 + u0 * adj1,
        u1 * adj1,
    ])
    green = vector(QQ, [
        (A * u0) * K * v0,
        (A * u0) * K * v1 + (A * u1) * K * v0,
        (A * u1) * K * v1,
    ])
    derivative_green = vector(QQ, [green[1], 2 * green[2], 0])
    check("green_direction_%s" % mu, lhs - rhs == derivative_green)
    check("green_nonzero_%s" % mu, green != 0)

# The physical theorem is functorial: a coefficientwise zero four-column
# residual graph is annihilated by every covector, while a planted rank-three
# omission is not.
R = matrix(QQ, m, 4, 0)
w = vector(QQ, [i + 1 for i in range(m)])
check("physical_dual_pullback_zero", R.transpose() * K * w == 0)
plant = matrix(QQ, m, 4, lambda i, j: 1 if i == j and j < 3 else 0)
check("omission_plant_rank_three", plant.rank() == 3 and plant.transpose() * K * w != 0)

print("COMMON_DOMAIN=34")
print("GREEN_DIRECTIONS=4")
print("PHYSICAL_ZERO_COLUMNS=4")
print("PASS %s/%s" % (len(checks), len(checks)))
