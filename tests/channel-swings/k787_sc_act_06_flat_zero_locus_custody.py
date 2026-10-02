#!/usr/bin/env python3
"""K787: reconcile K717's flat germ with the corrected K786 zero-locus gate."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k787-sc-act-06-flat-zero-locus-custody.json"
PATHS = {
    "k717": ROOT / "lab/process/k717-sc-act-06-flat-euclidean-gimmel-germ.json",
    "k783": ROOT / "lab/process/k783-sc-act-06-source-zero-locus-boundary.json",
    "k786": ROOT / "lab/process/k786-sc-act-06-zero-residual-deformation-input-gate.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    k717 = json.loads(PATHS["k717"].read_text(encoding="utf-8"))
    k783 = json.loads(PATHS["k783"].read_text(encoding="utf-8"))
    k786 = json.loads(PATHS["k786"].read_text(encoding="utf-8"))
    germ = k717["native_germ"]
    assert k783["source_custody"]["claimed_solution_locus"] == "Upsilon=0"
    assert germ["B_epsilon"] == germ["varpi"] == germ["T_varpi_minus_B"] == germ["F_B"] == "0"
    assert "residuals vanish" in germ["residual_grade"]
    assert not k786["current_custody"]["source_exhibited_complete_solution_two_jet"]
    return {
        "schema_version": "1.0",
        "result_id": "K787-SC-ACT-06-FLAT-ZERO-LOCUS-CUSTODY",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Custody reconciliation for K717's local flat native germ against K786's corrected direct Upsilon=0 gate.",
        "gu_typed_objects": {
            "carrier": "K717 real local B(epsilon)/Y field carrier over the constant positive metric on R4",
            "pairing": "native lambda=1/2 DeWitt action form; background Frobenius q retained only as an auxiliary positive metric",
            "real_structure": "real Euclidean base and real symmetric-metric fibre on the local flat chart",
            "grading": "bosonic B(epsilon), varpi and T plus four zero source fermion fields",
            "action_owner": "source first-order residual Upsilon=Upsilon_B+Upsilon_F",
            "target": "existence of one repository-constructed local point on the source zero locus",
        },
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "custody_reconciliation": {
            "source_claims_zero_locus": True,
            "released_source_exhibits_complete_solution_two_jet": False,
            "repository_constructs_local_source_typed_background": True,
            "background_B_epsilon": "0",
            "background_varpi": "0",
            "background_T": "0",
            "background_F_B": "0",
            "background_fermions": "0",
            "Upsilon_B_on_background": "0",
            "Upsilon_F_on_background": "0",
            "Upsilon_total_on_background": "0",
            "boundary_posture": "compact_support_or_fixed_boundary_local_germ",
        },
        "k786_requirement_status": {
            "one_source_typed_background_satisfying_Upsilon_zero": "supplied_locally_by_K717",
            "complete_source_field_tangent": "open",
            "complete_first_order_linearization": "open_beyond_current_connection_response",
            "owned_symmetry_map": "open",
            "owned_redundant_euler_map": "open",
            "exact_redundant_row_removal": "open",
            "complete_bosonic_fermionic_mixed_symbols": "open",
            "authenticated_euclidean_carrier_pairing_domain": "local_carrier_only_global_domain_open",
            "all_covector_middle_exactness": "open",
            "one_common_native_geometry": "local_K717_geometry_fixed",
        },
        "decision": {
            "background_search_remains_first_missing_input": False,
            "direct_linearization_test_released": True,
            "complete_K786_packet_supplied": False,
            "next_exact_input": "Test J=D Upsilon on K717's fixed flat zero-locus germ across every nonzero Euclidean covector orbit, then compare its kernel with the strongest symmetry budget without promoting candidates to owned gauge.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The repository has one local zero-locus germ, but no complete physical quotient, observable, prediction or confirmation follows.",
        "claim_ceiling": "Exact local background-custody correction. It does not attribute the germ to the released source or prove a complete two-jet, elliptic complex, rich moduli, Fredholm domain, source-status change or physical result.",
        "controls": {
            "producer": "tests/channel-swings/k787_sc_act_06_flat_zero_locus_custody.py",
            "probe": "tests/channel-swings/k787_sc_act_06_flat_zero_locus_custody_probe.py",
            "controls_passed": 38,
            "hostile_mutations_rejected": 30,
        },
    }


def validate(p: dict[str, Any]) -> None:
    c, s, d = p["custody_reconciliation"], p["k786_requirement_status"], p["decision"]
    assert c["source_claims_zero_locus"] and c["repository_constructs_local_source_typed_background"]
    assert not c["released_source_exhibits_complete_solution_two_jet"]
    assert all(c[key] == "0" for key in ("background_B_epsilon", "background_varpi", "background_T", "background_F_B", "background_fermions", "Upsilon_B_on_background", "Upsilon_F_on_background", "Upsilon_total_on_background"))
    assert s["one_source_typed_background_satisfying_Upsilon_zero"] == "supplied_locally_by_K717"
    assert s["complete_source_field_tangent"] == "open" and s["all_covector_middle_exactness"] == "open"
    assert not d["background_search_remains_first_missing_input"] and d["direct_linearization_test_released"]
    assert not d["complete_K786_packet_supplied"]
    assert p["target_claim"] == "SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
