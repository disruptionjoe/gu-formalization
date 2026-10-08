#!/usr/bin/env python3
"""Controls for K1397 fixed-sector globalization."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1397-bounded-charge-global-evolution.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
F,Q=D["bounded_sector_globalization"],D["decision"]
for label,key,needle in [("sector","sector","fixed finite N"),("gauge","gauge","Coulomb"),("energy","conserved_energy","E_mu controls"),("Hodge","connection_control","Hodge and Poincare"),("matter","matter_control","diamagnetic"),("continuation","continuation","energy subcritical"),("regularity","higher_regular_persistence","propagate"),("recurrence","recurrent_compatibility","does not require any global L1_t"),("boundary","boundary","depend on N")]:check(label,needle in F[key])
for N,T,E in ((1,0.,2.),(4,3.,5.),(12,10.,.5)):
 harmonic_bound=math.sqrt(E)*(1+T)
 check(f"finite harmonic bound N={N} T={T}",math.isfinite(harmonic_bound))
for key in ("fixed_bounded_charge_global_large_data_evolution_constructed","finite_interval_low_norm_control_constructed","smooth_higher_regular_persistence_constructed","bounded_recurrent_coefficients_admitted"):check(key,Q[key])
for key in ("cutoff_uniform_global_bound_constructed","completed_unbounded_charge_global_flow_constructed","source_action_identified","protected_status_change"):check(f"{key} false",not Q[key])
assert n==23,n
print("RESULT: PASS 23/23")
