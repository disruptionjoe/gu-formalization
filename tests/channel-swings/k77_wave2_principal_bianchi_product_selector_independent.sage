#!/usr/bin/env sage
"""Independent Sage replay of the K77 principal-Bianchi product selector.

This file does not import the Python exterior/Clifford implementation.  It
rebuilds the exact ``Cl(7,7)`` blade algebra, Hodge star, invariant ``Phi1`` and
``Phi2``, all eight product Shiabs, the three principal-covector orbit banks,
and the scalar/Ricci/Weyl controls over ``QQ(i)``.
"""

from itertools import combinations, combinations_with_replacement, product


K.<ii> = QuadraticField(-1)
N = 14
ETA = (1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
FULL = (1 << N) - 1
PAIRS = list(combinations(range(N), 2))
SYMMETRIC = list(combinations_with_replacement(range(N), 2))
CHANNELS = list(product(("comm", "symi"), repeat=3))


def bits(mask):
    return tuple(i for i in range(N) if mask & (1 << i))


def clean(x):
    return {m: K(c) for m, c in x.items() if c != 0}


def add(*xs):
    out = {}
    for x in xs:
        for m, c in x.items():
            out[m] = out.get(m, K(0)) + c
    return clean(out)


def scale(c, x):
    return clean({m: K(c) * v for m, v in x.items()})


def blade_product(left, right):
    sign = (-1) ** sum(1 for i in bits(left) for j in bits(right) if i > j)
    for i in bits(left & right):
        sign *= ETA[i]
    return left ^^ right, sign


def mul(x, y):
    out = {}
    for mx, cx in x.items():
        for my, cy in y.items():
            mask, sign = blade_product(mx, my)
            out[mask] = out.get(mask, K(0)) + sign * cx * cy
    return clean(out)


def blade(indices=(), coefficient=1):
    if isinstance(indices, Integer) or isinstance(indices, int):
        indices = (int(indices),)
    return {sum(1 << i for i in indices): K(coefficient)}


def form_clean(x):
    return {m: clean(c) for m, c in x.items() if clean(c)}


def form_add(*xs):
    out = {}
    for x in xs:
        for m, c in x.items():
            out[m] = add(out.get(m, {}), c)
    return form_clean(out)


def form_scale(c, x):
    return form_clean({m: scale(c, value) for m, value in x.items()})


def wedge_sign(left, right):
    if left & right:
        return 0
    return (-1) ** sum(1 for i in bits(left) for j in bits(right) if i > j)


def coefficient_product(x, y, channel):
    xy = mul(x, y)
    if channel == "raw":
        return xy
    yx = mul(y, x)
    if channel == "comm":
        return add(xy, scale(-1, yx))
    if channel == "symi":
        return scale(ii, add(xy, yx))
    raise ValueError(channel)


def wedge(x, y, channel="raw"):
    out = {}
    for mx, cx in x.items():
        for my, cy in y.items():
            sign = wedge_sign(mx, my)
            if not sign:
                continue
            mask = mx | my
            value = scale(sign, coefficient_product(cx, cy, channel))
            out[mask] = add(out.get(mask, {}), value)
    return form_clean(out)


def hodge(x):
    out = {}
    for mask, coefficient in x.items():
        complement = FULL ^^ mask
        sign = wedge_sign(mask, complement)
        norm = prod(ETA[i] for i in bits(mask))
        out[complement] = add(
            out.get(complement, {}), scale(sign * norm, coefficient)
        )
    return form_clean(out)


PHI1 = {1 << i: blade(i) for i in range(N)}
PHI2 = form_scale(K(1) / 2, wedge(PHI1, PHI1, "raw"))


def shiab(curvature, channels):
    first_channel, inner_channel, outer_channel = channels
    star_curvature = hodge(curvature)
    first = wedge(PHI1, star_curvature, first_channel)
    middle = hodge(wedge(PHI2, star_curvature, inner_channel))
    second = hodge(wedge(PHI1, middle, outer_channel))
    return form_add(first, form_scale(K(-1) / 2, second))


def flatten(form):
    return {
        (fm, cm): value
        for fm, coefficient in form.items()
        for cm, value in coefficient.items()
        if value
    }


def sparse_rank(columns):
    pivots = {}
    for column in columns:
        value = dict(column)
        while value:
            pivot = min(value)
            if pivot not in pivots:
                lead = value[pivot]
                pivots[pivot] = {
                    row: coefficient / lead
                    for row, coefficient in value.items()
                    if coefficient / lead
                }
                break
            lead = value[pivot]
            for row, coefficient in pivots[pivot].items():
                updated = value.get(row, K(0)) - lead * coefficient
                if updated:
                    value[row] = updated
                elif row in value:
                    del value[row]
    return len(pivots)


def symmetric_value(p, q, i, j):
    return ZZ((i, j) == (p, q) or (p != q and (i, j) == (q, p)))


def principal_tensor(k, p, q):
    def tensor(i, j, a, b):
        s = lambda x, y: symmetric_value(p, q, x, y)
        return (
            k[i] * k[a] * s(j, b)
            - k[i] * k[b] * s(j, a)
            - k[j] * k[a] * s(i, b)
            + k[j] * k[b] * s(i, a)
        )
    return tensor


def spin_injection(tensor):
    out = {}
    for i, j in PAIRS:
        coefficient = {}
        for a, b in PAIRS:
            value = ETA[a] * ETA[b] * tensor(i, j, a, b)
            if value:
                coefficient = add(
                    coefficient,
                    scale(value, mul(blade(a), blade(b))),
                )
        if coefficient:
            out[(1 << i) | (1 << j)] = coefficient
    return out


def covector_form(k):
    return {1 << i: blade((), value) for i, value in enumerate(k) if value}


ORBIT_REPS = {
    "positive": (1,) + (0,) * 13,
    "negative": (0, 1) + (0,) * 12,
    "null": (1, 1) + (0,) * 12,
}

passes_by_orbit = {}
jet_ranks = {}
defect_columns = [dict() for _ in CHANNELS]
case_index = 0
for orbit, k in ORBIT_REPS.items():
    bank = [spin_injection(principal_tensor(k, p, q)) for p, q in SYMMETRIC]
    bank = [curvature for curvature in bank if curvature]
    jet_ranks[orbit] = sparse_rank([flatten(curvature) for curvature in bank])
    k_form = covector_form(k)
    passes = []
    for channel_index, channel in enumerate(CHANNELS):
        passed = True
        for curvature in bank:
            defect = wedge(k_form, shiab(curvature, channel), "raw")
            passed = passed and not defect
        if passed:
            passes.append(channel)
    passes_by_orbit[orbit] = tuple(passes)
    for curvature in bank:
        for channel_index, channel in enumerate(CHANNELS):
            defect = flatten(wedge(k_form, shiab(curvature, channel), "raw"))
            for (fm, cm), value in defect.items():
                defect_columns[channel_index][(case_index, fm, cm)] = value
        case_index += 1


def metric(i, j):
    return ETA[i] if i == j else 0


def scalar_tensor(i, j, a, b):
    return metric(i, a) * metric(j, b) - metric(i, b) * metric(j, a)


TRACELESS = {(0, 0): 1, (1, 1): 1}


def ricci_tensor(i, j, a, b):
    s = lambda x, y: TRACELESS.get((x, y), 0)
    return K(1) / (N - 2) * (
        s(i, a) * metric(j, b) + s(j, b) * metric(i, a)
        - s(i, b) * metric(j, a) - s(j, a) * metric(i, b)
    )


WEYL = {(4, 5): 1, (4, 6): -1, (5, 7): -1, (6, 7): 1}


def weyl_tensor(i, j, a, b):
    left = (i, j) if i < j else (j, i)
    right = (a, b) if a < b else (b, a)
    if left != right:
        return 0
    return (1 if i < j else -1) * (1 if a < b else -1) * WEYL.get(left, 0)


def ricci(tensor, j, b):
    return sum(ETA[i] * tensor(i, j, i, b) for i in range(N))


def scalar(tensor):
    return sum(ETA[j] * ricci(tensor, j, j) for j in range(N))


def symmetric_output(h):
    one = {}
    for i in range(N):
        coefficient = {}
        for j in range(N):
            value = h(i, j)
            if value:
                coefficient = add(coefficient, scale(ETA[j] * value, blade(j)))
        if coefficient:
            one[1 << i] = coefficient
    return hodge(one)


def einstein_output(tensor):
    scal = scalar(tensor)
    return symmetric_output(
        lambda i, j: ricci(tensor, i, j) - K(1) / 2 * scal * metric(i, j)
    )


fixtures = tuple(spin_injection(t) for t in (scalar_tensor, ricci_tensor, weyl_tensor))
expected_passers = (
    ("comm", "symi", "symi"),
    ("symi", "comm", "comm"),
    ("symi", "comm", "symi"),
    ("symi", "symi", "comm"),
)
selected = ("comm", "symi", "symi")
unique_nonzero = tuple(
    channel for channel in CHANNELS
    if channel in expected_passers and any(shiab(curvature, channel) for curvature in fixtures)
)
einstein_match = all(
    not form_add(
        shiab(spin_injection(tensor), selected),
        form_scale(2, einstein_output(tensor)),
    )
    for tensor in (scalar_tensor, ricci_tensor)
)

assert jet_ranks == {"positive": 91, "negative": 91, "null": 91}
assert all(value == expected_passers for value in passes_by_orbit.values())
assert sparse_rank(defect_columns) == 1
assert unique_nonzero == (selected,)
assert einstein_match
assert not shiab(spin_injection(weyl_tensor), selected)

print("JET_RANKS", jet_ranks)
print("BIANCHI_PASSERS", expected_passers)
print("BIANCHI_DEFECT_RANK", sparse_rank(defect_columns))
print("UNIQUE_NONZERO", selected)
print("EINSTEIN14_SCALE", -2)
print("WEYL_RESPONSE", 0)
print("SAGE_INDEPENDENT_SELECTOR_PASS")
