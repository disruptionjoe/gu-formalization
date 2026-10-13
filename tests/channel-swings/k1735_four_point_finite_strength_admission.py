#!/usr/bin/env python3
"""Protected-state and admission controls for K1735."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/"lab/process/k1735-four-point-finite-strength-admission.json").read_text());c=d["bridge_census"];p=d["protected_state"];z=d["decision"]
 checks=[("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1735"),("classification","NUMERICAL" in d["classification"]),
  ("rows",c["row_count"]==435),("sum",c["satisfied_count"]+c["conditional_count"]+c["excluded_count"]+c["missing_count"]==435),
  ("new rows",c["new_satisfied_rows"]==["K1731","K1732","K1733","K1734","K1735"]),("missing",len(c["protected_missing_rows"])==4),
  ("source","ASSERTS" in p["source_claims"] and "UNCERTAIN" in p["source_claims"]),("ledger","33 SAME" in p["physics_ledger"]),
  ("counts","0/7" in p["candidate_counts"]),("canon",not p["canon_change"]),("paper",not p["paper_change"]),
  ("prediction",not p["prediction_or_confirmation"]),("public",not p["public_posture_change"]),
  ("chart",z["complete_two_radius_chart_proved"]),("tangent",z["quartic_tangent_degeneracy_proved"]),
  ("computed",z["finite_strength_candidate_branch_computed"]),("finite open",not z["exact_finite_strength_optimizer_identified"]),
  ("lower open",not z["unrestricted_stationary_lower_bound_proved"]),("physical open",not z["source_owned_physical_theory"]),
  ("no status",not z["protected_status_change"]),("next coefficient","post-quartic" in d["next_condition"]),
  ("next singular","singular" in d["next_condition"]),("next Haar","Haar" in d["next_condition"])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
