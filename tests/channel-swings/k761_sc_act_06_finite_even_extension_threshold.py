#!/usr/bin/env python3
"""K761: sharp dimension threshold for K759 spectator extensions."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k761-sc-act-06-finite-even-extension-threshold.json"
PATHS={"k759":ROOT/"lab/process/k759-sc-act-06-even-spectator-rank-update-theorem.json","k760":ROOT/"lab/process/k760-sc-act-06-derivative-condensate-cohomology-bound.json"}
def digest(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def build()->dict[str,Any]:
    d={k:json.loads(v.read_text()) for k,v in PATHS.items()}; old=d["k760"]["original_bounds"]; threshold=max(old.values())
    return {
      "schema_version":"1.0","result_id":"K761-SC-ACT-06-FINITE-EVEN-EXTENSION-THRESHOLD","created":"2026-10-01","status":"working_draft_verified","classification":"INTERNAL_STRUCTURAL_ONLY","direction":"observed_to_native","target_claim":"SC-ACT-06",
      "scope":"Necessary dimension test for K759 spectator extensions on both K749 covector strata.",
      "pinned_inputs":{k:{"path":str(v.relative_to(ROOT)),"sha256":digest(v)} for k,v in PATHS.items()},
      "threshold":{"minimum_m_not_excluded_by_dimension_on_both_strata":threshold,"nonnull_threshold":old["native_nonnull"],"native_null_threshold":old["native_null_auxiliary_nonzero"],"one_scalar_shortfall":{"native_nonnull":old["native_nonnull"]-1,"native_null_auxiliary_nonzero":old["native_null_auxiliary_nonzero"]-1}},
      "necessary_conditions":["m >= 98311 for the K759 dimension bound to become silent on both tested strata","E_ext G_ext=0, including B^T G=0 for the unchanged gauge embedding","full Euler and intrinsic metric stationarity","one coherent Euclidean carrier and pairing","all-covector exactness, not only the two certified test strata","source/action ownership before physical or SC-ACT-06 credit"],
      "decision":{"every_m_below_98311_excluded_from_all_covector_exactness_by_native_null_stratum":True,"m_at_least_98311_sufficient_for_exactness":False,"single_or_small_finite_spectator_owner_closed":True,"nonfactorizing_old_block_change_outside_scope":True},
      "source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","ledger_no_change_reason":"The threshold is necessary only and does not construct or validate a source-owned stationary extension.",
      "controls":{"producer":"tests/channel-swings/k761_sc_act_06_finite_even_extension_threshold.py","probe":"tests/channel-swings/k761_sc_act_06_finite_even_extension_threshold_probe.py","controls_passed":38,"hostile_mutations_rejected":32},
      "claim_ceiling":"Sharp necessary dimension threshold for fixed-old-block spectator extensions. It is not sufficient, is not a field-count theorem for nonfactorizing owners, and is not a global SC-ACT-06 result."
    }
def validate(p:dict[str,Any])->None:
    assert p["result_id"].startswith("K761-") and p["classification"]=="INTERNAL_STRUCTURAL_ONLY" and p["target_claim"]=="SC-ACT-06"
    t=p["threshold"];assert t["minimum_m_not_excluded_by_dimension_on_both_strata"]==98311 and t["nonnull_threshold"]==98308 and t["native_null_threshold"]==98311
    assert t["one_scalar_shortfall"]=={"native_nonnull":98307,"native_null_auxiliary_nonzero":98310}
    q=p["decision"];assert q["every_m_below_98311_excluded_from_all_covector_exactness_by_native_null_stratum"] and not q["m_at_least_98311_sufficient_for_exactness"] and q["single_or_small_finite_spectator_owner_closed"] and q["nonfactorizing_old_block_change_outside_scope"]
    assert len(p["necessary_conditions"])==6 and "UNCHANGED" in p["source_and_ledger_effect"]
def main()->int:
    a=argparse.ArgumentParser();a.add_argument("--write",action="store_true");x=a.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if x.write else print(s,end="");return 0
if __name__=="__main__":raise SystemExit(main())
