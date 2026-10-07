#!/usr/bin/env python3
"""Composition controls for K1335's operator and physical boundary."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1335-operator-intertwiner-admission-boundary.json").read_text()); ncheck=0
def check(label,value):
 global ncheck; assert value,label; ncheck+=1; print(f"PASS {ncheck:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C=D["certificate"]; Q=D["decision"]
check("twenty rows",C["row_count"]==20)
check("counts close",sum(C[k] for k in ("satisfied_count","excluded_count","conditional_count","missing_count"))==C["row_count"])
check("ten satisfied",C["satisfied_count"]==10)
check("three excluded",C["excluded_count"]==3)
check("one conditional",C["conditional_count"]==1 and C["retained_conditional_rows"]==["finite_polarized_bfv_compatibility"])
check("six missing",C["missing_count"]==6 and len(C["retained_missing_rows"])==6)
check("operator row advanced",C["advanced_row"]=={"row":"full_operator_coxeter_flat_G_intertwiner_completion","from":"conditional","to":"satisfied"})
check("rank-one completion",Q["full_rank_one_kernel_and_even_k_spectrum_constructed"])
check("common domain",Q["common_dense_k_finite_domain_constructed"])
check("unitary irreducible",Q["regular_imaginary_unitarity_and_irreducibility_constructed"])
check("operator Coxeter",Q["operator_valued_D7_coxeter_relations_constructed"])
check("G descent",Q["G_equivariant_full_chamber_descent_constructed"])
check("source ceiling",not Q["source_charge_or_chamber_selected"])
check("physical ceiling",not Q["positive_physical_pairing_constructed"])
check("protected unchanged",not Q["k1145_k1150_candidate_counts_move"] and not Q["protected_status_change"])
check("ledger unchanged","LEDGER_UNCHANGED" in D["source_and_ledger_effect"])
assert ncheck==21; print("RESULT: PASS 21/21")
