#!/usr/bin/env python3
"""Scope and wiring audit for the residual-zero transverse-117 owner retype."""

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


r = strict("lab/process/selected-second-layer-transverse117-residual-zero-owner-class.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.55.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-second-layer-transverse117-residual-zero-owner-class-2026-08-07.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-07-selected-second-layer-transverse117-residual-zero-owner-class-review.md").read_text()
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
next_steps = (ROOT / "NEXT-STEPS.md").read_text()
status = (ROOT / "RESEARCH-STATUS.md").read_text()
lanes = (ROOT / "lab/process/RESEARCH-AGENDA.json").read_text()

assert "CONNECTION_CLASS_KILLED_AT_RESIDUAL_ZERO" in r["status"]
assert r["rerun"] == "30/30 PASS"
assert r["exact_result"]["connection_q_exact_support"] == 28
assert r["exact_result"]["transverse_support"] == 117
assert r["exact_result"]["support_intersection"] == 0
assert r["exact_result"]["moving_operator_at_zero_background"] == "ZERO"
assert r["exact_result"]["nonzero_background_control"] == "LIVE"

assert ledger["schema_version"] == "0.55"
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["function_valued_at_least"] == 19
assert ledger["residue"]["open_discrete_forks"] == 9
assert ledger["residue"]["quotients_ranked"] == 4
assert "independent-varpi" in ledger["next_work_queue"][0]["why"]

assert reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.55.json"
)

for token in ("117 transverse", "q wedge delta A", "F_0=Upsilon_0=0", "nonzero-background control", "SOURCE-CORRECTS", "P1/P2/P3 remain"):
    assert token in report
for lens in ("Source geometry", "Differential geometry", "Representation theory", "Variational PDE", "Symplectic geometry", "Krein/operator theory", "Source criticism", "Repo archaeology"):
    assert lens in review
assert r["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert r["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert r["third_lane_gate"] == "NOT_PROMOTED"
assert r["claim_status_change"] == r["canon_verdict_change"] == r["public_posture_change"] == "none"

print("PASS: historical v0.55 transverse-owner certificate is immutable and reachable from the current append-only ledger without quotient, datum, canon or posture inflation")
