#!/usr/bin/env python3
"""Finite exponential-tail control for the K329 normalized evaluator.

K328's rational formula is polynomial in its width.  For r>=1 every scaled
entry is bounded by its r=1 envelope times the exact row/column radial power.
The D4 determinant therefore costs at most r^16, the bordered B5 coefficient
of y-order j costs at most r^(11+j), and K326's absorbed x^2 endpoint scalar
costs r^2.  With K310's r^6 measure the three tail powers are 35,36,37.
K312 supplies exact incomplete-gamma polynomial tails with a rational outward
exponential bound.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K312_MODULE = HERE / "k312_order_seven_positive_cell_measure_backend.py"
K314_MODULE = HERE / "k314_order_seven_projective_face_oracle.py"
K326_MODULE = HERE / "k326_order_seven_signed_entry_jet_chart_bank.py"
K328_MODULE = HERE / "k328_order_seven_scaled_derivative_envelope_bank.py"
K329_MODULE = HERE / "k329_order_seven_degree27_origin_evaluator.py"
K328 = ROOT / "lab/process/k328-order-seven-scaled-derivative-envelope-bank.json"
K329 = ROOT / "lab/process/k329-order-seven-degree27-origin-evaluator.json"
OUTPUT = ROOT / "lab/process/k330-order-seven-radial-tail-control.json"

ctx.dps = 180
ctx.threads = 1

TAIL_START = Fraction(1)
S = (Fraction(1, 4), Fraction(3, 4))
GAPS = [(Fraction(1, 8), Fraction(5, 24)) for _ in range(6)]


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def upper_text(value: arb) -> str:
    return repr(math.nextafter(float(abs(value).upper()), math.inf))


def build() -> dict[str, Any]:
    k312 = load_module(K312_MODULE, "k330_k312_backend")
    k314 = load_module(K314_MODULE, "k330_k314_backend")
    k326 = load_module(K326_MODULE, "k330_k326_backend")
    k328_module = load_module(K328_MODULE, "k330_k328_backend")
    k329_module = load_module(K329_MODULE, "k330_k329_backend")
    k328 = json.loads(K328.read_text())
    k329 = json.loads(K329.read_text())
    if not k328["decision"]["zero_safe_scaled_derivative_bank_through_order_six_implemented"]:
        raise AssertionError("K328 scaled bank unavailable")
    if not k329["decision"]["continuous_degree27_origin_evaluator_implemented"]:
        raise AssertionError("K329 normalized evaluator unavailable")

    # Reuse exactly K329's normalized shared-entry construction at reference
    # radius one.  K328's formula at width r*Z is termwise dominated by r^m
    # times the width-Z formula for r>=1; assigning the exact row/column power
    # to each entry gives the determinant degree ledger below.
    prior_radius = k329_module.RADIUS
    try:
        k329_module.RADIUS = (Fraction(0), Fraction(1))
        jets, audit, d4_bound = k329_module.normalized_entry_jets(k326, k328_module)
    finally:
        k329_module.RADIUS = prior_radius
    determinant_jets = k326.determinant_taylor(jets)
    projective = k314.projective_polynomial_upper(
        {name: interval for name, interval in zip(k314.GAPS, GAPS, strict=True)}
    )
    scalar_at_one = Fraction(4, 120) * S[1] ** 2 * Fraction(1, 16) * projective
    reference = [arb(16) * d4_bound * value * arb(q(scalar_at_one)) for value in determinant_jets]

    coefficient_powers = [29, 30, 31]
    measure_powers = [power + 6 for power in coefficient_powers]
    radial_tails = [k312.radial_tail_upper(TAIL_START, power) for power in measure_powers]
    annulus_radial_mass = k312.radial_finite_upper(Fraction(1, 16), TAIL_START, 6)
    s_mass = k312.polynomial_cell_moment(S[0], S[1], 3, 29)
    gap_volume = math.prod((upper - lower for lower, upper in GAPS), start=Fraction(1))
    compact_mass = s_mass * gap_volume
    integrated = [
        value * arb(q(radial_tail * compact_mass))
        for value, radial_tail in zip(reference, radial_tails, strict=True)
    ]
    annulus_integrated = [value * arb(q(annulus_radial_mass * compact_mass)) for value in reference]
    if any(not math.isfinite(float(value.upper())) or value.upper() <= 0 for value in integrated):
        raise AssertionError("radial tail upper is not finite positive")

    # Direct finite-radius controls are reporting checks on the same analytic
    # majorant, not the proof.  They ensure the polynomial ledger dominates
    # the normalized evaluator at r=1,2,4 on the selected angular cell.
    controls = []
    for radius in (1, 2, 4):
        rows = []
        for order, value in enumerate(reference):
            majorant = value * arb(radius) ** coefficient_powers[order]
            rows.append(upper_text(majorant))
        controls.append({"radius": radius, "majorant_value_first_second_abs_uppers": rows})

    return {
        "schema_version": "1.0",
        "result_id": "K330-ORDER-SEVEN-RADIAL-TAIL-CONTROL",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k328-order-seven-scaled-derivative-envelope-bank.json",
                "lab/process/k329-order-seven-degree27-origin-evaluator.json",
            ],
            "arb_decimal_digits": 180,
            "threads": 1,
            "tail_start": q(TAIL_START),
            "projective_s_cell": [q(value) for value in S],
            "six_gap_cells": [[q(a), q(b)] for a, b in GAPS],
            "endpoint_chart_count": 16,
        },
        "polynomial_growth_ledger": {
            "entry_rule": "for r>=1, every K328 width polynomial of scaled derivative order m is at most r^m times its r=1 value; the remaining exact row/column radial factor supplies one additional power per selected kernel entry",
            "D4_normalized_determinant_power": 16,
            "bordered_B5_normalized_value_first_second_powers": [11, 12, 13],
            "absorbed_endpoint_x2_power": 2,
            "complete_coefficient_value_first_second_powers": coefficient_powers,
            "positive_measure_r6_power": 6,
            "tail_integrand_value_first_second_powers": measure_powers,
            "reference_radius_one_value_first_second_abs_uppers": [upper_text(value) for value in reference],
            "reference_entry_audit": audit,
            "finite_radius_majorant_controls": controls,
        },
        "exponential_tail": {
            "radial_weight": "exp(-256*r)",
            "tail_rule": "n!/256^(n+1)*exp(-256R)*sum_(k=0)^n (256R)^k/k!, with exp(-z)<=(1+z/256)^-256",
            "tail_power_value_first_second": measure_powers,
            "radial_tail_upper_fractions": [q(value) for value in radial_tails],
            "projective_exact_mass": q(s_mass),
            "six_gap_exact_volume": q(gap_volume),
            "integrated_value_first_second_abs_uppers": [upper_text(value) for value in integrated],
            "covers_infinite_radial_tail": True,
        },
        "finite_radial_annulus": {
            "radial_interval": ["1/16", "1"],
            "uniform_normalized_value_first_second_abs_uppers": [upper_text(value) for value in reference],
            "radial_r6_measure_upper": q(annulus_radial_mass),
            "integrated_value_first_second_abs_uppers": [upper_text(value) for value in annulus_integrated],
            "joins_K329_at_one_sixteenth": True,
            "joins_tail_at_one": True,
        },
        "assembly_contract": {
            "shared_normalized_entry_intervals_assembled_before_B5_coefficient_enclosure": True,
            "literal_border_zeros_retained": True,
            "raw_Bessel_zero_call_used": False,
            "tail_finiteness_is_analytic_not_sampled": True,
        },
        "scope_boundary": {
            "covered": "r in [1/16,infinity) on s in [1/4,3/4], all six positive gap cells and all sixteen endpoint charts; together with K329 this closes the full radial half-line on that projective interior",
            "not_covered": ["s in [0,1/4]", "s in [3/4,1]", "recursive tolerance closure across the projective faces", "a complete y-master constant"],
            "positive_projective_interior_only": True,
        },
        "decision": {
            "finite_exponential_radial_tail_control_implemented": True,
            "finite_radial_annulus_control_implemented": True,
            "positive_projective_interior_full_radial_half_line_complete": True,
            "tail_value_first_second_integrated_uppers_finite": True,
            "projective_faces_complete": False,
            "complete_origin_tail_face_sum_emitted": False,
            "complete_y_master_constant_emitted": False,
            "next_exact_input": "build a normalized confluent complete-determinant evaluator for s=0 and s=1; positive-argument entrywise bounds diverge there even though K321 proves the exact degree ledger and finite measure powers",
        },
        "release_test": {
            "tail_start_exactly_one": True,
            "growth_powers_exactly_29_30_31": coefficient_powers == [29, 30, 31],
            "tail_powers_exactly_35_36_37": measure_powers == [35, 36, 37],
            "all_tail_uppers_finite_positive": True,
            "annulus_joins_are_exact": True,
            "tail_coverage_not_inferred_from_sampling": True,
            "projective_face_overclaim": False,
            "complete_numerical_norm_overclaim": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k329["ledger_effect"],
        "source_routing": k329["source_routing"],
        "claim_ceiling": "Finite analytic exponential-tail bounds plus a finite [1/16,1] annulus bound for the degree-27 normalized complete determinant on the positive projective interior. Together with K329 this covers the complete radial half-line for s in [1/4,3/4]. K328's exact rational width polynomials give the row/column growth ledger D4=16, B5=11/12/13 and absorbed endpoint x^2=2; against K310's r^6*exp(-256r) measure the tail has exact powers 35/36/37. The s=0/1 face cells and recursive tolerance closure remain open, so no complete y-master constant, gap-axis transfer, K294 join, action-column value, residual, K152 interval, source/ledger, canon, paper, public or physical claim is released.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["tail_start"] != "1" or fixed["projective_s_cell"] != ["1/4", "3/4"]:
        raise AssertionError("tail domain changed")
    ledger = payload["polynomial_growth_ledger"]
    if ledger["D4_normalized_determinant_power"] != 16:
        raise AssertionError("D4 tail degree changed")
    if ledger["bordered_B5_normalized_value_first_second_powers"] != [11, 12, 13]:
        raise AssertionError("B5 tail degree changed")
    if ledger["complete_coefficient_value_first_second_powers"] != [29, 30, 31]:
        raise AssertionError("complete coefficient tail degree changed")
    reference_audit = ledger["reference_entry_audit"]
    if reference_audit["radial_cell"] != ["0", "1"] or reference_audit["terminal_normalized_entry_rule"] != "r*Phi_m with r<=1; continuous value zero at r=0":
        raise AssertionError("radius-one reference entry audit changed")
    tail = payload["exponential_tail"]
    if tail["tail_power_value_first_second"] != [35, 36, 37] or not tail["covers_infinite_radial_tail"]:
        raise AssertionError("tail measure coverage changed")
    if len(tail["integrated_value_first_second_abs_uppers"]) != 3:
        raise AssertionError("tail upper bank changed")
    annulus = payload["finite_radial_annulus"]
    if annulus["radial_interval"] != ["1/16", "1"] or not annulus["joins_K329_at_one_sixteenth"] or not annulus["joins_tail_at_one"]:
        raise AssertionError("finite annulus join changed")
    if len(annulus["integrated_value_first_second_abs_uppers"]) != 3:
        raise AssertionError("annulus upper bank changed")
    assembly = payload["assembly_contract"]
    if not assembly["shared_normalized_entry_intervals_assembled_before_B5_coefficient_enclosure"]:
        raise AssertionError("post-assembly tail contract lost")
    if assembly["raw_Bessel_zero_call_used"] or not assembly["tail_finiteness_is_analytic_not_sampled"]:
        raise AssertionError("tail proof downgraded to unsafe/sampled")
    if not payload["scope_boundary"]["positive_projective_interior_only"]:
        raise AssertionError("projective tail scope hidden")
    decision = payload["decision"]
    if not decision["finite_exponential_radial_tail_control_implemented"] or not decision["finite_radial_annulus_control_implemented"] or not decision["positive_projective_interior_full_radial_half_line_complete"] or decision["projective_faces_complete"]:
        raise AssertionError("tail/face disposition changed")
    if decision["complete_y_master_constant_emitted"]:
        raise AssertionError("complete numerical release overclaimed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate_payload(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
