#!/usr/bin/env python3
"""K1814: compose the exact slab-three stationary and boundary status."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1814-full-fisher-slab-three-boundary-cover.json"
def load(n):return json.loads((ROOT/f"lab/process/{n}.json").read_text())
def compute():
 a=load("k1804-full-fisher-deduplicated-boundary-atlas");s=load("k1812-full-fisher-slab-three-whole-line-bank");w=load("k1813-full-fisher-slab-three-stationary-cover")
 return {"slab_three_leaf_count":s["certificate"]["leaf_count"],"stationary_rejected_leaves":s["certificate"]["rejected_leaf_count"],"retained_leaves":s["certificate"]["retained_leaf_count"],"deduplicated_exposed_atomic_faces_total":a["certificate"]["exposed_atomic_faces"],"deduplicated_exposed_boundary_vertices_total":a["certificate"]["exposed_boundary_vertices"],"first_parent_fixed_score_margin_lower":w["certificate"]["compact_bounds"]["cross_margin_lower"],"first_parent_margin_certified_positive":w["certificate"]["compact_bounds"]["cross_margin_positive"]}
def validate(d,got=None):
 got=compute() if got is None else got;return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1814"),("exact replay",d["certificate"]==got),("78 retained",got["retained_leaves"]==78),("parent open",not got["first_parent_margin_certified_positive"]),("boundary open",not d["decision"]["all_slab_three_faces_and_vertices_certified"])]
def main():
 got=compute()
 if not ARTIFACT.exists() or "--print" in __import__('sys').argv:print(json.dumps(got,indent=2));return
 checks=validate(json.loads(ARTIFACT.read_text()),got)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
