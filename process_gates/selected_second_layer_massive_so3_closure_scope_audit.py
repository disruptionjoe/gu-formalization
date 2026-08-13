#!/usr/bin/env python3
"""Scope and wiring audit for massive SO3 closure and identifiability."""

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


registry = strict("lab/process/selected-second-layer-massive-so3-closure-identifiability.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.41.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-second-layer-massive-so3-closure-identifiability-2026-08-07.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-07-selected-second-layer-massive-so3-closure-review.md").read_text(encoding="utf-8")
context = (ROOT / "lab/process/agent-context-pack.md").read_text(encoding="utf-8")
next_steps = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8")
status = (ROOT / "RESEARCH-STATUS.md").read_text(encoding="utf-8")
lanes = (ROOT / "LANES.yaml").read_text(encoding="utf-8")

assert registry["status"] == "MASSIVE_SPIN2_CLOSURE_EXACT__SPIN0_CHARACTERISTIC_POLYNOMIAL_OPEN"
assert registry["rerun"] == "31/31 PASS"
assert registry["independent_sage"] == "SO3_CLOSURE_DIM_5__TRACE_COMPLEMENT_DIM_6"
assert registry["frontier_delta"] == {
    "headline_delta": "NONE",
    "conditions_closed": 3,
    "conditions_opened": 0,
    "remaining_named_conditions": 3,
}
assert "SOURCE-CONFIRMS" in registry["source_return"]
assert "SOURCE-SILENT" in registry["source_return"]
assert ledger["schema_version"] == "0.41"
assert ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
assert ledger["residue"]["quotients_ranked"] == 4
assert "conditional-physics-ledger-v0.41.json" in lanes
assert contract["standing_ledger"]["ref"].endswith("conditional-physics-ledger-v0.41.json")

directive = contract["active_scientific_directives"][0]
assert "MASSIVE_SO3_SPIN2_DIM5_EXACT" in directive["status"]
assert "SPIN0_POLYNOMIAL" in directive["status"]
assert directive["next_run_method"]["target"] == "ACTUAL_BACKGROUND_SUBTRACTED_OFF_TT_SECTION_SECOND_VARIATION_AND_SPIN0_POLYNOMIAL"
assert "DERIVE_SPIN0_POLYNOMIAL" in directive["next_gate"]
assert "SYMPLECTIC_GEOMETRY" in directive["next_run_method"]["mandatory_reviews"]

for token in (
    "dimension five",
    "Casimir `-6`",
    "spin-zero",
    "commutant",
    "background-subtracted",
    "massless constraint",
    "Symplectic geometry",
):
    assert token in report

for lens in (
    "Representation theory",
    "Differential geometry",
    "Variational PDE",
    "Symplectic geometry",
    "Krein/operator theory",
    "Source criticism",
):
    assert lens in review

for fence in (
    "five positive physical states on a selected global domain",
    "cannot be read from TT data",
    "No coefficient, external datum or fifth quotient is added",
    "P1/P2/P3 remain",
):
    assert fence in report

assert "CURRENT MASSIVE SO(3) CLOSURE FENCE" in context
assert "NEXT RUN: OFF-TT SPIN-ZERO ACTION BLOCK" in next_steps
assert "ledger v0.41; five distance/priority" in status

print("PASS: massive SO3 spin-two closure and the independent spin-zero identifiability boundary are wired without physical-state, scalar-coefficient, massless-constraint, domain, datum or public-posture inflation")
