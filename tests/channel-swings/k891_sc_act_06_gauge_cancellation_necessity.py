#!/usr/bin/env python3
"""K891: exact necessary restriction on every selected-I1B gauge completion."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k891-sc-act-06-gauge-cancellation-necessity.json"
PATHS = {
    "k887": ROOT / "lab/process/k887-sc-act-06-selected-i1b-gauge-descent-obstruction.json",
    "k888": ROOT / "lab/process/k888-sc-act-06-selected-i1b-gauge-defect-character.json",
}

def digest(p: Path) -> str: return hashlib.sha256(p.read_bytes()).hexdigest()

def build() -> dict:
    p = {n: json.loads(path.read_text()) for n, path in PATHS.items()}
    d = p["k887"]["exact_gauge_test"]
    char = p["k888"]["character_theorem"]
    rows = [{
        "so6_highest_weights": r["so6_highest_weights"],
        "so7_highest_weight": r["so7_highest_weight"],
        "real_type": r["real_type"],
        "real_irreducible_dimension": r["real_irreducible_dimension"],
        "required_cancellation_multiplicity": r["gauge_defect_multiplicity"],
        "required_cancellation_dimension": r["gauge_defect_dimension"],
    } for r in char["rows"]]
    return {
        "schema_version": "1.0", "result_id": "K891-SC-ACT-06-GAUGE-CANCELLATION-NECESSITY",
        "created": "2026-10-03", "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE", "direction": "observed_to_native", "target_claim": "SC-ACT-06",
        "scope": "Necessary radial restriction of any extra linearized Euler block C that completes the frozen selected-I1B Hessian H to a gauge-descending map at K717.",
        "gu_typed_objects": {
            "carrier": "K873 radial q-lambda gauge image inside the connection tangent",
            "pairing": "K132/K720 selected-I1B formal Euler pairing plus an unspecified completion block C",
            "real_structure": "real SO(6)xSO(7)-equivariant K717 nonnull symbol",
            "grading": "gauge parameter --G--> field tangent --(H+C)--> Euler target",
            "action_owner": "H is frozen selected I1B; C is not owned by this theorem",
            "target": "MAP-TYPE=necessary gauge-cancellation restriction before quotient descent",
        },
        "pinned_inputs": {n: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for n, path in PATHS.items()},
        "cancellation_theorem": {
            "descent_equation": "(H+C)G=0",
            "forced_restriction": "CG=-HG",
            "radial_domain_dimension": d["radial_domain_dimension"],
            "selected_i1b_defect_rank": d["i1b_euler_rank_on_radial"],
            "minimum_completion_restriction_rank": d["i1b_euler_rank_on_radial"],
            "restriction_rank_is_exact_not_only_lower_bound": True,
            "required_image_character": char["defect_character"],
            "required_real_type_count": char["real_irreducible_type_count"],
            "required_total_real_multiplicity": char["total_real_multiplicity"],
            "required_total_dimension": char["total_dimension"],
            "equivariant_rows": rows,
        },
        "decision": {
            "zero_restriction_completion_can_restore_descent": False,
            "rank_below_8191_can_restore_descent": False,
            "matching_rank_alone_proves_action_ownership": False,
            "matching_character_alone_proves_variational_ownership": False,
            "quotient_ranks_now_admissible": False,
            "next_exact_input": "Exhibit an action-owned completion block C on the same stationary germ and domain with CG=-HG on all sixteen defect types; then retest descent before quotient ranks.",
        },
        "source_and_ledger_effect": "SC-ACT-01_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "A necessary local cancellation identity supplies no action-owned completion, physical quotient, observable, prediction or confirmation.",
        "claim_ceiling": "Exact necessary rank and SO(6)xSO(7) character for any completion of the frozen selected-I1B realization. It neither constructs nor attributes the missing block.",
        "controls": {"producer": "tests/channel-swings/k891_sc_act_06_gauge_cancellation_necessity.py", "probe": "tests/channel-swings/k891_sc_act_06_gauge_cancellation_necessity_probe.py", "controls_passed": 39, "hostile_mutations_rejected": 20},
    }

def validate(x: dict) -> None:
    t, d = x["cancellation_theorem"], x["decision"]; rows = t["equivariant_rows"]
    checks = [
        x["classification"] == "SOURCE_NATIVE_ROUTE", x["target_claim"] == "SC-ACT-06",
        set(x["pinned_inputs"]) == set(PATHS), all(len(v["sha256"]) == 64 for v in x["pinned_inputs"].values()),
        t["descent_equation"] == "(H+C)G=0", t["forced_restriction"] == "CG=-HG",
        t["radial_domain_dimension"] == 16384, t["selected_i1b_defect_rank"] == 8191,
        t["minimum_completion_restriction_rank"] == 8191, t["restriction_rank_is_exact_not_only_lower_bound"],
        t["required_image_character"] == "2 Lambda^odd(R^6 direct-sum R^7) - 1",
        t["required_real_type_count"] == 16, t["required_total_real_multiplicity"] == 55,
        t["required_total_dimension"] == 8191, len(rows) == 16,
        sum(r["required_cancellation_dimension"] for r in rows) == 8191,
        sum(r["required_cancellation_multiplicity"] for r in rows) == 55,
        all(r["required_cancellation_dimension"] == r["required_cancellation_multiplicity"] * r["real_irreducible_dimension"] for r in rows),
        len({(str(r["so6_highest_weights"]), str(r["so7_highest_weight"])) for r in rows}) == 16,
        any(r["required_cancellation_multiplicity"] == 3 and r["real_irreducible_dimension"] == 1 for r in rows),
        sum(r["real_type"] == "complex_conjugate_pair" for r in rows) == 4,
        not d["zero_restriction_completion_can_restore_descent"], not d["rank_below_8191_can_restore_descent"],
        not d["matching_rank_alone_proves_action_ownership"], not d["matching_character_alone_proves_variational_ownership"],
        not d["quotient_ranks_now_admissible"], "CG=-HG" in d["next_exact_input"],
        x["source_and_ledger_effect"] == "SC-ACT-01_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "no action-owned completion" in x["ledger_no_change_reason"], "neither constructs nor attributes" in x["claim_ceiling"],
        x["controls"]["controls_passed"] == 39, x["controls"]["hostile_mutations_rejected"] == 20,
        x["gu_typed_objects"]["target"].startswith("MAP-TYPE="), x["schema_version"] == "1.0",
        x["status"] == "working_draft_verified", x["direction"] == "observed_to_native",
        x["result_id"].startswith("K891-"), t["minimum_completion_restriction_rank"] == t["selected_i1b_defect_rank"],
        t["required_total_dimension"] == t["minimum_completion_restriction_rank"],
    ]
    assert len(checks) == 39, len(checks)
    assert all(checks), [i for i, v in enumerate(checks) if not v]

def main() -> int:
    a = argparse.ArgumentParser(); a.add_argument("--write", action="store_true"); a.add_argument("--check", action="store_true"); z = a.parse_args()
    p = build(); validate(p); s = json.dumps(p, indent=2, sort_keys=True) + "\n"
    if z.write: OUTPUT.write_text(s)
    elif not z.check: print(s, end="")
    return 0
if __name__ == "__main__": raise SystemExit(main())
