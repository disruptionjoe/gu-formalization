#!/usr/bin/env python3
"""Replay K1795's global optimizer admission boundary."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1795-full-fisher-global-optimizer-admission.json"
def validate(d):
 c=d["bridge_census"];e=d["entry_state"];z=d["decision"];p=d["protected_state"]
 return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1795"),("inputs",d["inputs"]==["K1790","K1791","K1792","K1793","K1794"]),("census arithmetic",c["total"]==c["satisfied"]+c["conditional"]+c["excluded"]+c["missing"]),("exact partition",e["degree_nine_exact_partition_replayed"]),("area contraction",Fraction(e["excluded_fraction_of_input_area"])==Fraction(919,944)),("slab one",e["slab_one_complete_sublevel_excluded"] and z["slab_one_globally_excluded"]),("25 retained",e["slab_two_retained_boxes"]+e["slab_three_retained_boxes"]==25),("cover open",not e["complete_complement_cover_available"]),("slab two open",not z["slab_two_globally_excluded"]),("slab three open",not z["unique_stationary_point_on_complete_slab_three"]),("global open",not z["global_optimizer_proved"]),("physical open",not z["source_owned_physical_theory"]),("protected",not any(v for k,v in p.items() if k.endswith("_changed"))),("K1145",p["k1145_score"]=="0/7"),("K1150",p["k1150_score"]=="0/7")]
def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
