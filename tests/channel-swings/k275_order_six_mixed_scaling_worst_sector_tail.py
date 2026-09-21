#!/usr/bin/env python3
"""K275: complete mixed-scaling face scan and global K218 tail bound."""
from __future__ import annotations

import argparse
from collections import Counter
from decimal import Decimal, getcontext
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
import sys

from k225_order_six_diagonal_cancellation import terms

sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parents[2]
PROCESS = ROOT / "lab/process"
K185 = PROCESS / "k185-order-six-duffy-face-tail-wave.json"
K215 = PROCESS / "k215-order-six-angular-integrated-auxiliary-tail.json"
K218 = PROCESS / "k218-order-six-exact-angular-elimination.json"
K225 = PROCESS / "k225-order-six-diagonal-cancellation.json"
K274 = PROCESS / "k274-order-six-one-axis-exact-integration-pilot.json"
OUT = PROCESS / "k275-order-six-mixed-scaling-worst-sector-tail.json"

AXES = 8
DENOMINATORS = 14
FACES = range(1, 1 << AXES)
TARGET = Q(1, 10**21)
PI_LOWER = Q(31, 10)
LOG2_UPPER = Q(7, 10)
GENERIC_COSHES = (
    Q(5, 4), Q(17, 8), Q(9, 8), Q(13, 8),
    Q(21, 8), Q(25, 8), Q(29, 8), Q(33, 8),
)


def face_margin(masks: tuple[int, ...], face: int) -> int:
    touched = 0
    for axis in range(AXES):
        if face & (1 << axis):
            touched |= masks[axis]
    return touched.bit_count() - face.bit_count()


def margin_certificate(items: list[tuple[int, tuple[int, ...]]]) -> dict:
    term_minima = Counter()
    face_minima: dict[int, int] = {}
    face_minimum_counts: dict[int, int] = {}
    checks = 0
    for _, masks in items:
        assert len(masks) == AXES
        assert all(0 < mask < 1 << DENOMINATORS for mask in masks)
        assert (masks[0] | masks[1] | masks[2] | masks[3]
                | masks[4] | masks[5] | masks[6] | masks[7]) == (1 << DENOMINATORS) - 1
        minimum = DENOMINATORS
        for face in FACES:
            margin = face_margin(masks, face)
            checks += 1
            assert margin >= 1
            minimum = min(minimum, margin)
            if face not in face_minima or margin < face_minima[face]:
                face_minima[face] = margin
                face_minimum_counts[face] = 1
            elif margin == face_minima[face]:
                face_minimum_counts[face] += 1
        term_minima[minimum] += 1
    worst_faces = {
        str(face.bit_length() - 1): face_minimum_counts[face]
        for face in FACES
        if face_minima[face] == 1 and face.bit_count() == 1
    }
    assert set(worst_faces) == {"2", "3", "4", "5", "6", "7"}
    assert all(face_minima[face] >= 2 for face in FACES if face.bit_count() >= 2)
    return {
        "term_face_checks": checks,
        "global_minimum_margin": min(face_minima.values()),
        "term_minimum_margin_histogram": {
            str(margin): term_minima[margin] for margin in sorted(term_minima)
        },
        "worst_singleton_face_term_counts": worst_faces,
        "minimum_over_nonsingleton_faces": min(
            face_minima[face] for face in FACES if face.bit_count() >= 2
        ),
    }


def leading_face_coefficient(
    items: list[tuple[int, tuple[int, ...]]], axis: int
) -> Q:
    """Limit c_axis times the K218 integrand without its common constant/pi^8."""
    total = Q(0)
    other_measure = Q(1)
    for other, value in enumerate(GENERIC_COSHES):
        if other != axis:
            other_measure *= value
    for weight, masks in items:
        touched = masks[axis]
        if touched.bit_count() != 2:
            continue
        denominator = Q(1)
        for load_index in range(DENOMINATORS):
            if touched & (1 << load_index):
                continue
            load = Q(256) + sum(
                (GENERIC_COSHES[other] for other in range(AXES)
                 if other != axis and masks[other] & (1 << load_index)),
                Q(0),
            )
            denominator *= load
        total += Q(weight, denominator)
    return other_measure * total


def tail_polynomial(dyadic_m: int) -> Q:
    upper_t = LOG2_UPPER * dyadic_m
    return sum((upper_t**degree / factorial(degree) for degree in range(AXES)), Q(0))


def tail_bound(coefficient: Q, dyadic_m: int) -> Q:
    return coefficient * tail_polynomial(dyadic_m) / 2**dyadic_m


def decimal_string(value: Q, digits: int = 24) -> str:
    getcontext().prec = digits
    return str(Decimal(value.numerator) / Decimal(value.denominator))


def generate() -> dict:
    source = json.loads(K185.read_text())
    k215 = json.loads(K215.read_text())
    k274 = json.loads(K274.read_text())
    items = list(terms(source))
    assert len(items) == 1864
    assert len({masks for _, masks in items}) == 1276
    sum_abs_weights = sum(abs(weight) for weight, _ in items)
    assert sum_abs_weights == 2928

    margins = margin_certificate(items)
    assert margins["term_face_checks"] == 1864 * 255
    assert margins["global_minimum_margin"] == 1
    assert margins["term_minimum_margin_histogram"] == {
        "1": 676, "2": 588, "3": 510, "4": 52, "5": 38
    }

    leading = {str(axis): leading_face_coefficient(items, axis) for axis in range(2, 8)}
    assert all(value != 0 for value in leading.values())
    normalization_upper = Q(2**8 * 256**6, factorial(5)) * (1 / PI_LOWER) ** 8
    uniform_coefficient = (
        normalization_upper * 2**DENOMINATORS * factorial(AXES) * sum_abs_weights
    )
    first_sufficient = next(
        m for m in range(1, 1000) if tail_bound(uniform_coefficient, m) <= TARGET
    )
    assert first_sufficient == 184
    assert tail_bound(uniform_coefficient, first_sufficient - 1) > TARGET
    assert int(k215["first_sufficient_universal_whole_sum_dyadic_m"]) == 215
    assert k274["decision"]["result"] == "retain_as_exact_dimension_reduction_but_not_yet_global_certificate"

    exact_checks = 0
    assert margins["term_face_checks"] == 475320; exact_checks += 1
    assert margins["global_minimum_margin"] == 1; exact_checks += 1
    assert margins["minimum_over_nonsingleton_faces"] == 2; exact_checks += 1
    assert sum_abs_weights == 2928; exact_checks += 1
    assert first_sufficient == 184; exact_checks += 1
    assert tail_bound(uniform_coefficient, 183) > TARGET >= tail_bound(uniform_coefficient, 184); exact_checks += 1

    hostile_checks = 0
    assert set(margins["worst_singleton_face_term_counts"]) == {str(i) for i in range(2, 8)}; hostile_checks += 1
    assert all(value != 0 for value in leading.values()); hostile_checks += 1
    assert min(face_margin(masks, 1 << axis) - 1
               for _, masks in items for axis in range(2, 8)) == 0; hostile_checks += 1
    assert margins["minimum_over_nonsingleton_faces"] > margins["global_minimum_margin"]; hostile_checks += 1

    bound_183 = tail_bound(uniform_coefficient, 183)
    bound_184 = tail_bound(uniform_coefficient, 184)
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {
            path.stem.split("-")[0]: sha256(path.read_bytes()).hexdigest()
            for path in (K185, K215, K218, K225, K274)
        },
        "object": "Complete mixed-scaling exterior of the 1,864-term signed K218 eight-auxiliary integrand",
        "sector_theorem": {
            "face_margin": "For nonempty axis set A, m_A equals the number of the fourteen denominator loads touched by A minus |A|.",
            "ordered_sector": "For t_pi1>=...>=t_pi8>=0, let y_k=t_pik-t_pi(k+1), with t_pi9=0. The exponential majorant has rates M_k=m_{pi1,...,pik}. Exhaustive all-face certification gives every M_k>=1, including equality faces and every subface.",
            "uniform_remainder": "Using cosh(t)<=exp(t), every touched denominator >=cosh(t)>=exp(t)/2, and pi>31/10, the normalized absolute exterior max_j t_j>=T is at most C*exp(-T)*sum_(r=0)^7 T^r/r!, where C uses all 8! labeled sectors and the complete absolute signed weight 2928.",
            "termwise_not_signed": "The theorem uses termwise absolute values. Exact generic singleton-face leading coefficients are nonzero on every exchangeable axis, so the worst margin cannot be raised by a universal signed cancellation claim from the current data.",
        },
        "certificate": margins,
        "counts": {
            "signed_terms": len(items),
            "distinct_allocations": len({masks for _, masks in items}),
            "nonempty_faces_per_term": 255,
            "labeled_order_sectors": factorial(AXES),
            "complete_absolute_weight": sum_abs_weights,
        },
        "worst_faces": {
            "axes": [2, 3, 4, 5, 6, 7],
            "type": "single exchangeable auxiliary coordinate",
            "margin": 1,
            "generic_remaining_coshes": [str(value) for value in GENERIC_COSHES],
            "exact_leading_coefficients_without_common_constant_or_pi8": {
                axis: str(value) for axis, value in leading.items()
            },
            "signs": {axis: ("positive" if value > 0 else "negative") for axis, value in leading.items()},
            "consequence": "K225 diagonal/single-exception cancellation does not cancel the generic worst scaling face when the other exchangeable coordinates are unequal.",
        },
        "dyadic_tail": {
            "target": "1/10^21",
            "pi_lower": str(PI_LOWER),
            "log2_upper": str(LOG2_UPPER),
            "uniform_coefficient_rational": str(uniform_coefficient),
            "first_sufficient_m": first_sufficient,
            "T": "184 log(2)",
            "bound_at_m_183_rational": str(bound_183),
            "bound_at_m_183_decimal": decimal_string(bound_183),
            "bound_at_m_184_rational": str(bound_184),
            "bound_at_m_184_decimal": decimal_string(bound_184),
        },
        "cost_and_coverage": {
            "one_time_exact_face_checks": margins["term_face_checks"],
            "k215_sufficient_whole_sum_m": 215,
            "k275_sufficient_whole_sum_m": 184,
            "dyadic_steps_saved": 31,
            "relative_cutoff_reduction": "31/215",
            "k274_comparison": "K274 removes one full coordinate exactly but requires 1,864 exact partial-fraction decompositions at each remaining point and has no uniform seven-dimensional remainder. K275 supplies a closed-form complete exterior bound without point evaluation but removes no finite coordinate.",
            "collar_comparison": "K265-K269 certify finite disjoint low/high and middle collars near the origin and q about 1792-2304. K275 controls the complete extreme exterior outside [0,184 log(2)]^8 but leaves the vast finite cube and its signed complement unresolved; it cannot replace the collar composition by itself.",
            "k215_comparison": "The sufficient complete absolute-tail cutoff improves from K215 m=215 to m=184 under this exact post-angular sector theorem. Both are conservative sufficient thresholds, not necessary cutoffs, and K215 is not invalidated.",
        },
        "decision": {
            "result": "retain_global_tail_theorem_but_finite_complement_remains",
            "r7b_disposition": "concluded_with_uniform_subface_complete_remainder_and_finite_cube_debt",
            "next_use": "R9 may replace K215's sufficient extreme-tail threshold by K275's m=184 theorem, but must not resume routine collars or infer the full sign until R8 and the finite complement are reranked.",
        },
        "selftests": {"exact_passed": exact_checks, "hostile_passed": hostile_checks},
        "claim_ceiling": "Exact all-face mixed-scaling integrability and a conservative normalized exterior bound for the complete K218 signed assembly after termwise absolute values. No finite-cube integration, full K218 sign, complete order-six error, K152 numerical decision, K215 impossibility, source, ledger, canon, paper, public-posture or physical conclusion.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K275 mixed-scaling all-face tail", result["decision"]["result"])
