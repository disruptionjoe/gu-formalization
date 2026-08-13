#!/usr/bin/env sage
"""Independent QQ certificate for the matched-q physical diffeomorphism split."""

from itertools import combinations

K = QQ
ETA = diagonal_matrix(K, [1, -1, -1, -1])
SLOTS = [(i, j) for i in range(4) for j in range(i, 4)]


def sym_basis():
    out = []
    for i, j in SLOTS:
        value = matrix(K, 4, 4)
        value[i, j] = 1
        value[j, i] = 1
        out.append(value)
    return out


SYM = sym_basis()


def sym_coords(value):
    return vector(K, [value[i, j] for i, j in SLOTS])


def sym_rep(b):
    return matrix(K, 10, 10, lambda i, j: sym_coords(b.transpose() * SYM[j] + SYM[j] * b)[i])


def dewitt(ginv):
    return matrix(K, 10, 10, lambda i, j:
        (ginv * SYM[i] * ginv * SYM[j]).trace()
        - K(1) / 2 * (ginv * SYM[i]).trace() * (ginv * SYM[j]).trace())


def d_dewitt(ginv, h):
    dinv = -ginv * h * ginv
    return matrix(K, 10, 10, lambda i, j:
        (dinv * SYM[i] * ginv * SYM[j] + ginv * SYM[i] * dinv * SYM[j]).trace()
        - K(1) / 2 * ((dinv * SYM[i]).trace() * (ginv * SYM[j]).trace()
                      + (ginv * SYM[i]).trace() * (dinv * SYM[j]).trace()))


def block_diag(left, right):
    out = matrix(K, left.nrows() + right.nrows(), left.ncols() + right.ncols())
    out[:left.nrows(), :left.ncols()] = left
    out[left.nrows():, left.ncols():] = right
    return out


def sequence_sign(values):
    if len(set(values)) != len(values):
        return 0
    inversions = sum(values[a] > values[b] for a in range(len(values)) for b in range(a + 1, len(values)))
    return -1 if inversions % 2 else 1


def exterior_rep(linear, degree):
    basis = list(combinations(range(linear.nrows()), degree))
    position = {item: i for i, item in enumerate(basis)}
    out = matrix(K, len(basis), len(basis))
    for column, item in enumerate(basis):
        for slot, old in enumerate(item):
            for new in range(linear.nrows()):
                coefficient = linear[new, old]
                if coefficient == 0:
                    continue
                changed = list(item)
                changed[slot] = new
                sign = sequence_sign(changed)
                if sign:
                    out[position[tuple(sorted(changed))], column] += sign * coefficient
    return out


def hodge1(metric):
    inverse = metric.inverse()
    volume = 8
    basis_out = list(combinations(range(14), 13))
    position = {item: i for i, item in enumerate(basis_out)}
    out = matrix(K, 14, 14)
    for i in range(14):
        complement = tuple(j for j in range(14) if j != i)
        sign = sequence_sign((i,) + complement)
        for column in range(14):
            out[position[complement], column] = sign * volume * inverse[i, column]
    return out


def dhodge1(metric, h):
    inverse = metric.inverse()
    dinverse = -inverse * h * inverse
    volume = 8
    dvolume = volume * K(1) / 2 * (inverse * h).trace()
    basis_out = list(combinations(range(14), 13))
    position = {item: i for i, item in enumerate(basis_out)}
    out = matrix(K, 14, 14)
    for i in range(14):
        complement = tuple(j for j in range(14) if j != i)
        sign = sequence_sign((i,) + complement)
        for column in range(14):
            out[position[complement], column] = sign * (dvolume * inverse[i, column] + volume * dinverse[i, column])
    return out


GV = dewitt(ETA)
G = block_diag(ETA, GV)
assert G.det() == -64
x = polygen(K)
assert G.charpoly(x) == (x^2 - 1)^4 * (x^2 - 4)^3
STAR1 = hodge1(G)
CAUSAL = {
    "timelike": vector(K, [1, 0, 0, 0]),
    "spacelike": vector(K, [0, 1, 0, 0]),
    "null": vector(K, [1, 0, 0, 1]),
}
J = matrix(K, 10, 4, lambda i, j: K((((i + 2) * (j + 3)) % 7) - 3) / 5)
L = block_matrix([[identity_matrix(K, 4)], [J]])
R = block_matrix([[identity_matrix(K, 4), zero_matrix(K, 4, 10)]])
assert R * L == identity_matrix(K, 4)

summary = {}
for name, q in CAUSAL.items():
    bs = []
    skews = []
    syms = []
    vs = []
    hodge_live = 0
    leaks = 0
    for nu in range(4):
        xi = identity_matrix(K, 4).column(nu)
        b = xi.column() * q.row()
        badj = ETA * b.transpose() * ETA
        skew = K(1) / 2 * (b - badj)
        sym = K(1) / 2 * (b + badj)
        v = sym_rep(b)
        hb = b.transpose() * ETA + ETA * b
        hv = d_dewitt(ETA, hb)
        h = block_diag(hb, hv)
        a = block_diag(-b, v)
        assert h + a.transpose() * G + G * a == 0
        assert K(1) / 2 * (G.inverse() * h).trace() + a.trace() == 0
        pull = a.transpose()
        direct = dhodge1(G, h)
        rhs = STAR1 * exterior_rep(pull, 1) - exterior_rep(pull, 13) * STAR1
        assert direct == rhs
        hodge_live += int(direct != 0)
        ah = -b
        atotal = block_diag(ah, v)
        dj = v * J - J * ah
        dl = block_matrix([[zero_matrix(K, 4, 4)], [dj]])
        assert atotal * L - L * ah - dl == 0
        leak = (identity_matrix(K, 14) - L * R) * (atotal * L - L * ah)
        leaks += int(leak != 0)
        bs.append(b)
        skews.append(skew)
        syms.append(sym)
        vs.append(v)
    flat = lambda mats: matrix(K, 16, 4, lambda i, j: mats[j].list()[i])
    assert flat(bs).rank() == 4
    assert flat(skews).rank() == 3
    assert flat(syms).rank() == 4
    assert matrix(K, 100, 4, lambda i, j: vs[j].list()[i]).rank() == 4
    qsharp = ETA * q
    kernel = flat(skews).right_kernel().basis()
    assert len(kernel) == 1 and matrix(K, 4, 2, lambda i, j: kernel[0][i] if j == 0 else qsharp[i]).rank() == 1
    assert hodge_live > 0 and leaks > 0
    summary[name] = (4, 3, 4, hodge_live, leaks)

print("SAGE_INDEPENDENT_K77_PHYSICAL_DIFFEO_SPLIT_PASS")
print("RANKS=PHYSICAL4_KOSMANN3_SYMMETRIC4")
print("DENSITY_HODGE_OBSERVATION=NATURAL_EXACT")
print("FROZEN_OBSERVATION_LEAK=LIVE")
print("SUMMARY=" + repr(summary))
