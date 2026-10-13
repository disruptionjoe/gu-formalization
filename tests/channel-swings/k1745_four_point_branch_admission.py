#!/usr/bin/env python3
"""Protected-state and admission controls for K1745."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/"lab/process/k1745-four-point-branch-admission.json").read_text());c=d["bridge_census"];p=d["protected_state"];z=d["decision"]
 checks=[("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1745"),("classification","INTERNAL_STRUCTURAL_ONLY" in d["classification"]),
  ("rows",c["row_count"]==445),("satisfied",c["satisfied_count"]==366),("conditional",c["conditional_count"]==10),
  ("excluded",c["excluded_count"]==65),("missing",c["missing_count"]==4),("new rows",c["new_satisfied_rows"]==["K1741","K1742","K1743","K1744","K1745"]),
  ("protected rows",c["protected_missing_rows"]==["SC-ACT-01","SC-ACT-02","SC-ACT-06","SC-META-53"]),
  ("source",p["source_claims"]=="SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN."),
  ("ledger",p["physics_ledger"]=="33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED"),("candidates","0/7" in p["candidate_counts"]),
  ("canon",not p["canon_change"]),("paper",not p["paper_change"]),("prediction",not p["prediction_or_confirmation"]),("public",not p["public_posture_change"]),
  ("twelfth",z["twelfth_order_fisher_law_proved"]),("half blind",z["q_eleven_halves_blindness_proved"]),("q6 selector",z["q_six_second_order_selector_proved"]),
  ("second jet",z["unique_second_order_chart_jet_proved"]),("boundary",z["rational_interval_boundary_discriminator_proved"]),
  ("branch open",not z["complete_local_branch_identified"]),("finite interval open",not z["finite_strength_fisher_interval_proved"]),
  ("global open",not z["global_two_radius_optimizer_identified"]),("unrestricted open",not z["unrestricted_stationary_lower_bound_proved"]),
  ("physical open",not z["source_owned_physical_theory"]),("next third order","third-order chart freedom" in d["next_condition"]),("next arb","Arb backend" in d["next_condition"])]
 assert len(checks)==29
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
