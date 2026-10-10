#!/usr/bin/env python3
"""Certificate for K1655's protected admission."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/"lab/process/k1655-score-saturation-admission.json").read_text());q,z=d["admission"],d["decision"]
 checks=[("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1655"),("N3 remainder","O_(g,eta)(N^3)" in q["quantum_result"]),("positive gap","positive Theta(N^4)" in q["quantum_result"]),("larger amplitude","larger admissible amplitudes" in q["remaining_quantum_gate"]),("physical 0/7","0/7" in q["physical_admission"]),("census","370 rows" in q["bridge_census"] and "291 satisfied" in q["bridge_census"]),("source assertions","SC-ACT-01/02/06 remain ASSERTS" in q["protected_state"]),("ledger counts","33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED" in q["protected_state"]),("scope","Do not promote" in q["scope_guard"]),("classified",z["small_amplitude_family_classified"]),("larger open",z["larger_amplitude_family_open"]),("coefficient open",z["unrestricted_coefficient_open"]),("source protected",not z["source_status_changed"]),("ledger protected",not z["physics_ledger_changed"]),("public protected",not z["canon_or_public_status_changed"])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
