#!/usr/bin/env python3
from pathlib import Path
import json
from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot
R=Path(__file__).resolve().parents[1]
load=lambda p: json.loads((R/p).read_text())
r=load("lab/process/selected-second-layer-residual-constituent-operator-correction.json")
l=load("lab/process/conditional-physics-ledger-v0.54.json")
c=load("lab/methods/research-evidence-contract-v1.0.json")
report=(R/"explorations/conditional-build/selected-second-layer-residual-constituent-operator-correction-2026-08-07.md").read_text()
review=(R/"lab/process/hostile-reviews/2026-08-07-selected-second-layer-residual-constituent-operator-correction-review.md").read_text()
assert "MOVING_OPERATOR_KILL_RETRACTED" in r["status"]
assert l["schema_version"]=="0.54" and l["residue"]["continuous_real"]==84
assert reaches_historical_snapshot(c, "lab/process/conditional-physics-ledger-v0.54.json")
assert "T*=-(kappa_1/312)Phi1" in report and "SOURCE-SILENT" in report
assert "Symplectic geometry" in review
assert r["rerun"]=="17/17 PASS" and r["third_lane_gate"]=="NOT_PROMOTED"
print("PASS: historical v0.54 residual-constituent correction is immutable and reachable from the current append-only ledger")
