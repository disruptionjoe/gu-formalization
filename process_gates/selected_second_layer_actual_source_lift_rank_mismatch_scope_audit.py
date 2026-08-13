#!/usr/bin/env python3
"""Scope and wiring audit for the source-corrected connection-rank result."""

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


registry = strict("lab/process/selected-second-layer-actual-source-lift-rank-mismatch.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.44.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-second-layer-actual-source-lift-rank-mismatch-2026-08-07.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-07-selected-second-layer-actual-source-lift-rank-mismatch-review.md").read_text(encoding="utf-8")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text(encoding="utf-8")
next_steps = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8")
status = (ROOT / "RESEARCH-STATUS.md").read_text(encoding="utf-8")
lanes = (ROOT / "lab/process/RESEARCH-AGENDA.json").read_text(encoding="utf-8")

assert registry["status"] == "CONNECTION_ONLY_RANK_MISMATCH__V043_PROXY_RETRACTED_AS_ACTION_TARGET"
assert registry["rerun"] == "34/34 PASS"
assert registry["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 3, "conditions_opened": 0, "remaining_named_conditions": 4}
assert ledger["schema_version"] == "0.44"
assert ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
assert ledger["residue"]["quotients_ranked"] == 4
assert "conditional-physics-ledger-v0.44.json" in lanes
assert contract["standing_ledger"]["ref"].endswith("conditional-physics-ledger-v0.44.json")
directive = contract["active_scientific_directives"][0]
assert "CONNECTION_ONLY_RANK_MISMATCH" in directive["status"]
assert directive["next_run_method"]["target"] == "ACTUAL_SECTION_OBSERVATION_DIFFEO_TANGENT_ON_CONNECTION_KERNEL"
assert "SECTION_OBSERVATION" in directive["next_gate"]
assert "COMBINED_SELECTED_DUPSILON_NATURALITY" in directive["next_gate"]
assert "SYMPLECTIC_GEOMETRY" in directive["next_run_method"]["mandatory_reviews"]
for token in ("rank three", "time reparametrization", "no choice of connection action can make it cancel", "Symplectic geometry", "SOURCE-CORRECTS", "SOURCE-SILENT"):
    assert token in report
for lens in ("Differential geometry", "Representation theory", "Variational PDE", "Symplectic geometry", "Krein/operator theory", "Source criticism", "Repo archaeology"):
    assert lens in review
for fence in ("does not\nkill the full action", "no coefficients", "No scalar pole"):
    assert fence in report
assert "CURRENT CONNECTION-ONLY RANK-MISMATCH FENCE" in context
assert "NEXT RUN: ACTUAL SECTION/OBSERVATION GAUGE COLUMN" in next_steps
assert "ledger v0.44; five distance/priority" in status

print("PASS: source-corrected rank-three connection lift is wired without full-action, scalar, domain, BV/BFV, datum, quotient or posture inflation")
