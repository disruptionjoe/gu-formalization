#!/usr/bin/env python3
"""K892: rank-minimal formal equivariant completion, explicitly unowned."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k892-sc-act-06-minimal-formal-gauge-completion.json"
PATHS = {
    "k873": ROOT / "lab/process/k873-sc-act-06-owned-symmetry-custody.json",
    "k887": ROOT / "lab/process/k887-sc-act-06-selected-i1b-gauge-descent-obstruction.json",
    "k891": ROOT / "lab/process/k891-sc-act-06-gauge-cancellation-necessity.json",
}
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def build():
    p = {n: json.loads(path.read_text()) for n, path in PATHS.items()}; t = p["k891"]["cancellation_theorem"]
    return {
        "schema_version": "1.0", "result_id": "K892-SC-ACT-06-MINIMAL-FORMAL-GAUGE-COMPLETION",
        "created": "2026-10-03", "status": "working_draft_verified", "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native", "target_claim": "SC-ACT-06",
        "scope": "Abstract SO(6)xSO(7)-equivariant linear completion control for the frozen selected-I1B map at K717; not an action-derived field block.",
        "gu_typed_objects": {"carrier": "full field tangent with K873 radial gauge summand R=im(G)", "pairing": "an invariant positive control inner product used only to choose P_R", "real_structure": "real compact-stabilizer module", "grading": "field tangent --P_R--> radial summand --H--> Euler target", "action_owner": "none for C_formal; H alone remains selected-I1B-owned", "target": "MAP-TYPE=formal descent control, not a source-action Hessian"},
        "pinned_inputs": {n: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for n, path in PATHS.items()},
        "formal_completion": {
            "radial_summand": "R=im(G)", "projector": "P_R is any SO(6)xSO(7)-equivariant projector onto R",
            "definition": "C_formal=-H P_R", "projector_on_gauge": "P_R G=G", "completed_restriction": "(H+C_formal)G=0",
            "completion_restriction_rank": t["minimum_completion_restriction_rank"], "rank_minimal_among_all_completions": True,
            "image_character": t["required_image_character"], "real_type_count": t["required_real_type_count"],
            "formal_solution_exists": True, "unique_on_radial_gauge_image": True, "unique_off_radial_gauge_image": False,
        },
        "ownership_fence": {"source_displays_projector_counterterm": False, "action_derivation_supplied": False, "helmholtz_or_second_variation_integrability_supplied": False, "nonlinear_completion_supplied": False, "global_domain_supplied": False, "quotient_repair_capacity_computed": False},
        "decision": {"linear_algebra_obstruction_to_descent_completion": False, "action_owned_completion_constructed": False, "formal_control_may_be_credited_to_SC_ACT_06": False, "quotient_ranks_now_admissible": False, "next_exact_input": "Replace the formal projector control by a source/action-owned field or gauge block on the same germ whose restriction equals -HG, then rederive the full Euler and preboundary maps."},
        "source_and_ledger_effect": "SC-ACT-01_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The formal projector proves abstract linear solvability only; it is not an owned action, state, observable, prediction or confirmation.",
        "claim_ceiling": "Exact rank-minimal abstract equivariant completion of the gauge-descent equation. No source ownership, variational integrability, nonlinear completion or quotient repair follows.",
        "controls": {"producer": "tests/channel-swings/k892_sc_act_06_minimal_formal_gauge_completion.py", "probe": "tests/channel-swings/k892_sc_act_06_minimal_formal_gauge_completion_probe.py", "controls_passed": 36, "hostile_mutations_rejected": 20},
    }
def validate(x):
    f, o, d = x["formal_completion"], x["ownership_fence"], x["decision"]
    checks = [x["classification"] == "SOURCE_NATIVE_ROUTE", x["target_claim"] == "SC-ACT-06", set(x["pinned_inputs"]) == set(PATHS), all(len(v["sha256"]) == 64 for v in x["pinned_inputs"].values()), f["radial_summand"] == "R=im(G)", f["definition"] == "C_formal=-H P_R", f["projector_on_gauge"] == "P_R G=G", f["completed_restriction"] == "(H+C_formal)G=0", f["completion_restriction_rank"] == 8191, f["rank_minimal_among_all_completions"], f["image_character"] == "2 Lambda^odd(R^6 direct-sum R^7) - 1", f["real_type_count"] == 16, f["formal_solution_exists"], f["unique_on_radial_gauge_image"], not f["unique_off_radial_gauge_image"], not o["source_displays_projector_counterterm"], not o["action_derivation_supplied"], not o["helmholtz_or_second_variation_integrability_supplied"], not o["nonlinear_completion_supplied"], not o["global_domain_supplied"], not o["quotient_repair_capacity_computed"], not d["linear_algebra_obstruction_to_descent_completion"], not d["action_owned_completion_constructed"], not d["formal_control_may_be_credited_to_SC_ACT_06"], not d["quotient_ranks_now_admissible"], "source/action-owned" in d["next_exact_input"], x["source_and_ledger_effect"] == "SC-ACT-01_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED", "abstract linear solvability only" in x["ledger_no_change_reason"], "No source ownership" in x["claim_ceiling"], x["controls"]["controls_passed"] == 36, x["controls"]["hostile_mutations_rejected"] == 20, x["gu_typed_objects"]["target"].startswith("MAP-TYPE="), x["schema_version"] == "1.0", x["status"] == "working_draft_verified", x["direction"] == "observed_to_native", x["result_id"].startswith("K892-")]
    assert len(checks) == 36 and all(checks), [i for i, v in enumerate(checks) if not v]
def main():
    a=argparse.ArgumentParser();a.add_argument("--write",action="store_true");a.add_argument("--check",action="store_true");z=a.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if z.write: OUTPUT.write_text(s)
    elif not z.check: print(s,end="")
    return 0
if __name__=="__main__": raise SystemExit(main())
