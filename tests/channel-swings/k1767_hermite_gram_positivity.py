#!/usr/bin/env python3
"""Exact controls for K1767's Gram positivity and denominator orientation."""
import importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1767-hermite-gram-positivity.json"
P=ROOT/"tests/channel-swings/k1768_bernstein_sublevel_partition.py";s=importlib.util.spec_from_file_location("engine",P);e=importlib.util.module_from_spec(s);s.loader.exec_module(e)
def controls():
 out={}
 for degree in (5,7):
  _,_,den,_=e.threshold_polynomial(degree);out[degree]=den.subs({e.t:e.s.Rational(1,20),e.z:e.s.Rational(1,2)})
 return out
def validate(d,rows=None):
 rows=controls() if rows is None else rows;t=d["theorem"];o=d["orientation"];z=d["decision"]
 return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1767"),("density",t["density"]=="For 0<t<1, Y=sqrt(t)X+sqrt(1-t)Z has a strictly positive smooth density on R."),("quadratic",t["quadratic_form"]=="alpha^T G alpha=E[(sum alpha_j H_(2j+1)(Y))^2]."),("independence",t["linear_independence"]=="A nonzero polynomial cannot vanish almost everywhere under a strictly positive density."),("positive definite",t["conclusion"]=="Every finite odd-Hermite Gram matrix is positive definite; its determinant and every principal minor are positive."),("D5 control",rows[5]>0 and o["degree_five_denominator_positive"]),("D7 control",rows[7]>0 and o["degree_seven_denominator_positive"]),("sign constant",o["sign_constant_on_regular_chart"]),("cross multiply",z["cross_multiplication_by_normalized_denominator_is_valid"]),("singular fenced",not z["positivity_extends_to_the_singular_t_equals_one_face"]),("Fisher fenced",not z["positivity_identifies_the_full_fisher"])]
def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
