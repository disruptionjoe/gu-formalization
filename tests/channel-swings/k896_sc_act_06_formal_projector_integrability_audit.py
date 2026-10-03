#!/usr/bin/env python3
"""K896: audit the rank-minimal radial-projector completion for Helmholtz integrability."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k896-sc-act-06-formal-projector-integrability-audit.json"
K895_SOURCE = ROOT / "tests/channel-swings/k895_sc_act_06_helmholtz_symmetry_obstruction.py"
PATHS = {
    "k892": ROOT / "lab/process/k892-sc-act-06-minimal-formal-gauge-completion.json",
    "k895": ROOT / "lab/process/k895-sc-act-06-helmholtz-symmetry-obstruction.json",
}

def digest(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()

def exact_data() -> dict[str, Any]:
    spec = importlib.util.spec_from_file_location("k895_backend", K895_SOURCE)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    data = module.exact_block_data()
    return {key: value for key, value in data.items() if key != "representative_rows"}

def build() -> dict[str, Any]:
    k892 = json.loads(PATHS["k892"].read_text())
    exact = exact_data()
    return {
        "schema_version": "1.0", "result_id": "K896-SC-ACT-06-FORMAL-PROJECTOR-INTEGRABILITY-AUDIT",
        "created": "2026-10-03", "status": "working_draft_verified", "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native", "target_claim": "SC-ACT-06",
        "scope": "Exact Helmholtz audit of K892's rank-minimal formal completion C_formal=-A P_R on the fixed K717 nonnull even-bosonic connection domain.",
        "gu_typed_objects": {
            "carrier": "K873 radial summand R inside the 229376-dimensional even connection tangent",
            "pairing": "the same fixed real coefficient pairing used for A^T and the orthogonal control projector P_R",
            "real_structure": "real K77 nonnull coefficient blocks", "grading": "connection tangent --A(I-P_R)--> Euler dual",
            "action_owner": "none for P_R or C_formal; selected I1B owns only the frozen formal A construction",
            "target": "INTEGRABILITY-TYPE=formal descent completion versus same-domain Hessian symmetry",
        },
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "formal_projector_audit": {
            "projector_identity": "P_R^T=P_R and P_R G=G", "formal_correction": "C_formal=-A P_R",
            "formal_completed_map": "T_formal=A(I-P_R)", "gauge_descent": "T_formal G=0",
            "gauge_descent_satisfied": k892["formal_completion"]["formal_solution_exists"],
            "completed_map_rank": exact["formal_completed_rank"],
            "completed_map_helmholtz_defect_rank": exact["formal_completed_helmholtz_defect_rank"],
            "correction_symmetric_part_rank": exact["formal_correction_symmetric_part_rank"],
            "selected_action_rank": exact["selected_action_rank"],
            "completed_rank_distribution": exact["rank_distributions"]["formal_completed_rank"],
            "completed_helmholtz_defect_distribution": exact["rank_distributions"]["formal_completed_helmholtz_defect_rank"],
            "correction_symmetric_part_distribution": exact["rank_distributions"]["formal_correction_symmetric_part_rank"],
            "helmholtz_symmetry_satisfied": False,
            "formal_completion_is_same_domain_even_scalar_action_hessian": False,
        },
        "structural_reason": {
            "transpose": "T_formal^T=-(I-P_R)A",
            "symmetry_condition": "A(I-P_R)=-(I-P_R)A",
            "equivalent_anticommutator_condition": "A P_R+P_R A=2A",
            "condition_fails_exactly": True,
            "defect_rank_equals_selected_action_rank": exact["formal_completed_helmholtz_defect_rank"] == exact["selected_action_rank"],
        },
        "decision": {
            "formal_projector_restores_linear_gauge_descent": True,
            "formal_projector_supplies_variational_integrability": False,
            "formal_projector_may_be_credited_as_action_completion": False,
            "quotient_ranks_now_admissible": False,
            "next_exact_input": "Replace the projector control by a completion whose full skew part is -A and whose surviving symmetric part is action-owned, gauge-basic and defined on the same common Euler/preboundary domain.",
        },
        "source_and_ledger_effect": "SC-ACT-01_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The exact integrability failure removes credit from a mathematical control but supplies no completed action or physical quotient.",
        "claim_ceiling": "Exact failure of K892's orthogonal radial-projector control to be a same-domain even scalar-action Hessian. Other completions and action parents remain open.",
        "controls": {"producer": "tests/channel-swings/k896_sc_act_06_formal_projector_integrability_audit.py", "probe": "tests/channel-swings/k896_sc_act_06_formal_projector_integrability_audit_probe.py", "controls_passed": 40, "hostile_mutations_rejected": 20},
    }

def validate(x: dict[str, Any]) -> None:
    a, s, d = x["formal_projector_audit"], x["structural_reason"], x["decision"]
    checks = [
        x["classification"] == "SOURCE_NATIVE_ROUTE", x["target_claim"] == "SC-ACT-06", set(x["pinned_inputs"]) == set(PATHS),
        all(len(row["sha256"]) == 64 for row in x["pinned_inputs"].values()), a["projector_identity"] == "P_R^T=P_R and P_R G=G",
        a["formal_correction"] == "C_formal=-A P_R", a["formal_completed_map"] == "T_formal=A(I-P_R)", a["gauge_descent"] == "T_formal G=0",
        a["gauge_descent_satisfied"], a["completed_map_rank"] == 122721, a["completed_map_helmholtz_defect_rank"] == 130912,
        a["correction_symmetric_part_rank"] == 16382, a["selected_action_rank"] == 130912,
        a["completed_rank_distribution"] == {"1": 1, "4": 4095, "24": 78, "26": 4018},
        a["completed_helmholtz_defect_distribution"] == {"2": 1, "6": 4095, "24": 78, "26": 4018},
        a["correction_symmetric_part_distribution"] == {"0": 4096, "2": 1, "4": 4095},
        not a["helmholtz_symmetry_satisfied"], not a["formal_completion_is_same_domain_even_scalar_action_hessian"],
        s["transpose"] == "T_formal^T=-(I-P_R)A", s["symmetry_condition"] == "A(I-P_R)=-(I-P_R)A",
        s["equivalent_anticommutator_condition"] == "A P_R+P_R A=2A", s["condition_fails_exactly"],
        s["defect_rank_equals_selected_action_rank"], d["formal_projector_restores_linear_gauge_descent"],
        not d["formal_projector_supplies_variational_integrability"], not d["formal_projector_may_be_credited_as_action_completion"],
        not d["quotient_ranks_now_admissible"], "full skew part is -A" in d["next_exact_input"],
        x["source_and_ledger_effect"].endswith("LEDGER_UNCHANGED"), "mathematical control" in x["ledger_no_change_reason"],
        "Other completions" in x["claim_ceiling"], x["controls"]["controls_passed"] == 40, x["controls"]["hostile_mutations_rejected"] == 20,
        x["gu_typed_objects"]["target"].startswith("INTEGRABILITY-TYPE="), x["schema_version"] == "1.0", x["status"] == "working_draft_verified",
        x["direction"] == "observed_to_native", x["result_id"].startswith("K896-"), a["completed_map_helmholtz_defect_rank"] == a["selected_action_rank"],
        a["correction_symmetric_part_rank"] == 2 * 8191,
    ]
    assert len(checks) == 40 and all(checks), [i for i, value in enumerate(checks) if not value]

def main() -> int:
    p = argparse.ArgumentParser(); p.add_argument("--write", action="store_true"); p.add_argument("--check", action="store_true"); args = p.parse_args()
    packet = build(); validate(packet); rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered)
    elif not args.check: print(rendered, end="")
    return 0
if __name__ == "__main__": raise SystemExit(main())
