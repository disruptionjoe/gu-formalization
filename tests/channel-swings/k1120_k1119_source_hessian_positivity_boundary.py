#!/usr/bin/env python3
"""K1120: reconcile exact source-Hessian progress with unchanged ownership gaps."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1120-k1119-source-hessian-positivity-boundary.json"


def build():
    rows = [
        {"requirement": "source_native_mixed_block", "evidence": "K128", "state": "exact_local"},
        {"requirement": "causal_metric_to_distortion_ranks", "evidence": "K129", "state": "exact_finite_symbol"},
        {"requirement": "mixed_hessian_inertia_floor", "evidence": "K1116-K1118", "state": "exact_finite_symbol"},
        {"requirement": "definite_C_schur_sign", "evidence": "K1119", "state": "exact_finite_symbol"},
        {"requirement": "global_stationary_functional_domain", "evidence": None, "state": "open"},
        {"requirement": "proper_BV_BFV_positive_cohomology", "evidence": None, "state": "open"},
        {"requirement": "apparatus_and_scorable_observable", "evidence": None, "state": "open"},
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K1120-K1119-SOURCE-HESSIAN-POSITIVITY-BOUNDARY",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "requirements": rows,
        "counts": {"source_native_local_constraints": 4, "global_physical_owned": 0, "open": 3, "scorable": 0},
        "protected_disposition": "SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN; LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "next_condition": "construct an action-owned constraint/KT/BFV reduction on a common closed domain and prove that it removes or controls at least the rank(A) negative sector, or derive the actual source boundary coupling or stationary global background",
        "do_not_continue": "do not substitute another conditional inverse refinement for the missing action-owned reduction, domain, background or apparatus",
        "scope_boundary": "source-native local action structure advances; no physical positivity, GU confirmation, prediction or empirical score follows",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert len(d["requirements"]) == 7
    assert [r["state"] for r in d["requirements"]].count("open") == 3
    assert d["counts"] == {"source_native_local_constraints": 4, "global_physical_owned": 0, "open": 3, "scorable": 0}
    assert "SC-ACT-01/02/06 remain ASSERTS" in d["protected_disposition"]
    assert "SC-META-53 remains UNCERTAIN" in d["protected_disposition"]
    assert "rank(A) negative sector" in d["next_condition"]
    assert "do not substitute another conditional inverse refinement" in d["do_not_continue"]
    assert "no physical positivity" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1120 controls: 9/9")
