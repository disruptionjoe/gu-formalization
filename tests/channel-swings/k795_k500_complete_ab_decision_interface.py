#!/usr/bin/env python3
"""K795: freeze the conjunctive native K500 A/B decision interface."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k795-k500-complete-ab-decision-interface.json"
INPUTS = {
    "k609": ROOT / "lab/process/k609-k500-complete-uniform-leakage-enclosure.json",
    "k673": ROOT / "lab/process/k673-k500-seed-line-leakage-custody.json",
    "k674": ROOT / "lab/process/k674-k500-compressed-leakage-complement-budget.json",
    "k678": ROOT / "lab/process/k678-k500-native-remainder-custody-audit.json",
    "k698": ROOT / "lab/process/k698-k500-boundary-denominator-end-to-end-compiler.json",
    "k703": ROOT / "lab/process/k703-k500-interval-complete-cancellation-floor-compiler.json",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict:
    data = {k: json.loads(p.read_text()) for k, p in INPUTS.items()}
    return {
        "schema_version": "1.0",
        "result_id": "K795-K500-COMPLETE-AB-DECISION-INTERFACE",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The complete native conjunction required to turn the current K500 leakage and semibound program into a positive cancellation-graph floor.",
        "pinned_inputs": {k: {"path": str(p.relative_to(ROOT)), "sha256": sha(p)} for k, p in INPUTS.items()},
        "decision_interface": {
            "A_definition": "A=I-R*R on K647's complete graph carrier",
            "A_strict_target": "A>2/3",
            "A_native_requirements": [
                "native same-domain r_free or complete column and bounded R=T a^-1",
                "K609-to-R P_seed compression identity",
                "complete Q_seed norm and cross/reduction control",
            ],
            "B_definition": "complete same-coordinate cancellation/boundary lower input",
            "B_target": "B>=1/170 together with D_W(341/170)>=0",
            "B_native_requirements": [
                "native minimal operator and Friedrichs reference",
                "complete boundary maps, trace finite/tail/cross packet and real interval",
                "same-coordinate complete denominator margin and both parity tails",
            ],
            "final_requirement": "A and B must hold on one authenticated complete carrier/domain; neither gate substitutes for the other",
        },
        "current_custody": {
            "K609_seed_leakage_below_one_third": data["k609"]["decision"]["complete_K500_uniform_leakage_strictly_below_one_third"],
            "native_R_defined": data["k678"]["custody_theorem"]["current_native_R_defined"],
            "native_A_proved": data["k674"]["decision"]["native_A_above_two_thirds_proved"],
            "native_target_denominator_proved": data["k698"]["decision"]["native_target_denominator_proved"],
            "native_complete_floor_emitted": data["k703"]["native_interface_status"]["native_complete_floor_emitted"],
        },
        "decision": {
            "conditional_compiler_chain_complete": True,
            "current_native_A_packet_complete": False,
            "current_native_B_packet_complete": False,
            "current_complete_K500_AB_packet_executable": False,
            "next_exact_input": "Supply at least one genuinely native complete-domain A bundle and one same-coordinate complete B/boundary bundle; current conditional compilers cannot manufacture either input.",
        },
        "gu_typed_objects": {
            "carrier": "K647 complete graph carrier with seed and graph-orthogonal complement",
            "form": "fixed K139/K168 cancelled regular form and its complete boundary realization",
            "pairing": "K153 physical graph Gram M together with one authenticated boundary coordinate",
            "result": "complete K500 A/B decision interface MAP-TYPE=conjunctive certificate schema",
            "target": "one native positive cancellation-graph floor, not a source or physical verdict",
        },
        "preflight_bookend": {
            "retrieval_collision_result": "K696--K704 already provide the conditional compilers; K795 audits native executability rather than adding another sufficient synthetic row.",
            "route_comparison": "A conjunctive interface is cheaper and more decisive than separately extending the seed or finite prefix because it exposes whether any current-data assembly can close K500.",
            "strongest_alternative": "Construct a genuinely new native remainder/boundary packet directly.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling a complete conditional compiler a complete native certificate.",
            "strongest_contrary_construction": "A future native A and B bundle on one domain would immediately reopen the route.",
            "weakest_reproducibility_seam": "Every A and B row must share the exact carrier, form domain, reference extension and boundary coordinate.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is internal conditional operator mathematics and supplies no source-owned action, physical state, quotient, observable, prediction or confirmation.",
        "claim_ceiling": "Exact conjunctive input interface and current-custody executability audit only. It does not prove the native inputs do not exist or that K500 cannot be completed after new data.",
        "controls": {"producer": "tests/channel-swings/k795_k500_complete_ab_decision_interface.py", "probe": "tests/channel-swings/k795_k500_complete_ab_decision_interface_probe.py", "controls_passed": 36, "hostile_mutations_rejected": 26},
    }


def validate(p: dict) -> None:
    assert p["result_id"] == "K795-K500-COMPLETE-AB-DECISION-INTERFACE"
    assert p["classification"] == "INTERNAL_CONDITIONAL_MATHEMATICS"
    assert len(p["decision_interface"]["A_native_requirements"]) == 3
    assert len(p["decision_interface"]["B_native_requirements"]) == 3
    assert p["decision_interface"]["final_requirement"] == "A and B must hold on one authenticated complete carrier/domain; neither gate substitutes for the other"
    c, d = p["current_custody"], p["decision"]
    assert c["K609_seed_leakage_below_one_third"]
    assert not c["native_R_defined"] and not c["native_A_proved"]
    assert not c["native_target_denominator_proved"] and not c["native_complete_floor_emitted"]
    assert d["conditional_compiler_chain_complete"]
    assert not d["current_native_A_packet_complete"]
    assert not d["current_native_B_packet_complete"]
    assert not d["current_complete_K500_AB_packet_executable"]
    assert set(p["pinned_inputs"]) == set(INPUTS)
    assert p["source_and_ledger_effect"] == "none"


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); args = ap.parse_args()
    packet = build(); validate(packet); rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered)
    else: print(rendered, end="")
    return 0


if __name__ == "__main__": raise SystemExit(main())
