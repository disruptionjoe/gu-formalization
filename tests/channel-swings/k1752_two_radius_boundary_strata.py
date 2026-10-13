#!/usr/bin/env python3
"""Exact boundary-mechanism controls for K1752."""
import json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
ARTIFACT=ROOT/"lab/process/k1752-two-radius-boundary-strata.json"

def validate(d):
    b=d["boundary_strata"]; z=Q(1,1000); c=Q(3,2)
    p=c/(c+z*z); a=1-z; outer=1+c/z; outer_mass=1-p
    m4=p*a*a+outer_mass*outer*outer
    m6=p*a**3+outer_mass*outer**3
    checks=[("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1752"),
      ("four faces",all(k in b for k in ("c_zero","z_one","z_zero","c_two_minus_q"))),
      ("c zero Rademacher",b["c_zero"]["name"]=="radius_coalescence_rademacher"),
      ("z one three point",b["z_one"]["name"]=="complete_symmetric_three_point"),
      ("rare atom",b["z_zero"]["name"]=="rare_atom_growing_support"),
      ("outer mass small",outer_mass==z*z/(c+z*z)),("outer diverges",outer>1000),
      ("m4 fixed",m4==1+c),("m6 large",m6>1000),
      ("zero noise",b["c_two_minus_q"]["name"]=="zero_gaussian_noise_singular_face"),
      ("infinity",b["c_two_minus_q"]["fisher_type"].startswith("+infinity")),
      ("joint warning","two-parameter" in b["joint_corner"]["warning"]),
      ("not collars",not d["decision"]["all_boundary_collars_excluded"]),
      ("scope","does not prove collar" in d["scope_guard"])]
    return checks
def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
