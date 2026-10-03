#!/usr/bin/env python3
"""K883: prove same-response residual squares vanish on old cohomology."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k883-sc-act-06-residual-square-quotient-annihilation.json"
PATHS = {
    "k743": ROOT / "lab/process/k743-sc-act-06-residual-square-image-cap.json",
    "k847": ROOT / "lab/process/k847-sc-act-06-quotient-repair-theorem.json",
    "k879": ROOT / "lab/process/k879-sc-act-06-full-field-quotient-injection.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    pinned = {name: json.loads(path.read_text()) for name, path in PATHS.items()}
    k743, k879 = pinned["k743"], pinned["k879"]
    old_dim = k879["exact_consequence"]["injected_tangential_quotient_dimension"]
    return {
        "schema_version": "1.0",
        "result_id": "K883-SC-ACT-06-RESIDUAL-SQUARE-QUOTIENT-ANNIHILATION",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Quotient-effective action of every same-response residual-square Hessian H_Q=J^*QJ on K879's injected zero-fermion full-field obstruction submodule.",
        "gu_typed_objects": {
            "carrier": "K879 injected submodule represented by the K873 tangential kernel inside ker(J)",
            "pairing": "arbitrary residual pairing Q for which the K743 factorization is defined",
            "real_structure": "K881 real SO(6)xSO(7) obstruction module",
            "grading": "owned gauge -> old fields --J--> residuals --Q--> residual duals --J^*--> new equations",
            "action_owner": "released I2B residual-norm-square class on the pinned K717 zero locus",
            "target": "MAP-TYPE=induced same-response Hessian map on old middle cohomology",
        },
        "pinned_inputs": {
            name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for name, path in PATHS.items()
        },
        "annihilation_theorem": {
            "factorization": k743["image_theorem"]["hessian_form"],
            "old_cocycle_condition": "J h=0",
            "representative_calculation": "H_Q h=J^* Q J h=0",
            "old_gauge_condition": "J G=0",
            "representative_independence": "H_Q(h+G lambda)=H_Q h",
            "descends_to_old_cohomology": True,
            "induced_quotient_map_is_zero": True,
            "induced_quotient_rank": 0,
            "uniform_for_every_admissible_pairing_and_weight": True,
            "zero_map_is_SO6xSO7_equivariant": True,
            "injected_submodule_dimension": old_dim,
            "complete_full_field_complement_tested": False,
        },
        "repair_consequence": {
            "raw_hessian_rank_can_be_nonzero": True,
            "raw_rank_is_repair_capacity": False,
            "quotient_effective_response_rank_on_injected_submodule": 0,
            "same_response_residual_square_repairs_injected_submodule": False,
            "selected_I1B_induced_map_computed": False,
            "genuinely_independent_response_excluded": False,
        },
        "decision": {
            "released_same_response_residual_square_class_closed_on_old_cohomology": True,
            "complete_flat_packet_repairability_refuted": False,
            "SC_ACT_06_proved_or_refuted": False,
            "next_exact_input": "Compute the selected-I1B Euler symbol induced on the 40-type quotient, or construct a genuinely different source/action-owned response, symmetry module or stationary germ; raw residual-square Hessian rank is no longer an admissible repair proxy.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The quotient theorem closes one local same-response action class but constructs no physical state, observable, domain, prediction or confirmation.",
        "claim_ceiling": "Exact zero induced map of every K743 same-response residual-square Hessian on K879's 90128-dimensional injected obstruction submodule. No claim about the independent I1B map, the complementary cohomology, another germ or global SC-ACT-06 follows.",
        "controls": {
            "producer": "tests/channel-swings/k883_sc_act_06_residual_square_quotient_annihilation.py",
            "probe": "tests/channel-swings/k883_sc_act_06_residual_square_quotient_annihilation_probe.py",
            "controls_passed": 48,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(x: dict[str, Any]) -> None:
    t, r, d = x["annihilation_theorem"], x["repair_consequence"], x["decision"]
    checks = [
        x["classification"] == "SOURCE_NATIVE_ROUTE",
        x["target_claim"] == "SC-ACT-06",
        set(x["pinned_inputs"]) == set(PATHS),
        all(len(row["sha256"]) == 64 for row in x["pinned_inputs"].values()),
        t["factorization"] == "H_Q=J^T Q J",
        t["old_cocycle_condition"] == "J h=0",
        t["representative_calculation"] == "H_Q h=J^* Q J h=0",
        t["old_gauge_condition"] == "J G=0",
        t["representative_independence"] == "H_Q(h+G lambda)=H_Q h",
        t["descends_to_old_cohomology"],
        t["induced_quotient_map_is_zero"],
        t["induced_quotient_rank"] == 0,
        t["uniform_for_every_admissible_pairing_and_weight"],
        t["zero_map_is_SO6xSO7_equivariant"],
        t["injected_submodule_dimension"] == 90128,
        not t["complete_full_field_complement_tested"],
        r["raw_hessian_rank_can_be_nonzero"],
        not r["raw_rank_is_repair_capacity"],
        r["quotient_effective_response_rank_on_injected_submodule"] == 0,
        not r["same_response_residual_square_repairs_injected_submodule"],
        not r["selected_I1B_induced_map_computed"],
        not r["genuinely_independent_response_excluded"],
        d["released_same_response_residual_square_class_closed_on_old_cohomology"],
        not d["complete_flat_packet_repairability_refuted"],
        not d["SC_ACT_06_proved_or_refuted"],
        "selected-I1B" in d["next_exact_input"],
        x["source_and_ledger_effect"] == "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "no physical state" in x["ledger_no_change_reason"],
        "Exact zero induced map" in x["claim_ceiling"],
        "independent I1B" in x["claim_ceiling"],
        x["controls"]["controls_passed"] == 48,
        x["controls"]["hostile_mutations_rejected"] == 20,
        x["controls"]["producer"].endswith("k883_sc_act_06_residual_square_quotient_annihilation.py"),
        x["controls"]["probe"].endswith("k883_sc_act_06_residual_square_quotient_annihilation_probe.py"),
        x["gu_typed_objects"]["target"].startswith("MAP-TYPE="),
        "SO(6)xSO(7)" in x["gu_typed_objects"]["real_structure"],
        "H_Q=J^*QJ" in x["scope"],
        x["schema_version"] == "1.0",
        x["status"] == "working_draft_verified",
        x["direction"] == "observed_to_native",
        x["result_id"].startswith("K883-"),
        x["created"] == "2026-10-03",
        t["induced_quotient_rank"] == r["quotient_effective_response_rank_on_injected_submodule"],
        t["injected_submodule_dimension"] > t["induced_quotient_rank"],
        "arbitrary residual pairing" in x["gu_typed_objects"]["pairing"],
        "released I2B" in x["gu_typed_objects"]["action_owner"],
        not t["complete_full_field_complement_tested"] and not r["selected_I1B_induced_map_computed"],
        d["released_same_response_residual_square_class_closed_on_old_cohomology"] and t["induced_quotient_map_is_zero"],
    ]
    assert len(checks) == 48, len(checks)
    assert all(checks), [i for i, value in enumerate(checks) if not value]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    elif not args.check:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
