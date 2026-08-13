#!/usr/bin/env python3
"""Static scope gate for the cross-theory donor Compose checkpoint."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def unique(pairs: list[tuple[str, object]]) -> dict:
    out: dict[str, object] = {}
    for key, value in pairs:
        assert key not in out, f"duplicate key: {key}"
        out[key] = value
    return out


data = json.loads(
    (ROOT / "lab/process/cross-theory-mechanism-donor-crosswalk.json").read_text(),
    object_pairs_hook=unique,
)
contract = json.loads(
    (ROOT / "lab/methods/research-evidence-contract-v1.0.json").read_text(),
    object_pairs_hook=unique,
)
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
next_steps = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")

assert data["functional_channel"] == "COMPOSE"
assert data["selected_port_ids"] == ["NCG-CONTROL", "STRING-LINF"]
assert len(data["selected_port_ids"]) <= data["selection_cap"] == 2
assert data["exact_port_count"] == 0
assert data["ledger"]["row_changes"] == "none"
assert data["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert data["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert data["third_lane"] == "NOT_PROMOTED"

donor = contract["cross_theory_mechanism_donor_policy"]
assert donor["standing_role"] == "BOUNDED_COMPOSE_CHECKPOINT__NOT_A_LANE"
assert donor["selection_cap"] == 2
assert donor["selected_ports"] == ["NCG-CONTROL", "STRING-LINF"]
assert donor["frg_admission"] == "STABLE_ACTION_NUMERATOR_FIELD_CONTENT_AND_COMMON_DOMAIN_REQUIRED"
assert donor["wrong_type_is_not_gap"] is True

for needle in (
    "Cross-theory donor checkpoint",
    "NCG-CONTROL",
    "STRING-LINF",
    "Do not run FRG",
):
    assert needle in context or needle in next_steps, needle

print("PASS: cross-theory donor scope, two-port cap, frozen ledger and front door")
