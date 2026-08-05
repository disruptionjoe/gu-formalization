#!/usr/bin/env sage
"""Independent QQ reconstruction of the K77 receiver and weld identities."""

G = diagonal_matrix(QQ, [1, 1, 1, 1, 1, 1, -1, -1, -1, -1])
eta_c = diagonal_matrix(QQ, [1] * 7 + [-1] * 7)
v_indices = [1, 2, 3, 4, 5, 6, 10, 11, 12, 13]
q = vector(QQ, [0, 0, 0, 0, 0, 0, 1, 0, 0, 0])
q_flat = G * q
q2 = q * G * q

sigma = matrix(QQ, 10, 140)
for i, ambient in enumerate(v_indices):
    for a in range(10):
        sigma[i, 14 * a + ambient] = q[a]

iota = matrix(QQ, 140, 10)
for i, ambient in enumerate(v_indices):
    for a in range(10):
        iota[14 * a + ambient, i] = q_flat[a] / q2

p = iota * sigma
qc = identity_matrix(QQ, 140) - p
h_domain = -G.inverse().tensor_product(eta_c)

assert q2 == -1
assert sigma.rank() == 10
assert sigma * iota == identity_matrix(QQ, 10)
assert p.rank() == 10 and p * p == p
assert qc.rank() == 130 and qc * qc == qc
assert iota.transpose() * h_domain == G * sigma
assert p.transpose() * h_domain == h_domain * p
assert iota.transpose() * h_domain * iota == G

x = vector(QQ, [QQ(((7 * i + 3) % 17) - 8) / 5 for i in range(140)])
r = vector(QQ, [QQ(((11 * i + 1) % 19) - 9) / 7 for i in range(140)])
e = vector(QQ, [QQ(((5 * i + 2) % 13) - 6) / 3 for i in range(10)])
kappa = QQ(7) / 11

pair_d = lambda a, b: a * h_domain * b
pair_v = lambda a, b: a * G * b
xq, rq = qc * x, qc * r
xg, rg = sigma * x, sigma * r

old_linear = pair_d(x, r)
split_linear = pair_d(xq, rq) + pair_v(xg, rg)
old_gain = kappa * pair_d(x, x) / 2
split_gain = kappa * (pair_d(xq, xq) + pair_v(xg, xg)) / 2
assert old_linear == split_linear
assert old_gain == split_gain
assert pair_d(p * x, qc * r) == 0
assert pair_d(qc * x, p * r) == 0

old_action = old_linear + old_gain
weld_old = pair_d(xq, rq) + pair_v(xg, rg) + split_gain
weld_new = pair_d(xq, rq) + pair_v(xg, e) + split_gain
assert weld_old == old_action
assert weld_new - old_action == pair_v(xg, e - rg)

# Independent five-map lower bound for the equivariant Sym2 x Sym2 -> Sym2
# search.  This prevents equivariance from being misreported as uniqueness.
eta4 = diagonal_matrix(QQ, [-1, 1, 1, 1])
sym_basis = []
for i in range(4):
    for j in range(i, 4):
        b = matrix(QQ, 4)
        b[i, j] = 1
        b[j, i] = 1
        sym_basis.append(b)

def tr_g(h):
    return (eta4 * h).trace()

def tr0(h):
    return h - tr_g(h) * eta4 / 4

def maps(h, k):
    h0, k0 = tr0(h), tr0(k)
    pairing = (eta4 * h0 * eta4 * k0).trace()
    jordan = h0 * eta4 * k0 + k0 * eta4 * h0
    return [
        tr_g(h) * tr_g(k) * eta4,
        pairing * eta4,
        tr_g(h) * k0,
        tr_g(k) * h0,
        tr0(jordan),
    ]

columns = [[] for _ in range(5)]
for h in sym_basis:
    for k in sym_basis:
        values = maps(h, k)
        for n, value in enumerate(values):
            columns[n].extend(value[i, j] for i in range(4) for j in range(i, 4))
assert matrix(QQ, columns).rank() == 5

print("PASS: independent QQ receiver rank/right-inverse/projector, Krein isometry, sector weld, and five-map lower bound")
