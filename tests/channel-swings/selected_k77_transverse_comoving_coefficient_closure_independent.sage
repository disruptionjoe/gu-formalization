#!/usr/bin/env sage
"""Independent exact Sage certificate for the K77 comoving transverse lift."""

from itertools import combinations


Q = QQ
eta = diagonal_matrix(Q, [1, -1, -1, -1])
slots = [(i, j) for i in range(4) for j in range(i, 4)]
sym2 = []
for i, j in slots:
    value = matrix(Q, 4, 4, 0)
    value[i, j] = 1
    value[j, i] = 1
    sym2.append(value)


def dewitt(ginv):
    return matrix(Q, 10, 10, lambda a, b:
        (ginv * sym2[a] * ginv * sym2[b]).trace()
        - Q(1) / 2 * (ginv * sym2[a]).trace() * (ginv * sym2[b]).trace())


def d_dewitt(ginv, h):
    dinv = -ginv * h * ginv
    return matrix(Q, 10, 10, lambda a, b:
        (dinv * sym2[a] * ginv * sym2[b] + ginv * sym2[a] * dinv * sym2[b]).trace()
        - Q(1) / 2 * (
            (dinv * sym2[a]).trace() * (ginv * sym2[b]).trace()
            + (ginv * sym2[a]).trace() * (dinv * sym2[b]).trace()))


def block_diag(a, b):
    out = matrix(Q, a.nrows() + b.nrows(), a.ncols() + b.ncols(), 0)
    out[:a.nrows(), :a.ncols()] = a
    out[a.nrows():, a.ncols():] = b
    return out


def metric_symbol(q):
    out = matrix(Q, 10, 4, 0)
    for row, (i, j) in enumerate(slots):
        for column in range(4):
            out[row, column] = (q[i] if j == column else 0) + (q[j] if i == column else 0)
    return out


GV = dewitt(eta)
G = block_diag(eta, GV)
dGs = [block_diag(h, d_dewitt(eta, h)) for h in sym2]
As = [-Q(1) / 2 * G.inverse() * dG for dG in dGs]

assert QuadraticForm(Q, G).signature_vector() == (7, 7, 0)
assert all(dG + A.transpose() * G + G * A == 0 for dG, A in zip(dGs, As))
assert matrix(Q, 14 * 14, 10, lambda row, col: dGs[col][row // 14, row % 14]).rank() == 10
assert matrix(Q, 14 * 14, 10, lambda row, col: As[col][row // 14, row % 14]).rank() == 10

causal = {
    "timelike": vector(Q, [1, 0, 0, 0]),
    "spacelike": vector(Q, [0, 1, 0, 0]),
    "null": vector(Q, [1, 0, 0, 1]),
}

for name, q in causal.items():
    D = metric_symbol(q)
    projector = identity_matrix(Q, 10) - D * (D.transpose() * D).inverse() * D.transpose()
    transverse_dG = [sum((projector[j, i] * dGs[j] for j in range(10)), matrix(Q, 14, 14, 0)) for i in range(10)]
    transverse_A = [sum((projector[j, i] * As[j] for j in range(10)), matrix(Q, 14, 14, 0)) for i in range(10)]
    flat_dG = matrix(Q, 14 * 14, 10, lambda row, col: transverse_dG[col][row // 14, row % 14])
    flat_A = matrix(Q, 14 * 14, 10, lambda row, col: transverse_A[col][row // 14, row % 14])
    assert projector.rank() == 6
    assert flat_dG.rank() == 6
    assert flat_A.rank() == 6
    assert all(dG + A.transpose() * G + G * A == 0 for dG, A in zip(transverse_dG, transverse_A))

wrong = -G.inverse() * dGs[1]
assert dGs[1] + wrong.transpose() * G + G * wrong != 0

print("PASS 13/13")
print("K77_TOTAL_SIGNATURE=7_PLUS_7")
print("TEN_DIRECTION_COMOVING_LIFT_RANK=10")
print("TRANSVERSE_RANKS=6_6_6")
