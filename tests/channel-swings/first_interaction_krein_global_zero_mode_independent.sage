"""Independent exact Sage reconstruction for the interaction/zero-mode wave."""

R = PolynomialRing(QQ, names=("alpha", "b", "q0", "qm", "theta", "c"))
QF = R.fraction_field()
alpha, b, q0, qm, theta, c = QF.gens()

K = matrix(QF, [[alpha, 1], [1, 0]])
M = matrix(QF, [[0, 0], [0, b]])
L = K.inverse() * M
P = identity_matrix(QF, 2) + 2 * L / (alpha * b)
assert P == matrix(QF, [[1, 2 / alpha], [0, -1]])
assert P * P == identity_matrix(QF, 2)
assert P.transpose() * K == K * P

U = matrix(QF, [[1, 1], [0, -alpha]])
assert P * U == U * diagonal_matrix(QF, [1, -1])
vertex = c * theta * (q0 + qm)^2
even_image = vertex(qm=-qm)
odd_image = vertex(theta=-theta, qm=-qm)
assert even_image - vertex == -4 * c * q0 * qm * theta
assert odd_image - vertex == -2 * c * theta * (q0^2 + qm^2)

L4 = matrix(QQ, [
    [2, -1, 0, -1],
    [-1, 2, -1, 0],
    [0, -1, 2, -1],
    [-1, 0, -1, 2],
])
one = vector(QQ, [1, 1, 1, 1])
Pi0 = matrix(QQ, 4, 4, [QQ(1) / 4] * 16)
Q0 = identity_matrix(QQ, 4) - Pi0
assert L4 * one == 0
assert Pi0 * Pi0 == Pi0
assert Pi0.transpose() == Pi0
assert Pi0.rank() == 1
assert Q0 * one == 0
assert Pi0 * L4 == L4 * Pi0

Kscreen = identity_matrix(QQ, 4) + L4
source = vector(QQ, [2, -1, 4, 3])
for shift in [-7, 0, 11]:
    assert Kscreen.solve_right(Q0 * (source + shift * one)) == Kscreen.solve_right(Q0 * source)

# Normalization plus cyclic equality fixes the finite averaging weights.
A = matrix(QQ, [
    [1, 1, 1, 1],
    [1, -1, 0, 0],
    [0, 1, -1, 0],
    [0, 0, 1, -1],
])
rhs = vector(QQ, [1, 0, 0, 0])
assert A.rank() == 4
assert A.solve_right(rhs) == vector(QQ, [1/4, 1/4, 1/4, 1/4])

print("PASS: independent Sage exact reconstruction")
print("free parity obstruction: diagonal and mixed monomials require opposite theta signs")
print("finite global horn: rank(Pi0)=1, rank(Q0)=3, constant-shift response=0")
