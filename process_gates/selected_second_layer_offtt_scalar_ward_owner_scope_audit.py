#!/usr/bin/env python3
"""Scope and wiring audit for the off-TT scalar/Ward owner correction."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def strict(relative):
    path = ROOT / relative
    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


registry = strict("lab/process/selected-second-layer-offtt-scalar-ward-owner.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.42.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-second-layer-offtt-scalar-ward-owner-2026-08-07.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-07-selected-second-layer-offtt-scalar-ward-owner-review.md").read_text(encoding="utf-8")
context = (ROOT / "lab/process/agent-context-pack.md").read_text(encoding="utf-8")
next_steps = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8")
status = (ROOT / "RESEARCH-STATUS.md").read_text(encoding="utf-8")
lanes = (ROOT / "LANES.yaml").read_text(encoding="utf-8")

assert registry["status"] == "METRIC_BLOCK_NOT_BASIC__COUPLED_OWNER_REQUIRED"
assert registry["rerun"] == "30/30 PASS"
assert registry["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 3, "conditions_opened": 1, "remaining_named_conditions": 4}
assert ledger["schema_version"] == "0.42"
assert ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
assert ledger["residue"]["quotients_ranked"] == 4
assert "conditional-physics-ledger-v0.42.json" in lanes
assert contract["standing_ledger"]["ref"].endswith("conditional-physics-ledger-v0.42.json")
directive = contract["active_scientific_directives"][0]
assert "METRIC_ONLY_OFFTT_WARD_DEFECT_RANK4" in directive["status"]
assert directive["next_run_method"]["target"] == "FULL_COMOVING_DUPSILON_AND_COUPLED_WARD_DESCENT"
assert "FULL_COMOVING_DUPSILON" in directive["next_gate"]
assert "SYMPLECTIC_GEOMETRY" in directive["next_run_method"]["mandatory_reviews"]
for token in ("1157/3589", "rank four", "rank K_metric", "full co-moving", "Symplectic geometry", "SOURCE-SILENT"):
    assert token in report
for lens in ("Differential geometry", "Representation theory", "Variational PDE", "Symplectic geometry", "Krein/operator theory", "Source criticism"):
    assert lens in review
for fence in ("not** yet a scalar particle pole", "No scalar pole, coefficient, external datum or fifth quotient", "P1/P2/P3 remain unused"):
    assert fence in report
assert "CURRENT OFF-TT WARD/OWNER FENCE" in context
assert "NEXT RUN: FULL CO-MOVING D UPSILON" in next_steps
assert "ledger v0.42; five distance/priority" in status

print("PASS: off-TT metric recovery, Ward failure and action-owner correction are wired without scalar-pole, full-action, domain, datum, quotient or posture inflation")
