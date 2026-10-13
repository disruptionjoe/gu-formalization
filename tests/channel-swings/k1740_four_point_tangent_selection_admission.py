#!/usr/bin/env python3
"""Protected-state and admission controls for K1740."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/"lab/process/k1740-four-point-tangent-selection-admission.json").read_text());c=d["bridge_census"];p=d["protected_state"];z=d["decision"]
 checks=[("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1740"),("classification","INTERNAL_STRUCTURAL_ONLY" in d["classification"]),
  ("rows",c["row_count"]==440),("satisfied",c["satisfied_count"]==361),("conditional",c["conditional_count"]==10),
  ("excluded",c["excluded_count"]==65),("missing",c["missing_count"]==4),("new rows",c["new_satisfied_rows"]==["K1736","K1737","K1738","K1739","K1740"]),
  ("protected rows",c["protected_missing_rows"]==["SC-ACT-01","SC-ACT-02","SC-ACT-06","SC-META-53"]),
  ("source",p["source_claims"]=="SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN."),
  ("ledger",p["physics_ledger"]=="33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED"),("candidates","0/7" in p["candidate_counts"]),
  ("canon",not p["canon_change"]),("paper",not p["paper_change"]),("prediction",not p["prediction_or_confirmation"]),("public",not p["public_posture_change"]),
  ("tenth",z["tenth_order_fisher_law_proved"]),("half",z["q_nine_halves_cancellation_proved"]),("tangent",z["unique_leading_chart_tangent_proved"]),
  ("regression",z["finite_channel_regression_computed"]),("branch open",not z["complete_local_branch_identified"]),("global open",not z["exact_finite_strength_optimizer_identified"]),
  ("next","remaining second-order chart freedom" in d["next_condition"])]
 assert len(checks)==24
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
