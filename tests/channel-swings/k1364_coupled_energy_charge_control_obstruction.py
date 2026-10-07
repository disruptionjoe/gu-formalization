#!/usr/bin/env python3
"""Ordinary-energy versus charge-graph coercivity controls for K1364."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1364-coupled-energy-charge-control-obstruction.json").read_text());n=0
def check(label,value):
 global n;assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C,R,Q=D["counterexample"],D["repair_boundary"],D["decision"]
check("charge witnesses","Q e_n=4n e_n" in C["charge_witnesses"])
check("zero gauge fixture","A=0" in C["truncated_fields"])
check("ordinary bound stated","pi^2/6" in C["ordinary_norm"])
check("charge divergence stated","16N" in C["charge_graph_norm"])
for N in (1,2,8,32,128):
 ordinary=sum(1/(k*k) for k in range(1,N+1));charge=sum((4*k)**2/(k*k) for k in range(1,N+1))
 energy=.5*ordinary+.25*ordinary*ordinary
 check(f"ordinary energy bounded N={N}",energy<.5*(math.pi**2/6)+.25*(math.pi**2/6)**2+1e-12)
 check(f"charge graph exact N={N}",charge==16*N)
check("no coercive constant","No constant C" in C["conclusion"])
check("three repair classes",len(R["admissible_repairs"])==3)
check("three nonrepairs",len(R["nonrepairs"])==3)
check("seagull nonrepair",any("seagull" in x for x in R["nonrepairs"]))
check("energy control rejected",not Q["ordinary_positive_energy_controls_charge_graph_norm"])
check("sequence constructed",Q["explicit_uniformly_energy_bounded_divergent_graph_sequence_constructed"])
check("zero gauge sufficient",Q["zero_gauge_sector_already_exhibits_obstruction"])
check("seagull rejected",not Q["seagull_term_supplies_uniform_charge_coercivity"])
check("repairs preserved",not Q["augmented_action_or_graph_propagation_excluded"])
check("source no-go rejected",not Q["source_action_no_go_proved"])
check("protected fixed",not Q["protected_status_change"])
assert n==27;print("RESULT: PASS 27/27")
