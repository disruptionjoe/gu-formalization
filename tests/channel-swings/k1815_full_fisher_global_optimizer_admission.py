#!/usr/bin/env python3
"""K1815: protected global-optimizer admission after the slab-three method test."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1815-full-fisher-global-optimizer-admission.json"
def load(n):return json.loads((ROOT/f"lab/process/{n}.json").read_text())
def compute():
 two=load("k1809-full-fisher-slab-two-global-exclusion");three=load("k1814-full-fisher-slab-three-boundary-cover")
 return {"slab_one_excluded":two["certificate"]["slab_one_already_excluded"],"slab_two_excluded":two["decision"]["slab_two_complete_sublevel_excluded"],"slab_three_retained_leaves":three["certificate"]["retained_leaves"],"slab_three_complete_stationary_uniqueness":three["decision"]["complete_stationary_uniqueness_proved"],"slab_three_complete_boundary_cover":three["decision"]["all_slab_three_faces_and_vertices_certified"]}
def validate(d,got=None):
 got=compute() if got is None else got;return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1815"),("exact replay",d["certificate"]==got),("two slabs closed",got["slab_one_excluded"] and got["slab_two_excluded"]),("slab three open",got["slab_three_retained_leaves"]==78),("global withheld",not d["decision"]["global_optimizer_proved"]),("physical withheld",not d["decision"]["source_owned_physical_theory"])]
def main():
 got=compute()
 if not ARTIFACT.exists() or "--print" in __import__('sys').argv:print(json.dumps(got,indent=2));return
 checks=validate(json.loads(ARTIFACT.read_text()),got)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
