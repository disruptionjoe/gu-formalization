#!/usr/bin/env python3
"""Audit the K314/K315 data needed for a complete y-master sum.

The audit closes the radial/projective-s moment of every K311 terminal term
after the K310 r^27 scaling and K315 determinant placement.  It then checks
whether K314 supplies the remaining compact-angular coefficient on the whole
K312 domain.  K314 is deliberately an interior radial/y/split face oracle, so
that second condition is false: the complete y-master constant is not emitted.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K310 = ROOT / "lab/process/k310-order-seven-two-radius-origin-compactification.json"
K311 = ROOT / "lab/process/k311-order-seven-terminal-radial-join.json"
K312 = ROOT / "lab/process/k312-order-seven-positive-cell-measure-backend.json"
K314 = ROOT / "lab/process/k314-order-seven-projective-face-oracle.json"
K315 = ROOT / "lab/process/k315-order-seven-terminal-bordered-adapter.json"
OUTPUT = ROOT / "lab/process/k316-order-seven-complete-y-master.json"


def beta_integer(a: int, b: int) -> Fraction:
    return Fraction(math.factorial(a) * math.factorial(b), math.factorial(a + b + 1))


def radial_gamma(power: int, rate: int = 256) -> Fraction:
    return Fraction(math.factorial(power), rate ** (power + 1))


TERMINAL_TERMS = {
    0: [(Fraction(1), 0, -1, "1/x")],
    1: [(Fraction(1, 4), 1, 0, "1/4"), (Fraction(2), 0, -1, "2/x")],
    2: [(Fraction(3, 8), 2, 1, "3*x/8"), (Fraction(6), 0, -1, "6/x")],
}


def terminal_moment_rows() -> list[dict[str, Any]]:
    rows = []
    for order, terms in TERMINAL_TERMS.items():
        pieces = []
        total = Fraction(0)
        for coefficient, radial_increment, s_increment, source in terms:
            radial_power = 6 + radial_increment
            s_power = 3 + s_increment
            radial = radial_gamma(radial_power)
            projective = beta_integer(s_power, 29)
            contribution = coefficient * radial * projective
            total += contribution
            pieces.append({
                "source_term": source,
                "coefficient": str(coefficient),
                "scaled_radial_power": radial_power,
                "scaled_s_power": s_power,
                "one_minus_s_power": 29,
                "radial_gamma_moment": str(radial),
                "projective_beta_moment": str(projective),
                "contribution": str(contribution),
            })
        rows.append({
            "terminal_jet_order": order,
            "pieces": pieces,
            "complete_radial_projective_upper_fraction": str(total),
            "complete_radial_projective_upper_decimal": repr(float(total)),
        })
    return rows


def build() -> dict[str, Any]:
    k310 = json.loads(K310.read_text())
    k311 = json.loads(K311.read_text())
    k312 = json.loads(K312.read_text())
    k314 = json.loads(K314.read_text())
    k315 = json.loads(K315.read_text())
    if k310["compactification"]["origin_radial_power"] != 6:
        raise AssertionError("K310 radial power changed")
    if not k315["decision"]["K311_inserted_into_all_complete_bordered_jet_monomials"]:
        raise AssertionError("K315 terminal compiler unavailable")
    rows = terminal_moment_rows()
    multiplicities = {
        int(key): value
        for key, value in k315["census"]["terminal_monomials_by_jet_order_with_cross_factors"].items()
    }
    totals = {row["terminal_jet_order"]: Fraction(row["complete_radial_projective_upper_fraction"]) for row in rows}
    checksum = sum(multiplicities[order] * totals[order] for order in totals)

    k314_scope = k314["fixed_control"]["interior_radial_y_split_cell"]
    global_axes = k312["adaptive_contract"]["cell_key_order"]
    missing = [
        "s=0 and s=1 radial-projective faces outside K314's positive x,b slab",
        "y=0 and y=1 endpoint cells outside K314's y in [1/4,3/4] slab",
        "u_i and z_i endpoint cells outside K314's common [1/4,3/4] split slab",
        "one uniform coefficient for the nonterminal regularized entries in every K315 monomial after r^27 scaling",
    ]

    return {
        "schema_version": "1.0",
        "result_id": "K316-ORDER-SEVEN-COMPLETE-Y-MASTER-SUFFICIENCY-AUDIT",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k310-order-seven-two-radius-origin-compactification.json",
                "lab/process/k311-order-seven-terminal-radial-join.json",
                "lab/process/k312-order-seven-positive-cell-measure-backend.json",
                "lab/process/k314-order-seven-projective-face-oracle.json",
                "lab/process/k315-order-seven-terminal-bordered-adapter.json",
            ],
            "scaled_origin_weight": "exp(-256*r)*r^6*s^3*(1-s)^29",
            "scaled_regularizer_degree": 27,
            "terminal_jet_orders": [0, 1, 2],
            "K314_scope": k314_scope,
            "K312_axis_order": global_axes,
        },
        "homogeneity_composition": {
            "D4_regularizer_degree": -16,
            "bordered_nonterminal_degree_when_terminal_slot_present": -10,
            "terminal_term_rule": "multiply r^27*r^-16*r^-10 by B_m; the 1/x pieces leave r^0*s^-1, the constant piece leaves r^1, and the x piece leaves r^2*s",
            "dimensionless_y_derivatives_preserve_total_degree": True,
            "terminal_radial_projective_moments": rows,
            "weighted_complete_term_moment_checksum_fraction": str(checksum),
            "weighted_complete_term_moment_checksum_decimal": repr(float(checksum)),
            "checksum_role": "finite radial/projective-s factor after complete K315 placement; it still multiplies the missing compact-angular coefficient of the remaining entries",
        },
        "sufficiency_audit": {
            "K312_positive_measure_complete": k312["coverage"]["missing_measure_cells"] == 0,
            "K314_all_six_one_gap_faces_confluent": k314["decision"]["all_six_repeated_node_faces_have_finite_regularizer_bounds"],
            "K315_all_terminal_monomials_typed": k315["decision"]["terminal_monomial_census_complete"],
            "radial_projective_terminal_moments_complete": True,
            "global_nonterminal_angular_coefficient_available": False,
            "complete_y_master_inputs_sufficient": False,
            "missing_inputs": missing,
            "why_K314_cannot_be_reused_as_global": "its certified x,b,y and split intervals are strict interior slabs; taking their largest bound as a global coefficient would silently discard the radial-projective and terminal endpoint cells that K312 explicitly requires",
        },
        "decision": {
            "terminal_radial_projective_join_complete": True,
            "naive_K312_times_K314_times_K315_composition_rejected": True,
            "reason": "the factors have different certified domains; K315 closes placement and K316 closes radial/projective-s moments, but no accepted oracle bounds every remaining regularized entry on the complete compact angular cell family",
            "complete_y_master_constant_emitted": False,
            "five_gap_axis_transfer_released": False,
            "k294_gamma_join_released": False,
            "next_exact_input": "construct a homogeneous coefficient oracle for the remaining nonterminal entries on the full s,y,u,z compact boundary atlas, reusing K314 on one-gap p faces and K315's monomial typing; only then multiply by these exact moments and sum K312 cells",
        },
        "release_test": {
            "all_terminal_moments_finite_positive": all(
                Fraction(row["complete_radial_projective_upper_fraction"]) > 0 for row in rows
            ),
            "minimum_s_power_after_terminal_substitution": min(
                piece["scaled_s_power"] for row in rows for piece in row["pieces"]
            ) == 2,
            "all_K315_terminal_orders_consumed": set(multiplicities) == set(totals),
            "domain_mismatch_explicit": len(missing) == 4,
            "complete_numerical_norm_overclaim": False,
            "five_gap_transfer_overclaim": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k315["ledger_effect"],
        "source_routing": k315["source_routing"],
        "claim_ceiling": "Exact terminal radial/projective-s homogeneity join for every K315 complete bordered determinant monomial. After r^27 scaling, all B0/B1/B2 pieces reduce to finite gamma-beta moments with minimum s power two; the full factor-two-weighted terminal census has an exact rational checksum. A direct sufficiency audit rejects multiplying K312, K314 and K315 into a purported global norm because K314 covers only an interior x,b,y,split slab and does not supply the remaining-entry coefficient on s/y/split endpoint cells. Therefore no complete y-master constant, five gap-axis transfer, K294 gamma join, action-column value, residual, K152 interval, source/ledger, canon, paper, public or physical claim is emitted.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["terminal_jet_orders"] != [0, 1, 2] or fixed["scaled_regularizer_degree"] != 27:
        raise AssertionError("K316 fixed control changed")
    audit = payload["sufficiency_audit"]
    if not audit["radial_projective_terminal_moments_complete"]:
        raise AssertionError("terminal moment join missing")
    if audit["global_nonterminal_angular_coefficient_available"] or audit["complete_y_master_inputs_sufficient"]:
        raise AssertionError("domain mismatch hidden")
    decision = payload["decision"]
    if not decision["terminal_radial_projective_join_complete"]:
        raise AssertionError("radial-projective join missing")
    if not decision["naive_K312_times_K314_times_K315_composition_rejected"]:
        raise AssertionError("invalid factor composition restored")
    if decision["complete_y_master_constant_emitted"] or decision["five_gap_axis_transfer_released"] or decision["k294_gamma_join_released"]:
        raise AssertionError("K316 closure overclaim")


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
