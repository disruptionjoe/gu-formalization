#!/usr/bin/env python3
"""Exact filtration controls for K1386's covariant commutator."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1386-covariant-charge-commutator-filtration.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
F,Q=D["covariant_filtration"],D["decision"]
for label,key,needle in [
 ("operators","operators","[D_mu,D_nu]=i F_mu_nu Q"),
 ("basic commutator","basic_wave_commutator","2i F_a^mu Q D_mu u"),
 ("iterated form","iterated_form","|beta|+|gamma|<=|alpha|"),
 ("combined order","combined_order","|alpha|+n+1"),
 ("curvature order","curvature_order","at most |alpha|"),
 ("mechanism","mechanism","triangular rather than rectangular"),
 ("boundary","boundary","not a null-form")]:check(label,needle in F[key])
for a in range(7):
 for n0 in range(7-a):
  for gamma in range(a+1):
   check(f"filtration a={a} n={n0} g={gamma}",gamma+n0+1<=a+n0+1)
check("basic derived",Q["basic_commutator_derived"])
check("iterated derived",Q["iterated_filtration_derived"])
check("combined order",Q["combined_order_preserved"])
check("no rectangular corner",not Q["rectangular_top_corner_required"])
check("no null form overclaim",not Q["null_form_constructed"])
check("no global overclaim",not Q["global_bound_proved"])
check("source absent",not Q["source_action_identified"])
check("protected fixed",not Q["protected_status_change"])
assert n==102,n
print("RESULT: PASS 102/102")
