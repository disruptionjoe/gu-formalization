#!/usr/bin/env python3
"""Exact symbolic controls for K1766's correlated Hermite rationals."""
import importlib.util, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
ARTIFACT=ROOT/"lab/process/k1766-correlated-hermite-rational.json"
P=ROOT/"tests/channel-swings/k1768_bernstein_sublevel_partition.py"
spec=importlib.util.spec_from_file_location("engine",P);engine=importlib.util.module_from_spec(spec);spec.loader.exec_module(engine)

def compute():
    rows={}
    for degree in (5,7):
        _,_,den,terms=engine.threshold_polynomial(degree)
        rows[degree]={"terms":len(terms),"control_denominator":den.subs({engine.t:engine.s.Rational(1,20),engine.z:engine.s.Rational(1,2)})}
    return rows

def validate(d,rows=None):
    rows=compute() if rows is None else rows;c=d["coordinate"];r=d["cancelled_tests"];z=d["decision"]
    return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1766"),("q",c["q"]=="1/1024"),("substitution",c["substitution"]=="c=2-q/t^2"),("outer square",engine.T_BOX[0]**2<engine.Q_FIXED/2),("D5 terms",rows[5]["terms"]==r["degree_five_threshold_polynomial_terms"]==69),("D7 terms",rows[7]["terms"]==r["degree_seven_threshold_polynomial_terms"]==255),("D5 orientation",rows[5]["control_denominator"]>0),("D7 orientation",rows[7]["control_denominator"]>0),("threshold",r["threshold"]==engine.encode_fraction(engine.UPPER)),("upper margin",r["threshold_exceeds_k1763_candidate_upper"]),("correlation",z["matched_coordinate_preserves_c_t_correlation"]),("removable",z["z_zero_is_removable_for_the_cancelled_threshold_polynomials"]),("raw fenced",not z["raw_moment_substitution_at_z_zero_is_allowed"]),("full Fisher fenced",not z["full_fisher_computed_by_the_rational_tests"])]

def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
