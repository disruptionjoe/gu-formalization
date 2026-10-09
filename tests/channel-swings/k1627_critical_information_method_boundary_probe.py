#!/usr/bin/env python3
"""Hostile mutations for K1627's variational guard."""
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def reject(d):
    q,z=d["method_boundary"],d["decision"]
    return (q["classification"]=="method-sharp but variationally undecided"
            and z["subcritical_information_hypothesis_scale_sharp"]
            and not z["critical_rigidity_from_information_alone"]
            and not z["actual_coefficient_change_proved"]
            and z["direct_all_term_analysis_still_required"]
            and not z["protected_status_change"])

def main():
    d=json.loads((ROOT/"lab/process/k1627-critical-information-method-boundary.json").read_text())
    checks=[("baseline",reject(d))]
    for label,key,val in [
        ("critical rigidity overclaim","critical_rigidity_from_information_alone",True),
        ("coefficient overclaim","actual_coefficient_change_proved",True),
        ("drop all-term need","direct_all_term_analysis_still_required",False),
        ("drop sharpness","subcritical_information_hypothesis_scale_sharp",False),
        ("protected mutation","protected_status_change",True),
    ]:
        m=deepcopy(d);m["decision"][key]=val;checks.append((label,not reject(m)))
    m=deepcopy(d);m["method_boundary"]["classification"]="coefficient changed";checks.append(("classification mutation",not reject(m)))
    for i,(label,ok) in enumerate(checks,1): assert ok,label;print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")

if __name__=="__main__":main()
