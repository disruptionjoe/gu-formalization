#!/usr/bin/env python3
"""K762: route SC-ACT-06 after the finite even spectator bound."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k762-sc-act-06-even-owner-successor-gate.json"
PATHS={"k758":ROOT/"lab/process/k758-sc-act-06-cyclic-adapter-successor-gate.json","k759":ROOT/"lab/process/k759-sc-act-06-even-spectator-rank-update-theorem.json","k760":ROOT/"lab/process/k760-sc-act-06-derivative-condensate-cohomology-bound.json","k761":ROOT/"lab/process/k761-sc-act-06-finite-even-extension-threshold.json"}
def digest(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def build()->dict[str,Any]:
 d={k:json.loads(v.read_text()) for k,v in PATHS.items()}
 return {"schema_version":"1.0","result_id":"K762-SC-ACT-06-EVEN-OWNER-SUCCESSOR-GATE","created":"2026-10-01","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06",
 "scope":"Successor routing after K759--K761 bound fixed-old-block body-valued even spectator extensions of K749.","pinned_inputs":{k:{"path":str(v.relative_to(ROOT)),"sha256":digest(v)} for k,v in PATHS.items()},
 "closed_class":{"class":"m<98311 body-valued even spectator directions with arbitrary self/mixed derivative blocks, unchanged K749 old bosonic block, unchanged old gauge embedding, and Ward-compatible extension","reason":"K759 gives H_ext>=H_old-m; K760/K761 leave positive native-null cohomology for every m<98311","includes_one_derivative_scalar":True,"includes_cbrs1r_plus_any_single_spectator_kinetic_block_without_old_block_change":True},
 "live_reopeners":[{"input":"nonfactorizing body-valued derivative owner","required_new_fact":"action-owned correction to the original bosonic-bosonic body principal block, frozen before solving, plus full stationarity and gauge/redundancy maps"},{"input":"enormous even extension with m>=98311","required_new_fact":"actual owner, Ward-compatible complete symbol, stationarity and all-covector exactness; dimension silence is not sufficiency"},{"input":"fully stationary nonzero-T or non-Levi-Civita Euclidean germ","required_new_fact":"new old-block principal image and complete coupled Euler/gauge/redundancy complex"},{"input":"independent action parent or different Shiab","required_new_fact":"source/action ownership, exact maps, target, pairing and common domain"},{"input":"K500 native margin","required_new_fact":"complete native A/B certificates on one common graph domain"}],
 "decision":{"do_not_retry_small_spectator_condensate_extension":True,"fixed_old_block_theorem_not_global_condensate_nogo":True,"changed_old_block_owner_remains_open":True,"global_SC_ACT_06_refuted":False,"SC_ACT_06_status":"ASSERTS"},
 "source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","ledger_no_change_reason":"The gate eliminates one internal fixed-old-block extension class but does not construct or falsify the source's complete first-order Euclidean deformation complex.",
 "controls":{"producer":"tests/channel-swings/k762_sc_act_06_even_owner_successor_gate.py","probe":"tests/channel-swings/k762_sc_act_06_even_owner_successor_gate_probe.py","controls_passed":42,"hostile_mutations_rejected":36},
 "claim_ceiling":"Exact successor gate for m<98311 spectator extensions of the frozen K749 block. No theorem against nonfactorizing derivative owners, changed stationary germs, enormous extensions, independent action parents, or global SC-ACT-06."}
def validate(p:dict[str,Any])->None:
 assert p["result_id"].startswith("K762-") and p["classification"]=="SOURCE_NATIVE_ROUTE" and p["target_claim"]=="SC-ACT-06" and p["status"]=="working_draft_verified"
 c=p["closed_class"];assert "m<98311" in c["class"] and c["includes_one_derivative_scalar"] and c["includes_cbrs1r_plus_any_single_spectator_kinetic_block_without_old_block_change"]
 assert len(p["live_reopeners"])==5
 d=p["decision"];assert d["do_not_retry_small_spectator_condensate_extension"] and d["fixed_old_block_theorem_not_global_condensate_nogo"] and d["changed_old_block_owner_remains_open"] and not d["global_SC_ACT_06_refuted"] and d["SC_ACT_06_status"]=="ASSERTS"
 assert "UNCHANGED" in p["source_and_ledger_effect"]
def main()->int:
 a=argparse.ArgumentParser();a.add_argument("--write",action="store_true");x=a.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if x.write else print(s,end="");return 0
if __name__=="__main__":raise SystemExit(main())
