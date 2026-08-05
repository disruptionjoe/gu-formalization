#!/usr/bin/env sage
"""Independent Sage replay of the selected K77 vacuum/P2-norm gate.

No Python channel-swing implementation is imported.  This reconstructs the
exact split-signature Gauss receiver and the selected exterior/Clifford scalar
action over QQ(i).
"""

from itertools import combinations


K.<ii> = QuadraticField(-1)
N = 14
ETA = (1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
FULL = (1 << N) - 1


def bits(mask):
    return tuple(index for index in range(N) if mask & (1 << index))


def clean(element):
    return {mask: K(value) for mask, value in element.items() if value}


def add(*elements):
    out = {}
    for element in elements:
        for mask, value in element.items():
            out[mask] = out.get(mask, K(0)) + value
    return clean(out)


def scale(value, element):
    return clean({mask: K(value) * coefficient for mask, coefficient in element.items()})


def blade_product(left, right):
    sign = (-1) ** sum(1 for i in bits(left) for j in bits(right) if i > j)
    for index in bits(left & right):
        sign *= ETA[index]
    return left ^^ right, sign


def mul(left, right):
    out = {}
    for left_mask, left_value in left.items():
        for right_mask, right_value in right.items():
            mask, sign = blade_product(left_mask, right_mask)
            out[mask] = out.get(mask, K(0)) + sign * left_value * right_value
    return clean(out)


def blade(indices=(), coefficient=1):
    if isinstance(indices, (Integer, int)):
        indices = (int(indices),)
    return {sum(1 << index for index in indices): K(coefficient)}


def form_clean(form):
    return {mask: clean(value) for mask, value in form.items() if clean(value)}


def form_add(*forms):
    out = {}
    for form in forms:
        for mask, value in form.items():
            out[mask] = add(out.get(mask, {}), value)
    return form_clean(out)


def form_scale(value, form):
    return form_clean({mask: scale(value, coefficient) for mask, coefficient in form.items()})


def wedge_sign(left, right):
    if left & right:
        return 0
    return (-1) ** sum(1 for i in bits(left) for j in bits(right) if i > j)


def coefficient_product(left, right, channel):
    lr = mul(left, right)
    if channel == "raw":
        return lr
    rl = mul(right, left)
    if channel == "comm":
        return add(lr, scale(-1, rl))
    if channel == "symi":
        return scale(ii, add(lr, rl))
    raise ValueError(channel)


def wedge(left, right, channel="raw"):
    out = {}
    for left_mask, left_value in left.items():
        for right_mask, right_value in right.items():
            sign = wedge_sign(left_mask, right_mask)
            if not sign:
                continue
            mask = left_mask | right_mask
            value = scale(sign, coefficient_product(left_value, right_value, channel))
            out[mask] = add(out.get(mask, {}), value)
    return form_clean(out)


def hodge(form):
    out = {}
    for mask, coefficient in form.items():
        complement = FULL ^^ mask
        sign = wedge_sign(mask, complement)
        norm = prod(ETA[index] for index in bits(mask))
        out[complement] = add(out.get(complement, {}), scale(sign * norm, coefficient))
    return form_clean(out)


PHI1 = {1 << index: blade(index) for index in range(N)}
PHI2 = form_scale(K(1) / 2, wedge(PHI1, PHI1))


def shiab(curvature):
    star_curvature = hodge(curvature)
    first = wedge(PHI1, star_curvature, "comm")
    middle = hodge(wedge(PHI2, star_curvature, "symi"))
    second = hodge(wedge(PHI1, middle, "symi"))
    return form_add(first, form_scale(K(-1) / 2, second))


def top_scalar(form):
    return form.get(FULL, {}).get(0, K(0))


def pairing(left, right):
    return top_scalar(wedge(left, right))


raw_tt = wedge(PHI1, PHI1)
raw_shiab = shiab(raw_tt)
assert pairing(PHI1, raw_shiab) == 4368
assert pairing(PHI1, hodge(PHI1)) == 14

R.<t, kappa> = PolynomialRing(QQ, 2)
action = 1456 * t^3 + 7 * kappa * t^2
assert derivative(action, t) == 14 * t * (312 * t + kappa)
assert derivative(action, t)(t=-kappa/312) == 0
assert derivative(action, t, 2)(t=-kappa/312) == -14 * kappa

t_star = K(-1) / 312
T_STAR = form_scale(t_star, PHI1)
TT_STAR = wedge(T_STAR, T_STAR)
S_TT_STAR = shiab(TT_STAR)


def basis(form_index, clifford_mask):
    return {1 << form_index: {clifford_mask: K(1)}}


def directional(direction):
    delta_tt = form_add(wedge(direction, T_STAR), wedge(T_STAR, direction))
    cubic = pairing(direction, form_scale(K(1) / 3, S_TT_STAR))
    cubic += pairing(T_STAR, form_scale(K(1) / 3, shiab(delta_tt)))
    return cubic + pairing(direction, hodge(T_STAR))


assert all(
    directional(basis(form_index, 1 << clifford_index)) == 0
    for form_index in range(N) for clifford_index in range(N)
)
assert all(
    directional(basis(form_index, FULL ^^ (1 << omitted))) == 0
    for form_index in range(N) for omitted in range(N)
)
assert not form_add(S_TT_STAR, hodge(T_STAR))


# Independent Gauss receiver and norm reconstruction.
ETA_H = (1, -1, -1, -1)
ETA_V = (1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
ETA_C = ETA_H + ETA_V
SO_PAIRS = list(combinations(range(14), 2))
DOMAIN = [(mu, pair) for mu in range(4) for pair in SO_PAIRS]
DOMAIN_INDEX = {item: index for index, item in enumerate(DOMAIN)}
II_COORDS = [(mu, nu, a) for mu in range(4) for nu in range(mu, 4) for a in range(10)]
II_INDEX = {item: index for index, item in enumerate(II_COORDS)}

receiver = matrix(QQ, 100, 364, sparse=True)
for column, (mu, pair) in enumerate(DOMAIN):
    left, right = pair
    if left < 4 <= right:
        nu = left
        a = right - 4
        output = II_INDEX[(min(mu, nu), max(mu, nu), a)]
        value = -ETA_H[nu] * ETA_V[a]
        receiver[output, column] += value if mu == nu else QQ(1) / 2 * value

insertion = matrix(QQ, 364, 100, sparse=True)
for column, (mu, nu, a) in enumerate(II_COORDS):
    vertical = 4 + a
    insertion[DOMAIN_INDEX[(mu, (nu, vertical))], column] += -ETA_H[nu] * ETA_V[a]
    if mu != nu:
        insertion[DOMAIN_INDEX[(nu, (mu, vertical))], column] += -ETA_H[mu] * ETA_V[a]

h_domain = diagonal_matrix(QQ, [
    ETA_H[mu] * ETA_C[pair[0]] * ETA_C[pair[1]]
    for mu, pair in DOMAIN
])
h_ii = diagonal_matrix(QQ, [
    (1 if mu == nu else 2) * ETA_H[mu] * ETA_H[nu] * ETA_V[a]
    for mu, nu, a in II_COORDS
])

assert receiver.rank() == 100
assert receiver * insertion == identity_matrix(QQ, 100)
assert insertion.transpose() * h_domain * insertion == h_ii
assert receiver == h_ii.inverse() * insertion.transpose() * h_domain
projector = insertion * receiver
assert projector.rank() == 100 and projector * projector == projector

trace = matrix(QQ, 10, 100, sparse=True)
for a in range(10):
    for mu in range(4):
        trace[a, II_INDEX[(mu, mu, a)]] = ETA_H[mu]
trace_square = trace.transpose() * diagonal_matrix(QQ, ETA_V) * trace
assert h_ii.rank() == 100
assert trace_square.rank() == 10

print("SAGE_INDEPENDENT_SELECTED_K77_VACUUM_P2_NORM_PASS")
print("RAW_CUBIC=4368 MASS_NORM=14")
print("SOURCE_ACTION=1456*t^3+7*kappa_1*t^2")
print("NONZERO_BRANCH=t_star=-kappa_1/312")
print("RADIAL_HESSIAN=-14*kappa_1")
print("PRINTED_ENDPOINT=SPECIAL_BRANCH_ZERO")
print("FULL_II_RANK=100 TRACE_FIRST_RANK=10")
