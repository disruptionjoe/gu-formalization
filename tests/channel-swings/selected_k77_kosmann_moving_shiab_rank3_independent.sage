#!/usr/bin/env sage
"""Independent Sage/QQ(i) certificate for the K77 bivector Ward completion.

No Python channel-swing implementation is imported.  The script rebuilds the
split Clifford algebra, exterior calculus, selected Shiab, its moving-Phi
derivative, and the inverse-Kosmann rank-three causal orbits.
"""

K.<ii> = QuadraticField(-1)
N = 14
ETA = (1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
FULL = (1 << N) - 1
PAIRS4 = [(a, b) for a in range(4) for b in range(a + 1, 4)]


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
    for lm, lc in left.items():
        for rm, rc in right.items():
            mask, sign = blade_product(lm, rm)
            out[mask] = out.get(mask, K(0)) + sign * lc * rc
    return clean(out)


def blade(indices=(), coefficient=1):
    if isinstance(indices, (Integer, int)):
        indices = (int(indices),)
    return {sum(1 << index for index in indices): K(coefficient)}


def comm(left, right):
    return add(mul(left, right), scale(-1, mul(right, left)))


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
    for lm, lc in left.items():
        for rm, rc in right.items():
            sign = wedge_sign(lm, rm)
            if not sign:
                continue
            mask = lm | rm
            out[mask] = add(out.get(mask, {}), scale(sign, coefficient_product(lc, rc, channel)))
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


def shiab(curvature, phi1=PHI1, phi2=PHI2):
    star_curvature = hodge(curvature)
    first = wedge(phi1, star_curvature, "comm")
    middle = hodge(wedge(phi2, star_curvature, "symi"))
    second = hodge(wedge(phi1, middle, "symi"))
    return form_add(first, form_scale(K(-1) / 2, second))


def coefficient_derivative(form, chi):
    return {mask: comm(value, chi) for mask, value in form.items()}


def d_shiab(curvature, chi):
    dphi1 = coefficient_derivative(PHI1, chi)
    dphi2 = coefficient_derivative(PHI2, chi)
    star_curvature = hodge(curvature)
    first = wedge(dphi1, star_curvature, "comm")
    second_left = wedge(dphi1, hodge(wedge(PHI2, star_curvature, "symi")), "symi")
    second_right = wedge(PHI1, hodge(wedge(dphi2, star_curvature, "symi")), "symi")
    return form_add(first, form_scale(K(-1) / 2, hodge(form_add(second_left, second_right))))


def flatten(form):
    return {(fm, cm): coefficient for fm, element in form.items()
            for cm, coefficient in element.items() if coefficient}


def family_rank(forms):
    coordinates = sorted(set().union(*(set(flatten(form)) for form in forms)))
    if not coordinates:
        return 0
    matrix_rows = [[flatten(form).get(coordinate, K(0)) for form in forms]
                   for coordinate in coordinates]
    return matrix(K, matrix_rows).rank()


T = form_scale(K(-1) / 312, PHI1)
F = wedge(T, T)
assert form_add(hodge(shiab(F)), T) == {}


def q_form(q):
    return {1 << mu: blade((), q[mu]) for mu in range(4) if q[mu]}


def eta(q, nu):
    out = {}
    for a, b in PAIRS4:
        coefficient = -K(1) / 2 * (q[a] * (1 if b == nu else 0)
                                    - q[b] * (1 if a == nu else 0))
        if coefficient:
            out = add(out, scale(coefficient, mul(blade(a), blade(b))))
    return out


def principal(q, chi):
    return {1 << mu: scale(q[mu], chi) for mu in range(4) if q[mu]}


def curvature(q, delta_a):
    return form_add(wedge(q_form(q), delta_a), wedge(T, delta_a), wedge(delta_a, T))


orbits = {
    "timelike": (K(1), K(0), K(0), K(0)),
    "spacelike": (K(0), K(1), K(0), K(0)),
    "null": (K(1), K(0), K(0), K(1)),
}
q0 = orbits["timelike"]
results = {}
for name, q in orbits.items():
    chis = [eta(q, nu) for nu in range(4)]
    principals = [principal(q, chi) for chi in chis]
    assert family_rank(principals) == 3
    moving = [hodge(d_shiab(F, chi)) for chi in chis]
    coherent = [hodge(shiab(curvature(q, value))) for value in principals]
    frozen = [hodge(shiab(curvature(q0, value))) for value in principals]
    assert family_rank(coherent) == family_rank(moving) == 3
    assert family_rank([form_add(left, right) for left, right in zip(frozen, moving)]) == 3
    assert family_rank([form_add(left, form_scale(-1, right)) for left, right in zip(frozen, moving)]) == 3

    completed = []
    for column, (chi, first) in enumerate(zip(chis, principals)):
        lower_t = coefficient_derivative(T, chi)
        homogeneous_f = coefficient_derivative(F, chi)
        full_a = form_add(first, lower_t)
        assert form_add(curvature(q, full_a), form_scale(-1, homogeneous_f)) == {}
        total = form_add(
            hodge(shiab(curvature(q, first))),
            hodge(shiab(curvature(q, lower_t))),
            lower_t,
            hodge(d_shiab(F, chi)),
        )
        assert total == {}
        completed.append(total)
    assert family_rank(completed) == 0
    coherent_supports = [len(flatten(value)) for value in coherent]
    frozen_supports = [len(flatten(value)) for value in frozen]
    assert (coherent_supports == frozen_supports) == (name == "timelike")
    results[name] = (coherent_supports, frozen_supports)


# Controls: omit moving Shiab and reverse the lower homogeneous sign.
q = orbits["null"]
chi = eta(q, 0)
first = principal(q, chi)
lower_t = coefficient_derivative(T, chi)
without_moving = form_add(
    hodge(shiab(curvature(q, first))),
    hodge(shiab(curvature(q, lower_t))),
    lower_t,
)
assert without_moving != {}
assert curvature(q, form_add(first, form_scale(-1, lower_t))) != coefficient_derivative(F, chi)

print("SAGE_INDEPENDENT_K77_KOSMANN_MOVING_SHIAB_RANK3_PASS")
print("INTERNAL_ORBIT_RANK=3")
print("MOVING_SHIAB_ALONE=DOES_NOT_CANCEL_FROZEN_Q0_PACKET")
print("FULL_LOWER_ORDER_COMPLETION=RAW_UPSILON_ZERO")
print("MATCHED_Q_VERSUS_FROZEN_Q0=TIMELIKE_SAME_SPACELIKE_NULL_DIFFERENT")
print("SUPPORTS=" + repr(results))
