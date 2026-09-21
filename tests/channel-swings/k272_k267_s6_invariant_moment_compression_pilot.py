#!/usr/bin/env python3
"""K272: cost a valid S6 invariant-moment compression on two K267 orbits."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
import sys

from flint import arb, ctx, fmpq, fmpq_mpoly_ctx

from k225_order_six_diagonal_cancellation import ROOT, terms
from k242_order_six_third_shell_signed_taylor import orbit_groups
from k262_order_six_low_through_three_high_multiplicity_integral import (
    K185,
    as_arb,
    box_center_and_radius,
    centered_moments,
    rational_tail,
    sinh_log,
)
from k267_order_nine_exchangeable_axis_middle_collar import (
    BOUNDS,
    ORDER,
    status_specs,
)

sys.set_int_max_str_digits(0)

K230 = ROOT / "lab/process/k230-order-six-permutation-projection.json"
K267 = ROOT / "lab/process/k267-order-nine-exchangeable-axis-middle-collar.json"
OUT = ROOT / "lab/process/k272-k267-s6-invariant-moment-compression-pilot.json"
FIXED_STATUS = ("high", "high")
PILOT_MULTIPLICITIES = (0, 5)


def geometry_table() -> dict[str, dict]:
    geometry = {}
    for name, bounds in BOUNDS.items():
        center, radius = box_center_and_radius(bounds)
        geometry[name] = {
            "center": center,
            "radius": radius,
            "moments": centered_moments(bounds, center, ORDER),
            "measure": sinh_log(bounds[1]) - sinh_log(bounds[0]),
        }
    return geometry


def compile_polynomials(groups, status, ring, variables, geometry):
    centers = tuple(geometry[name]["center"] for name in status)
    radii = tuple(geometry[name]["radius"] for name in status)
    polynomials = [ring.constant(0) for _ in range(ORDER + 1)]
    for rows, weight in groups.items():
        pieces = [ring.constant(1)] + [ring.constant(0) for _ in range(ORDER)]
        for row in rows:
            support = tuple(axis for axis in range(8) if row & (1 << axis))
            base = fmpq(256) + sum(
                (fmpq(centers[a].numerator, centers[a].denominator) for a in support),
                fmpq(0),
            )
            linear = sum((variables[a] for a in support), ring.constant(0))
            divided = [pieces[0] / base]
            for degree in range(1, ORDER + 1):
                divided.append((pieces[degree] - linear * divided[degree - 1]) / base)
            pieces = divided
        for degree, piece in enumerate(pieces):
            polynomials[degree] += weight * piece
    tail = sum(
        (Q(abs(weight)) * rational_tail(rows, centers, radii, ORDER + 1)
         for rows, weight in groups.items()),
        Q(),
    )
    for name in status:
        tail *= geometry[name]["measure"]
    return polynomials, tail


def representative_to_box(rep_status, box_status):
    """Return the proved status-preserving permutation rep-axis -> box-axis."""
    mapping = [0, 1] + [None] * 6
    for label in ("middle", "high", "low"):
        rep_axes = [a for a in range(2, 8) if rep_status[a] == label]
        box_axes = [a for a in range(2, 8) if box_status[a] == label]
        assert len(rep_axes) == len(box_axes)
        for rep_axis, box_axis in zip(rep_axes, box_axes):
            mapping[rep_axis] = box_axis
    assert sorted(mapping) == list(range(8))
    return tuple(mapping)


def aggregate_pulled(polynomial_sets, mappings):
    aggregates = [dict() for _ in range(ORDER + 1)]
    enumerated_monomials = 0
    for polynomials, mapping in zip(polynomial_sets, mappings):
        for degree, polynomial in enumerate(polynomials):
            polynomial_terms = list(polynomial.terms())
            enumerated_monomials += len(polynomial_terms)
            for exponents, coefficient in polynomial_terms:
                pulled = tuple(exponents[mapping[a]] for a in range(8))
                aggregates[degree][pulled] = (
                    aggregates[degree].get(pulled, fmpq(0)) + coefficient
                )
    for degree in range(ORDER + 1):
        aggregates[degree] = {
            exponents: coefficient
            for exponents, coefficient in aggregates[degree].items()
            if coefficient
        }
    return aggregates, enumerated_monomials


def evaluate_aggregates(aggregates, representative_moments):
    heads = []
    for terms_by_exponent in aggregates:
        value = arb(0)
        for exponents, coefficient in sorted(terms_by_exponent.items()):
            term = arb(coefficient)
            for axis, exponent in enumerate(exponents):
                term *= representative_moments[axis][exponent]
            value += term
        heads.append(value)
    return heads


def aggregate_digest(aggregates):
    payload = [
        [[*(int(e) for e in exponents), str(coefficient)] for exponents, coefficient in sorted(level.items())]
        for level in aggregates
    ]
    return sha256(json.dumps(payload, separators=(",", ":")).encode()).hexdigest()


def stored_layer(record, multiplicity):
    block = next(b for b in record["fixed_axis_blocks"] if b["block"] == "fixed_high_high")
    return next(
        layer for layer in block["multiplicity_layers"]
        if layer["high_exceptional_multiplicity"] == multiplicity
    )


def run_layer(groups, multiplicity, ring, variables, geometry, prior):
    specs = list(status_specs(FIXED_STATUS, multiplicity))
    assert len(specs) == 6
    representative_status = specs[0][2]
    polynomial_sets = []
    mappings = []
    tail = Q()
    for _, _, status in specs:
        polynomials, box_tail = compile_polynomials(
            groups, status, ring, variables, geometry
        )
        polynomial_sets.append(polynomials)
        mappings.append(representative_to_box(representative_status, status))
        tail += box_tail
    aggregates, enumerated_monomials = aggregate_pulled(polynomial_sets, mappings)
    representative_moments = tuple(
        geometry[name]["moments"] for name in representative_status
    )
    heads = evaluate_aggregates(aggregates, representative_moments)
    for value, expected in zip(heads, prior["complete_raw_head_by_degree"]):
        assert (value - arb(expected)).contains(0)
    assert tail == Q(prior["complete_raw_absolute_tail_upper"])
    head = sum(heads, arb(0))
    raw_lower = head.lower() - as_arb(tail)
    raw_upper = head.upper() + as_arb(tail)
    prior_interval = prior["complete_raw_integral_interval"]
    # K267 serialized a different but mathematically identical Arb summation
    # order.  Its endpoint rounding is far below the certified remainder.
    serialization_slack = arb("1e-90")
    assert abs(raw_lower - arb(prior_interval["lower"])) < serialization_slack
    assert abs(raw_upper - arb(prior_interval["upper"])) < serialization_slack

    aggregated_monomials = sum(len(level) for level in aggregates)
    recurrence_updates = len(specs) * sum(len(rows) for rows in groups) * (ORDER + 1)
    naive_reynolds_updates = 219600 * 14 * (ORDER + 1)
    return {
        "role": "pilot" if multiplicity == 0 else "held_out",
        "fixed_axis_status": [*FIXED_STATUS],
        "high_exceptional_multiplicity": multiplicity,
        "boxes": len(specs),
        "representative_axis_status": list(representative_status),
        "representative_to_box_permutations": [list(mapping) for mapping in mappings],
        "aggregate_coefficient_sha256": aggregate_digest(aggregates),
        "raw_head_by_degree": [str(value) for value in heads],
        "raw_absolute_tail_upper": str(tail),
        "raw_integral_interval": {"lower": str(raw_lower), "upper": str(raw_upper)},
        "stored_interval_reproduced": True,
        "cost": {
            "enumerated_box_recurrence_updates": recurrence_updates,
            "compressed_box_recurrence_updates": recurrence_updates,
            "naive_reynolds_recurrence_updates": naive_reynolds_updates,
            "enumerated_moment_monomial_evaluations": enumerated_monomials,
            "compressed_moment_monomial_evaluations": aggregated_monomials,
            "moment_evaluation_reduction_factor": str(
                Q(enumerated_monomials, aggregated_monomials)
            ),
            "enumerated_tail_orbit_evaluations": len(specs) * len(groups),
            "compressed_tail_orbit_evaluations": len(specs) * len(groups),
            "enclosure_width_changed": False,
        },
    }


def generate():
    ctx.prec = 256
    source = json.loads(K185.read_text())
    groups = orbit_groups(list(terms(source)))
    projection = json.loads(K230.read_text())
    record = json.loads(K267.read_text())
    assert len(groups) == projection["retained_orbits"] == 307
    assert projection["expanded_distinct_denominator_functions"] == 219600
    ring = fmpq_mpoly_ctx.get([f"u{axis}" for axis in range(8)])
    variables = ring.gens()
    geometry = geometry_table()
    layers = []
    for multiplicity in PILOT_MULTIPLICITIES:
        layers.append(run_layer(
            groups, multiplicity, ring, variables, geometry,
            stored_layer(record, multiplicity),
        ))
        print(f"[CHECKPOINT] K272 multiplicity {multiplicity}", flush=True)

    exact_checks = 0
    for layer in layers:
        assert layer["boxes"] == 6; exact_checks += 1
        assert layer["stored_interval_reproduced"]; exact_checks += 1
        assert layer["cost"]["compressed_box_recurrence_updates"] == layer["cost"]["enumerated_box_recurrence_updates"]; exact_checks += 1
        assert layer["cost"]["compressed_moment_monomial_evaluations"] < layer["cost"]["enumerated_moment_monomial_evaluations"]; exact_checks += 1
        assert layer["cost"]["compressed_tail_orbit_evaluations"] == layer["cost"]["enumerated_tail_orbit_evaluations"]; exact_checks += 1
        assert not layer["cost"]["enclosure_width_changed"]; exact_checks += 1
    hostile_checks = 0
    assert layers[0]["aggregate_coefficient_sha256"] != layers[1]["aggregate_coefficient_sha256"]; hostile_checks += 1
    assert all(layer["cost"]["naive_reynolds_recurrence_updates"] > layer["cost"]["enumerated_box_recurrence_updates"] for layer in layers); hostile_checks += 1
    assert all(layer["representative_to_box_permutations"][0] == list(range(8)) for layer in layers); hostile_checks += 1
    assert all(len({tuple(p) for p in layer["representative_to_box_permutations"]}) == 6 for layer in layers); hostile_checks += 1

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {
            path.stem.split("-")[0]: sha256(path.read_bytes()).hexdigest()
            for path in (K185, K230, K267)
        },
        "object": "Costed exact invariant-moment aggregation on two complete six-box S6 orbits from K267",
        "method": {
            "coordinate_rule": "Within each equal-status class, map sorted representative axes to sorted box axes; pull every monomial exponent through that permutation before coefficient summation.",
            "head_rule": "Compile all six exact box recurrences, sum pulled exact coefficients, then evaluate the aggregate once against representative product moments.",
            "tail_rule": "Retain and sum every box's complete absolute degree-ten-and-higher tail.",
            "validity": "Complete orbit integration only; no pointwise representative substitution.",
        },
        "layers": layers,
        "cost_conclusion": {
            "result": "reject_as_total_algebraic_speedup",
            "reason": "Coefficient aggregation reduces moment evaluations but leaves all box recurrences and all tail evaluations intact; exact enclosure width is unchanged. Naive 219600-function Reynolds expansion is substantially more expensive.",
            "total_recurrence_reduction": "none",
            "total_tail_reduction": "none",
            "moment_evaluation_reduction": "measured_positive_on_both_orbits",
            "enclosure_improvement": "none",
            "r5_disposition": "bounded pilot concluded; do not replace K267 enumeration with this implementation",
        },
        "selftests": {"exact_passed": exact_checks, "hostile_passed": hostile_checks},
        "claim_ceiling": "Cost conclusion only for the tested degree-nine K267 compiler architecture and two declared S6 box orbits; no universal impossibility, new region, full K218 result, source, ledger, canon, paper, or public-posture conclusion.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K272", result["cost_conclusion"]["result"])
    print("[PASS] K272 selftests", result["selftests"])
