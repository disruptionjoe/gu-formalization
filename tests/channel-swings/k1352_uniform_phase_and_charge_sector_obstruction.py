#!/usr/bin/env python3
"""Manifest audit for the irreducible uniform-phase boundary K1352."""
import hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1352-uniform-phase-and-charge-sector-obstruction.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
S=D["scalar_phase_theorem"]; C=D["charge_sector_theorem"]; Q=D["decision"]
check("irreducible principal series","irreducible" in S["representation"])
check("uniform phase hypothesis","exp(i q t) I" in S["hypothesis"])
check("derived scalar generator","i q I" in S["derived_action"])
check("commutator identity","=0" in S["commutator_identity"])
check("simple-kernel argument","proper ideal" in S["faithfulness_reason"])
check("centrality","zero center" in S["centrality_conclusion"])
check("trivial scalar result","X=0 and q=0" in S["result"])
check("nonzero charge candidate","nonzero fixed-q" in C["candidate"])
check("irreducible sector step","equals H_ps" in C["full_G_invariance_test"])
check("uniform-phase contradiction","contradicting" in C["contradiction"])
check("centralizer survives","centralizer or normalizer" in C["surviving_scope"])
check("no internal uniform phase",not Q["nontrivial_internal_uniform_scalar_phase_exists"])
check("no full-G charged sector",not Q["nonzero_fixed_charge_sector_full_G_invariant"])
check("external U1 typed",Q["k1346_phase_is_external_commuting_u1_for_this_control"])
check("nonuniform decomposition open",not Q["nonuniform_subgroup_charge_decomposition_excluded"])
check("reduction required",Q["symmetry_reduction_required_for_single_nonzero_charge_sector"])
check("selector missing",not Q["source_charge_selector_constructed"])
check("protected fixed",not Q["protected_status_change"])
check("ceiling preserves open routes","leaves nonuniform charge decompositions" in D["claim_ceiling"])
assert n==21; print("RESULT: PASS 21/21")
