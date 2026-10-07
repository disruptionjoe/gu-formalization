#!/usr/bin/env python3
"""Composition controls for K1325's braid-normalization admission boundary."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1325-braid-normalization-admission-boundary.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C=D["certificate"]; Q=D["decision"]
check("nineteen rows",C["row_count"]==19)
check("counts close",sum(C[k] for k in ("satisfied_count","excluded_count","conditional_count","missing_count"))==C["row_count"])
check("eight satisfied",C["satisfied_count"]==8)
check("three excluded",C["excluded_count"]==3)
check("two conditional",C["conditional_count"]==2 and len(C["retained_conditional_rows"])==2)
check("six missing",C["missing_count"]==6 and len(C["retained_missing_rows"])==6)
check("new finite row",C["new_row"]=={"row":"finite_D7_sign_braid_normalization","state":"satisfied"})
check("K1319 refined",not Q["K1319_minus_one_phase_is_intrinsic_obstruction"] and Q["sign_only_D7_braid_normalization_constructed"])
check("analytic family absent",not Q["analytic_normalized_intertwiner_family_constructed"])
check("general cocycle open",not Q["general_projective_relator_class_trivialized"])
check("G descent open",not Q["G_equivariant_chamber_descent_constructed"])
check("physical ceiling",not Q["canonical_or_source_selected_chamber_constructed"] and not Q["positive_physical_pairing_constructed"])
check("protected unchanged",not Q["k1145_k1150_candidate_counts_move"] and not Q["protected_status_change"])
assert n==18; print("RESULT: PASS 18/18")
