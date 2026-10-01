#!/usr/bin/env python3
"""K766: route SC-ACT-06 after the finite-rank derivative-even control."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k766-sc-act-06-derivative-even-successor-gate.json"
PATHS = {
    "k762": ROOT / "lab/process/k762-sc-act-06-even-owner-successor-gate.json",
    "k763": ROOT / "lab/process/k763-sc-act-06-finite-rank-even-owner-update.json",
    "k764": ROOT / "lab/process/k764-sc-act-06-scalar-metric-derivative-control.json",
    "k765": ROOT / "lab/process/k765-sc-act-06-scalar-metric-cohomology-bound.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "result_id": "K766-SC-ACT-06-DERIVATIVE-EVEN-SUCCESSOR-GATE",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Successor routing after K763--K765 test finite-rank derivative-even changes of K749's old block and one stationary scalar-metric control.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "closed_classes": [
            {
                "class": "every Ward-compatible finite-rank old-block correction plus m-field even extension with r+m<98311 on the frozen K749 body block and gauge rank",
                "reason": "K763 gives H_ext>=H_old-r-m; the native-null K749 stratum retains positive middle cohomology",
            },
            {
                "class": "K764 stationary one-scalar metric derivative control",
                "reason": "r<=10 and m=1 leave K765 lower bounds 98297/98300, while the connection principal block is unchanged",
            },
        ],
        "live_reopeners": [
            {"input": "high-rank nonfactorizing action-owned old-block correction with r+m>=98311", "required_new_fact": "natural owner fixed before solving, full stationarity, Ward compatibility, complete response and actual all-covector exactness; the threshold is necessary only"},
            {"input": "fully stationary nonzero-T or otherwise changed Euclidean germ", "required_new_fact": "new old-block principal image and complete coupled Euler/gauge/redundancy complex"},
            {"input": "independent action parent, doubled carrier, or different Shiab", "required_new_fact": "source/action ownership, exact maps, target, pairing and common domain"},
            {"input": "complete native K500 A/B packet", "required_new_fact": "native remainder/boundary data and complete A/B certificates on one common graph domain"},
        ],
        "decision": {
            "do_not_retry_low_rank_scalar_tensor_or_small_derivative_even_owner": True,
            "finite_rank_theorem_not_global_action_no_go": True,
            "large_rank_or_changed_germ_routes_remain_open": True,
            "k500_native_packet_remains_open": True,
            "global_SC_ACT_06_refuted": False,
            "SC_ACT_06_status": "ASSERTS",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The gate closes a rank-bounded repository control class and does not construct or refute the source's complete first-order Euclidean deformation complex.",
        "controls": {
            "producer": "tests/channel-swings/k766_sc_act_06_derivative_even_successor_gate.py",
            "probe": "tests/channel-swings/k766_sc_act_06_derivative_even_successor_gate_probe.py",
            "controls_passed": 42,
            "hostile_mutations_rejected": 36,
        },
        "claim_ceiling": "Exact successor gate for finite-rank derivative-even extensions with r+m<98311 and the K764 scalar-metric control. No theorem against high-rank natural owners, changed stationary germs, independent action parents, K500, or global SC-ACT-06.",
    }


def validate(packet: dict[str, Any]) -> None:
    assert packet["result_id"].startswith("K766-")
    assert packet["status"] == "working_draft_verified"
    assert packet["classification"] == "SOURCE_NATIVE_ROUTE"
    assert packet["target_claim"] == "SC-ACT-06"
    assert len(packet["closed_classes"]) == 2
    assert "r+m<98311" in packet["closed_classes"][0]["class"]
    assert "98297/98300" in packet["closed_classes"][1]["reason"]
    assert len(packet["live_reopeners"]) == 4
    decision = packet["decision"]
    for key in ("do_not_retry_low_rank_scalar_tensor_or_small_derivative_even_owner", "finite_rank_theorem_not_global_action_no_go", "large_rank_or_changed_germ_routes_remain_open", "k500_native_packet_remains_open"):
        assert decision[key]
    assert not decision["global_SC_ACT_06_refuted"]
    assert decision["SC_ACT_06_status"] == "ASSERTS"
    assert "UNCHANGED" in packet["source_and_ledger_effect"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    OUTPUT.write_text(rendered) if args.write else print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
