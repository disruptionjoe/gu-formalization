#!/usr/bin/env python3
"""Scope and wiring audit for the normal-jet owner correction."""

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


registry = strict("lab/process/selected-second-layer-normal-jet-carrier-compatibility.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.46.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-second-layer-normal-jet-carrier-compatibility-2026-08-07.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-07-selected-second-layer-normal-jet-carrier-compatibility-review.md").read_text(encoding="utf-8")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text(encoding="utf-8")
next_steps = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8")
status = (ROOT / "RESEARCH-STATUS.md").read_text(encoding="utf-8")
lanes = (ROOT / "lab/process/RESEARCH-AGENDA.json").read_text(encoding="utf-8")

assert registry["status"] == "OWNER_MAP_RETYPED__RAW_CARRIER_COMPATIBLE__ACTUAL_PROLONGATION_OPEN"
assert registry["rerun"] == "42/42 PASS"
assert ledger["schema_version"] == "0.46"
assert ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
assert ledger["residue"]["quotients_ranked"] == 4
assert "conditional-physics-ledger-v0.46.json" in lanes
assert contract["standing_ledger"]["ref"].endswith("conditional-physics-ledger-v0.46.json")
directive = contract["active_scientific_directives"][0]
assert "OWNER_MAP_RETYPED" in directive["status"]
assert directive["next_run_method"]["target"] == "ACTUAL_SOURCE_OWNED_FIRST_PROLONGATION_AND_TOTAL_RAW_DUPSILON"
assert "CONSTRUCT_J1_LIE_XI_A" in directive["next_gate"]
assert "NO_BACKGROUND_SUBTRACTION_WITHOUT_OWNER" in directive["next_gate"]
assert "SYMPLECTIC_GEOMETRY" in directive["next_run_method"]["mandatory_reviews"]
for token in ("difference of two Gram", "rank-`1,190`", "all four", "Symplectic", "SOURCE-CORRECTS", "SOURCE-SILENT"):
    assert token in report
for lens in ("differential geometry", "representation theory", "variational PDE", "symplectic geometry", "Krein/operator theory", "source criticism", "repo archaeology"):
    assert lens in review
for fence in ("does not solve for or", "No scalar", "P1/P2/P3 remain unused"):
    assert fence in report
assert "CURRENT NORMAL-JET OWNER FENCE" in context
assert "NEXT RUN: ACTUAL RAW PROLONGED ORBIT" in next_steps
assert "ledger v0.46; five" in status

print("PASS: the background-subtracted Hessian is no longer typed as a residual Gram, raw source-carrier compatibility is retained, and actual prolongation remains open without datum, quotient, canon or posture inflation")
