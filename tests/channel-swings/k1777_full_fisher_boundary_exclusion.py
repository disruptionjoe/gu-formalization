#!/usr/bin/env python3
"""Arb replay of K1777's semiconvex boundary exclusion."""
import json
from fractions import Fraction as F
from pathlib import Path
from flint import arb,ctx,fmpq
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1777-full-fisher-boundary-exclusion.json"
ctx.dps=100;ctx.threads=1
def aq(x):x=F(x);return arb(fmpq(x.numerator,x.denominator))
def compute():
 d=json.loads((ROOT/"lab/process/k1772-boundary-strip-refinement.json").read_text())["refinement"]
 tmax=F(d["retained_hull"][1]);zmax=F(d["retained_hull"][3]);cmax=F(2)-F(1,1024)/tmax**2
 t,z,c=aq(tmax),aq(zmax),aq(cmax);v=1-t;beta=t/v
 modulus=(aq(F(231,400))*beta**2+aq(F(41,80))*beta**3)/(1-z).sqrt()
 penalty=t/v**2*modulus*c/2
 gap=arb(json.loads((ROOT/"lab/process/k1756-rademacher-arb-gap.json").read_text())["comparison"]["whole_line_gap"])
 candidate=arb(json.loads((ROOT/"lab/process/k1763-hermite-degree-escalation.json").read_text())["certificate"]["candidate_upper"])
 slack=aq(F(159178645305,10**18))-candidate
 return d,tmax,zmax,cmax,beta,modulus,penalty,gap,slack,gap-penalty-slack
def validate(d):
 src,t,z,c,b,m,p,g,s,r=compute();x=d["certificate"];zdec=d["decision"]
 return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1777"),
  ("digest",x["input_partition_digest"]==src["partition_digest"]),("cells",x["physical_cell_count"]==2),
  ("t",F(x["t_upper"])==t),("z",F(x["z_upper"])==z),("c",F(x["c_upper"])==c),
  ("beta",arb(x["beta_upper"]).contains(b)),("modulus",arb(x["semiconvexity_modulus_upper"]).contains(m)),
  ("penalty",arb(x["full_fisher_penalty_upper"]).contains(p)),("gap",arb(x["k1756_rademacher_gap"]).contains(g)),
  ("threshold slack",arb(x["threshold_above_k1763_candidate"]).contains(s)),
  ("residual",arb(x["residual_gap_lower"]).contains(r) and arb(x["residual_gap_lower"])>0),
  ("excluded",zdec["both_boundary_cells_excluded"] and zdec["boundary_piece_count_remaining"]==0),
  ("three slabs",zdec["interior_slab_count_remaining"]==3),("not Newton",not zdec["full_fisher_interval_newton_completed"]),
  ("not optimizer",not zdec["global_optimizer_proved"])]
def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
