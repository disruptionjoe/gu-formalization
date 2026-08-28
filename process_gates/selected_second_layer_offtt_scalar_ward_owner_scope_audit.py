#!/usr/bin/env python3
"""Scope and wiring audit for the off-TT scalar/Ward owner correction."""

from pathlib import Path
import json

from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot

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
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-second-layer-offtt-scalar-ward-owner-2026-08-07.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-07-selected-second-layer-offtt-scalar-ward-owner-review.md").read_text(encoding="utf-8")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text(encoding="utf-8")
next_steps = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8")
status = (ROOT / "RESEARCH-STATUS.md").read_text(encoding="utf-8")
lanes = (ROOT / "lab/process/RESEARCH-AGENDA.json").read_text(encoding="utf-8")

assert registry["status"] == "METRIC_BLOCK_NOT_BASIC__COUPLED_OWNER_REQUIRED"
assert registry["rerun"] == "30/30 PASS"
assert registry["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 3, "conditions_opened": 1, "remaining_named_conditions": 4}
assert ledger["schema_version"] == "0.42"
assert ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
assert ledger["residue"]["quotients_ranked"] == 4
assert reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.42.json"
)
for token in ("1157/3589", "rank four", "rank K_metric", "full co-moving", "Symplectic geometry", "SOURCE-SILENT"):
    assert token in report
for lens in ("Differential geometry", "Representation theory", "Variational PDE", "Symplectic geometry", "Krein/operator theory", "Source criticism"):
    assert lens in review
for fence in ("not** yet a scalar particle pole", "No scalar pole, coefficient, external datum or fifth quotient", "P1/P2/P3 remain unused"):
    assert fence in report
print("PASS: historical v0.42 off-TT Ward/owner certificate is immutable and reachable from the current append-only ledger without scalar-pole, full-action, domain, datum, quotient or posture inflation")
