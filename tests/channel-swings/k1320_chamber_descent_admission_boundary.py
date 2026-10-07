#!/usr/bin/env python3
"""Exact controls for K1320's chamber-descent admission boundary."""
import collections,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1320-chamber-descent-admission-boundary.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C=D["certificate"]; Q=D["decision"]; z=collections.Counter(r["state"] for r in C["rows"])
check("row count",C["row_count"]==len(C["rows"])==18)
check("satisfied",z["satisfied"]==C["satisfied_count"]==7)
check("excluded",z["excluded"]==C["excluded_count"]==3)
check("conditional",z["conditional"]==C["conditional_count"]==2)
check("missing",z["missing"]==C["missing_count"]==6)
check("raw average satisfied",Q["raw_chamber_multiplicity_has_canonical_Hilbert_projection"])
check("G descent absent",not Q["G_equivariant_chamber_descent_constructed"])
check("analytic family absent",not Q["analytic_normalized_intertwiner_family_constructed"])
check("phase not harmless",not Q["projective_relator_phase_is_harmless"])
check("chamber not selected",not Q["canonical_or_source_selected_chamber_constructed"])
check("physical and protected unchanged",not Q["positive_physical_pairing_constructed"] and not Q["k1145_k1150_candidate_counts_move"] and not Q["protected_status_change"] and "LEDGER_UNCHANGED" in D["source_and_ledger_effect"])
assert n==16; print("RESULT: PASS 16/16")
