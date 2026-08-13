#!/usr/bin/env python3
"""Scope and wiring audit for the selected second-layer TT result."""

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


registry = strict("lab/process/selected-second-layer-tt-euler-preboundary-helicity.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.40.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-second-layer-tt-euler-preboundary-helicity-2026-08-07.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-07-selected-second-layer-tt-euler-preboundary-helicity-review.md").read_text(encoding="utf-8")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text(encoding="utf-8")
next_steps = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8")
status = (ROOT / "RESEARCH-STATUS.md").read_text(encoding="utf-8")
lanes = (ROOT / "lab/process/RESEARCH-AGENDA.json").read_text(encoding="utf-8")

assert registry["status"].startswith("TT_MASSLESS_HELICITY2_AND_MASSIVE_AXIAL_WEIGHT2_WITH_EXTRA_OPEN")
assert registry["rerun"] == "44/44 PASS"
assert "MASS2_1922_OVER3589" in registry["independent_sage"]
assert registry["frontier_delta"] == {
    "headline_delta": "NONE",
    "conditions_closed": 4,
    "conditions_opened": 1,
    "remaining_named_conditions": 3,
}
assert "SOURCE-CONFIRMS" in registry["source_return"]
assert "SOURCE-SILENT" in registry["source_return"]
assert ledger["schema_version"] == "0.40"
assert ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
assert ledger["residue"]["quotients_ranked"] == 4
assert "conditional-physics-ledger-v0.40.json" in lanes
assert contract["standing_ledger"]["ref"].endswith("conditional-physics-ledger-v0.40.json")

directive = contract["active_scientific_directives"][0]
assert "MASSLESS_HELICITY2_AND_MASSIVE_AXIAL_WEIGHT2" in directive["status"]
assert "MASSIVE_SO3_TYPE_OPEN" in directive["status"]
assert directive["next_run_method"]["target"] == "COMPLETE_ZERO_FERMION_SCALAR_VECTOR_CONSTRAINT_CHARACTERISTIC_QUOTIENT"
assert "ONLY_AFTER_COMPLETE_QUOTIENT" in directive["next_gate"]
assert "SYMPLECTIC_GEOMETRY" in directive["next_run_method"]["mandatory_reviews"]

for token in (
    "14356/13689",
    "1922/3589",
    "x^2+4",
    "massless helicity-`+/-2`",
    "axial `SO(2)` spin weight `+/-2`",
    "full massive `SO(3)`",
    "preboundary",
    "scalar/vector/constraint",
    "coupled nonzero-fermion",
):
    assert token in report

for lens in (
    "differential geometry",
    "representation theory",
    "variational PDE",
    "symplectic geometry",
    "Krein/operator theory",
    "source criticism",
):
    assert lens in review

for fence in (
    "not the complete physical spectrum",
    "not a global domain theorem",
    "no fifth quotient is booked",
    "P1/P2/P3 remain unused",
):
    assert fence in report

assert "CURRENT SECOND-LAYER TT FENCE" in context
assert "NEXT RUN: COMPLETE SECOND-LAYER CONSTRAINT QUOTIENT" in next_steps
assert "ledger v0.40; four distance-only" in status

print("PASS: exact selected second-layer TT Euler, preboundary, massless helicity-two and massive axial-weight-two subquotient is wired without massive-SO3, complete-spectrum, positivity, quotient, datum or public-posture inflation")
