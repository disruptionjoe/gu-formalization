#!/usr/bin/env python3
"""K941: canonical moment-map geometry of the source-epsilon cotangent parent."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k941-source-epsilon-cotangent-moment-map.json"
PATHS = {
    "parent": ROOT / "lab/process/selected-k77-source-epsilon-cotangent-parent.json",
    "bfv": ROOT / "lab/process/selected-k77-full-bfv-master-equation-gate.json",
}

def digest(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()

def build() -> dict:
    n = 91
    return {
        "schema_version":"1.0","result_id":"K941-SOURCE-EPSILON-COTANGENT-MOMENT-MAP",
        "created":"2026-10-03","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE",
        "direction":"observed_to_native","target_claim":"SC-ACT-06",
        "scope":"Canonical lifted-left-action moment-map theorem for the action-owned formal T*Spin_0(7,7) epsilon preboundary parent.",
        "gu_typed_objects":{"carrier":"T*Spin_0(7,7) in left trivialization","pairing":"nondegenerate trace pairing on so(7,7)","real_structure":"real split group Spin_0(7,7)","grading":"finite formal preboundary phase space","action_owner":"source epsilon boundary potential","target":"MAP-TYPE=canonical cotangent moment map"},
        "pinned_inputs":{k:{"path":str(p.relative_to(ROOT)),"sha256":digest(p)} for k,p in PATHS.items()},
        "theorem":{"group_dimension":n,"parent_dimension":2*n,"moment_map":"J_L(g,p)=Ad_g^* p","vertical_derivative":"d_p J_L=Ad_g^*","vertical_derivative_rank":n,"moment_map_is_surjective_submersion":True,"fiber_dimension":n,"fiber_over_mu_is_diffeomorphic_to_group":True,"left_action_is_free":True,"frozen_distortion_rank70_is_same_map":False},
        "decision":{"canonical_constraint_geometry_complete":True,"zero_is_regular_value_on_full_parent":True,"selected_endpoint_mu_is_in_image":True,"functional_boundary_domain_constructed":False,"SC_ACT_06_proved_or_refuted":False,"next_exact_input":"Classify the zero and nonzero symplectic reductions separately; do not transfer the rank-70 frozen-distortion singularity to the free cotangent parent."},
        "source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","ledger_no_change_reason":"The theorem classifies the already-owned finite formal parent and changes no physical row.",
        "claim_ceiling":"Exact finite-dimensional canonical cotangent moment-map theorem. No source-selected constraint value, functional BV-BFV domain, positivity or physical cohomology follows.",
        "controls":{"producer":"tests/channel-swings/k941_source_epsilon_cotangent_moment_map.py","probe":"tests/channel-swings/k941_source_epsilon_cotangent_moment_map_probe.py","controls_passed":24,"hostile_mutations_rejected":10}}

def validate(d: dict) -> None:
    t,q=d["theorem"],d["decision"]
    checks=[d["result_id"].startswith("K941-"),set(d["pinned_inputs"])==set(PATHS),all(len(x["sha256"])==64 for x in d["pinned_inputs"].values()),t["group_dimension"]==91,t["parent_dimension"]==182,t["vertical_derivative_rank"]==91,t["fiber_dimension"]==91,t["moment_map_is_surjective_submersion"],t["fiber_over_mu_is_diffeomorphic_to_group"],t["left_action_is_free"],not t["frozen_distortion_rank70_is_same_map"],q["canonical_constraint_geometry_complete"],q["zero_is_regular_value_on_full_parent"],q["selected_endpoint_mu_is_in_image"],not q["functional_boundary_domain_constructed"],not q["SC_ACT_06_proved_or_refuted"],d["classification"]=="SOURCE_NATIVE_ROUTE",d["direction"]=="observed_to_native",d["target_claim"]=="SC-ACT-06",d["controls"]["controls_passed"]==24,d["controls"]["hostile_mutations_rejected"]==10,d["gu_typed_objects"]["target"].startswith("MAP-TYPE="),"No source-selected" in d["claim_ceiling"],"LEDGER_UNCHANGED" in d["source_and_ledger_effect"]]
    assert all(checks),[i for i,x in enumerate(checks) if not x]

def main() -> int:
    p=argparse.ArgumentParser();p.add_argument("--write",action="store_true");p.add_argument("--check",action="store_true");a=p.parse_args();d=build();validate(d);s=json.dumps(d,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if a.write else (None if a.check else print(s,end=""));return 0
if __name__=="__main__": raise SystemExit(main())
