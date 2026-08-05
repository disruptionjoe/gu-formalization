#!/usr/bin/env sage
"""Independent QQ reconstruction of the K77 defect null split.

This intentionally does not import the SymPy certificate.
"""

from sage.all import (
    QQ,
    block_matrix,
    diagonal_matrix,
    identity_matrix,
    matrix,
    vector,
    zero_matrix,
)


eta = diagonal_matrix(QQ, (-1, 1, 1, 1))
pairs = [(i, j) for i in range(4) for j in range(i, 4)]


def sym_matrix(values):
    out = zero_matrix(QQ, 4, 4)
    for value, (i, j) in zip(values, pairs):
        out[i, j] = value
        out[j, i] = value
    return out


def sym_vector(tensor):
    return vector(QQ, [tensor[i, j] for i, j in pairs])


def gauge(k):
    cols = []
    for a in range(4):
        xi = vector(QQ, 4)
        xi[a] = 1
        cols.append(sym_vector(matrix(QQ, 4, 4,
            lambda i, j: k[i] * xi[j] + k[j] * xi[i])))
    return matrix(QQ, 10, 4, lambda i, j: cols[j][i])


def harmonic(k):
    kv = vector(QQ, k)
    kr = eta * kv
    out = zero_matrix(QQ, 4, 10)
    for j in range(10):
        e = vector(QQ, 10)
        e[j] = 1
        h = sym_matrix(e)
        tr = sum(eta[a, b] * h[a, b] for a in range(4) for b in range(4))
        for nu in range(4):
            out[nu, j] = sum(kr[mu] * h[mu, nu] for mu in range(4)) - QQ(1)/2 * kv[nu] * tr
    return out


def einstein(k):
    kv = vector(QQ, k)
    kr = eta * kv
    k2 = kv * kr
    cols = []
    for j in range(10):
        e = vector(QQ, 10)
        e[j] = 1
        h = sym_matrix(e)
        tr = sum(eta[a, b] * h[a, b] for a in range(4) for b in range(4))
        ric = zero_matrix(QQ, 4, 4)
        for mu in range(4):
            for nu in range(4):
                kh_nu = sum(kr[rho] * h[rho, nu] for rho in range(4))
                kh_mu = sum(kr[rho] * h[rho, mu] for rho in range(4))
                ric[mu, nu] = QQ(1)/2 * (kv[mu] * kh_nu + kv[nu] * kh_mu - k2 * h[mu, nu] - kv[mu] * kv[nu] * tr)
        scalar = sum(eta[a, b] * ric[a, b] for a in range(4) for b in range(4))
        cols.append(sym_vector(ric - QQ(1)/2 * eta * scalar))
    return matrix(QQ, 10, 10, lambda i, j: cols[j][i])


def dewit_gram():
    out = zero_matrix(QQ, 10, 10)
    for a in range(10):
        ea = vector(QQ, 10)
        ea[a] = 1
        A = sym_matrix(ea)
        for b in range(10):
            eb = vector(QQ, 10)
            eb[b] = 1
            B = sym_matrix(eb)
            tr = sum(eta[i, j] * B[i, j] for i in range(4) for j in range(4))
            Br = B - QQ(1)/2 * eta * tr
            raised = eta * Br * eta
            out[a, b] = sum(A[i, j] * raised[i, j] for i in range(4) for j in range(4))
    return out


k = (1, 1, 0, 0)
G = einstein(k)
W = dewit_gram()
J = block_matrix(QQ, [[zero_matrix(QQ, 10), G.transpose() * W], [W * G, 2 * W]])
D = block_matrix(QQ, [[gauge(k)], [zero_matrix(QQ, 10, 4)]])
H = harmonic(k)
H20 = block_matrix(QQ, [[H, zero_matrix(QQ, 4, 10)]])
K = matrix(QQ, J.right_kernel().basis()).transpose()

assert J.rank() == 10
assert K.ncols() == 10
assert H.rank() == 4
assert (H20 * K).rank() == 4
assert D.rank() == 4
assert J * D == 0
assert H * D[:10, :] == 0
assert K.ncols() - (H20 * K).rank() - D.rank() == 2

plus_h = vector(QQ, 10)
plus_h[pairs.index((2, 2))] = 1
plus_h[pairs.index((3, 3))] = -1
cross_h = vector(QQ, 10)
cross_h[pairs.index((2, 3))] = 1
plus = vector(QQ, list(plus_h) + list(-G * plus_h / 2))
cross = vector(QQ, list(cross_h) + list(-G * cross_h / 2))
physical = matrix(QQ, 20, 2, lambda i, j: [plus, cross][j][i])
assert J * physical == 0
assert H20 * physical == 0
assert block_matrix(QQ, [[D, physical]]).rank() == 6

for test_k in [(1, 0, 0, 0), (0, 1, 0, 0)]:
    kv = vector(QQ, test_k)
    k2 = kv * (eta * kv)
    assert harmonic(test_k) * gauge(test_k) == k2 * identity_matrix(QQ, 4)

T1 = matrix(QQ, [[0, 0, 0], [0, 0, -1], [0, 1, 0]])
T2 = matrix(QQ, [[0, 0, 1], [0, 0, 0], [-1, 0, 0]])
T3 = matrix(QQ, [[0, -1, 0], [1, 0, 0], [0, 0, 0]])
assert T1 * T2 - T2 * T1 == T3
assert T2 * T3 - T3 * T2 == T1
assert T3 * T1 - T1 * T3 == T2

print("PASS independent Sage/QQ null split")
print("NULL_KERNEL=10 CONSTRAINT_RANK=4 CONSTRAINED=6 GAUGE=4 PHYSICAL=2")
print("FORMAL_EVEN_LIE_CLOSURE=PASS")
