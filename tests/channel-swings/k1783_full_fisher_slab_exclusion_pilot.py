#!/usr/bin/env python3
"""Deterministic computed scout of the three K1771 slabs for K1783."""
import json,math
from fractions import Fraction as F
from pathlib import Path
from scipy.integrate import quad
from scipy.optimize import differential_evolution
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1783-full-fisher-slab-exclusion-pilot.json";SLABS=json.loads((ROOT/"lab/process/k1771-interior-survivor-topology.json").read_text())["topology"]["slabs"];Q=1/1024
def value(x):
 t,z=map(float,x);c=2-Q/t**2;p=c/(c+z*z);a=1-z;b=1+c/z;v=1-t;ra,rb,rt=math.sqrt(a),math.sqrt(b),math.sqrt(t);ca,cb=rt*ra/v,rt*rb/v;wa=p*math.exp(-t*a/(2*v));wb=(1-p)*math.exp(-t*b/(2*v));pref=t/(v**2*math.sqrt(v*2*math.pi))
 def f(y):
  d=wa*math.cosh(ca*y)+wb*math.cosh(cb*y);n=wa*ra*math.sinh(ca*y)+wb*rb*math.sinh(cb*y);return pref*math.exp(-y*y/(2*v))*(n-rt*y*d)**2/d
 return quad(f,-11,11,epsabs=1e-14,epsrel=1e-12,limit=300)[0]
def compute():
 rows=[]
 for i,s in enumerate(SLABS,1):
  tb=list(map(lambda x:float(F(x)),s["t"]));zb=list(map(lambda x:float(F(x)),s["z"]));r=differential_evolution(value,[tuple(tb),tuple(zb)],tol=1e-10,popsize=12,polish=True,seed=1780+i,workers=1)
  rows.append({"slab":i,"point":[format(r.x[0],".17g"),format(r.x[1],".17g")],"compact_value":format(r.fun,".17g"),"on_t_boundary":bool(min(abs(r.x[0]-tb[0]),abs(r.x[0]-tb[1]))<1e-7),"on_z_boundary":bool(min(abs(r.x[1]-zb[0]),abs(r.x[1]-zb[1]))<1e-7)})
 return rows
def validate(d,got=None):
 got=compute() if got is None else got;rows=d["computed_pilot"]["slabs"];z=d["decision"]
 checks=[("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1783"),("three slabs",len(rows)==len(got)==3)]
 for a,b in zip(rows,got):checks += [(f"slab {b['slab']} value",abs(float(a["compact_value"])-float(b["compact_value"]))<1e-15),(f"slab {b['slab']} point",max(abs(float(x)-float(y)) for x,y in zip(a["point"],b["point"]))<1e-5)]
 checks += [("ordering",float(rows[0]["compact_value"])>float(rows[1]["compact_value"])>float(rows[2]["compact_value"])),("pilot only",not z["slabs_one_and_two_excluded"]),("stationarity open",not z["stationary_box_isolated"]),("global open",not z["global_optimizer_proved"])]
 return checks
def main():
 if not ARTIFACT.exists() or "--print" in __import__("sys").argv:print(json.dumps(compute(),indent=2));return
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
