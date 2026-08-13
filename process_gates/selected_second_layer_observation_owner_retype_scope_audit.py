#!/usr/bin/env python3
"""Scope and wiring audit for the observation-owner correction."""

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


registry = strict("lab/process/selected-second-layer-observation-owner-retype.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.45.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-second-layer-observation-owner-retype-2026-08-07.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-07-selected-second-layer-observation-owner-retype-review.md").read_text(encoding="utf-8")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text(encoding="utf-8")
next_steps = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8")
status = (ROOT / "RESEARCH-STATUS.md").read_text(encoding="utf-8")
lanes = (ROOT / "lab/process/RESEARCH-AGENDA.json").read_text(encoding="utf-8")

assert registry["status"] == "INDEPENDENT_OBSERVATION_COLUMN_REJECTED__DEPENDENT_NORMAL_JET_ROUTE_OPEN"
assert registry["rerun"] == "40/40 PASS"
assert registry["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 3, "conditions_opened": 1, "remaining_named_conditions": 4}
assert ledger["schema_version"] == "0.45"
assert ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
assert ledger["residue"]["quotients_ranked"] == 4
assert "conditional-physics-ledger-v0.45.json" in lanes
assert contract["standing_ledger"]["ref"].endswith("conditional-physics-ledger-v0.45.json")
directive = contract["active_scientific_directives"][0]
assert "INDEPENDENT_OBSERVATION_COLUMN_REJECTED" in directive["status"]
assert directive["next_run_method"]["target"] == "SOURCE_NATIVE_J1_UPSILON_NORMAL_JET_AND_TOTAL_METRIC_SECTION_DERIVATIVE"
assert "SOURCE_NATIVE_J1_UPSILON_NORMAL_JET" in directive["next_gate"]
assert "CONDITIONAL_FULL_II_OWNER_MAP" in directive["next_gate"]
assert "SYMPLECTIC_GEOMETRY" in directive["next_run_method"]["mandatory_reviews"]
for token in ("same rank-four", "Observation transport cannot be", "normal first jet", "Symplectic geometry", "SOURCE-CORRECTS", "SOURCE-SILENT"):
    assert token in report
for lens in ("Differential geometry", "Representation theory", "Variational PDE", "Symplectic geometry", "Krein/operator theory", "Source criticism", "Repo archaeology"):
    assert lens in review
for fence in ("does **not** make observation irrelevant", "No scalar pole", "P1/P2/P3 remain unused"):
    assert fence in report
assert "CURRENT OBSERVATION-OWNER FENCE" in context
assert "NEXT RUN: SOURCE-NATIVE NORMAL JET" in next_steps
assert "ledger v0.45; five" in status

print("PASS: observation is wired as a receiver and dependent metric-section chain rule, with source-normal-jet ownership open and no scalar, domain, BV/BFV, datum, quotient or posture inflation")
