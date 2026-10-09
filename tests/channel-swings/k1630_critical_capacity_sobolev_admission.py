#!/usr/bin/env python3
"""Certificate for K1630 protected integration."""
import hashlib,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
 d=json.loads((ROOT/"lab/process/k1630-critical-capacity-sobolev-admission.json").read_text());c=d["census"];p=d["protected_boundaries"]
 checks=[("claim",d["claim_id"]=="K1630"),("rows",c["rows"]==345),("partition",c["satisfied"]+c["conditional"]+c["excluded"]+c["missing"]==c["rows"]),("satisfied",c["satisfied"]==266),("conditional",c["conditional"]==10),("excluded",c["excluded"]==65),("missing",c["missing"]==4)]
 for key,pin in d["pinned_inputs"].items(): checks.append((f"pin {key}",sha(ROOT/pin["path"])==pin["sha256"]))
 checks += [("asserts",c["source_asserts"]==["SC-ACT-01","SC-ACT-02","SC-ACT-06"]),("uncertain",c["source_uncertain"]==["SC-META-53"]),("ledger",c["physics_ledger"]=={"SAME":33,"DIFFERS":22,"NEEDS":31,"OVER_DETERMINED":2}),("scorable",c["k1145_k1150_scorable_rows"]=="0/7")]
 checks += [(key,not value) for key,value in p.items()]
 checks += [("three wakes",len(d["next_wakes"])==3),("all-term wake","all-term" in d["next_wakes"][0]),("L2 source wake","L2" in d["next_wakes"][1]),("tuple wake","tuple" in d["next_wakes"][2])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
