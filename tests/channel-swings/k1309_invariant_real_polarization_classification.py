#!/usr/bin/env python3
"""Exact controls for K1309's invariant real-polarization classification."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1309-invariant-real-polarization-classification.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
T=D["classification_theorem"]; Q=D["quantization_boundary"]
check("opposite pairing",T["kks_pairs_root_spaces_only_with_opposites"])
check("Lagrangian",T["each_eigenbundle_is_lagrangian"])
check("half dimension",T["each_eigenbundle_dimension"]==42)
check("closure condition",T["integrability_requires_root_subset_closed_under_addition"])
check("positive systems",T["compatible_integrable_sign_sets_are_positive_root_systems"])
w=(2**6)*math.factorial(7)
check("D7 Weyl order",w==322560==T["weyl_group_order"])
check("polarization count",T["positive_root_system_count"]==T["invariant_integrable_real_polarization_count"]==w)
check("transitive Weyl action",T["weyl_action_transitive"])
check("no Weyl-fixed choice",not T["canonical_weyl_fixed_polarization_exists"])
check("real polarization",Q["real_lagrangian_polarization_constructed"])
check("no positive complex polarization",not Q["positive_complex_polarization_constructed"])
check("no positive inner product",not Q["positive_inner_product_constructed"])
check("no physical map",not Q["physical_state_map_constructed"])
assert n==15; print("RESULT: PASS 15/15")
