#!/usr/bin/env python3
"""K274: exact one-axis integration for the complete signed K218 group."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import prod
from pathlib import Path
import sys

from flint import arb, ctx

from k225_order_six_diagonal_cancellation import terms

sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parents[2]
PROCESS = ROOT / "lab/process"
K185 = PROCESS / "k185-order-six-duffy-face-tail-wave.json"
K218 = PROCESS / "k218-order-six-exact-angular-elimination.json"
K273 = PROCESS / "k273-k267-integrated-anisotropy-factorization-pilot.json"
OUT = PROCESS / "k274-order-six-one-axis-exact-integration-pilot.json"
AXIS = 1
PRECISION = 512
GENERIC_C = (Q(5, 4), Q(0), Q(17, 8), Q(9, 8), Q(13, 8), Q(21, 8), Q(25, 8), Q(29, 8))
COINCIDENT_C = (Q(5, 4), Q(0)) + (Q(5, 4),) * 6


def add(a: list[Q], b: list[Q]) -> list[Q]:
    out = [Q(0)] * max(len(a), len(b))
    for i, value in enumerate(a): out[i] += value
    for i, value in enumerate(b): out[i] += value
    while len(out) > 1 and out[-1] == 0: out.pop()
    return out


def mul(a: list[Q], b: list[Q]) -> list[Q]:
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i + j] += x * y
    return out


def power(a: list[Q], n: int) -> list[Q]:
    out = [Q(1)]
    for _ in range(n): out = mul(out, a)
    return out


def solve(matrix: list[list[Q]], rhs: list[Q]) -> list[Q]:
    n = len(rhs)
    aug = [matrix[i][:] + [rhs[i]] for i in range(n)]
    for col in range(n):
        pivot = next(row for row in range(col, n) if aug[row][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for row in range(n):
            if row == col or not aug[row][col]: continue
            factor = aug[row][col]
            aug[row] = [x - factor * y for x, y in zip(aug[row], aug[col])]
    return [aug[i][-1] for i in range(n)]


def partial_fractions(loads: list[Q]) -> dict[tuple[Q, int], Q]:
    """Decompose the exact x=tanh(t/2) integrand into (lambda-x^2)^-r."""
    assert len(loads) >= 2 and all(value > 1 for value in loads)
    nodes = [Q(value + 1, value - 1) for value in loads]
    counts = Counter(nodes)
    denominator_scale = prod((value - 1 for value in loads), start=Q(1))
    numerator = [Q(2) / denominator_scale, Q(2) / denominator_scale]
    numerator = mul(numerator, power([Q(1), Q(-1)], len(loads) - 2))
    qpoly = [Q(1)]
    for node in nodes: qpoly = mul(qpoly, [node, Q(-1)])
    labels: list[tuple[Q, int]] = []
    bases: list[list[Q]] = []
    for node in sorted(counts):
        multiplicity = counts[node]
        other = [Q(1)]
        for other_node, other_multiplicity in counts.items():
            if other_node != node:
                other = mul(other, power([other_node, Q(-1)], other_multiplicity))
        for order in range(1, multiplicity + 1):
            labels.append((node, order))
            bases.append(mul(other, power([node, Q(-1)], multiplicity - order)))
    degree = len(loads)
    matrix = [[bases[col][row] if row < len(bases[col]) else Q(0)
               for col in range(degree)] for row in range(degree)]
    rhs = numerator + [Q(0)] * (degree - len(numerator))
    coefficients = solve(matrix, rhs)
    reconstructed = [Q(0)]
    for coefficient, basis in zip(coefficients, bases):
        reconstructed = add(reconstructed, [coefficient * value for value in basis])
    assert reconstructed + [Q(0)] * (degree - len(reconstructed)) == rhs
    return {label: coefficient for label, coefficient in zip(labels, coefficients) if coefficient}


def endpoint_integrals(node: Q, maximum_order: int) -> list[arb]:
    lam = arb(node.numerator) / node.denominator
    values = [arb(0), (arb(1) / lam.sqrt()).atanh() / lam.sqrt()]
    for order in range(2, maximum_order + 1):
        prior = values[-1]
        boundary = arb(1) / (2 * lam * (order - 1) * (lam - 1) ** (order - 1))
        values.append(boundary + (2 * order - 3) * prior / (2 * lam * (order - 1)))
    return values


def integrated_group(items: list, coshes: tuple[Q, ...]) -> tuple[arb, dict]:
    assert coshes[AXIS] == 0 and all(value >= 1 for i, value in enumerate(coshes) if i != AXIS)
    combined: dict[tuple[Q, int], Q] = defaultdict(Q)
    participation = Counter()
    repeated_terms = 0
    coefficient_bits = 0
    polynomial_checks = 0
    for weight, masks in items:
        participating = [i for i in range(14) if masks[AXIS] & (1 << i)]
        k = len(participating)
        participation[k] += 1
        loads = []
        constant_denominator = Q(1)
        for i in range(14):
            base = Q(256) + sum((coshes[j] for j in range(8)
                                 if j != AXIS and masks[j] & (1 << i)), Q(0))
            if i in participating: loads.append(base)
            else: constant_denominator *= base
        decomposition = partial_fractions(loads)
        polynomial_checks += 1
        if len(set(loads)) < len(loads): repeated_terms += 1
        prefactor = Q(weight, constant_denominator)
        for label, coefficient in decomposition.items():
            value = prefactor * coefficient
            combined[label] += value
            coefficient_bits = max(coefficient_bits, abs(value.numerator).bit_length(), value.denominator.bit_length())
    other_measure = prod((value for i, value in enumerate(coshes) if i != AXIS), start=Q(1))
    total = arb(0)
    nonzero = {label: value * other_measure for label, value in combined.items() if value}
    by_node: dict[Q, int] = defaultdict(int)
    for node, order in nonzero: by_node[node] = max(by_node[node], order)
    endpoints = {node: endpoint_integrals(node, order) for node, order in by_node.items()}
    for (node, order), coefficient in nonzero.items():
        total += arb(coefficient.numerator) / coefficient.denominator * endpoints[node][order]
    return total, {
        "participating_load_histogram": {str(k): participation[k] for k in sorted(participation)},
        "total_participating_loads": sum(k * count for k, count in participation.items()),
        "terms_with_coincident_loads": repeated_terms,
        "exact_polynomial_reconstructions": polynomial_checks,
        "combined_nonzero_primitive_terms": len(nonzero),
        "distinct_endpoint_nodes": len(by_node),
        "maximum_rational_coefficient_bits": coefficient_bits,
    }


def generate() -> dict:
    ctx.prec = PRECISION
    source = json.loads(K185.read_text())
    items = list(terms(source))
    assert len(items) == 1864
    totals = [sum(masks[axis].bit_count() for _, masks in items) for axis in range(8)]
    assert totals[AXIS] == min(totals)
    generic_value, generic_stats = integrated_group(items, GENERIC_C)
    coincident_value, coincident_stats = integrated_group(items, COINCIDENT_C)
    assert generic_stats["exact_polynomial_reconstructions"] == 1864
    strict_native_chains = 0
    minimum_native_gap = 14
    for _, masks in items:
        supports = [frozenset(j for j in range(8) if j != AXIS and masks[j] & (1 << i))
                    for i in range(14) if masks[AXIS] & (1 << i)]
        ordered = sorted(supports, key=len)
        assert all(ordered[i] < ordered[i + 1] for i in range(len(ordered) - 1))
        minimum_native_gap = min(minimum_native_gap,
                                 *(len(ordered[i + 1] - ordered[i]) for i in range(len(ordered) - 1)))
        strict_native_chains += 1
    confluent = partial_fractions([Q(257), Q(257), Q(258)])
    assert any(order == 2 for _, order in confluent)
    confluent_endpoints = {node: endpoint_integrals(node, max(order for n, order in confluent if n == node))
                           for node, _ in confluent}
    confluent_value = sum((arb(coefficient.numerator) / coefficient.denominator
                           * confluent_endpoints[node][order]
                           for (node, order), coefficient in confluent.items()), arb(0))
    exact_checks = 0
    assert generic_stats["participating_load_histogram"] == {"3": 792, "5": 600, "7": 472}; exact_checks += 1
    assert generic_stats["total_participating_loads"] == 8680; exact_checks += 1
    assert generic_stats["exact_polynomial_reconstructions"] == 1864; exact_checks += 1
    assert coincident_stats["exact_polynomial_reconstructions"] == 1864; exact_checks += 1
    assert all(Q(value + 1, value - 1) > 1 for value in (Q(257), Q(258))); exact_checks += 1
    hostile_checks = 0
    assert strict_native_chains == 1864 and minimum_native_gap >= 1; hostile_checks += 1
    assert any(order == 2 for _, order in confluent) and confluent_value > 0; hostile_checks += 1
    assert generic_stats["combined_nonzero_primitive_terms"] > 0; hostile_checks += 1
    assert json.loads(K273.read_text())["decision"]["result"] == "reject_integrated_anisotropy_majorant_for_this_case"; hostile_checks += 1
    decision = "retain_as_exact_dimension_reduction_but_not_yet_global_certificate"
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {path.stem.split("-")[0]: sha256(path.read_bytes()).hexdigest()
                         for path in (K185, K218, K273)},
        "object": "Exact integration of auxiliary axis 1 over [0,infinity) for the complete 1,864-term signed K218 group at fixed remaining coordinates",
        "selection": {
            "axis": AXIS,
            "reason": "Axis 1 has 8,680 participating denominator loads across the complete group, fewer than every other axis.",
            "all_axis_participating_load_totals": totals,
        },
        "derivation": {
            "chart": "x=tanh(t_1/2), so cosh(t_1)=(1+x^2)/(1-x^2), cosh(t_1)dt_1=2(1+x^2)/(1-x^2)^2 dx, and x runs from 0 to 1",
            "term_form": "With k participating loads B_i+cosh(t_1), each term becomes 2(1+x^2)(1-x^2)^(k-2)/product_i((B_i+1)-(B_i-1)x^2), times its seven-coordinate rational prefactor.",
            "primitive_basis": "After exact confluent partial fractions, integrate (lambda-x^2)^(-r). I_1=atanh(x/sqrt(lambda))/sqrt(lambda); I_r=x/[2 lambda (r-1)(lambda-x^2)^(r-1)]+(2r-3)I_(r-1)/[2 lambda(r-1)].",
            "endpoints": "t_1=0 is x=0 and every basis primitive vanishes there; t_1=infinity is x=1, strictly below every lambda=(B+1)/(B-1)>1. I_1(1)=acosh(B)/(2 sqrt(lambda)).",
            "coincident_load_control": "Equal B values are represented as repeated poles and evaluated by the recurrence. No coefficient divides by B_i-B_j, so the formula is the exact confluent limit.",
        },
        "controls": {
            "generic_remaining_coshes": [str(value) if i != AXIS else "integrated" for i, value in enumerate(GENERIC_C)],
            "generic_integrated_value_without_common_constant_or_pi8": str(generic_value),
            "generic_stats": generic_stats,
            "coincident_remaining_coshes": [str(value) if i != AXIS else "integrated" for i, value in enumerate(COINCIDENT_C)],
            "coincident_integrated_value_without_common_constant_or_pi8": str(coincident_value),
            "coincident_stats": coincident_stats,
            "native_load_separation": {
                "strict_support_chains": strict_native_chains,
                "minimum_support_increment": minimum_native_gap,
                "consequence": "Every native participating load differs from the next by at least one positive remaining cosh, hence by at least one on the physical domain; native load coincidence is excluded rather than assumed away."
            },
            "artificial_confluent_control": {
                "loads": ["257", "257", "258"],
                "contains_second_order_pole": True,
                "integrated_value": str(confluent_value),
                "purpose": "Exercises the exact repeated-pole limit required if a later specialization admits coincident loads."
            },
        },
        "cost_and_coverage": {
            "coverage": "The formula integrates the entire t_1 half-line for all 1,864 signed terms at arbitrary fixed positive remaining coshes, reducing the exact K218 integral from eight to seven dimensions without collars on t_1.",
            "producer_exact_decompositions_per_seven_coordinate_evaluation": 1864,
            "producer_linear_system_orders": [3, 5, 7],
            "comparison": "Unlike K265-K269 collars this covers a complete coordinate. It does not yet bound the remaining seven-dimensional signed integral; coefficient and transcendental endpoint growth must be controlled there before it can replace collars.",
        },
        "decision": {
            "result": decision,
            "r7a_disposition": "concluded_with_exact_reduction_and_remaining_applicability_debt",
            "next_use": "R9 may retain the formula as a seven-dimensional integrand. Do not adopt it as a global certificate unless a uniform seven-dimensional remainder beats collar cost; compare R7b first.",
        },
        "selftests": {"exact_passed": exact_checks, "hostile_passed": hostile_checks},
        "claim_ceiling": "Exact one-axis dimension reduction and confluent endpoint formula for the complete K218 signed group, plus two fixed seven-coordinate controls. No uniform bound on the remaining seven-dimensional integral, full K218 sign, complete order-six error, K215, source, ledger, canon, paper, public-posture or physical conclusion.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write: OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K274 one-axis exact-integration pilot", result["decision"]["result"])
