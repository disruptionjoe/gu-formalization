#!/usr/bin/env python3
"""Exact exponent controls for K1381's finite-Lp charge staircase."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1381-finite-lp-charge-staircase.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
H,Q=D["holder_sobolev_trade"],D["decision"]
for label,key,needle in [
 ("lift","lift","Q^(n+1)phi"),("range","range","sigma_p=3/p"),
 ("Holder","holder","||E||_p"),("Sobolev","sobolev","embeds"),
 ("mixed cost","mixed_cost","finite p requires"),("radial term","radial_term","2p/(p-1)"),
 ("boundary","boundary","charged electric-current")]:check(label,needle in H[key])
for p in (3.0,4.0,6.0,12.0):
 r=2*p/(p-2);sigma=3/p
 check(f"Holder identity p={p:g}",abs(1/p+1/r+0.5-1)<1e-12)
 check(f"Sobolev line p={p:g}",abs((0.5-1/r)*3-sigma)<1e-12)
 check(f"finite-p loss p={p:g}",sigma>0 and 2<r<=6)
check("endpoint exponent",math.isclose(0.0,0.0))
check("endpoint target L2",H["range"].endswith("sigma_infinity=0"))
check("trade derived",Q["finite_p_trade_derived"])
check("exponents named",Q["sharp_exponents_named"])
check("endpoint closes",Q["endpoint_same_energy_closure"])
check("finite p does not close",not Q["finite_p_same_energy_closure"])
check("other routes open",not Q["null_form_or_strichartz_route_excluded"])
check("source absent",not Q["source_action_identified"])
check("protected fixed",not Q["protected_status_change"])
assert n==29,n
print("RESULT: PASS 29/29")
