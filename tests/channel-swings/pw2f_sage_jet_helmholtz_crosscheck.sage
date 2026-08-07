# Independent SageMath exact jet/Helmholtz cross-check for PW2F.
#
# The primary repository probe uses SymPy and the active Clifford fixture.
# This file proves the universal affine-second-jet cancellation again over an
# exact multivariate polynomial ring with symbolic coefficient matrix C.

n = 4
names = []
for owner in range(n):
    names += [f"q{owner}_{order}" for order in range(5)]
for owner in range(n):
    names += [f"e{owner}_{order}" for order in range(3)]
for row in range(n):
    names += [f"c{row}_{column}" for column in range(n)]

R = PolynomialRing(QQ, names)
v = R.gens_dict()
q = [[v[f"q{owner}_{order}"] for order in range(5)] for owner in range(n)]
e = [[v[f"e{owner}_{order}"] for order in range(3)] for owner in range(n)]
C = matrix(R, n, n, lambda row, column: v[f"c{row}_{column}"])


def total_d(poly, rows):
    result = R.zero()
    for jets in rows:
        for left, right in zip(jets[:-1], jets[1:]):
            result += poly.derivative(left) * right
    return result


L = R.zero()
for row in range(n):
    affine = R(row + 1)
    for column in range(n):
        affine += C[row, column] * q[column][1]
    L += affine * q[row][2]
    L += R(row + 1) * q[row][1]^2
    L += R(row + 2) * q[row][0]^2

E = []
for owner in range(n):
    value = L.derivative(q[owner][0])
    value -= total_d(L.derivative(q[owner][1]), q)
    value += total_d(total_d(L.derivative(q[owner][2]), q), q)
    E.append(value)

fourth = matrix(R, n, n, lambda row, column: E[row].derivative(q[column][4]))
third = matrix(R, n, n, lambda row, column: E[row].derivative(q[column][3]))
assert fourth == zero_matrix(R, n)
assert third == C - C.transpose()
assert third.transpose() == -third

direct = R.zero()
bulk = R.zero()
theta = R.zero()
for owner in range(n):
    for order in range(3):
        direct += L.derivative(q[owner][order]) * e[owner][order]
    bulk += E[owner] * e[owner][0]
    theta += (
        L.derivative(q[owner][1])
        - total_d(L.derivative(q[owner][2]), q)
    ) * e[owner][0]
    theta += L.derivative(q[owner][2]) * e[owner][1]

assert direct - bulk - total_d(theta, q + e) == 0

# A symmetric nonzero owner coefficient cannot be the coefficient of a
# formally self-adjoint odd-order block.
S = C + C.transpose()
assert S != zero_matrix(R, n)
assert S != -S.transpose()

print("PW2F SAGE EXACT CROSS-CHECK: 5 PASS; fourth=0; third=C-C^T; Green=0")
