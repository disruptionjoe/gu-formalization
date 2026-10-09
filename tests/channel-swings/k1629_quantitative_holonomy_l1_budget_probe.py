#!/usr/bin/env python3
"""Hostile mutations for K1629's nonlinear and source guards."""
import json
from copy import deepcopy
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]

def reject(d):
    q,z=d["quantitative_budget"],d["decision"]
    return ("electric-field L1" in q["scope_guard"]
            and "source-owned" in q["scope_guard"]
            and z["explicit_budget_proved"] and z["optimized_scale_proved"]
            and z["finite_vector_extension_proved"]
            and not z["nonlinear_remainders_controlled"]
            and not z["protected_status_change"])

def main():
    d=json.loads((ROOT/"lab/process/k1629-quantitative-holonomy-l1-budget.json").read_text())
    checks=[("baseline",reject(d))]
    for label,key,val in [
        ("drop budget","explicit_budget_proved",False),
        ("drop optimizer","optimized_scale_proved",False),
        ("drop vector","finite_vector_extension_proved",False),
        ("nonlinear overclaim","nonlinear_remainders_controlled",True),
        ("protected mutation","protected_status_change",True),
    ]:
        m=deepcopy(d);m["decision"][key]=val;checks.append((label,not reject(m)))
    m=deepcopy(d);m["quantitative_budget"]["scope_guard"]="global flow";checks.append(("scope deletion",not reject(m)))
    for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")

if __name__=="__main__":main()
