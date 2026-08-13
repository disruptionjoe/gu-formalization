#!/usr/bin/env python3
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
load=lambda p: json.loads((R/p).read_text())
r=load("lab/process/selected-invariant-constituent-operator-naturality.json")
l=load("lab/process/conditional-physics-ledger-v0.54.json")
c=load("lab/process/functional-channel-operating-contract-v1.0.json")
report=(R/"explorations/conditional-build/selected-invariant-constituent-operator-naturality-2026-08-07.md").read_text()
review=(R/"lab/process/hostile-reviews/2026-08-07-selected-invariant-constituent-operator-naturality-review.md").read_text()
assert "BRANCH_TANGENT_OPERATOR_PACKET_ZERO" in r["status"]
assert r["exact_result"]["T_support"]==14 and r["exact_result"]["F_A_support"]==91
assert r["exact_result"]["operator_transverse_intersection"]==0
assert l["schema_version"]=="0.54" and l["residue"]["continuous_real"]==84
assert c["standing_ledger"]["ref"]=="lab/process/conditional-physics-ledger-v0.55.json"
assert "independent ambient" in report and "Symplectic geometry" in review
assert r["rerun"]=="35/35 PASS" and r["third_lane_gate"]=="NOT_PROMOTED"
assert r["claim_status_change"]==r["canon_verdict_change"]==r["public_posture_change"]=="none"
print("PASS: selected constituent branch-tangent naturality is scoped away from independent field jets, quotient, datum and posture")
