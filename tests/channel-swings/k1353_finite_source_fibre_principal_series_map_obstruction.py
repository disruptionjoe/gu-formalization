#!/usr/bin/env python3
"""Typed finite-fibre intertwiner obstruction audit for K1353."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1353-finite-source-fibre-principal-series-map-obstruction.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
T=D["finite_fibre_theorem"]; A=D["typed_application"]; Q=D["decision"]
check("finite domain","finite-dimensional" in T["domain"])
check("infinite irreducible codomain","infinite-dimensional irreducible" in T["codomain"])
check("linear equivariant candidate","linear G-equivariant" in T["candidate"])
check("finite image","finite-dimensional" in T["image_dimension"])
check("invariant image","G-invariant" in T["image_invariance"])
check("closed image","closed" in T["closure"])
check("irreducible dichotomy","either zero or all" in T["irreducibility_step"])
check("dimension contradiction","cannot equal" in T["dimension_step"])
check("zero map","T=0" in T["conclusion"])
check("adjoint covered",any("91-dimensional adjoint" in x for x in A["covered"]))
check("sections open",any("spaces of source sections" in x for x in A["not_covered"]))
check("nonlinear open",any("nonlinear" in x for x in A["not_covered"]))
check("no finite-fibre map",not Q["nonzero_pointwise_finite_fibre_linear_equivariant_map_exists"])
check("no direct fibre identity",not Q["released_source_fibre_directly_identified_with_H_ps"])
check("section-space route open",not Q["section_space_or_nonlocal_bridge_excluded"])
check("nonlinear route open",not Q["nonlinear_bridge_excluded"])
check("reduced route open",not Q["symmetry_reduced_bridge_excluded"])
check("source bridge missing",not Q["source_action_bridge_constructed"])
check("protected fixed",not Q["protected_status_change"])
assert n==20; print("RESULT: PASS 20/20")
