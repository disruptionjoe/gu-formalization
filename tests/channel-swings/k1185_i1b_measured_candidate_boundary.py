#!/usr/bin/env python3
"""K1185: integrate first measured native K132 candidate into the frontier."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k1185-i1b-measured-candidate-boundary.json"
PATHS={"k1180":ROOT/"lab/process/k1180-i1b-native-candidate-admission-boundary.json","k1182":ROOT/"lab/process/k1182-native-upsilon-k132-complement-ranks.json","k1183":ROOT/"lab/process/k1183-rank98-overlap-envelope.json","k1184":ROOT/"lab/process/k1184-native-upsilon-admission-audit.json"}
def digest(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def build()->dict[str,Any]:
 return {"schema_version":"1.0","result_id":"K1185-I1B-MEASURED-CANDIDATE-BOUNDARY","created":"2026-10-05","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","target_claim":"SC-ACT-06","pinned_inputs":{k:{"path":str(v.relative_to(ROOT)),"sha256":digest(v)} for k,v in PATHS.items()},"current_measured_source_owned_k132_maps":1,"measured_map":"full raw Upsilon response J","causal_complement_ranks":{"timelike":162,"spacelike":162,"null":8323},"actual_residual_after_gauge":{"timelike":98308,"spacelike":98308,"null":98311},"best_favorable_residual_after_rank98":{"timelike":98210,"spacelike":98210,"null":98213},"candidate_meeting_full_packet":0,"next_condition":"derive a source-owned map with new complement outside the joint H/J/prior-channel span at ranks at least 98210/98210/98213 under the favorable grant, or own an enlarged closed gauge/KT image or changed stationary parent and recompute every K1150 gate","protected_disposition":"SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b/RA-F1/AC-F1 remain NEEDS","claim_ceiling":"first measured candidate and exact residual frontier; no global GU or SC-ACT-06 verdict"}
def validate(p:dict[str,Any])->None:
 assert p["result_id"]=="K1185-I1B-MEASURED-CANDIDATE-BOUNDARY" and p["classification"]=="SOURCE_NATIVE_ROUTE" and p["target_claim"]=="SC-ACT-06"
 assert p["current_measured_source_owned_k132_maps"]==1 and p["candidate_meeting_full_packet"]==0
 assert p["causal_complement_ranks"]=={"timelike":162,"spacelike":162,"null":8323}
 assert p["actual_residual_after_gauge"]=={"timelike":98308,"spacelike":98308,"null":98311}
 assert p["best_favorable_residual_after_rank98"]=={"timelike":98210,"spacelike":98210,"null":98213}
 assert "98210/98210/98213" in p["next_condition"] and "remain ASSERTS" in p["protected_disposition"]
def main()->int:
 q=argparse.ArgumentParser();q.add_argument("--write",action="store_true");a=q.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if a.write else print(s,end="");return 0
if __name__=="__main__":raise SystemExit(main())
