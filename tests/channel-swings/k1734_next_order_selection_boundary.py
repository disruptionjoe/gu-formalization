#!/usr/bin/env python3
"""Boundary and next-calculation controls for K1734."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/"lab/process/k1734-next-order-selection-boundary.json").read_text());b=d["boundary"];e=d["excluded_promotions"]
 checks=[("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1734"),
  ("rank","one affine constraint" in b["rank_defect"]),("null","null direction" in b["rank_defect"]),
  ("not selected","determines the exact" in b["consequence"]),("beyond t8","beyond t^8" in b["required_next_calculation"]),
  ("second order","second-order" in b["required_next_calculation"]),("locator","candidate branch" in b["finite_grid_role"]),
  ("not proof","not the coefficient proof" in b["finite_grid_role"]),("finite excluded","exact finite-strength optimizer" in e),
  ("two radius excluded","global two-radius uniqueness" in e),("all seed excluded","all-seed infimum" in e),
  ("singular excluded","growing-support or vanishing-defect exclusion" in e),
  ("stationary excluded","unrestricted stationary lower bound" in e),("physical excluded","source-owned physical state" in e),
  ("not no-go","not a no-go theorem" in d["scope_guard"])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
