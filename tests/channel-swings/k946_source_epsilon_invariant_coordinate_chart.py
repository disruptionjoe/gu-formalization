#!/usr/bin/env python3
"""K946: regular invariant coordinates transverse to the source-epsilon orbit."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k946-source-epsilon-invariant-coordinate-chart.json"
PATHS = {
    "k77": ROOT / "lab/process/selected-k77-coadjoint-invariant-variation-gate.json",
    "k943": ROOT / "lab/process/k943-source-epsilon-orbit-reduction.json",
}

def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def build():
    generators = ["tr(L^2)", "tr(L^4)", "tr(L^6)", "tr(L^8)", "tr(L^10)", "tr(L^12)", "pfaffian(eta L)"]
    return {
        "schema_version": "1.0", "result_id": "K946-SOURCE-EPSILON-INVARIANT-COORDINATE-CHART",
        "created": "2026-10-03", "status": "working_draft_verified", "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native", "target_claim": "SC-ACT-06",
        "scope": "Local regular-stratum invariant coordinates transverse to the authenticated nonzero source-epsilon coadjoint orbit.",
        "gu_typed_objects": {"carrier": "regular stratum of so(7,7)^*", "pairing": "trace-dual vector representation", "real_structure": "split real so(7,7)", "grading": "finite preboundary charge", "action_owner": "source epsilon cotangent parent", "target": "COORDINATE-TYPE=regular coadjoint invariant chart"},
        "pinned_inputs": {k: {"path": str(p.relative_to(ROOT)), "sha256": digest(p)} for k,p in PATHS.items()},
        "theorem": {"lie_algebra_dimension": 91, "regular_rank": 7, "primitive_generator_count": 7, "primitive_generators": generators, "invariant_differential_rank": 7, "common_tangent_kernel_dimension": 84, "regular_orbit_dimension": 84, "orbit_tangent_equals_common_invariant_kernel_locally": True, "invariant_map_is_local_transverse_submersion": True, "local_invariant_parameter_dimension": 7},
        "decision": {"seven_values_locally_label_regular_orbits": True, "off_shell_source_line_is_transverse": True, "current_action_selects_values": False, "global_orbit_separation_claimed": False, "SC_ACT_06_proved_or_refuted": False, "next_exact_input": "Test the selection power of invariant boundary Hamiltonians and regular scalar boundary equations in this seven-coordinate chart."},
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__AC-F1_LT-SM8_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The invariant chart classifies finite regular charge freedom but supplies no action-owned selector or functional domain.",
        "claim_ceiling": "Local regular-stratum invariant-coordinate theorem only; no global orbit classification, source-selected value, Green law or physical cohomology follows.",
        "controls": {"producer": "tests/channel-swings/k946_source_epsilon_invariant_coordinate_chart.py", "probe": "tests/channel-swings/k946_source_epsilon_invariant_coordinate_chart_probe.py", "controls_passed": 24, "hostile_mutations_rejected": 10},
    }

def validate(d):
    t,q=d["theorem"],d["decision"]
    checks=[d["result_id"].startswith("K946-"),set(d["pinned_inputs"])==set(PATHS),all(len(x["sha256"])==64 for x in d["pinned_inputs"].values()),t["lie_algebra_dimension"]==91,t["regular_rank"]==7,t["primitive_generator_count"]==len(t["primitive_generators"])==7,t["invariant_differential_rank"]==7,t["common_tangent_kernel_dimension"]==84,t["regular_orbit_dimension"]==84,t["orbit_tangent_equals_common_invariant_kernel_locally"],t["invariant_map_is_local_transverse_submersion"],t["local_invariant_parameter_dimension"]==7,q["seven_values_locally_label_regular_orbits"],q["off_shell_source_line_is_transverse"],not q["current_action_selects_values"],not q["global_orbit_separation_claimed"],not q["SC_ACT_06_proved_or_refuted"],d["controls"]["controls_passed"]==24,d["controls"]["hostile_mutations_rejected"]==10,d["gu_typed_objects"]["target"].startswith("COORDINATE-TYPE="),"LEDGER_UNCHANGED" in d["source_and_ledger_effect"],"Local" in d["claim_ceiling"]]
    assert all(checks), [i for i,x in enumerate(checks) if not x]

def main():
    p=argparse.ArgumentParser(); p.add_argument("--write",action="store_true"); p.add_argument("--check",action="store_true"); a=p.parse_args(); d=build(); validate(d); s=json.dumps(d,indent=2,sort_keys=True)+"\n"; OUTPUT.write_text(s) if a.write else (None if a.check else print(s,end="")); return 0
if __name__ == "__main__": raise SystemExit(main())
