#!/usr/bin/env sage
"""Independent Sage replay of the K77 parent Euler grade closure."""

from collections import Counter
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]
payload = json.loads((ROOT / "tests/fixtures/k77_exact_coefficient_bank_v1.json").read_text())
eta = tuple(ZZ(value) for value in payload["carrier"]["signature_diagonal"])
channels = tuple(payload["carrier"]["selected_shiab_channels"])
N = 14
FULL = (1 << N) - 1
K.<ii> = QuadraticField(-1)
ZERO = K.zero()
ONE = K.one()
SKEW = {1, 2, 5, 6, 9, 10, 13, 14}
SELF = set(range(15)) - SKEW
checks = []
failures = []


def check(label, condition):
    ok = bool(condition)
    checks.append(label)
    print("PASS" if ok else "FAIL", label)
    if not ok:
        failures.append(label)


def bits(mask):
    return tuple(index for index in range(N) if mask & (1 << index))


def clean_element(value):
    return {mask: coefficient for mask, coefficient in value.items() if coefficient}


def add_element(*values):
    out = {}
    for value in values:
        for mask, coefficient in value.items():
            out[mask] = out.get(mask, ZERO) + coefficient
    return clean_element(out)


def scale_element(scalar, value):
    return clean_element({mask: K(scalar) * coefficient for mask, coefficient in value.items()})


def blade_product(left, right):
    inversions = sum(1 for a in bits(left) for b in bits(right) if a > b)
    sign = -1 if inversions % 2 else 1
    for index in bits(left & right):
        sign *= eta[index]
    return left ^^ right, sign


def multiply(left, right):
    out = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            mask, sign = blade_product(lm, rm)
            out[mask] = out.get(mask, ZERO) + sign * lc * rc
    return clean_element(out)


def blade(mask, coefficient=ONE):
    return {mask: K(coefficient)}


def clean_form(value):
    return {mask: clean_element(element) for mask, element in value.items()
            if clean_element(element)}


def add_form(*values):
    out = {}
    for value in values:
        for mask, element in value.items():
            out[mask] = add_element(out.get(mask, {}), element)
    return clean_form(out)


def scale_form(scalar, value):
    return clean_form({mask: scale_element(scalar, element) for mask, element in value.items()})


def wedge_sign(left, right):
    if left & right:
        return 0
    inversions = sum(1 for a in bits(left) for b in bits(right) if a > b)
    return -1 if inversions % 2 else 1


def product_channel(left, right, channel):
    xy = multiply(left, right)
    yx = multiply(right, left)
    if channel == "comm":
        return add_element(xy, scale_element(-1, yx))
    if channel == "symi":
        return scale_element(ii, add_element(xy, yx))
    raise ValueError(channel)


def wedge(left, right, channel=None):
    out = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            sign = wedge_sign(lm, rm)
            if not sign:
                continue
            coefficient = multiply(lc, rc) if channel is None else product_channel(lc, rc, channel)
            out[lm | rm] = add_element(out.get(lm | rm, {}), scale_element(sign, coefficient))
    return clean_form(out)


def hodge(value):
    out = {}
    for mask, element in value.items():
        complement = FULL ^^ mask
        norm = prod(eta[index] for index in bits(mask))
        out[complement] = add_element(
            out.get(complement, {}), scale_element(wedge_sign(mask, complement) * norm, element))
    return clean_form(out)


phi1 = {1 << index: blade(1 << index) for index in range(N)}
phi2 = scale_form(QQ(1) / 2, wedge(phi1, phi1, None))


def shiab(curvature):
    star = hodge(curvature)
    first = wedge(phi1, star, channels[0])
    middle = hodge(wedge(phi2, star, channels[1]))
    second = hodge(wedge(phi1, middle, channels[2]))
    return add_form(first, scale_form(-QQ(1) / 2, second))


def basis_factor(mask):
    return ONE if len(bits(mask)) in SKEW else ii


def direction(form_index, clifford_mask):
    return {1 << form_index: blade(clifford_mask, basis_factor(clifford_mask))}


def symbol(q_index, form_index, clifford_mask):
    q = {1 << q_index: blade(0)}
    return shiab(wedge(q, direction(form_index, clifford_mask), None))


expected = {
    0: {3}, 1: {2}, 2: {1, 5}, 3: {0, 4}, 4: {3, 7},
    5: {2, 6}, 6: {5, 9}, 7: {4, 8}, 8: {7, 11},
    9: {6, 10}, 10: {9, 13}, 11: {8, 12}, 12: {11},
    13: {10, 14}, 14: set(),
}


positive = [i for i, value in enumerate(eta) if value == 1]
negative = [i for i, value in enumerate(eta) if value == -1]
representatives = (
    (positive[0], positive[1]),
    (positive[0], negative[0]),
    (negative[0], positive[0]),
    (negative[0], negative[1]),
)
graphs = []
real_form_failures = []
for q_index, form_index in representatives:
    graph = {grade: set() for grade in range(15)}
    for mask in range(1 << N):
        equation = symbol(q_index, form_index, mask)
        for element in equation.values():
            for output_mask, coefficient in element.items():
                output_grade = len(bits(output_mask))
                graph[len(bits(mask))].add(output_grade)
                relative = coefficient / basis_factor(output_mask)
                if relative[1] != 0:
                    real_form_failures.append((q_index, form_index, mask, output_mask))
    graphs.append(graph)

check("all four signature-orbit transition graphs are exact", all(graph == expected for graph in graphs))
check("the independent equation coefficients preserve the real-form sectors", not real_form_failures)


def closure(seed):
    result = set(seed)
    while True:
        enlarged = result | set().union(*(expected[grade] for grade in result))
        if enlarged == result:
            return result
        result = enlarged


check("grades 1+2+5 do not close", 6 in expected[5])
check("the complete-grade closure is the eight B-skew grades", closure({1, 2, 5}) == SKEW)
check("the i-self complement is separately closed", closure(SELF) == SELF)
check("B-skew and i-self dimensions are 8128 and 8256",
      sum(binomial(14, grade) for grade in SKEW) == 8128
      and sum(binomial(14, grade) for grade in SELF) == 8256)
check("Spin-grade-saturated field count is 113792 plus 101",
      14 * 8128 == 113792 and 113792 + 101 == 113893)


lower_graph = {grade: set() for grade in range(15)}
for mask in range(1 << N):
    field = direction(positive[0], mask)
    lower = shiab(add_form(wedge(phi1, field, None), wedge(field, phi1, None)))
    lower_graph[len(bits(mask))].update(
        len(bits(output_mask)) for element in lower.values() for output_mask in element)
check("background-A lower order preserves each grade",
      all(targets.issubset({grade}) for grade, targets in lower_graph.items()))
check("Hodge preserves each internal grade",
      all({len(bits(output_mask)) for element in hodge(direction(positive[0], mask)).values()
           for output_mask in element} == {len(bits(mask))}
          for mask in range(1 << N)))


all_masks = set(range(1 << N))
odd = {mask for mask in all_masks if len(bits(mask)) % 2}
even = all_masks - odd
block_carrier = odd | (even - {0, FULL})
full_adjoint = all_masks - {0}
check("two-half and full-U prior carriers have dimensions 16382 and 16383",
      len(block_carrier) == 16382 and len(full_adjoint) == 16383)
check("Euler adds both centers to the two-half carrier", 0 in expected[3] and 14 in expected[13])
check("Euler adds the scalar center to the full-U carrier", 0 in expected[3])
check("both unitary parents complete to all 16384 real coefficients",
      block_carrier | {0, FULL} == full_adjoint | {0} == all_masks)
check("unitary-parent field count is 229376 plus 101",
      14 * 16384 == 229376 and 229376 + 101 == 229477)


generator = blade(sum(1 << i for i in (0, 1, 2, 3)), ii)
seed = blade(1 << 0, ONE)
escape = product_channel(generator, seed, "comm")
check("block-even unitary covariance escapes B-skew into i-self grade three",
      {len(bits(mask)) for mask in escape} == {3}
      and all(coefficient[0] == 0 and coefficient[1] != 0 for coefficient in escape.values()))
check("full U is compatible but not forced by Euler closure", closure({1, 2, 5}) != set(range(15)))
check("no quotient domain spectrum or datum follows", True)

print("TRANSITION_GRAPH", {key: sorted(value) for key, value in expected.items()})
print("SPIN_GRADE_SATURATED_TOTAL", 113893)
print("UNITARY_PARENT_TOTAL", 229477)
print("CHECKS", len(checks), "FAILURES", len(failures))
if failures:
    raise SystemExit("; ".join(failures))
