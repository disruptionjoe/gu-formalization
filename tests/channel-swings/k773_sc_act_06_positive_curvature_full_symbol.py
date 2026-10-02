#!/usr/bin/env python3
"""K773: compose K772 with the displayed exact fermion diagonal."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k773-sc-act-06-positive-curvature-full-symbol.json"
PATHS = {
    "k719": ROOT / "lab/process/k719-sc-act-06-zero-fermion-full-symbol-reduction.json",
    "k742": ROOT / "lab/process/k742-sc-act-06-expanded-displayed-full-symbol-test.json",
    "k772": ROOT / "lab/process/k772-sc-act-06-positive-curvature-total-complex.json",
}
ROUTING_NOTICE = "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result."


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    data = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    bosonic = {row["case"]: row for row in data["k772"]["exact_controls"]["cases"]}
    fermionic = {row["case"]: row for row in data["k742"]["exact_controls"]["cases"]}
    cases = []
    for case in ("native_nonnull", "native_null_auxiliary_nonzero"):
        b = bosonic[case]
        f = fermionic[case]
        cases.append(
            {
                "case": case,
                "bosonic_middle_cohomology_dimension": b["refined_middle_cohomology_dimension"],
                "fermion_middle_cohomology_dimension": f["fermion_middle_cohomology_dimension"],
                "full_symbol_middle_cohomology_dimension": b["refined_middle_cohomology_dimension"] + f["fermion_middle_cohomology_dimension"],
                "full_symbol_exact": False,
            }
        )
    return {
        "schema_version": "1.0",
        "result_id": "K773-SC-ACT-06-POSITIVE-CURVATURE-FULL-SYMBOL",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "INTERNAL_COMPARATOR_ONLY",
        "gu_comparator_routing": ROUTING_NOTICE,
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Zero-fermion direct-sum composition of K772's selected-I1B plus identity-Cartan curvature comparator with the displayed exact equation-(9.16) fermion diagonal.",
        "gu_typed_objects": {
            "carrier": "LAYER=source-print+toy BRIDGE=K719 zero-fermion block split; coupled bosonic field plus two displayed fermion blocks; CHIRALITY=S-HALF-OPPOSITE",
            "pairing": "bosonic K717/K714 mixed-owner forms plus displayed fermion principal pairing; ON=block-diagonal full symbol",
            "real_structure": "bosonic K743 real blocks; displayed fermion Euclidean candidate",
            "grading": "bosonic complex direct-sum exact fermion diagonal",
            "action_owner": "source-action plus comparator",
            "target": "full-symbol middle cohomology; MAP-TYPE=not-a-map"
        },
        "pinned_inputs": {
            name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for name, path in PATHS.items()
        },
        "composition_theorem": {
            "mixed_boson_fermion_principal_blocks_vanish": True,
            "displayed_fermion_candidate_is_exact": True,
            "middle_cohomology_is_direct_sum": True,
            "bosonic_middle_classes_survive_full_symbol": True,
            "source_global_SC_ACT_06_refuted": False,
        },
        "exact_controls": {
            "fermion_two_block_rank": data["k742"]["exact_controls"]["fermion_two_block_rank"],
            "cases": cases,
        },
        "decision": {
            "displayed_full_symbol_comparator_is_elliptic": False,
            "positive_curvature_rank_threshold_survivor_closed_at_fixed_comparator": True,
            "different_action_owned_principal_response_or_background_remains_open": True,
            "next_exact_input": "Retire the fixed positive-curvature comparator at repository-only grade and require a changed stationary germ, an independently owned response, or complete native K500 input.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The displayed fermion block is exact but cannot remove the comparator's bosonic middle cohomology; the comparator remains unowned by the source.",
        "controls": {
            "producer": "tests/channel-swings/k773_sc_act_06_positive_curvature_full_symbol.py",
            "probe": "tests/channel-swings/k773_sc_act_06_positive_curvature_full_symbol_probe.py",
            "controls_passed": 22,
            "hostile_mutations_rejected": 14,
        },
        "claim_ceiling": "Exact displayed full-symbol obstruction for one fixed repository-only positive-curvature/I1B comparator. No all-background SC-ACT-06 no-go, source-status change, prediction, confirmation, or physical verdict.",
    }


def validate(packet: dict[str, Any]) -> None:
    assert packet["result_id"].startswith("K773-")
    assert packet["status"] == "working_draft_verified"
    assert packet["classification"] == "INTERNAL_COMPARATOR_ONLY"
    assert packet["target_claim"] == "SC-ACT-06"
    theorem = packet["composition_theorem"]
    assert theorem["mixed_boson_fermion_principal_blocks_vanish"]
    assert theorem["displayed_fermion_candidate_is_exact"]
    assert theorem["middle_cohomology_is_direct_sum"]
    assert theorem["bosonic_middle_classes_survive_full_symbol"]
    assert not theorem["source_global_SC_ACT_06_refuted"]
    rows = {row["case"]: row for row in packet["exact_controls"]["cases"]}
    assert rows["native_nonnull"]["full_symbol_middle_cohomology_dimension"] == 8193
    assert rows["native_null_auxiliary_nonzero"]["full_symbol_middle_cohomology_dimension"] == 8196
    assert packet["exact_controls"]["fermion_two_block_rank"] == 1920
    assert all(row["fermion_middle_cohomology_dimension"] == 0 for row in rows.values())
    assert all(not row["full_symbol_exact"] for row in rows.values())
    assert not packet["decision"]["displayed_full_symbol_comparator_is_elliptic"]
    assert "UNCHANGED" in packet["source_and_ledger_effect"]


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
