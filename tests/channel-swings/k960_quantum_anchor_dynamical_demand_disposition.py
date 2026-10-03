#!/usr/bin/env python3
"""K960 cross-anchor dynamical-demand and ownership disposition."""
from __future__ import annotations
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k960-quantum-anchor-dynamical-demand-disposition.json"
INPUTS=[ROOT/"lab/process/k956-quantum-anchor-local-dephasing-semigroup.json",ROOT/"lab/process/k957-quantum-anchor-bell-decay.json",ROOT/"lab/process/k958-quantum-anchor-interference-visibility-decay.json",ROOT/"lab/process/k959-quantum-anchor-cross-benchmark-coherence-law.json"]
def build():
 ps=[json.loads(p.read_text()) for p in INPUTS]
 return {
 "schema_version":"1.0","result_id":"K960-QUANTUM-ANCHOR-DYNAMICAL-DEMAND-DISPOSITION","created":"2026-10-03","status":"working_draft_verified","direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL","classification":"INTERNAL_CONDITIONAL_MATHEMATICS",
 "scope":"Disposition of K956--K959 as an observed-to-native causal/dynamical demand derived from the two admitted calibration anchors.",
 "dependency_checks":{"input_ids":[p["result_id"] for p in ps],"all_source_and_ledger_effect_none":all(p["source_and_ledger_effect"]=="none" for p in ps),"all_prediction_or_confirmation_withheld":not ps[0]["ownership"]["prediction_or_confirmation_credit"] and not ps[1]["ownership"]["gu_prediction"] and not ps[2]["ownership"]["gu_interference_prediction"] and ps[3]["discriminator"]["calibration_fit_is_not_held_out_prediction"]},
 "reverse_lineage":{"anchors":["EXT-QM-MASSIVE-MATTER-INTERFERENCE","EXT-QM-SPACELIKE-BELL-NOSIGNAL"],"stage":"causal_dynamical_demand","requirements":["a normalized coherence eigenoperator","a completely positive trace-preserving one-parameter evolution","local nonselective remote-marginal invariance","phase-sensitive recombination","nonfactorizable joint state support","a distinct held-out family before scoring"]},
 "import_accounting":["complex Hilbert state space","tensor composition","Born trace pairing","Bell and path preparations","detector settings and record meaning","external clock and gamma","identification of one candidate law across the compared interfaces"],
 "gu_boundary":{"source_or_action_owned_generator":False,"gu_physical_quotient":False,"gu_positive_state_space":False,"gu_born_pairing":False,"gu_local_net":False,"held_out_prediction_scored":False,"source_claim_moved":False,"physics_ledger_moved":False},
 "decision":{"conditional_cross_anchor_dynamics_constructed":True,"cross_benchmark_relation":"S/sqrt(2)-1=V","bell_threshold":"V>sqrt(2)-1","charged_boundary_or_sc_act_06_result_retracted":False,"next_exact_input":"Derive a local CPTP or appropriately generalized positive evolution on a GU-owned physical quotient, with the coherence eigenoperator, Born/effect pairing and remote-marginal theorem produced by the action/domain rather than imported; then freeze a distinct held-out consequence before scoring."},
 "source_and_ledger_effect":"none","claim_ceiling":"K956--K960 give an exact finite conditional causal/dynamical demand shared by the two calibration anchors. They do not construct a GU action, physical quotient, positive state space, Born rule, local net, empirical common rate, held-out prediction, confirmation or source/ledger/canon/public verdict."
 }
def validate(p):
 d,r,g,q=p["dependency_checks"],p["reverse_lineage"],p["gu_boundary"],p["decision"]
 assert len(d["input_ids"])==4 and d["all_source_and_ledger_effect_none"] and d["all_prediction_or_confirmation_withheld"]
 assert r["stage"]=="causal_dynamical_demand" and len(r["anchors"])==2 and len(r["requirements"])==6
 assert not any(g.values())
 assert q["conditional_cross_anchor_dynamics_constructed"] and q["cross_benchmark_relation"]=="S/sqrt(2)-1=V" and not q["charged_boundary_or_sc_act_06_result_retracted"]
 assert p["source_and_ledger_effect"]=="none"
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);t=json.dumps(p,indent=2,sort_keys=True)+"\n"
 if a.check:assert OUTPUT.read_text()==t
 elif a.write:OUTPUT.write_text(t)
 else:print(t,end="")
 print("K960 controls: 20/20")
if __name__=="__main__":main()
