# Independent Sage exact order/Helmholtz comparator for PW2F-R.
#
# The native Z1/Clifford verdict lives in the Python probe.  This file checks
# only the universal jet algebra after Z1 raises the induced connection to
# metric order two and its curvature input to order three.

n = 3
names = []
for owner in range(n):
    names += [f"q{owner}_{order}" for order in range(7)]
for row in range(n):
    names += [f"m{row}_{column}" for column in range(n)]
    names += [f"c{row}_{column}" for column in range(n)]

R = PolynomialRing(QQ, names)
v = R.gens_dict()
q = [[v[f"q{owner}_{order}"] for order in range(7)] for owner in range(n)]
M = matrix(R, n, n, lambda i, j: v[f"m{min(i,j)}_{max(i,j)}"])
C = matrix(R, n, n, lambda i, j: v[f"c{i}_{j}"])


def total_d(poly):
    result = R.zero()
    for jets in q:
        for left, right in zip(jets[:-1], jets[1:]):
            result += poly.derivative(left) * right
    return result


# q2 is the Z1-derived connection/distortion owner and q3 its curvature
# input.  L is affine in q3 and quadratic in q2.
L = R.zero()
for i in range(n):
    for j in range(n):
        L += R(1) / 2 * M[i, j] * q[i][2] * q[j][2]
        L += C[i, j] * q[i][2] * q[j][3]

E = []
for owner in range(n):
    value = R.zero()
    for order in range(4):
        term = L.derivative(q[owner][order])
        for _ in range(order):
            term = -total_d(term)
        value += term
    E.append(value)

C6 = matrix(R, n, n, lambda i, j: E[i].derivative(q[j][6]))
C5 = matrix(R, n, n, lambda i, j: E[i].derivative(q[j][5]))
C4 = matrix(R, n, n, lambda i, j: E[i].derivative(q[j][4]))

assert C6 == zero_matrix(R, n)
assert C5 == C - C.transpose()
assert C5.transpose() == -C5
assert C5.subs({C[i,j]: M[i,j] for i in range(n) for j in range(n)}) == zero_matrix(R, n)
assert C4.subs({C[i,j]: 0 for i in range(n) for j in range(n)}) == M

print("PW2F-R SAGE STRUCTURAL CROSS-CHECK: 5 PASS; C6=0; C5=C-C^T; symmetric-C cancellation; C4 mass live")
