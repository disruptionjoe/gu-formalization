#!/usr/bin/env python3
"""Hostile mutations for K1628's sufficient-class scope."""
import json
from copy import deepcopy
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]

def reject(d):
    q,z=d["sobolev_sufficiency"],d["decision"]
    return ("arbitrary atom-free singular-continuous" in q["scope_guard"]
            and z["l2_density_sufficient_for_holonomy_L1"]
            and not z["atom_free_alone_sufficient"]
            and not z["singular_continuous_class_closed"]
            and not z["electric_field_L1_proved"]
            and not z["source_owned_flow"]
            and not z["protected_status_change"])

def main():
    d=json.loads((ROOT/"lab/process/k1628-l2-derivative-holonomy-sufficiency.json").read_text())
    checks=[("baseline",reject(d))]
    for label,key,val in [
        ("atom-free overclaim","atom_free_alone_sufficient",True),
        ("singular overclaim","singular_continuous_class_closed",True),
        ("electric overclaim","electric_field_L1_proved",True),
        ("source overclaim","source_owned_flow",True),
        ("drop theorem","l2_density_sufficient_for_holonomy_L1",False),
        ("protected mutation","protected_status_change",True),
    ]:
        m=deepcopy(d);m["decision"][key]=val;checks.append((label,not reject(m)))
    m=deepcopy(d);m["sobolev_sufficiency"]["scope_guard"]="all atom-free measures";checks.append(("scope deletion",not reject(m)))
    for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")

if __name__=="__main__":main()
