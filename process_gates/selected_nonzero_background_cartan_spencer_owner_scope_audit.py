#!/usr/bin/env python3
from pathlib import Path
import json

from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot

R = Path(__file__).resolve().parents[1]
load = lambda p: json.loads((R / p).read_text())
r = load("lab/process/selected-nonzero-background-cartan-spencer-owner.json")
l = load("lab/process/conditional-physics-ledger-v0.55.json")
c = load("lab/methods/research-evidence-contract-v1.0.json")
report = (R / "explorations/conditional-build/selected-nonzero-background-cartan-spencer-owner-2026-08-07.md").read_text()
review = (R / "lab/process/hostile-reviews/2026-08-07-selected-nonzero-background-cartan-spencer-owner-review.md").read_text()

assert "FULL_UNRESTRICTED_CARTAN_SPENCER" in r["status"]
assert r["exact_result"]["cartan_spencer_rank"] == 1274
assert r["exact_result"]["transverse_preimage_supports"] == [57, 34, 34, 34]
assert r["exact_result"]["levi_civita_transverse_intersection"] == 0
assert l["schema_version"] == "0.55" and l["residue"]["continuous_real"] == 84
assert reaches_historical_snapshot(c, "lab/process/conditional-physics-ledger-v0.56.json")
assert "Levi-Civita subclass" in report and "Symplectic geometry" in review
assert r["rerun"] == "48/48 PASS" and r["third_lane_gate"] == "NOT_PROMOTED"
assert r["claim_status_change"] == r["canon_verdict_change"] == r["public_posture_change"] == "none"
print("PASS: historical v0.56 Cartan/Spencer certificate is immutable and reachable from the current append-only ledger, fenced from Levi-Civita, actual graph jets, Euler, quotient, datum and posture")
