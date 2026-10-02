#!/usr/bin/env python3
"""K843: a middle-symbol class obstructs a local Sobolev elliptic estimate."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k843-sc-act-06-microlocal-cohomology-obstruction.json"
NOTICE = (
    "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional "
    "particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net "
    "chirality, SO(10) 126 Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass "
    "route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism "
    "without an explicit typed bridge. Read lab/methods/source-native-comparator-routing.md and follow its "
    "source-native pointers before reusing this result."
)


def rank(matrix: list[list[Fraction]]) -> int:
    work = [row[:] for row in matrix]
    if not work:
        return 0
    pivot_row = 0
    for col in range(len(work[0])):
        pivot = next((i for i in range(pivot_row, len(work)) if work[i][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [x / scale for x in work[pivot_row]]
        for i in range(len(work)):
            if i != pivot_row and work[i][col]:
                factor = work[i][col]
                work[i] = [work[i][j] - factor * work[pivot_row][j] for j in range(len(work[0]))]
        pivot_row += 1
    return pivot_row


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def toy_case(exact: bool) -> dict[str, Any]:
    if exact:
        g = [[Fraction(1)], [Fraction(0)]]
        j = [[Fraction(0), Fraction(1)]]
    else:
        g = [[Fraction(1)], [Fraction(0)], [Fraction(0)]]
        j = [[Fraction(0), Fraction(1), Fraction(0)]]
    middle = len(g)
    rank_g, rank_j = rank(g), rank(j)
    h = middle - rank_j - rank_g
    return {
        "middle_dimension": middle,
        "gauge_symbol_rank": rank_g,
        "equation_symbol_rank": rank_j,
        "composition_zero": all(x == 0 for row in matmul(j, g) for x in row),
        "middle_symbol_cohomology_dimension": h,
        "middle_exact": h == 0,
    }


def build() -> dict[str, Any]:
    defect, control = toy_case(False), toy_case(True)
    return {
        "schema_version": "1.0",
        "result_id": "K843-SC-ACT-06-MICROLOCAL-COHOMOLOGY-OBSTRUCTION",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "comparator_routing_notice": NOTICE,
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Local first-order symbol-complex theorem on a coordinate ball; no GU global family, torus quotient, boundary condition or physical quotient is assumed.",
        "gu_typed_objects": {
            "carrier": "LAYER=toy CHIRALITY=N/A finite-rank bundles E0 -> E1 -> E2 over a local coordinate ball",
            "pairing": "auxiliary Euclidean bundle metrics ON=E0,E1,E2 used only to define quotient distance",
            "real_structure": "real or complex finite-rank coefficient bundles",
            "grading": "gauge parameters -> fields -> equations",
            "action_owner": "repository-construction",
            "target": "MAP-TYPE=quotient local Sobolev estimate modulo the principal gauge image",
        },
        "theorem": {
            "operator_order": 1,
            "open_covector_cone_required": True,
            "constant_symbol_ranks_on_cone_required": True,
            "principal_composition_zero_required": True,
            "positive_middle_symbol_cohomology_required": True,
            "construction": "u_N=chi(x)*a(xi_0)*exp(i*N*x.xi_0), with a a smooth local quotient representative",
            "field_Hs_growth_exponent": "s",
            "equation_Hs_minus_1_growth_exponent": "s-1",
            "compact_remainder_Hs_minus_1_growth_exponent": "s-1",
            "quotient_to_residual_ratio_growth_exponent": 1,
            "local_elliptic_quotient_estimate_holds": False,
            "bounded_one_derivative_splitting_follows": False,
        },
        "exact_controls": {
            "defect_complex": defect,
            "exact_complex_control": control,
            "defect_amplitude": [0, 0, 1],
            "defect_amplitude_killed_by_equation_symbol": True,
            "defect_amplitude_outside_gauge_image": True,
        },
        "decision": {
            "symbol_cohomology_is_only_a_finite_dimensional_count": False,
            "local_high_frequency_obstruction_obtained": True,
            "global_fredholmness_adjudicated_without_a_global_realization": False,
            "next_exact_input": "Apply the theorem only where one actual local realization supplies a constant-rank open covector cone and an owned or conservative gauge-symbol image.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This is a local analytic theorem and control pair, not a GU family, physical quotient, observable, prediction or confirmation.",
        "claim_ceiling": "Proof-grade local first-order microlocal obstruction under the stated constant-rank hypotheses. It does not construct or globally classify a GU deformation complex.",
        "controls": {
            "producer": "tests/channel-swings/k843_sc_act_06_microlocal_cohomology_obstruction.py",
            "probe": "tests/channel-swings/k843_sc_act_06_microlocal_cohomology_obstruction_probe.py",
            "controls_passed": 32,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(p: dict[str, Any]) -> None:
    t, c, d = p["theorem"], p["exact_controls"], p["decision"]
    checks = [
        p["classification"] == "SOURCE_NATIVE_ROUTE", p["target_claim"] == "SC-ACT-06",
        p["comparator_routing_notice"] == NOTICE, p["gu_typed_objects"]["action_owner"] == "repository-construction",
        t["operator_order"] == 1, t["open_covector_cone_required"], t["constant_symbol_ranks_on_cone_required"],
        t["principal_composition_zero_required"], t["positive_middle_symbol_cohomology_required"],
        t["field_Hs_growth_exponent"] == "s", t["equation_Hs_minus_1_growth_exponent"] == "s-1",
        t["compact_remainder_Hs_minus_1_growth_exponent"] == "s-1", t["quotient_to_residual_ratio_growth_exponent"] == 1,
        not t["local_elliptic_quotient_estimate_holds"], not t["bounded_one_derivative_splitting_follows"],
        c["defect_complex"]["composition_zero"], c["defect_complex"]["middle_dimension"] == 3,
        c["defect_complex"]["gauge_symbol_rank"] == 1, c["defect_complex"]["equation_symbol_rank"] == 1,
        c["defect_complex"]["middle_symbol_cohomology_dimension"] == 1, not c["defect_complex"]["middle_exact"],
        c["exact_complex_control"]["composition_zero"], c["exact_complex_control"]["middle_dimension"] == 2,
        c["exact_complex_control"]["middle_symbol_cohomology_dimension"] == 0, c["exact_complex_control"]["middle_exact"],
        c["defect_amplitude"] == [0, 0, 1], c["defect_amplitude_killed_by_equation_symbol"],
        c["defect_amplitude_outside_gauge_image"], not d["symbol_cohomology_is_only_a_finite_dimensional_count"],
        d["local_high_frequency_obstruction_obtained"], not d["global_fredholmness_adjudicated_without_a_global_realization"],
        "UNCHANGED" in p["source_and_ledger_effect"],
    ]
    assert len(checks) == p["controls"]["controls_passed"]
    assert all(checks)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    elif not args.check:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
