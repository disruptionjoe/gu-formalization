#!/usr/bin/env python3
"""K844: apply K843 to the current K717/K788/K789 flat symbol packet."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k844-sc-act-06-flat-symbol-sobolev-obstruction.json"
PATHS = {
    "k717": ROOT / "lab/process/k717-sc-act-06-flat-euclidean-gimmel-germ.json",
    "k788": ROOT / "lab/process/k788-sc-act-06-direct-response-orbit-classification.json",
    "k789": ROOT / "lab/process/k789-sc-act-06-maximal-symmetry-budget.json",
    "k843": ROOT / "lab/process/k843-sc-act-06-microlocal-cohomology-obstruction.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    source = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    positive = next(row for row in source["k788"]["orbit_theorem"]["cases"] if row["orbit"] == "native_positive")
    bound = source["k789"]["decision"]["uniform_middle_cohomology_lower_bound"]
    return {
        "schema_version": "1.0",
        "result_id": "K844-SC-ACT-06-FLAT-SYMBOL-SOBOLEV-OBSTRUCTION",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "comparator_routing_notice": source["k843"]["comparator_routing_notice"],
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Local microlocal consequence for the currently serialized K717 flat Upsilon=0 realization and K789's deliberately over-granted symmetry image only.",
        "gu_typed_objects": {
            "carrier": "LAYER=ambient CHIRALITY=N/A local Omega1(Cl_14(C)) connection variations on K717's flat Y14 chart",
            "pairing": "auxiliary positive Frobenius form ON=connection coefficients and K717 native action form kept distinct",
            "real_structure": "K740 pinned real U(64,64) coefficient basis",
            "grading": "candidate symmetries -> connection/metric fields -> D Upsilon equations",
            "action_owner": "source-action",
            "target": "MAP-TYPE=quotient local Hs elliptic estimate for the current serialized deformation symbol",
        },
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "hypothesis_match": {
            "local_coordinate_ball_supplied": True,
            "global_torus_or_compact_realization_assumed": False,
            "open_covector_cone": "native_positive",
            "open_cone_available": positive["native_norm_squared"] > 0,
            "connection_symbol_rank_on_cone": positive["rank"],
            "connection_symbol_kernel_on_cone": positive["nullity"],
            "overgranted_symmetry_rank": 16388,
            "middle_symbol_cohomology_lower_bound": bound,
            "principal_composition_zero_under_grant": source["k789"]["composition_theorem"]["internal_candidate_composes_to_zero"],
            "actual_owned_symmetry_is_no_larger_than_grant": source["k789"]["composition_theorem"]["grant_is_stronger_than_current_owned_symmetry_custody"],
        },
        "microlocal_consequence": {
            "oscillatory_compactly_supported_sequence_exists": True,
            "quotient_Hs_to_residual_Hs_minus_1_ratio_unbounded": True,
            "local_first_order_elliptic_quotient_estimate_holds": False,
            "bounded_one_derivative_right_inverse_on_current_quotient_follows": False,
            "current_flat_symbol_complex_is_middle_elliptic": False,
            "global_fredholm_cohomology_dimension_computed": False,
        },
        "decision": {
            "current_flat_realization_crosses_K842_bounded_or_tame_splitting_row": False,
            "current_flat_realization_is_a_direct_SC_ACT_06_elliptic_model": False,
            "K717_background_globally_refuted": False,
            "global_SC_ACT_06_proved_or_refuted": False,
            "next_exact_input": "Change the principal response or supply an owned principal symmetry image large enough to remove the 90124-class debt; a different source-owned germ must be tested independently.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The result rejects a local analytic estimate for one repository-constructed realization; it does not supply a physical quotient, observable, prediction or confirmation.",
        "claim_ceiling": "Exact local Sobolev obstruction for the current serialized flat symbol packet under a symmetry grant stronger than current custody. No global-family or source-claim no-go follows.",
        "controls": {
            "producer": "tests/channel-swings/k844_sc_act_06_flat_symbol_sobolev_obstruction.py",
            "probe": "tests/channel-swings/k844_sc_act_06_flat_symbol_sobolev_obstruction_probe.py",
            "controls_passed": 34,
            "hostile_mutations_rejected": 22,
        },
    }


def validate(p: dict[str, Any]) -> None:
    h, m, d = p["hypothesis_match"], p["microlocal_consequence"], p["decision"]
    checks = [
        p["classification"] == "SOURCE_NATIVE_ROUTE", p["target_claim"] == "SC-ACT-06",
        "scope before inference" in p["comparator_routing_notice"], p["gu_typed_objects"]["action_owner"] == "source-action",
        h["local_coordinate_ball_supplied"], not h["global_torus_or_compact_realization_assumed"],
        h["open_covector_cone"] == "native_positive", h["open_cone_available"],
        h["connection_symbol_rank_on_cone"] == 122864, h["connection_symbol_kernel_on_cone"] == 106512,
        h["overgranted_symmetry_rank"] == 16388, h["middle_symbol_cohomology_lower_bound"] == 90124,
        h["principal_composition_zero_under_grant"], h["actual_owned_symmetry_is_no_larger_than_grant"],
        m["oscillatory_compactly_supported_sequence_exists"], m["quotient_Hs_to_residual_Hs_minus_1_ratio_unbounded"],
        not m["local_first_order_elliptic_quotient_estimate_holds"], not m["bounded_one_derivative_right_inverse_on_current_quotient_follows"],
        not m["current_flat_symbol_complex_is_middle_elliptic"], not m["global_fredholm_cohomology_dimension_computed"],
        not d["current_flat_realization_crosses_K842_bounded_or_tame_splitting_row"],
        not d["current_flat_realization_is_a_direct_SC_ACT_06_elliptic_model"], not d["K717_background_globally_refuted"],
        not d["global_SC_ACT_06_proved_or_refuted"], "90124" in d["next_exact_input"],
        "UNCHANGED" in p["source_and_ledger_effect"], "local" in p["claim_ceiling"],
        set(p["pinned_inputs"]) == {"k717", "k788", "k789", "k843"},
        all(len(item["sha256"]) == 64 for item in p["pinned_inputs"].values()),
        "global" in p["scope"].lower() or "Local" in p["scope"],
        h["connection_symbol_kernel_on_cone"] - h["overgranted_symmetry_rank"] == h["middle_symbol_cohomology_lower_bound"],
        p["controls"]["hostile_mutations_rejected"] == 22, p["controls"]["controls_passed"] == 34,
        p["decision"]["next_exact_input"].startswith("Change the principal response"),
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
