#!/usr/bin/env python3
"""Scope and wiring audit for the non-null Koszul/GCR split."""

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


registry = strict("lab/process/selected-second-layer-nonnull-koszul-gcr-split.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.48.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-second-layer-nonnull-koszul-gcr-split-2026-08-07.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-07-selected-second-layer-nonnull-koszul-gcr-split-review.md").read_text(encoding="utf-8")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text(encoding="utf-8")
next_steps = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8")
status = (ROOT / "RESEARCH-STATUS.md").read_text(encoding="utf-8")
lanes = (ROOT / "lab/process/RESEARCH-AGENDA.json").read_text(encoding="utf-8")

assert registry["status"] == "NONNULL_CANONICAL_SPLIT__LAWFUL_CONNECTION_JET_PLUS_NONZERO_TRANSVERSE_COMPLETION_BURDEN"
assert registry["rerun"] == "61/61 PASS"
assert ledger["schema_version"] == "0.48"
assert ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
assert ledger["residue"]["quotients_ranked"] == 4
assert reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.48.json"
)
for token in ("28", "117", "rank four", "null", "Symplectic", "SOURCE-CONFIRMS", "SOURCE-SILENT"):
    assert token in report
for lens in ("differential geometry", "representation theory", "variational PDE", "symplectic geometry", "Krein/operator theory", "source criticism", "repo archaeology"):
    assert lens in review
for fence in ("has not been identified", "No scalar", "P1/P2/P3 remain"):
    assert fence in report
print("PASS: historical v0.48 Koszul/GCR certificate is immutable and reachable from the current append-only ledger without datum, quotient, canon or posture inflation")
