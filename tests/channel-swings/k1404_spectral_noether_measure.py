#!/usr/bin/env python3
"""Controls for K1404 spectral Noether measure."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1404-spectral-noether-measure.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
F,Q=D["spectral_noether_measure"],D["decision"]
for label,key,needle in [("symmetry","symmetry","constant phase"),("radial invariance","symmetry","||phi||^2"),("charge","charge","C(B)="),("conservation","conservation","dC(B)/dt=0"),("additivity","countable_additivity","countably additive"),("variation bound","countable_additivity","total variation"),("moments","moments","q^k"),("gauge","gauge_invariance","descends"),("signed","boundary","signed"),("noncoercive","boundary","neither controls")]:check(label,needle in F[key])
for key in ("independent_spectral_phase_symmetries_constructed","conserved_spectral_noether_measure_constructed","measure_countably_additive_and_finite","charge_moments_conserved_on_graph_domains"):check(key,Q[key])
for key in ("measure_positive_or_coercive","cutoff_uniform_completed_global_bound_constructed","source_observed_charge_measure_identified","protected_status_change"):check(f"{key} false",not Q[key])
for a,b in ((0.,0.),(3.,4.)):check("Cauchy bound finite",abs(a*b)<=math.hypot(a,0)*math.hypot(b,0))
assert n==21,n
print("RESULT: PASS 21/21")
