#!/usr/bin/env sage
"""Independent exact Sage reconstruction of the TT background C theorem."""

R.<a,b,u> = PolynomialRing(QQ)
F = R.fraction_field()
a, b, u = F(a), F(b), F(u)

K = matrix(F, [[a, 1], [1, 0]])
M = matrix(F, [[u, u], [u, b + u]])
L = K.inverse() * M
trL = L.trace()
detL = L.det()
D = (b + u) * (a^2 * b + (a - 2)^2 * u)
N = 2 * L - trL * identity_matrix(F, 2)

assert trL^2 - 4 * detL == D
assert N * N == D * identity_matrix(F, 2)
assert N * L == L * N
assert N.transpose() * K == K * N
Gnum = K * N
assert Gnum == Gnum.transpose()
assert Gnum.det() == D

L0 = L.subs({u: 0})
P = identity_matrix(F, 2) + 2 * L0 / (a * b)
L1 = L.derivative(u)
C1 = matrix(F, [
    [2 * (a - 1) / (a^2 * b), 4 * (a - 1) / (a^3 * b)],
    [-2 * (a - 1) / (a * b), -2 * (a - 1) / (a^2 * b)],
])
assert P * C1 + C1 * P == 0
assert C1 * L0 - L0 * C1 + P * L1 - L1 * P == 0
assert C1.transpose() * K == K * C1

# Connected positive component sample.
connected = {a: QQ(3)/2, b: 2, u: 1}
D_connected = D.subs(connected)
G_connected = Gnum.subs(connected)
assert D_connected > 0
assert G_connected[1, 1] > 0
assert G_connected.det() == D_connected

# Generic exceptional point is Jordan.
wall = {a: QQ(3)/2, b: 2, u: -2}
L_wall = L.subs(wall)
lam = L_wall.trace() / 2
Jrem = L_wall - lam * identity_matrix(QQ, 2)
assert Jrem.rank() == 1
assert Jrem * Jrem == 0

# Complex interval and disconnected real component.
assert D.subs({a: QQ(3)/2, b: 2, u: -5}) < 0
far = {a: QQ(3)/2, b: 2, u: -20}
assert D.subs(far) == 9
assert Gnum.subs(far)[1, 1] < 0

# Coincident walls at a=1 are scalar and non-selecting.
assert L.subs({a: 1, b: 2, u: -2}) == -2 * identity_matrix(QQ, 2)

print("PASS: independent Sage exact background-C reconstruction")
print("D =", D)
print("connected sample D =", D_connected)
print("generic wall Jordan rank =", Jrem.rank())
