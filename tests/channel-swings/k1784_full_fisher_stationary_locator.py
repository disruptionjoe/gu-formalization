#!/usr/bin/env python3
"""Replay K1784's rational Newton checkpoint inside slab three."""
import importlib.util,json
from fractions import Fraction as F
from pathlib import Path
from flint import arb
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1784-full-fisher-stationary-locator.json";P=ROOT/"tests/channel-swings/k1781_full_fisher_compact_jet.py";s=importlib.util.spec_from_file_location("k1781",P);k=importlib.util.module_from_spec(s);s.loader.exec_module(k)
def compute():
 t,z=F(332081,6250000),F(880503,1562500);j=k.compact_jet(t,t,z,z);det=j.h[0][0]*j.h[1][1]-j.h[0][1]**2
 return {"point":{"t":str(t),"z":str(z)},"compact_value":k.enc(j.v),"compact_gradient":{"t":k.enc(j.g[0]),"z":k.enc(j.g[1])},"compact_hessian":{"tt":k.enc(j.h[0][0]),"tz":k.enc(j.h[0][1]),"zz":k.enc(j.h[1][1]),"determinant":k.enc(det)}}
def validate(d,got=None):
 got=compute() if got is None else got;x=d["checkpoint"];z=d["decision"];h=x["compact_hessian"]
 checks=[("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1784"),("point",x["point"]==got["point"])]
 for group in ("compact_gradient","compact_hessian"):
  for key,val in got[group].items():checks.append((f"{group}.{key}",arb(x[group][key]).contains(arb(val))))
 checks += [("tt positive",arb(h["tt"])>0),("det positive",arb(h["determinant"])>0),("locator",z["reproducible_rational_locator_available"]),("not stationary",not z["stationary_box_isolated"]),("not unique",not z["unique_stationary_component_proved"]),("not global",not z["global_optimizer_proved"])]
 return checks
def main():
 if not ARTIFACT.exists() or "--print" in __import__("sys").argv:print(json.dumps(compute(),indent=2));return
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
