#!/usr/bin/env python3
"""Replay the K1792 complete slab-one sublevel exclusion chain."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1792-full-fisher-slab-one-global-kkt.json"
def validate(d):
 p=json.loads((ROOT/"lab/process/k1791-full-fisher-three-slab-tail-cover.json").read_text())["partition"]
 b=json.loads((ROOT/"lab/process/k1777-full-fisher-boundary-exclusion.json").read_text())["decision"]
 s=json.loads((ROOT/"lab/process/k1788-full-fisher-first-two-slab-exclusion.json").read_text())["certificate"]["boundary_boxes"][0]
 c=d["certificate"];z=d["decision"];one=p["by_slab"][0]
 return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1792"),("digest",c["degree_nine_partition_digest"]==p["partition_digest"]),("boundary closed",b["boundary_piece_count_remaining"]==0),("37 cells",c["slab_one_input_cells"]==37),("72 pruned",c["slab_one_pruned_leaves"]==one["pruned_leaves"]==72),("zero retained",c["slab_one_retained_leaves"]==one["retained_leaves"]==0),("KKT value",c["local_boundary_kkt_value"]==s["boundary_stationary_value_enclosure"]),("slab one excluded",z["slab_one_complete_sublevel_excluded"]),("KKT not optimizer",not z["slab_one_local_boundary_kkt_is_global_optimizer"]),("others open",not z["slab_two_complete_sublevel_excluded"] and not z["slab_three_complete_sublevel_excluded"]),("not global",not z["global_optimizer_proved"])]
def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
