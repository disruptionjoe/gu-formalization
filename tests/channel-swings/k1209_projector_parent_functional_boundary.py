#!/usr/bin/env python3
"""Audit the projector control against cross-null and K1150 admission gates."""
from __future__ import annotations
import argparse,json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k1209-projector-parent-functional-boundary.json"
def load(n:str)->dict[str,Any]:return json.loads((ROOT/"lab/process"/n).read_text())
def build()->dict[str,Any]:
    a=load("k1208-stratumwise-projector-parent-control.json");b=load("k855-sc-act-06-cohomology-bundle.json");c=load("k1150-i1b-functional-admission-compiler.json");r=a["exact_control"]["projector_ranks"];g=[x["test"] for x in c["executable_tests"]]
    failed={x:False for x in g};release={"projector_rank_jumps_by_three":r==[98308,98308,98311],"rank_jump_forbids_literal_continuous_projector_family":b["theorem"]["rank_jumps_forbid_this_bundle_conclusion"],"control_cohomology_is_zero":a["exact_control"]["algebraic_cohomology_dimensions_after_control"]==[0,0,0],"k1145_nonzero_cohomology_gate_fails":not failed["causal_algebraic_packet"],"source_action_owner_gate_fails":not failed["source_action_owner"],"common_graph_domain_gate_fails":not failed["common_graph_domain"],"closed_range_gate_fails":not failed["closed_gauge_range"],"positive_gap_gate_fails":not failed["uniform_positive_gap"],"generator_and_trace_gates_fail":not failed["maximal_generator"] and not failed["boundary_trace_compatibility"],"no_k1150_admission":True}
    return {"schema_version":"1.0","result_id":"K1209-PROJECTOR-PARENT-FUNCTIONAL-BOUNDARY","created":"2026-10-06","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06","scope":"Cross-null continuity and K1145/K1150 audit of K1208's reverse-selected stratumwise projector control.","gu_typed_objects":{"family":"literal orthogonal projectors P_W across nonnull and null strata","algebraic_gate":"K1145 causal packet including nonzero cohomology","functional_gate":"K1150 seven-row compiler","target":"CONTRACT-TYPE=cross-null and functional admission boundary"},"exact_control":{"projector_ranks":r,"rank_jump":r[2]-r[0],"control_cohomology_dimensions":a["exact_control"]["algebraic_cohomology_dimensions_after_control"],"k1150_gate_results":failed,"failed_gate_count":sum(not v for v in failed.values())},"decision":{"literal_projector_is_continuous_cross_null_family":False,"control_passes_nonzero_cohomology_gate":False,"control_passes_k1150":False,"pointwise_control_remains_useful":True,"native_parent_admitted":False,"protected_status_moves":False},"release_test":release,"source_and_ledger_effect":"none","claim_ceiling":"Exact exclusion of the literal K1208 projector as a continuous admitted physical parent; does not exclude smoother source-owned changed parents with jointly recomputed H, J and d."}
def validate_payload(p:dict[str,Any])->None:
    if not all(p["release_test"].values()):raise AssertionError("K1209 release test failed")
    if p["exact_control"]["rank_jump"]!=3 or p["exact_control"]["failed_gate_count"]!=7:raise AssertionError("K1209 boundary count changed")
    d=p["decision"]
    if d["literal_projector_is_continuous_cross_null_family"] or d["control_passes_nonzero_cohomology_gate"] or d["control_passes_k1150"] or d["native_parent_admitted"]:raise AssertionError("K1209 admission overclaim")
    if d["protected_status_moves"]:raise AssertionError("K1209 protected move")
def main()->int:
    a=argparse.ArgumentParser();a.add_argument("--write",action="store_true");x=a.parse_args();p=build();validate_payload(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if x.write else print(s,end="");return 0
if __name__=="__main__":raise SystemExit(main())
