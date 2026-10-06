#!/usr/bin/env python3
"""K1184: audit native J against K1150 admission obligations."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k1184-native-upsilon-admission-audit.json"
PATHS={"k1150":ROOT/"lab/process/k1150-i1b-functional-admission-compiler.json","k1182":ROOT/"lab/process/k1182-native-upsilon-k132-complement-ranks.json","k1183":ROOT/"lab/process/k1183-rank98-overlap-envelope.json","k745":ROOT/"lab/process/k745-sc-act-06-gauge-redundancy-obstruction.json"}
def digest(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def build()->dict[str,Any]:
 rows=[
  {"gate":"source-owned map on frozen carrier","status":"PASS","evidence":"K740/K1182"},
  {"gate":"measured causal complement ranks","status":"PASS","evidence":"K1182: 162/162/8323"},
  {"gate":"annihilates owned gauge image","status":"PASS","evidence":"K745 principal complex"},
  {"gate":"captures Hessian radical modulo gauge","status":"FAIL","evidence":"residual dimensions 98308/98308/98311"},
  {"gate":"survives favorable rank-98 predecessor","status":"FAIL","evidence":"best residual dimensions 98210/98210/98213"},
  {"gate":"common complete graph domain","status":"OPEN","evidence":"not supplied"},
  {"gate":"closed range and Hausdorff quotient","status":"OPEN","evidence":"not supplied"},
  {"gate":"uniform positive quotient gap","status":"OPEN","evidence":"radical capture already fails"},
  {"gate":"maximal skew-adjoint generator","status":"OPEN","evidence":"not supplied"},
  {"gate":"boundary trace preservation","status":"OPEN","evidence":"not supplied"},
 ]
 return {"schema_version":"1.0","result_id":"K1184-NATIVE-UPSILON-ADMISSION-AUDIT","created":"2026-10-05","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","target_claim":"SC-ACT-06","pinned_inputs":{k:{"path":str(v.relative_to(ROOT)),"sha256":digest(v)} for k,v in PATHS.items()},"gate_rows":rows,"summary":{"pass":3,"fail":2,"open":5,"candidate_sufficient":False,"failure_precedes_functional_promotion":True},"protected_disposition":"SC-ACT-01/02/06 ASSERTS; SC-META-53 UNCERTAIN; LT-SM8/LT-GR6b/RA-F1/AC-F1 NEEDS","claim_ceiling":"candidate admission audit only; no global complex, positivity, prediction, confirmation or claim-status change"}
def validate(p:dict[str,Any])->None:
 assert p["result_id"]=="K1184-NATIVE-UPSILON-ADMISSION-AUDIT" and p["classification"]=="SOURCE_NATIVE_ROUTE" and p["target_claim"]=="SC-ACT-06"
 counts={s:sum(x["status"]==s for x in p["gate_rows"]) for s in ("PASS","FAIL","OPEN")};assert counts=={"PASS":3,"FAIL":2,"OPEN":5}
 assert p["summary"]["pass"]==3 and p["summary"]["fail"]==2 and p["summary"]["open"]==5
 assert not p["summary"]["candidate_sufficient"] and p["summary"]["failure_precedes_functional_promotion"]
 assert "residual dimensions 98308/98308/98311" in [x["evidence"] for x in p["gate_rows"]]
 assert "ASSERTS" in p["protected_disposition"] and "NEEDS" in p["protected_disposition"]
def main()->int:
 q=argparse.ArgumentParser();q.add_argument("--write",action="store_true");a=q.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if a.write else print(s,end="");return 0
if __name__=="__main__":raise SystemExit(main())
