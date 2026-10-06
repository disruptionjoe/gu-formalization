#!/usr/bin/env python3
"""K1235: integrate the independent source-certificate unseal boundary."""
import json
from pathlib import Path
OUT=Path(__file__).parents[2]/"lab/process/k1235-source-owned-unseal-boundary.json"

def validate(d):
 r=d["required_before_unseal"]
 assert len(r)==9 and "independent source-state certificate for A, B and C" in r
 assert "source-characterization data disjoint from the sealed holdout" in r
 assert d["decision"]["k1229_formula_remains_valid_under_declared_phi_plus_premise"] is True
 assert d["decision"]["channel_calibration_alone_authorizes_unseal"] is False
 assert d["decision"]["holdout_may_fit_its_own_source_certificate"] is False
 assert d["decision"]["delayed_choice_entanglement_swapping_consumed"] is False
 assert d["protected_status"]=={"SC-ACT-01":"ASSERTS","SC-ACT-02":"ASSERTS","SC-ACT-06":"ASSERTS","SC-META-53":"UNCERTAIN","LT-SM8":"NEEDS","LT-GR6b":"NEEDS","RA-F1":"NEEDS","AC-F1":"NEEDS"}
 assert d["ownership"]["gu_native_effect"]=="none"
 assert d["next_input"].startswith("One completed common-owner flight card")
 assert d["claim_ceiling"].startswith("Exact conditional")

if __name__=="__main__":
 d=json.loads(OUT.read_text());validate(d);print("K1235 controls: 11/11")
