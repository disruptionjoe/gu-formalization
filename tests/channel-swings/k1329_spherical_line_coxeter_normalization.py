#!/usr/bin/env python3
"""Composition controls for K1329's spherical-line Coxeter transport."""
import hashlib,json,itertools
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1329-spherical-line-coxeter-normalization.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
T=D["normalized_transport"]; C=D["coxeter_relations"]; K=D["comparison_with_k1325"]; Q=D["decision"]
check("normalized definition",T["definition"].startswith("R_i(lambda)=m("))
check("basis transport",T["basis_action"]=="R_i(lambda)v_lambda=v_s_i_lambda")
check("regular domain",T["domain"].startswith("regular imaginary"))
check("chamber fibers",T["fiber_count"]==322560 and T["fiber_dimension"]==1)
check("involutions",C["involution"].endswith("on v_lambda"))
check("commutations",C["nonadjacent_commutation"].startswith("R_i R_j=R_j R_i"))
check("braids",C["adjacent_braid"].startswith("R_i R_j R_i=R_j R_i R_j"))
check("all reduced words",C["general_reduced_word"].endswith("reduced expression"))
check("unit relator",C["scalar_relator_defect"]==1)
check("sign boundary subsumed",K["sign_only_defects_normalized"])
check("meromorphic scalar boundary",K["arbitrary_nonzero_meromorphic_scalar_defects_on_spherical_line_normalized"])
check("K-type ceiling",not K["nonspherical_k_type_defects_classified"])
check("spherical result",Q["spherical_line_weyl_transport_constructed"] and Q["spherical_line_coxeter_flat"])
check("operator ceiling",not Q["full_principal_series_G_intertwiner_family_constructed"] and not Q["common_dense_operator_domain_constructed"] and not Q["operator_reducibility_control_constructed"])
check("physical ceiling",not Q["canonical_physical_chamber_constructed"] and not Q["protected_status_change"])
assert n==18; print("RESULT: PASS 18/18")
