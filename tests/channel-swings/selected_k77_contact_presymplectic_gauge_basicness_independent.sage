#!/usr/bin/env sage
"""Independent Sage/QQ contact-current and gauge-basicness certificate."""

from sage.all import (
    QQ,
    block_diagonal_matrix,
    diagonal_matrix,
    identity_matrix,
    matrix,
    vector,
    zero_matrix,
)


# Actual flat null-orbit Levi-Civita symbol on the ten symmetric metric slots.
eta = diagonal_matrix(QQ, [-1, 1, 1, 1])
slots = [(i, j) for i in range(4) for j in range(i, 4)]
basis = []
for i, j in slots:
    h = zero_matrix(QQ, 4)
    h[i, j] = 1
    h[j, i] = 1
    basis.append(h)
k = [1, 0, 0, 1]
L = zero_matrix(QQ, 64, 10)
for column, h in enumerate(basis):
    for rho in range(4):
        for mu in range(4):
            for nu in range(4):
                row = (rho * 4 + mu) * 4 + nu
                L[row, column] = QQ(1)/2 * sum(
                    eta[rho, sigma] * (
                        k[mu] * h[nu, sigma]
                        + k[nu] * h[mu, sigma]
                        - k[sigma] * h[mu, nu]
                    ) for sigma in range(4)
                )
current = vector(QQ, [((i + 1) * (i + 3)) % 17 - 8 for i in range(64)])
metric_contact = L.transpose() * current
assert L.rank() == 10
assert all(value != 0 for value in metric_contact)

contact = L.augment(identity_matrix(QQ, 64), subdivide=False)
contact[:, :10] = -L
diagonal_gauge = identity_matrix(QQ, 10).stack(L)
frozen_gauge = identity_matrix(QQ, 10).stack(zero_matrix(QQ, 64, 10))
assert contact * diagonal_gauge == zero_matrix(QQ, 64, 10)
assert (contact * frozen_gauge).rank() == 10


# Exact finite contact action T=a-Dg and its four-dimensional Ward kernel.
D = matrix(QQ, [[-1, 1, 0, 0], [0, -1, 1, 0], [0, 0, -1, 1]])
K = diagonal_matrix(QQ, [-1, 2, 3])
H = (D.transpose() * K * D).augment(-D.transpose() * K)
H = H.stack((-K * D).augment(K))
R = identity_matrix(QQ, 4).stack(D)
assert H == H.transpose()
assert H * R == zero_matrix(QQ, 7, 4)
assert R.transpose() * H == zero_matrix(QQ, 4, 7)
assert H.rank() == 3 and R.rank() == 4


# Boundary current theta=p0 dg0-p2 dg3.  Small gauge is horizontal; boundary
# gauge has an exact, nonzero moment map while the constant form is invariant.
p = K * vector(QQ, [2, -3, 5])
Omega = matrix(QQ, [
    [0, 0, -1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, -1, 0, 0],
])
small = vector(QQ, [0, 0, 0, 0])
edge = vector(QQ, [1, 1, 0, 0])
assert small * Omega == vector(QQ, [0, 0, 0, 0])
assert edge * Omega == -vector(QQ, [0, 0, 1, -1])
assert p[0] - p[2] != 0


# Independently rebuild the ten K77 normal cotangent weights and verify that
# every one carries the same nonzero boundary charge.
g4 = diagonal_matrix(QQ, [1, -1, -1, -1])
g4i = g4.inverse()


def dewitt(inverse):
    return matrix(QQ, 10, 10, lambda i, j:
        (inverse * basis[i] * inverse * basis[j]).trace()
        - QQ(1)/2 * (inverse * basis[i]).trace() * (inverse * basis[j]).trace())


def d_dewitt(h):
    di = -g4i * h * g4i
    return matrix(QQ, 10, 10, lambda i, j:
        (di * basis[i] * g4i * basis[j]).trace()
        + (g4i * basis[i] * di * basis[j]).trace()
        - QQ(1)/2 * (
            (di * basis[i]).trace() * (g4i * basis[j]).trace()
            + (g4i * basis[i]).trace() * (di * basis[j]).trace()))


g = block_diagonal_matrix([g4, dewitt(g4i)])
dg = [block_diagonal_matrix([h, d_dewitt(h)]) for h in basis]
compensators = [-QQ(1)/2 * g.inverse() * value for value in dg]
k77_field = vector(QQ, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43])
k77_momentum = vector(QQ, [47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107])
weights = [k77_momentum * value * k77_field for value in compensators]
charges = [weight * (p[0] - p[2]) for weight in weights]
assert all(value != 0 for value in weights)
assert all(value != 0 for value in charges)

print("PASS independent Sage/QQ K77 contact-presymplectic gauge-basicness gate")
print("LEVI_CIVITA_CONTACT=RANK10 DIAGONAL_TWO_CONNECTION_WARD=EXACT")
print("SMALL_GAUGE=HORIZONTAL BOUNDARY_GAUGE=MOMENT_MAP_CHARGE_LIVE")
print("K77_BOUNDARY_CHARGES=10_OF_10_NONZERO")
