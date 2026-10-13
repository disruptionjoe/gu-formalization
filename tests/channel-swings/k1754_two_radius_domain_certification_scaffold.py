#!/usr/bin/env python3
"""Computed locator and fail-closed cover controls for K1754."""
import importlib.util,json
from pathlib import Path
from scipy.optimize import minimize,minimize_scalar
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1754-two-radius-domain-certification-scaffold.json"
P=ROOT/"tests/channel-swings/k1733_finite_strength_four_point_benchmark.py"
s=importlib.util.spec_from_file_location("k1733",P);k=importlib.util.module_from_spec(s);s.loader.exec_module(k)
def fcz(x,q,order):
 c,z=x
 if not (0<c<2-q and 0<z<1):return 1.
 p=c/(c+z*z);return k.f4((p,1-z),q,order)
def validate(d):
 q=1/1024;loc=d["computed_locator"]; sols=[]
 for order in loc["orders"]:
  for x0 in loc["starts"]:
   r=minimize(lambda x:fcz(x,q,order),x0,method="Nelder-Mead",options={"maxiter":6000,"xatol":1e-11,"fatol":1e-18})
   sols.append((r.fun,*r.x))
 tri=minimize_scalar(lambda p:k.f3(p,q,180),bounds=(1/3+1e-9,.999),method="bounded",options={"xatol":1e-12})
 rad=k.fisher(k.np.array([-1.,1.]),k.np.array([.5,.5]),(q/2)**.5,180)
 cover=d["cover_contract"];dec=d["decision"]
 return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1754"),
  ("five cover pieces",len(cover["partition"])==5),("corner joint","jointly" in cover["corner_rule"]),
  ("nonnegative prune","nonnegative" in cover["core_method"]),("fail closed","Unresolved boxes make the global verdict false" in cover["acceptance"]),
  ("objectives agree",max(x[0] for x in sols)-min(x[0] for x in sols)<1e-18),
  ("c range",all(loc["c_range"][0]<x[1]<loc["c_range"][1] for x in sols)),
  ("z range",all(loc["z_range"][0]<x[2]<loc["z_range"][1] for x in sols)),
  ("three control",min(x[0] for x in sols)<tri.fun),("rad control",min(x[0] for x in sols)<rad),
  ("cover defined",dec["complete_cover_contract_defined"]),("not global",not dec["global_branch_and_bound_completed"]),
  ("collars open",not dec["boundary_collars_completed"]),("scope","computed evidence" in d["scope_guard"])]
def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
