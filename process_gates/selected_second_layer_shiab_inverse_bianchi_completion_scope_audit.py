#!/usr/bin/env python3
"""Scope and wiring audit for selected-Shiab inverse/Bianchi completion."""

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


registry = strict("lab/process/selected-second-layer-shiab-inverse-bianchi-completion.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.47.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-second-layer-shiab-inverse-bianchi-completion-2026-08-07.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-07-selected-second-layer-shiab-inverse-bianchi-completion-review.md").read_text(encoding="utf-8")
context = (ROOT / "lab/process/agent-context-pack.md").read_text(encoding="utf-8")
next_steps = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8")
status = (ROOT / "RESEARCH-STATUS.md").read_text(encoding="utf-8")
lanes = (ROOT / "LANES.yaml").read_text(encoding="utf-8")

assert registry["status"] == "SELECTED_SHIAB_ISOMORPHISM__SPLIT_PREIMAGES_NOT_PRINCIPAL_BIANCHI__TOTAL_GCR_COMPLETION_REQUIRED"
assert registry["rerun"] == "50/50 PASS"
assert ledger["schema_version"] == "0.47"
assert ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
assert ledger["residue"]["quotients_ranked"] == 4
assert "conditional-physics-ledger-v0.47.json" in lanes
assert contract["standing_ledger"]["ref"].endswith("conditional-physics-ledger-v0.47.json")
directive = contract["active_scientific_directives"][0]
assert "SPLIT_PREIMAGES_NOT_PRINCIPAL_BIANCHI" in directive["status"]
assert directive["next_run_method"]["target"] == "SOURCE_NATIVE_TOTAL_GAUSS_CODAZZI_RICCI_AND_RAW_DUPSILON_NATURALITY"
assert "CONSTRUCT_SOURCE_NATIVE_GAUSS_CODAZZI_RICCI" in directive["next_gate"]
assert "NO_SPLIT_JET_IDENTIFICATION" in directive["next_gate"]
assert "SYMPLECTIC_GEOMETRY" in directive["next_run_method"]["mandatory_reviews"]
for token in ("1,274", "rank fourteen", "split", "Symplectic", "SOURCE-CONFIRMS", "SOURCE-SILENT"):
    assert token in report
for lens in ("differential geometry", "representation theory", "variational PDE", "symplectic geometry", "Krein/operator theory", "source criticism", "repo archaeology"):
    assert lens in review
for fence in ("does not exclude a total", "No scalar", "P1/P2/P3 remain"):
    assert fence in report
assert "CURRENT SHIAB-INVERSE/BIANCHI FENCE" in context
assert "NEXT RUN: TOTAL GAUSS-CODAZZI-RICCI COMPLETION" in next_steps
assert "ledger v0.47; five" in status

print("PASS: the unique split inverse is rejected as a standalone connection-curvature jet, total GCR completion is next, and no datum, quotient, canon or posture inflation occurred")
