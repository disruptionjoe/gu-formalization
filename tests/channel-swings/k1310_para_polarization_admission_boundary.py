#!/usr/bin/env python3
"""Exact controls for K1310's para-polarization admission boundary."""
import hashlib,json,collections
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1310-para-polarization-admission-boundary.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C=D["certificate"]; Q=D["decision"]; counts=collections.Counter(r["state"] for r in C["rows"])
check("row count",C["row_count"]==len(C["rows"] )==14)
check("satisfied",counts["satisfied"]==C["satisfied_count"]==5)
check("excluded",counts["excluded"]==C["excluded_count"]==2)
check("conditional",counts["conditional"]==C["conditional_count"]==1)
check("missing",counts["missing"]==C["missing_count"]==6)
check("horn refined",Q["k1304_noninvariant_polarization_horn_refined"])
check("real polarization",Q["invariant_real_polarization_exists"])
check("no positive Kahler",not Q["invariant_complex_or_positive_kahler_polarization_exists"])
check("neutral not physical",not Q["neutral_para_geometry_resolves_physical_positivity"])
check("not source selected",not Q["charge_or_chamber_selected_by_source"])
check("counts unchanged",not Q["k1145_k1150_candidate_counts_move"])
check("status unchanged",not Q["protected_status_change"])
assert n==18; print("RESULT: PASS 18/18")
