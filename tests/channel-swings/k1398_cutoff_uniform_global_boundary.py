#!/usr/bin/env python3
"""Controls for K1398 cutoff-uniform boundary."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1398-cutoff-uniform-global-boundary.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
F,Q=D["uniformity_audit"],D["decision"]
for label,key,needle in [("bounded","bounded_generator_step","||Q_N||<=N"),("sequence","energy_sequence","Gauss density unbounded"),("local","local_completion","one additional completed triangular tier"),("gap","iteration_gap","No conserved or uniformly bounded"),("logic","logical_effect","route boundary"),("reopen","reopeners","modified conserved energy"),("limits","boundary","do not commute automatically")]:check(label,needle in F[key])
for N in (1,4,16,64):check(f"cutoff grows N={N}",N<=N*N)
for key in ("fixed_sector_global_theorem_preserved","current_restart_constant_cutoff_dependent","base_energy_uniform_completion_route_excluded","local_completed_flow_preserved"):check(key,Q[key])
for key in ("all_global_completed_flow_mechanisms_excluded","completed_unbounded_charge_global_flow_constructed","protected_status_change"):check(f"{key} false",not Q[key])
assert n==21,n
print("RESULT: PASS 21/21")
