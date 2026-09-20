#!/usr/bin/env python3
"""K263: certify the complete four-high exceptional-coordinate K218 layer."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import factorial

from flint import arb, ctx, fmpq

from k225_order_six_diagonal_cancellation import ROOT, terms
from k242_order_six_third_shell_signed_taylor import orbit_groups
from k262_order_six_low_through_three_high_multiplicity_integral import generate_layer


K185 = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
K218 = ROOT / "lab/process/k218-order-six-exact-angular-elimination.json"
K230 = ROOT / "lab/process/k230-order-six-permutation-projection.json"
K261 = ROOT / "lab/process/k261-order-six-all-pair-box-taylor-integral.json"
K262 = ROOT / "lab/process/k262-order-six-low-through-three-high-multiplicity-integral.json"
OUT = ROOT / "lab/process/k263-order-six-four-high-multiplicity-integral.json"

MULTIPLICITY = 4
ORDER = 6
POSITIVE_LOWER = Q(42, 10**21)  # 4.2e-20
PRECISION = 256


def rational_row(value: Q) -> dict:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "decimal": f"{float(value):.12e}",
    }


def generate() -> dict:
    ctx.prec = PRECISION
    source = json.loads(K185.read_text())
    items = list(terms(source))
    groups = orbit_groups(items)
    assert len(items) == 1864 and len(groups) == 307
    projection = json.loads(K230.read_text())
    compact = ";".join(
        ",".join(map(str, rows)) + ":" + str(weight)
        for rows, weight in sorted(groups.items())
    )
    orbit_digest = sha256(compact.encode()).hexdigest()
    assert orbit_digest == projection["orbit_coefficient_manifest_sha256"]

    normalization_lower = fmpq(2**8 * 256**6, factorial(5)) * fmpq(7, 22) ** 8
    normalization_upper = fmpq(2**8 * 256**6, factorial(5)) * fmpq(10, 31) ** 8
    layer = generate_layer(
        groups, MULTIPLICITY, ORDER, normalization_lower, normalization_upper
    )
    layer_lower = arb(layer["normalized_integral_interval"]["lower"])
    assert layer_lower > arb(POSITIVE_LOWER.numerator) / POSITIVE_LOWER.denominator

    k261 = json.loads(K261.read_text())
    k261_raw = k261["reanchored_integral"]["complete_raw_integral_interval"]
    k261_lower = arb(normalization_upper) * arb(k261_raw["lower"])
    k261_upper = arb(normalization_lower) * arb(k261_raw["upper"])
    k262 = json.loads(K262.read_text())
    adjacent = {row["multiplicity"]: row for row in k262["new_multiplicity_layers"]}
    complete_lower = layer_lower + k261_lower
    complete_upper = arb(layer["normalized_integral_interval"]["upper"]) + k261_upper
    for multiplicity in (0, 1, 3):
        interval = adjacent[multiplicity]["normalized_integral_interval"]
        complete_lower += arb(interval["lower"])
        complete_upper += arb(interval["upper"])
    assert complete_lower < 0 < complete_upper

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "conditional_internal_structure_not_forward_physics_credit",
        "input_sha256": {
            path.stem.split("-")[0]: sha256(path.read_bytes()).hexdigest()
            for path in (K185, K218, K230, K261, K262)
        },
        "object": (
            "The exact K218 signed integral on the complete fifteen-box S6-invariant "
            "layer with fixed high axis 1, fixed low axis 0, and exactly four high "
            "exceptional coordinates among axes 2..7"
        ),
        "domain": {
            "fixed_high_axis": 1,
            "fixed_low_axis": 0,
            "exceptional_axes": list(range(2, 8)),
            "high_exceptional_multiplicity": MULTIPLICITY,
            "high_q_interval": ["1792", "2304"],
            "low_q_interval": ["1", "13/5"],
            "boxes": 15,
            "pairwise_disjoint": True,
            "s6_invariant_union": True,
        },
        "projection": {
            "raw_signed_terms": len(items),
            "retained_exact_s6_orbits": len(groups),
            "orbit_manifest_sha256": orbit_digest,
            "rule": (
                "K230 proves integral equality on the complete S6-invariant layer. "
                "No projected representative is asserted equal on one non-invariant box."
            ),
        },
        "four_high_layer": layer,
        "certificate": {
            "normalization_lower_using_pi_less_than_22_over_7": str(normalization_lower),
            "normalization_upper_using_pi_greater_than_31_over_10": str(normalization_upper),
            "normalization_direction_rule": (
                "Positive lower endpoints use pi<22/7; positive and absolute upper "
                "endpoints and tails use pi>31/10."
            ),
            "declared_strict_positive_mass_lower": rational_row(POSITIVE_LOWER),
            "result": "strictly_positive_complete_four_high_multiplicity_layer",
        },
        "zero_through_four_composition": {
            "normalized_integral_interval": {
                "lower": str(complete_lower),
                "upper": str(complete_upper),
            },
            "result": "sign_unresolved_by_current_independent_layer_intervals",
            "reason": (
                "The rigorous lower endpoint is negative and the rigorous upper endpoint "
                "is positive after composing K261, K262, and the new K263 layer."
            ),
        },
        "controls": (
            "An independent reverse-order raw-allocation probe reconstructs the orbit "
            "manifest, exact degree-zero head and degree-seven-and-higher tail, checks "
            "two- and three-point product quadratures, and applies absolute-weight, "
            "wrong-measure, subset-deletion and non-invariant-single-box controls."
        ),
        "source_routing": (
            "SC-ACT-01/02 ASSERTS and SC-META-53 UNCERTAIN remain unchanged; "
            "LT-GR6b/LT-SM8/RA-F1/AC-F1 remain NEEDS."
        ),
        "decision": (
            "Multiplicity four is rigorously positive, so K262's negative composition "
            "cannot be extended monotonically. The zero-through-four sign remains "
            "unresolved; multiplicities five and six require higher-order signed "
            "cancellation or a different reanchored/first-exceeding decomposition."
        ),
        "claim_ceiling": (
            "Exact positivity and interval only on the declared multiplicity-four layer, "
            "plus an unresolved interval composition for multiplicities zero through four. "
            "No sign for multiplicities five or six, the zero-through-four union, the full "
            "K218 integral, complete original order-six error, K215, source, ledger, canon, "
            "paper, public posture, or physical positivity."
        ),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    layer = result["four_high_layer"]
    print("[PASS] K263", result["certificate"]["result"])
    print("[PASS] K263 interval", layer["normalized_integral_interval"])
    print("[PASS] K263 zero-through-four", result["zero_through_four_composition"]["result"])
