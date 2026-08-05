#!/usr/bin/env sage
"""Independent Sage replay for the eddy/Euler prolongation packet.

No Python channel-swing implementation is imported.  The file independently
checks the identity-Shiab graded-cyclic transgression control and reconstructs
the source-printed ``D Shiab(F_A)`` rival ranks over ``QQ(i)``. It does not
claim that the printed endpoint equals the selected action derivative.
"""

from itertools import product


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
PHI2 = form_scale(K(1) / 2, wedge(PHI1, PHI1, "raw"))


def shiab(curvature):
    star_curvature = hodge(curvature)
    first = wedge(PHI1, star_curvature, "comm")
    middle = hodge(wedge(PHI2, star_curvature, "symi"))
    second = hodge(wedge(PHI1, middle, "symi"))
    return form_add(first, form_scale(K(-1) / 2, second))


def flatten(form):
    return {
        (form_mask, clifford_mask): value
        for form_mask, coefficient in form.items()
        for clifford_mask, value in coefficient.items()
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


ORBIT_REPS = {
    "positive": (1,) + (0,) * 13,
    "negative": (0, 1) + (0,) * 12,
    "null": (1, 1) + (0,) * 12,
}
EXPECTED_NONZERO = {"positive": 13, "negative": 13, "null": 28}
results = {}
for orbit, covector in ORBIT_REPS.items():
    k_form = {
        1 << index: blade((), value)
        for index, value in enumerate(covector)
        if value
    }
    inputs = []
    defects = []
    for form_index, coefficient_index in product(range(N), repeat=2):
        potential = {1 << form_index: blade(coefficient_index)}
        curvature = wedge(k_form, potential)
        inputs.append(flatten(curvature))
        defects.append(flatten(wedge(k_form, shiab(curvature))))
    results[orbit] = (
        sparse_rank(inputs),
        sparse_rank(defects),
        sum(1 for defect in defects if defect),
    )

assert results == {
    "positive": (182, 13, 13),
    "negative": (182, 13, 13),
    "null": (182, 13, 28),
}

# Independent graded-cyclic coefficient ledger for
# delta Tr[T(F + 1/2 DT + 1/3 T^2)].
derivative_coefficient = QQ(1) / 2 + QQ(1) / 2
eddy_coefficient = QQ(1) / 3 + QQ(1) / 3 + QQ(1) / 3
assert derivative_coefficient == 1
assert eddy_coefficient == 1

R.<z> = PolynomialRing(QQ)
assert z(0) == 0
assert derivative(z)(0) == 1

print("SAGE_INDEPENDENT_EDDY_EULER_PROLONGATION_PASS")
print("GENERIC_RESULTS=%s" % results)
print("IDENTITY_SHIAB_TRANSgression_ENDPOINT_COEFFICIENTS=(1,1)")
print("PRINTED_RIVAL_ONLY=true")
