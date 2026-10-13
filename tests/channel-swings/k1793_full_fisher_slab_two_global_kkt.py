#!/usr/bin/env python3
"""Replay K1793's slab-two retained frontier."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1793-full-fisher-slab-two-global-kkt.json"
def validate(d):
 p=json.loads((ROOT/"lab/process/k1791-full-fisher-three-slab-tail-cover.json").read_text())["partition"];row=p["by_slab"][1];c=d["certificate"];z=d["decision"]
 return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1793"),("digest",c["degree_nine_partition_digest"]==p["partition_digest"]),("pruned",c["pruned_leaves"]==row["pruned_leaves"]==40),("retained",c["retained_leaves"]==row["retained_leaves"]==8),("cells",c["retained_input_cells"]==row["retained_input_cells"]),("hull",c["retained_hull"]==row["retained_hull"]),("local",z["local_boundary_kkt_isolated"]),("slab open",not z["complete_slab_two_sublevel_excluded"]),("faces open",not z["every_slab_two_face_and_corner_closed"]),("not global",not z["global_optimizer_proved"])]
def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
