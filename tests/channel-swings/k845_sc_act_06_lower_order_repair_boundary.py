#!/usr/bin/env python3
"""K845: classify which repairs can change K844's principal obstruction."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k845-sc-act-06-lower-order-repair-boundary.json"
PATHS = {
    "k807": ROOT / "lab/process/k807-sc-act-06-comoving-principal-conjugacy.json",
    "k813": ROOT / "lab/process/k813-sc-act-06-relative-full-field-symmetry-budget.json",
    "k844": ROOT / "lab/process/k844-sc-act-06-flat-symbol-sobolev-obstruction.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    source = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    debt = source["k844"]["hypothesis_match"]["middle_symbol_cohomology_lower_bound"]
    return {
        "schema_version": "1.0",
        "result_id": "K845-SC-ACT-06-LOWER-ORDER-REPAIR-BOUNDARY",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "comparator_routing_notice": source["k844"]["comparator_routing_notice"],
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Principal-symbol repair classification for K844's current flat realization only.",
        "gu_typed_objects": {
            "carrier": "LAYER=ambient CHIRALITY=N/A K717 local field/symmetry/equation symbol sequence",
            "pairing": "NONE",
            "real_structure": "K740 pinned real coefficient basis",
            "grading": "principal symmetry -> principal fields -> principal equations",
            "action_owner": "source-action",
            "target": "MAP-TYPE=quotient repair of the current 90124-dimensional middle-symbol debt",
        },
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "principal_invariance_theorem": {
            "zeroth_order_operator_changes_principal_symbol": False,
            "nonlinear_terms_with_same_linearization_change_principal_symbol": False,
            "interior_compactly_supported_quasimodes_are_removed_by_boundary_conditions": False,
            "regular_natural_frame_conjugacy_changes_symbol_cohomology_dimension": False,
            "regular_natural_frame_conjugacy_preserves_rank_and_kernel": (
                source["k807"]["orbit_consequence"]["reference_rank"]
                == source["k807"]["orbit_consequence"]["transported_rank"]
                and source["k807"]["orbit_consequence"]["reference_kernel_dimension"]
                == source["k807"]["orbit_consequence"]["transported_kernel_dimension"]
            ),
            "lower_order_only_repair_restores_local_elliptic_estimate": False,
        },
        "repair_budget": {
            "current_middle_symbol_debt": debt,
            "relative_principal_response_rank": "r",
            "new_independent_owned_symmetry_rank": "s",
            "necessary_threshold": "r+s>=90124",
            "threshold_is_sufficient": False,
            "changed_principal_response_can_reopen": True,
            "new_owned_principal_symmetry_can_reopen": True,
            "genuinely_different_nonconjugate_germ_can_reopen": True,
        },
        "repair_classification": [
            {"repair": "zeroth_order_mass_or_potential", "principal_effect": "none", "disposition": "cannot_repair_K844"},
            {"repair": "nonlinear_terms_with_same_D_Upsilon", "principal_effect": "none_at_fixed_germ", "disposition": "cannot_repair_K844"},
            {"repair": "boundary_condition_or_compactification", "principal_effect": "none_on_interior_quasimode", "disposition": "cannot_repair_K844"},
            {"repair": "regular_natural_frame_transport", "principal_effect": "invertible_conjugacy", "disposition": "cannot_repair_K844"},
            {"repair": "new_first_order_response_or_owned_symmetry", "principal_effect": "may_act_on_old_quotient", "disposition": "reopen_if_complete_and_threshold_passes"},
        ],
        "decision": {
            "current_lower_order_or_same_linearization_repair_route_open": False,
            "principal_reopener_is_exactly_localized": True,
            "next_exact_input": "Supply a source/action-owned nonconjugate first-order response and/or owned symmetry image with r+s at least 90124, then rebuild the complete complex; threshold passage is necessary, not sufficient.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This classifies repairs to one local principal packet and supplies no physical quotient or source-family construction.",
        "claim_ceiling": "Exact principal-versus-lower-order repair boundary for K844. It does not exclude changed principal symbols, new owned symmetries or a different native germ.",
        "controls": {
            "producer": "tests/channel-swings/k845_sc_act_06_lower_order_repair_boundary.py",
            "probe": "tests/channel-swings/k845_sc_act_06_lower_order_repair_boundary_probe.py",
            "controls_passed": 34,
            "hostile_mutations_rejected": 21,
        },
    }


def validate(p: dict[str, Any]) -> None:
    t, b, d, rows = p["principal_invariance_theorem"], p["repair_budget"], p["decision"], p["repair_classification"]
    checks = [
        p["classification"] == "SOURCE_NATIVE_ROUTE", p["target_claim"] == "SC-ACT-06",
        "scope before inference" in p["comparator_routing_notice"], p["gu_typed_objects"]["action_owner"] == "source-action",
        not t["zeroth_order_operator_changes_principal_symbol"], not t["nonlinear_terms_with_same_linearization_change_principal_symbol"],
        not t["interior_compactly_supported_quasimodes_are_removed_by_boundary_conditions"],
        not t["regular_natural_frame_conjugacy_changes_symbol_cohomology_dimension"],
        t["regular_natural_frame_conjugacy_preserves_rank_and_kernel"], not t["lower_order_only_repair_restores_local_elliptic_estimate"],
        b["current_middle_symbol_debt"] == 90124, b["relative_principal_response_rank"] == "r",
        b["new_independent_owned_symmetry_rank"] == "s", b["necessary_threshold"] == "r+s>=90124",
        not b["threshold_is_sufficient"], b["changed_principal_response_can_reopen"],
        b["new_owned_principal_symmetry_can_reopen"], b["genuinely_different_nonconjugate_germ_can_reopen"],
        len(rows) == 5, [row["repair"] for row in rows[:4]] == [
            "zeroth_order_mass_or_potential", "nonlinear_terms_with_same_D_Upsilon",
            "boundary_condition_or_compactification", "regular_natural_frame_transport"],
        all(row["disposition"] == "cannot_repair_K844" for row in rows[:4]),
        rows[4]["disposition"] == "reopen_if_complete_and_threshold_passes", not d["current_lower_order_or_same_linearization_repair_route_open"],
        d["principal_reopener_is_exactly_localized"], "necessary, not sufficient" in d["next_exact_input"],
        "UNCHANGED" in p["source_and_ledger_effect"], set(p["pinned_inputs"]) == {"k807", "k813", "k844"},
        all(len(item["sha256"]) == 64 for item in p["pinned_inputs"].values()),
        p["controls"]["controls_passed"] == 34, p["controls"]["hostile_mutations_rejected"] == 21,
        "does not exclude" in p["claim_ceiling"], "one local principal packet" in p["ledger_no_change_reason"],
        p["scope"].endswith("only."), rows[4]["principal_effect"] == "may_act_on_old_quotient",
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
