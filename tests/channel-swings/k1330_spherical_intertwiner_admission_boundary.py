#!/usr/bin/env python3
"""Composition controls for K1330's spherical analytic boundary."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1330-spherical-intertwiner-admission-boundary.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C=D["certificate"]; Q=D["decision"]
check("twenty rows",C["row_count"]==20)
check("counts close",sum(C[k] for k in ("satisfied_count","excluded_count","conditional_count","missing_count"))==C["row_count"])
check("nine satisfied",C["satisfied_count"]==9)
check("three excluded",C["excluded_count"]==3)
check("two conditional",C["conditional_count"]==2 and len(C["retained_conditional_rows"])==2)
check("six missing",C["missing_count"]==6 and len(C["retained_missing_rows"])==6)
check("new spherical row",C["new_row"]=={"row":"analytic_spherical_line_normalization","state":"satisfied"})
check("spherical analytics",Q["rank_one_spherical_coefficient_constructed"] and Q["spherical_meromorphic_divisor_classified"] and Q["spherical_line_D7_coxeter_flat"])
check("full operator absent",not Q["full_analytic_normalized_intertwiner_family_constructed"] and not Q["operator_k_type_and_reducibility_control_constructed"])
check("G descent open",not Q["G_equivariant_full_chamber_descent_constructed"])
check("physical ceiling",not Q["canonical_or_source_selected_chamber_constructed"] and not Q["positive_physical_pairing_constructed"])
check("protected unchanged",not Q["k1145_k1150_candidate_counts_move"] and not Q["protected_status_change"])
check("ledger unchanged","LEDGER_UNCHANGED" in D["source_and_ledger_effect"])
assert n==18; print("RESULT: PASS 18/18")
