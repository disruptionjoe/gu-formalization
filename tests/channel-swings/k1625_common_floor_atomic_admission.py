#!/usr/bin/env python3
"""Certificate for K1625's protected integration."""
import hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def sha(path): return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()

def main():
 d=json.loads((ROOT/"lab/process/k1625-common-floor-atomic-admission.json").read_text());c=d["census"];p=d["protected_boundaries"]
 checks=[("claim",d["claim_id"]=="K1625"),("rows",c["rows"]==340),("partition",c["satisfied"]+c["conditional"]+c["excluded"]+c["missing"]==c["rows"]),
         ("satisfied",c["satisfied"]==261),("conditional",c["conditional"]==10),("excluded",c["excluded"]==65),("missing",c["missing"]==4),
         ("ledger total",sum(c["physics_ledger"].values())==88),("ledger SAME",c["physics_ledger"]["SAME"]==33),("scorable",c["k1145_k1150_scorable_rows"]=="0/7")]
 for key,rec in d["pinned_inputs"].items(): checks.append((f"pin {key}",rec["sha256"]==sha(rec["path"])))
 for key,val in p.items(): checks.append((f"protected {key}",val is False))
 checks += [("three wakes",len(d["next_wakes"])==3),("capacity wake","order-N^3 conditional capacity" in d["next_wakes"][0]),
            ("atom-free wake","atom-free primitive measure" in d["next_wakes"][1]),("source tuple wake","source-owned action/measure/Hamiltonian tuple" in d["next_wakes"][2])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
