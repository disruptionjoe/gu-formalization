#!/usr/bin/env python3
"""Hostile mutations for K1622's conditional-capacity ceiling."""
import json
from copy import deepcopy
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]

def reject(d):
    q, z = d["conditional_capacity"], d["decision"]
    return ("Order-N^3 conditional capacity" in q["scope_guard"] and "H(p_N)+(1/2)sum_z" in q["information_bound"]
            and z["entropy_plus_conditional_capacity_bound"] and z["arbitrary_means_admitted"]
            and z["arbitrary_covariance_eigenvectors_admitted"] and not z["order_n3_capacity_closed"]
            and not z["unrestricted_leading_coefficient_identified"] and not z["protected_status_change"])

def main():
    d=json.loads((ROOT/"lab/process/k1622-entropy-conditional-capacity-rigidity.json").read_text()); checks=[("baseline",reject(d))]
    m=deepcopy(d); m["conditional_capacity"]["information_bound"]=m["conditional_capacity"]["information_bound"].replace("+(1/2)sum_z", "")
    checks.append(("drop covariance capacity",not reject(m)))
    for key in ("entropy_plus_conditional_capacity_bound","arbitrary_means_admitted","arbitrary_covariance_eigenvectors_admitted","order_n3_capacity_closed","unrestricted_leading_coefficient_identified","protected_status_change"):
        m=deepcopy(d);m["decision"][key]=not m["decision"][key];checks.append((f"flip {key}",not reject(m)))
    for i,(label,ok) in enumerate(checks,1): assert ok,label; print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
