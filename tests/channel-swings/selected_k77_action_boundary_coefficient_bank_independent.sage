#!/usr/bin/env sage
"""Independent Sage reconstruction of the selected K77 boundary bank."""

from itertools import combinations

K.<ii> = QuadraticField(-1)
N = 14
ETA = (1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
FULL = (1 << N) - 1
ZERO = K(0)
FAIL = []
COUNTS = {"exact": 0, "planted": 0, "type": 0}


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(("PASS" if ok else "FAIL") + " [" + kind + "] " + label)
    if not ok:
        FAIL.append(label)


def inds(mask):
    return tuple(i for i in range(N) if mask & (1 << i))


def clean(element):
    return {mask: value for mask, value in element.items() if value != ZERO}


def eadd(*elements):
    out = {}
    for element in elements:
        for mask, value in element.items():
            out[mask] = out.get(mask, ZERO) + value
    return clean(out)


def escale(scalar, element):
    return clean({mask: K(scalar) * value for mask, value in element.items()})


def blade_product(left, right):
    inversions = sum(a > b for a in inds(left) for b in inds(right))
    sign = -1 if inversions % 2 else 1
    for index in inds(left & right):
        sign *= ETA[index]
    return left ^^ right, sign


def emul(left, right):
    out = {}
    for left_mask, left_value in left.items():
        for right_mask, right_value in right.items():
            mask, sign = blade_product(left_mask, right_mask)
            out[mask] = out.get(mask, ZERO) + sign * left_value * right_value
    return clean(out)


def blade(indices, coefficient=1):
    if isinstance(indices, (int, Integer)):
        indices = (int(indices),)
    return {sum(1 << i for i in indices): K(coefficient)}


def fclean(form):
    return {mask: clean(value) for mask, value in form.items() if clean(value)}


def fadd(*forms):
    out = {}
    for form in forms:
        for mask, value in form.items():
            out[mask] = eadd(out.get(mask, {}), value)
    return fclean(out)


def fscale(scalar, form):
    return fclean({mask: escale(scalar, value) for mask, value in form.items()})


def wedge_sign(left, right):
    if left & right:
        return 0
    return -1 if sum(a > b for a in inds(left) for b in inds(right)) % 2 else 1


def coeff_product(left, right, channel):
    xy, yx = emul(left, right), emul(right, left)
    if channel == "comm":
        return eadd(xy, escale(-1, yx))
    if channel == "symi":
        return escale(ii, eadd(xy, yx))
    raise ValueError(channel)


def wedge(left, right, channel=None):
    out = {}
    for lm, lv in left.items():
        for rm, rv in right.items():
            sign = wedge_sign(lm, rm)
            if not sign:
                continue
            value = emul(lv, rv) if channel is None else coeff_product(lv, rv, channel)
            out[lm | rm] = eadd(out.get(lm | rm, {}), escale(sign, value))
    return fclean(out)


def hodge(form):
    out = {}
    for mask, value in form.items():
        comp = FULL ^^ mask
        norm = prod(ETA[i] for i in inds(mask))
        out[comp] = eadd(out.get(comp, {}), escale(wedge_sign(mask, comp) * norm, value))
    return fclean(out)


phi1 = {1 << i: blade(i) for i in range(N)}
phi2 = fscale(QQ(1) / 2, wedge(phi1, phi1))


def shiab(curvature):
    star = hodge(curvature)
    first = wedge(phi1, star, "comm")
    middle = hodge(wedge(phi2, star, "symi"))
    second = hodge(wedge(phi1, middle, "symi"))
    return fadd(first, fscale(-QQ(1) / 2, second))


def top(form):
    return form.get(FULL, {}).get(0, ZERO)


def pairing(left, right):
    return top(wedge(left, right))


def direction(slot, coefficient):
    return {1 << slot: coefficient}


def packet(B, T):
    return fadd(wedge(B, B),
                fscale(QQ(1) / 2, fadd(wedge(B, T), wedge(T, B))),
                fscale(QQ(1) / 3, wedge(T, T)))


B = {}
T = {}
for i in range(N):
    B[1 << i] = blade(tuple(sorted(((i + 1) % N, (i + 2) % N))), i % 3 + 1)
    T[1 << i] = blade((2 * i + 2) % N, i % 5 + 1)

P = packet(B, T)
SP = shiab(P)


def e_b(d):
    dP = fadd(wedge(d, B), wedge(B, d),
              fscale(QQ(1) / 2, fadd(wedge(d, T), wedge(T, d))))
    return pairing(T, shiab(dP))


def e_t(d):
    dP = fadd(fscale(QQ(1) / 2, fadd(wedge(B, d), wedge(d, B))),
              fscale(QQ(1) / 3, fadd(wedge(d, T), wedge(T, d))))
    mass = pairing(d, hodge(T)) + pairing(T, hodge(d))
    return pairing(d, SP) + pairing(T, shiab(dP)) + mass / 2


coefficients = [blade(i) for i in range(N)]
masks = [1 << i for i in range(N)]
for i, j in combinations(range(N), 2):
    coefficients.append(blade((i, j)))
    masks.append((1 << i) | (1 << j))

bank_k = [[e_b(direction(a, c)) - e_t(direction(a, c)) for c in coefficients]
          for a in range(N)]
check("exact", "all reconstructed coefficients are real",
      all(value.imag() == 0 for row in bank_k for value in row))
bank = matrix(QQ, [[QQ(value.real()) for value in row] for row in bank_k])
normal = bank[4:14, :]
supports = tuple(sum(value != 0 for value in row) for row in bank.rows())
check("exact", "full action bank rank is fourteen", bank.rank() == 14)
check("exact", "normal action bank rank is ten", normal.rank() == 10)
check("exact", "normal support fingerprint agrees",
      supports[4:] == (13, 14, 12, 16, 13, 16, 13, 12, 5, 8))
check("exact", "selected cubic and mass fingerprints agree",
      pairing(T, SP) == 176 and pairing(T, hodge(T)) == -24)

metric_signs = [blade_product(mask, mask)[1] for mask in masks]
metric = diagonal_matrix(QQ, metric_signs)
gram = normal * metric * normal.transpose()
check("exact", "raw inherited Gram is nondegenerate", gram.rank() == 10)
check("exact", "raw inherited Gram determinant agrees",
      gram.det() == QQ(8820818455167586715744550671819374592) / 43046721)

J = matrix(QQ, 10, 4, lambda i, j: QQ(((i + 2) * (j + 3)) % 11 - 5) / 7)
O = block_matrix(QQ, [[identity_matrix(QQ, 4), zero_matrix(QQ, 4, 10)],
                      [-J, identity_matrix(QQ, 10)]])
Oinv = block_matrix(QQ, [[identity_matrix(QQ, 4), zero_matrix(QQ, 4, 10)],
                         [J, identity_matrix(QQ, 10)]])
observed = O * bank
observed_normal = observed[4:14, :]
observed_gram = observed_normal * metric * observed_normal.transpose()
check("exact", "observation equation dual has the stated inverse", Oinv * O == 1)
check("exact", "observation exactly recovers the full bank", Oinv * observed == bank)
check("exact", "observed normal bank remains rank ten", observed_normal.rank() == 10)
check("exact", "observed inherited Gram determinant agrees",
      observed_gram.det() == -QQ(352524857398662429170969678579148520580096) / 1688134559643)

check("type", "orientation reverses the covector and preserves its Gram",
      (-observed_normal) * metric * (-observed_normal).transpose() == observed_gram)
check("planted", "PLANT deleting one normal row drops rank", observed_normal[:9, :].rank() == 9)
check("planted", "PLANT tangential pullback cannot retain ten normal rows", bank[:4, :].rank() == 4)

print("RESULT=INDEPENDENT_SAGE_ACTION_BANK_AND_OBSERVATION_RECONSTRUCTION")
print("SUPPORTS=" + ",".join(str(value) for value in supports[4:]))
print("COUNTS=" + ",".join(key + ":" + str(value) for key, value in sorted(COUNTS.items())))
print("PASS " + str(sum(COUNTS.values()) - len(FAIL)) + "/" + str(sum(COUNTS.values())))
if FAIL:
    raise SystemExit("failures: " + "; ".join(FAIL))
