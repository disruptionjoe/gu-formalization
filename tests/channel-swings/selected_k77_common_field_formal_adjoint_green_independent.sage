#!/usr/bin/env sage
"""Independent QQ certificate for first-order adjoint signs and Riesz typing."""

from sage.all import QQ, PolynomialRing, diagonal_matrix, matrix, vector


R = PolynomialRing(QQ, "x")
x = R.gen()
A = matrix(QQ, [[1, 2], [-1, 3], [2, 0]])
B = matrix(QQ, [[0, 1], [2, -1], [1, 1]])
K = diagonal_matrix(QQ, [1, -1, 1])
u = vector(R, [1 + 2*x, 3 - x])
v = vector(R, [2 - x, 1 + 3*x, -1 + 2*x])


def derivative(values):
    return vector(R, [value.derivative() for value in values])


Ju = A * derivative(u) + B * u
equation_dual = -A.transpose() * K * derivative(v) + B.transpose() * K * v
green = (u * A.transpose() * K * v)
identity = (Ju * K * v) - (u * equation_dual) - green.derivative()
assert identity == 0

wrong = A.transpose() * K * derivative(v) + B.transpose() * K * v
assert (Ju * K * v) - (u * wrong) - green.derivative() != 0

covector = vector(QQ, [3, 5])
G1 = diagonal_matrix(QQ, [1, 1])
G2 = diagonal_matrix(QQ, [2, 1])
representative1 = G1.inverse() * covector
representative2 = G2.inverse() * covector
assert representative1 != representative2
assert G1 * representative1 == covector == G2 * representative2

# A symmetric residual Hessian is not a presymplectic form.
H = A.transpose() * K * A
assert H == H.transpose() and H != -H.transpose()

print("PASS 8/8")
print("FORMAL_ADJOINT=-A_TRANSPOSE_K_DERIVATIVE_PLUS_B_TRANSPOSE_K")
print("GREEN=u_TRANSPOSE_A_TRANSPOSE_K_v")
print("EQUATION_DUAL_CANONICAL__OPERATOR_REPRESENTATIVE_RIESZ_DEPENDENT")
