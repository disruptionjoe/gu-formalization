#!/usr/bin/env python3
"""K847: exact quotient theorem for principal response/symmetry repairs."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k847-sc-act-06-quotient-repair-theorem.json"
PATHS = {
    "k845": ROOT / "lab/process/k845-sc-act-06-lower-order-repair-boundary.json",
    "k846": ROOT / "lab/process/k846-sc-act-06-flat-function-space-disposition.json",
}


def rank(matrix: list[list[int | Fraction]]) -> int:
    work = [[Fraction(x) for x in row] for row in matrix]
    if not work:
        return 0
    pivot_row = 0
    for col in range(len(work[0])):
        pivot = next((i for i in range(pivot_row, len(work)) if work[i][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [x / scale for x in work[pivot_row]]
        for i in range(len(work)):
            if i != pivot_row and work[i][col]:
                factor = work[i][col]
                work[i] = [work[i][j] - factor * work[pivot_row][j] for j in range(len(work[0]))]
        pivot_row += 1
    return pivot_row


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def zero(matrix: list[list[int]]) -> bool:
    return all(x == 0 for row in matrix for x in row)


def hstack(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [ra + rb for ra, rb in zip(a, b)]


def repair_case(
    g: list[list[int]], j: list[list[int]], tau: list[list[int]], s: list[list[int]]
) -> dict[str, Any]:
    middle = len(g)
    j_new = j + tau
    g_new = hstack(g, s)
    base_composition = zero(matmul(j, g))
    response_descends = zero(matmul(tau, g))
    symmetry_is_cycle = zero(matmul(j, s))
    repaired_composition = zero(matmul(tau, s))
    old_h = middle - rank(j) - rank(g)
    response_effective_rank = rank(j_new) - rank(j)
    symmetry_effective_rank = rank(g_new) - rank(g)
    new_h = middle - rank(j_new) - rank(g_new)
    return {
        "middle_dimension": middle,
        "old_middle_cohomology_dimension": old_h,
        "raw_response_rank": rank(tau),
        "raw_symmetry_rank": rank(s),
        "response_effective_rank_on_old_cohomology": response_effective_rank,
        "symmetry_effective_rank_in_response_kernel": symmetry_effective_rank,
        "base_composition_zero": base_composition,
        "response_descends_to_old_cohomology": response_descends,
        "new_symmetry_is_old_cycle": symmetry_is_cycle,
        "new_response_kills_new_symmetry": repaired_composition,
        "repaired_complex_valid": all(
            [base_composition, response_descends, symmetry_is_cycle, repaired_composition]
        ),
        "new_middle_cohomology_dimension": new_h,
        "dimension_formula_holds": new_h == old_h - response_effective_rank - symmetry_effective_rank,
        "middle_exact_after_repair": new_h == 0,
    }


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    source = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    g = [[1], [0], [0], [0]]
    j = [[0, 1, 0, 0]]
    tau = [[0, 0, 1, 0]]
    s = [[0], [0], [0], [1]]
    control = repair_case(g, j, tau, s)
    return {
        "schema_version": "1.0",
        "result_id": "K847-SC-ACT-06-QUOTIENT-REPAIR-THEOREM",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "comparator_routing_notice": source["k846"]["comparator_routing_notice"],
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Finite-dimensional principal-symbol theorem for repairing one middle term of a complex; no GU repair map is supplied.",
        "gu_typed_objects": {
            "carrier": "LAYER=toy CHIRALITY=N/A finite-dimensional principal complex E0 -> E1 -> E2",
            "pairing": "NONE",
            "real_structure": "real or complex coefficient spaces",
            "grading": "old symmetries plus new symmetries -> fields -> old equations plus new response rows",
            "action_owner": "repository-construction",
            "target": "MAP-TYPE=quotient induced response and symmetry maps on old middle cohomology",
        },
        "pinned_inputs": {
            name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for name, path in PATHS.items()
        },
        "theorem": {
            "old_complex": "E0 --G--> E1 --J--> E2 with JG=0",
            "old_middle_cohomology": "H=ker(J)/im(G)",
            "new_response": "tau:E1->F with tau G=0, inducing tau_bar:H->F",
            "new_symmetry": "S:U->E1 with JS=0 and tau S=0, inducing S_bar:U->ker(tau_bar)",
            "repaired_complex": "E0 direct_sum U --[G,S]--> E1 --[J;tau]--> E2 direct_sum F",
            "repaired_middle_cohomology": "ker(tau_bar)/im(S_bar)",
            "exactness_criterion": "im(S_bar)=ker(tau_bar)",
            "dimension_formula": "h_new=h_old-rank(tau_bar)-rank(S_bar)",
            "raw_rank_budget_is_sufficient": False,
            "effective_rank_equality_is_sufficient_under_composition": True,
        },
        "exact_control": control,
        "decision": {
            "K845_necessary_budget_sharpened": True,
            "quotient_effect_and_overlap_are_required": True,
            "source_owned_GU_repair_constructed": False,
            "next_exact_input": "For every nonzero covector, construct source/action-owned tau_bar and S_bar and prove im(S_bar)=ker(tau_bar), with ownership, composition, domain and uniformity retained.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This is an exact linear-algebra theorem and synthetic control, not a source-owned GU response, symmetry, quotient or observable.",
        "claim_ceiling": "Necessary-and-sufficient finite-dimensional middle-exactness criterion for an admitted principal repair. No GU repair or global elliptic family follows.",
        "controls": {
            "producer": "tests/channel-swings/k847_sc_act_06_quotient_repair_theorem.py",
            "probe": "tests/channel-swings/k847_sc_act_06_quotient_repair_theorem_probe.py",
            "controls_passed": 43,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(p: dict[str, Any]) -> None:
    t, c, d = p["theorem"], p["exact_control"], p["decision"]
    checks = [
        p["classification"] == "SOURCE_NATIVE_ROUTE", p["target_claim"] == "SC-ACT-06",
        "scope before inference" in p["comparator_routing_notice"], p["gu_typed_objects"]["action_owner"] == "repository-construction",
        t["old_middle_cohomology"] == "H=ker(J)/im(G)", "tau_bar" in t["new_response"],
        "S_bar" in t["new_symmetry"], "[G,S]" in t["repaired_complex"],
        t["repaired_middle_cohomology"] == "ker(tau_bar)/im(S_bar)",
        t["exactness_criterion"] == "im(S_bar)=ker(tau_bar)",
        t["dimension_formula"] == "h_new=h_old-rank(tau_bar)-rank(S_bar)",
        not t["raw_rank_budget_is_sufficient"], t["effective_rank_equality_is_sufficient_under_composition"],
        c["middle_dimension"] == 4, c["old_middle_cohomology_dimension"] == 2,
        c["raw_response_rank"] == 1, c["raw_symmetry_rank"] == 1,
        c["response_effective_rank_on_old_cohomology"] == 1,
        c["symmetry_effective_rank_in_response_kernel"] == 1,
        c["base_composition_zero"], c["response_descends_to_old_cohomology"],
        c["new_symmetry_is_old_cycle"], c["new_response_kills_new_symmetry"],
        c["repaired_complex_valid"], c["new_middle_cohomology_dimension"] == 0,
        c["dimension_formula_holds"], c["middle_exact_after_repair"],
        d["K845_necessary_budget_sharpened"], d["quotient_effect_and_overlap_are_required"],
        not d["source_owned_GU_repair_constructed"], "im(S_bar)=ker(tau_bar)" in d["next_exact_input"],
        "UNCHANGED" in p["source_and_ledger_effect"], "No GU repair" in p["claim_ceiling"],
        set(p["pinned_inputs"]) == {"k845", "k846"},
        all(len(x["sha256"]) == 64 for x in p["pinned_inputs"].values()),
        p["controls"]["controls_passed"] == 43, p["controls"]["hostile_mutations_rejected"] == 20,
        "no GU repair map" in p["scope"], "synthetic control" in p["ledger_no_change_reason"],
        repair_case([[1], [0], [0], [0]], [[0, 1, 0, 0]], [[0, 1, 0, 0]], [[0], [0], [0], [1]])["response_effective_rank_on_old_cohomology"] == 0,
        c["old_middle_cohomology_dimension"] == c["response_effective_rank_on_old_cohomology"] + c["symmetry_effective_rank_in_response_kernel"],
        p["gu_typed_objects"]["target"].startswith("MAP-TYPE=quotient"),
        p["source_and_ledger_effect"] == "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
    ]
    assert len(checks) == p["controls"]["controls_passed"]
    assert all(checks)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    elif not args.check:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
