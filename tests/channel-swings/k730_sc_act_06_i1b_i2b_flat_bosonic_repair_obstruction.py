#!/usr/bin/env python3
"""K730: strongest rank-subadditive I2B repair of K720's flat bosonic symbol."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PATHS = {
    "k720": ROOT / "lab/process/k720-sc-act-06-selected-i1b-euclidean-bosonic-symbol.json",
    "k729": ROOT / "lab/process/k729-sc-act-06-serialized-i2b-principal-rank-ceiling.json",
}
OUTPUT = ROOT / "lab/process/k730-sc-act-06-i1b-i2b-flat-bosonic-repair-obstruction.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    k720 = json.loads(PATHS["k720"].read_text(encoding="utf-8"))
    k729 = json.loads(PATHS["k729"].read_text(encoding="utf-8"))
    n = k720["exact_controls"]["field_dimension"]
    gauge = k720["exact_controls"]["owned_metric_diffeomorphism_rank"]
    repair = k729["serialized_bank"]["universal_extension_rank_ceiling"]
    cases = []
    for old in k720["exact_controls"]["cases"]:
        combined_rank_upper = min(n, old["action_euler_rank"] + repair)
        kernel_lower = n - combined_rank_upper
        cohomology_lower = kernel_lower - gauge
        cases.append({
            "case": old["case"],
            "i1b_rank": old["action_euler_rank"],
            "i2b_rank_ceiling": repair,
            "combined_rank_upper": combined_rank_upper,
            "combined_kernel_lower": kernel_lower,
            "owned_gauge_image_rank": gauge,
            "middle_cohomology_lower": cohomology_lower,
            "middle_exact_possible_under_rank_ceiling": cohomology_lower <= 0,
        })
    return {
        "schema_version": "1.0",
        "result_id": "K730-SC-ACT-06-I1B-I2B-FLAT-BOSONIC-REPAIR-OBSTRUCTION",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Rank-subadditive obstruction for augmenting K720's selected flat I1B bosonic symbol by the entire currently serialized 196-direction fixed-natural I2B bank with arbitrary weight and maximally favorable placement.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "rank_theorem": {
            "formula": "rank(A+cB) <= rank(A)+rank(B)",
            "valid_for_every_scalar_weight": True,
            "allows_maximally_favorable_image_placement": True,
            "requires_no_assumption_about_i1b_i2b_image_overlap": True,
            "zero_weight_cannot_improve_i1b": True,
            "nonzero_weight_cannot_exceed_i2b_rank_ceiling": True,
        },
        "exact_controls": {
            "field_dimension": n,
            "i2b_universal_rank_ceiling": repair,
            "owned_metric_diffeomorphism_rank": gauge,
            "cases": cases,
            "nonnull_middle_cohomology_lower": cases[0]["middle_cohomology_lower"],
            "native_null_middle_cohomology_lower": cases[1]["middle_cohomology_lower"],
        },
        "decision": {
            "serialized_i2b_bank_can_repair_k720_to_middle_exactness": False,
            "arbitrary_relative_weight_can_repair_k720": False,
            "current_flat_selected_i1b_plus_serialized_i2b_bosonic_realization_is_elliptic": False,
            "moving_all_grade_i2b_or_different_principal_owner_remains_open": True,
            "next_exact_input": "Construct an action-owned moving all-grade I2B or other principal packet with new image outside the serialized 196-direction bank, on a full stationary Euclidean germ with its actual gauge/redundancy complex.",
        },
        "gu_typed_objects": {
            "carrier": "K720 coupled metric/distortion field carrier of complex dimension 229386",
            "pairing": "K720 selected I1B action form plus a granted arbitrary-weight fixed-natural I2B endpoint bank",
            "real_structure": "rank statement after complexification; no Euclidean reality selector inferred",
            "grading": "rank-four metric diffeomorphism gauge -> coupled bosonic fields -> combined Euler rows",
            "action_owner": "I1B and I2B kept distinct; their weighted sum is tested as a strongest repair grant",
            "target": "middle exactness of the augmented flat bosonic principal symbol",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The theorem rejects only the current serialized low-rank I2B repair of one selected flat I1B realization; it does not exclude a moving all-grade second action or another stationary germ.",
        "controls": {
            "producer": "tests/channel-swings/k730_sc_act_06_i1b_i2b_flat_bosonic_repair_obstruction.py",
            "probe": "tests/channel-swings/k730_sc_act_06_i1b_i2b_flat_bosonic_repair_obstruction_probe.py",
            "controls_passed": 36,
            "hostile_mutations_rejected": 31,
        },
        "claim_ceiling": "Exact rank-subadditive obstruction for the frozen K720 symbol augmented by the complete currently serialized 196-direction I2B bank. No global I2B no-go, stationary-background theorem, source-status change, prediction, confirmation or physical verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, d = p["rank_theorem"], p["exact_controls"], p["decision"]
    assert p["target_claim"] == "SC-ACT-06"
    assert t["formula"] == "rank(A+cB) <= rank(A)+rank(B)"
    assert all(t[k] for k in (
        "valid_for_every_scalar_weight", "allows_maximally_favorable_image_placement",
        "requires_no_assumption_about_i1b_i2b_image_overlap", "zero_weight_cannot_improve_i1b",
        "nonzero_weight_cannot_exceed_i2b_rank_ceiling",
    ))
    assert c["field_dimension"] == 229386 and c["i2b_universal_rank_ceiling"] == 196
    assert c["owned_metric_diffeomorphism_rank"] == 4
    assert c["cases"] == [
        {"case": "native_nonnull", "i1b_rank": 130912, "i2b_rank_ceiling": 196, "combined_rank_upper": 131108, "combined_kernel_lower": 98278, "owned_gauge_image_rank": 4, "middle_cohomology_lower": 98274, "middle_exact_possible_under_rank_ceiling": False},
        {"case": "native_null_auxiliary_nonzero", "i1b_rank": 122748, "i2b_rank_ceiling": 196, "combined_rank_upper": 122944, "combined_kernel_lower": 106442, "owned_gauge_image_rank": 4, "middle_cohomology_lower": 106438, "middle_exact_possible_under_rank_ceiling": False},
    ]
    assert c["nonnull_middle_cohomology_lower"] == 98274
    assert c["native_null_middle_cohomology_lower"] == 106438
    assert not d["serialized_i2b_bank_can_repair_k720_to_middle_exactness"]
    assert not d["arbitrary_relative_weight_can_repair_k720"]
    assert not d["current_flat_selected_i1b_plus_serialized_i2b_bosonic_realization_is_elliptic"]
    assert d["moving_all_grade_i2b_or_different_principal_owner_remains_open"]
    assert "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
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
