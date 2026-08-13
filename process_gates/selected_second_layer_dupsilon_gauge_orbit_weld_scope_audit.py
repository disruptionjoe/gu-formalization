#!/usr/bin/env python3
"""Scope and wiring audit for the selected D Upsilon gauge-orbit weld."""

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


registry = strict("lab/process/selected-second-layer-dupsilon-gauge-orbit-weld.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.43.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-second-layer-dupsilon-gauge-orbit-weld-2026-08-07.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-07-selected-second-layer-dupsilon-gauge-orbit-weld-review.md").read_text(encoding="utf-8")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text(encoding="utf-8")
next_steps = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8")
status = (ROOT / "RESEARCH-STATUS.md").read_text(encoding="utf-8")
lanes = (ROOT / "lab/process/RESEARCH-AGENDA.json").read_text(encoding="utf-8")

assert registry["status"] == "RANK4_CONNECTION_ORBIT_WELD_FORCED__TRANSVERSE_OWNER_OPEN"
assert registry["rerun"] == "37/37 PASS"
assert registry["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 3, "conditions_opened": 0, "remaining_named_conditions": 4}
assert ledger["schema_version"] == "0.43"
assert ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
assert ledger["residue"]["quotients_ranked"] == 4
assert "conditional-physics-ledger-v0.43.json" in lanes
assert contract["standing_ledger"]["ref"].endswith("conditional-physics-ledger-v0.43.json")
directive = contract["active_scientific_directives"][0]
assert "RANK4_CONNECTION_ORBIT_WELD_FORCED" in directive["status"]
assert directive["next_run_method"]["target"] == "ACTUAL_SELECTED_DUPSILON_FOUR_CONNECTION_DIFFEO_COLUMNS"
assert "FOUR_CONNECTION_DIFFEO_COLUMNS" in directive["next_gate"]
assert "SYMPLECTIC_GEOMETRY" in directive["next_run_method"]["mandatory_reviews"]
for token in ("exactly rank four", "twelve connection directions", "Xi=D Upsilon", "Symplectic geometry", "SOURCE-SILENT"):
    assert token in report
for lens in ("Differential geometry", "Representation theory", "Variational PDE", "Symplectic geometry", "Krein/operator theory", "Source criticism", "Repo archaeology"):
    assert lens in review
for fence in ("not the diffeomorphism Ward identity", "not\nunique on the other twelve", "No scalar pole, coefficient, external datum or fifth quotient"):
    assert fence in report
assert "CURRENT D UPSILON GAUGE-ORBIT WELD FENCE" in context
assert "NEXT RUN: FOUR ACTUAL D UPSILON COLUMNS" in next_steps
assert "ledger v0.43; five distance/priority" in status

print("PASS: rank-four residual/connection orbit matching is wired without action-derivative, scalar, BV/BFV, domain, datum, quotient or posture inflation")
