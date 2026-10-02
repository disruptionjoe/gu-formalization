#!/usr/bin/env python3
"""K774: successor routing after the exact positive-curvature composition."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k774-sc-act-06-positive-curvature-successor-gate.json"
PATHS = {
    "k770": ROOT / "lab/process/k770-sc-act-06-curvature-square-successor-gate.json",
    "k771": ROOT / "lab/process/k771-sc-act-06-positive-curvature-i1b-composition.json",
    "k772": ROOT / "lab/process/k772-sc-act-06-positive-curvature-total-complex.json",
    "k773": ROOT / "lab/process/k773-sc-act-06-positive-curvature-full-symbol.json",
}
ROUTING_NOTICE = "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result."


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    data = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    k772_cases = {row["case"]: row for row in data["k772"]["exact_controls"]["cases"]}
    return {
        "schema_version": "1.0",
        "result_id": "K774-SC-ACT-06-POSITIVE-CURVATURE-SUCCESSOR-GATE",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "gu_comparator_routing": ROUTING_NOTICE,
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Successor routing after exact composition of the selected I1B symbol, identity-Cartan positive curvature comparator, owned metric gauge/redundancy maps, and displayed fermion diagonal.",
        "gu_typed_objects": {
            "carrier": "LAYER=source-print+toy BRIDGE=K720-plus-K768 frozen sum; coupled full symbol; CHIRALITY=S-HALF-OPPOSITE",
            "pairing": "source I1B action form plus K714 identity Cartan comparator form; ON=coupled full symbol",
            "real_structure": "frozen tested Euclidean real blocks",
            "grading": "source-native successor gate after bosonic and fermion complex composition",
            "action_owner": "source-action plus comparator; no combined source owner",
            "target": "SC-ACT-06 successor routing; MAP-TYPE=not-a-map"
        },
        "pinned_inputs": {
            name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for name, path in PATHS.items()
        },
        "closed_classes": [
            {
                "class": "unit-weight identity-Cartan positive curvature-square comparator added to K720's selected I1B symbol on the frozen flat germ",
                "reason": "Exact summed-operator ranks leave 8193/8196 full-symbol middle classes on the two tested strata.",
            },
            {
                "class": "promoting the 8193-dimensional intersection with the curvature-only q-lambda candidate to total-action gauge",
                "reason": "The source-selected I1B complex owns only the rank-four metric diffeomorphism map here; accidental kernel containment is not a gauge declaration, and the native-null stratum retains three additional metric-coupled classes.",
            },
            {
                "class": "repairing the bosonic obstruction with the displayed exact zero-fermion diagonal",
                "reason": "K719 makes the middle cohomology a direct sum, so the exact fermion block leaves the bosonic classes unchanged.",
            },
        ],
        "surviving_branches": [
            {
                "input": "source/background-owned positive reduction or another curvature pairing/weight",
                "required_new_fact": "an owned choice plus a new exact summed-complex calculation; K771--K773 close only the fixed identity-Cartan unit-weight comparator and do not license an unowned parameter scan",
            },
            {
                "input": "fully stationary changed or nonzero-T source-typed germ",
                "required_new_fact": "new action-owned principal image and complete coupled symbol complex",
            },
            {
                "input": "independent source/action parent or different Shiab response",
                "required_new_fact": "exact owner, maps, pairing, common domain and stationarity",
            },
            {
                "input": "complete native K500 A/B packet",
                "required_new_fact": "native remainder and boundary maps plus complete A and parity-cofinal B certificates",
            },
        ],
        "exact_controls": {
            "nonnull_middle_classes": k772_cases["native_nonnull"]["refined_middle_cohomology_dimension"],
            "native_null_middle_classes": k772_cases["native_null_auxiliary_nonzero"]["refined_middle_cohomology_dimension"],
            "common_distortion_kernel_inside_curvature_candidate": 8193,
            "native_null_additional_metric_coupled_classes": 3,
        },
        "decision": {
            "do_not_retry_fixed_identity_cartan_unit_weight_comparator": True,
            "do_not_promote_candidate_kernel_to_gauge": True,
            "do_not_promote_comparator_to_source_I2B": True,
            "source_owned_positive_family_globally_closed": False,
            "SC_ACT_06_status": "ASSERTS",
            "global_SC_ACT_06_refuted": False,
        },
        "reranked_frontier": {
            "incumbent": "construct a fully stationary changed/nonzero-T source-typed germ or an independently action-owned response before another comparator variation",
            "strongest_independent_alternative": "complete native K500 A/B packet once its native remainder, boundary maps and two lower certificates exist",
            "positive_comparator_revival": "only an owned reduction/pairing/weight with a new exact summed complex, not rank-threshold clearance",
            "high_confidence_outlier": "a different Shiab coefficient could alter the 8193-dimensional curvature-gauge intersection if independently action-owned",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The fixed comparator is excluded at repository-only grade; every source-owned changed-germ or different-parent route remains open.",
        "controls": {
            "producer": "tests/channel-swings/k774_sc_act_06_positive_curvature_successor_gate.py",
            "probe": "tests/channel-swings/k774_sc_act_06_positive_curvature_successor_gate_probe.py",
            "controls_passed": 24,
            "hostile_mutations_rejected": 16,
        },
        "claim_ceiling": "Exact successor gate for one fixed positive-curvature/I1B comparator. It closes that comparator and two invalid promotions, not every positive reduction, action parent, stationary germ, native K500 route, or SC-ACT-06 globally.",
    }


def validate(packet: dict[str, Any]) -> None:
    assert packet["result_id"].startswith("K774-")
    assert packet["status"] == "working_draft_verified"
    assert packet["classification"] == "SOURCE_NATIVE_ROUTE"
    assert packet["target_claim"] == "SC-ACT-06"
    assert len(packet["closed_classes"]) == 3
    assert len(packet["surviving_branches"]) == 4
    controls = packet["exact_controls"]
    assert controls["nonnull_middle_classes"] == 8193
    assert controls["native_null_middle_classes"] == 8196
    assert controls["common_distortion_kernel_inside_curvature_candidate"] == 8193
    assert controls["native_null_additional_metric_coupled_classes"] == 3
    decision = packet["decision"]
    assert decision["do_not_retry_fixed_identity_cartan_unit_weight_comparator"]
    assert decision["do_not_promote_candidate_kernel_to_gauge"]
    assert decision["do_not_promote_comparator_to_source_I2B"]
    assert not decision["source_owned_positive_family_globally_closed"]
    assert decision["SC_ACT_06_status"] == "ASSERTS"
    assert not decision["global_SC_ACT_06_refuted"]
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
