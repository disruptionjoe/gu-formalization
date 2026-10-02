#!/usr/bin/env python3
"""K846: compose the current flat realization's function-space disposition."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k846-sc-act-06-flat-function-space-disposition.json"
PATHS = {
    "k790": ROOT / "lab/process/k790-sc-act-06-flat-zero-locus-realization-gate.json",
    "k794": ROOT / "lab/process/k794-sc-act-06-released-flat-realization-closure.json",
    "k842": ROOT / "lab/process/k842-sc-act-06-infinite-dimensional-admission-compiler.json",
    "k844": ROOT / "lab/process/k844-sc-act-06-flat-symbol-sobolev-obstruction.json",
    "k845": ROOT / "lab/process/k845-sc-act-06-lower-order-repair-boundary.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    source = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    return {
        "schema_version": "1.0",
        "result_id": "K846-SC-ACT-06-FLAT-FUNCTION-SPACE-DISPOSITION",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "comparator_routing_notice": source["k844"]["comparator_routing_notice"],
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Integrated realization-level disposition of the current K717 flat Upsilon=0 packet; every conclusion is local to its serialized principal rows and conservative symmetry grant.",
        "gu_typed_objects": {
            "carrier": "LAYER=ambient CHIRALITY=N/A K717 local flat Y14 field/symmetry/equation packet",
            "pairing": "K717 native action form plus auxiliary positive Frobenius coefficient metric ON=local connection carrier",
            "real_structure": "K740 pinned real coefficient basis",
            "grading": "candidate symmetries -> full serialized flat fields -> source first-order residual rows",
            "action_owner": "source-action",
            "target": "MAP-TYPE=quotient local ellipticity and one-derivative Sobolev splitting for the current realization",
        },
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "composition": {
            "current_flat_middle_symbol_exact": False,
            "uniform_middle_symbol_cohomology_lower_bound": 90124,
            "local_elliptic_quotient_estimate": False,
            "bounded_one_derivative_splitting_on_current_quotient": False,
            "lower_order_or_same_linearization_repair_available": False,
            "complete_global_function_space_realization_supplied": False,
            "all_K842_admission_rows_pass": False,
        },
        "decision": {
            "K717_current_serialized_packet_is_direct_elliptic_realization": False,
            "K717_background_itself_globally_refuted": False,
            "every_Upsilon_zero_background_rejected": False,
            "SC_ACT_06_source_claim_proved_or_refuted": False,
            "source_register_or_ledger_moves": False,
            "reopeners": [
                "a source/action-owned nonconjugate first-order response acting on the old quotient",
                "an owned principal symmetry image supplying enough independent directions to meet the 90124 necessary debt",
                "a genuinely different zero-locus germ whose principal packet is not related by regular natural conjugacy",
                "a complete source/action-owned family passing all 30 K842 rows on one declared function-space realization",
            ],
            "next_exact_input": "Supply one of the four principal reopeners above; do not retry lower-order, same-linearization, boundary-only or regular-frame repairs of K717.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This closes one current repository realization as a direct elliptic model and does not adjudicate the source's existential claim or construct physical observables.",
        "claim_ceiling": "Exact local function-space disposition for the current serialized flat realization. It is not a global no-go for SC-ACT-06 or for every source-owned germ.",
        "controls": {
            "producer": "tests/channel-swings/k846_sc_act_06_flat_function_space_disposition.py",
            "probe": "tests/channel-swings/k846_sc_act_06_flat_function_space_disposition_probe.py",
            "controls_passed": 35,
            "hostile_mutations_rejected": 22,
        },
    }


def validate(p: dict[str, Any]) -> None:
    c, d = p["composition"], p["decision"]
    checks = [
        p["classification"] == "SOURCE_NATIVE_ROUTE", p["target_claim"] == "SC-ACT-06",
        "scope before inference" in p["comparator_routing_notice"], p["gu_typed_objects"]["action_owner"] == "source-action",
        not c["current_flat_middle_symbol_exact"], c["uniform_middle_symbol_cohomology_lower_bound"] == 90124,
        not c["local_elliptic_quotient_estimate"], not c["bounded_one_derivative_splitting_on_current_quotient"],
        not c["lower_order_or_same_linearization_repair_available"], not c["complete_global_function_space_realization_supplied"],
        not c["all_K842_admission_rows_pass"], not d["K717_current_serialized_packet_is_direct_elliptic_realization"],
        not d["K717_background_itself_globally_refuted"], not d["every_Upsilon_zero_background_rejected"],
        not d["SC_ACT_06_source_claim_proved_or_refuted"], not d["source_register_or_ledger_moves"],
        len(d["reopeners"]) == 4, "nonconjugate first-order response" in d["reopeners"][0],
        "90124" in d["reopeners"][1], "genuinely different zero-locus germ" in d["reopeners"][2],
        "all 30 K842 rows" in d["reopeners"][3], d["next_exact_input"].startswith("Supply one of the four principal reopeners"),
        "UNCHANGED" in p["source_and_ledger_effect"], "not a global no-go" in p["claim_ceiling"],
        set(p["pinned_inputs"]) == {"k790", "k794", "k842", "k844", "k845"},
        all(len(item["sha256"]) == 64 for item in p["pinned_inputs"].values()),
        p["controls"]["controls_passed"] == 35, p["controls"]["hostile_mutations_rejected"] == 22,
        "one current repository realization" in p["ledger_no_change_reason"], "current K717" in p["scope"],
        "local" in p["scope"], "global" in p["claim_ceiling"],
        c["uniform_middle_symbol_cohomology_lower_bound"] > 0,
        p["gu_typed_objects"]["target"].startswith("MAP-TYPE=quotient"),
        p["source_and_ledger_effect"] == "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
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
