#!/usr/bin/env python3
"""Exact controls for K1315's principal-series admission boundary."""
import collections,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1315-principal-series-admission-boundary.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C=D["certificate"]; Q=D["decision"]; z=collections.Counter(r["state"] for r in C["rows"])
check("row count",C["row_count"]==len(C["rows"])==17)
check("satisfied",z["satisfied"]==C["satisfied_count"]==6)
check("excluded",z["excluded"]==C["excluded_count"]==3)
check("conditional",z["conditional"]==C["conditional_count"]==2)
check("missing",z["missing"]==C["missing_count"]==6)
check("mathematical Hilbert control",Q["positive_mathematical_Hilbert_control_constructed"])
check("physical pairing absent",not Q["positive_physical_pairing_constructed"])
check("charge remains continuous",not Q["prequantization_selects_or_discretizes_mu"])
check("chamber remains unselected",not Q["canonical_or_source_selected_chamber_constructed"])
check("candidate counts unchanged",not Q["k1145_k1150_candidate_counts_move"])
check("protected status unchanged",not Q["protected_status_change"])
check("ledger unchanged","LEDGER_UNCHANGED" in D["source_and_ledger_effect"])
assert n==16; print("RESULT: PASS 16/16")
