#!/usr/bin/env python3
"""Compose the exact full-Fisher search preconditioner."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1774-full-fisher-preconditioner.json"
def expected():
 a=json.loads((ROOT/"lab/process/k1771-interior-survivor-topology.json").read_text())["topology"]
 b=json.loads((ROOT/"lab/process/k1772-boundary-strip-refinement.json").read_text())["refinement"]
 return {"input_coarse_cells":60,"interior_cells":a["input_interior_cells"],"interior_slabs":a["slab_count"],"boundary_input_cells":1,"boundary_pruned_leaves":b["pruned_leaves"],"boundary_retained_cells":b["retained_leaves"],"effective_search_pieces":a["slab_count"]+b["retained_leaves"],"interior_topology_digest":a["topology_digest"],"boundary_partition_digest":b["partition_digest"]}
def validate(d):
 z=d["decision"];return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1774"),("composition",d["preconditioner"]==expected()),("five pieces",d["preconditioner"]["effective_search_pieces"]==5),("geometric only",z["geometric_preconditioner_completed"]),("no boundary exclusion",not z["boundary_strip_excluded"]),("no Newton",not z["full_fisher_interval_newton_completed"]),("no optimizer",not z["global_optimizer_proved"])]
def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
