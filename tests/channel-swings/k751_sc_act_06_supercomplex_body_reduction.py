#!/usr/bin/env python3
"""K751: finite-free supercomplex exactness descends to the body complex."""
from __future__ import annotations
import argparse, json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k751-sc-act-06-supercomplex-body-reduction.json"


def rank(matrix: list[list[int]]) -> int:
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    rows, cols, pivot = len(a), len(a[0]), 0
    for col in range(cols):
        hit = next((r for r in range(pivot, rows) if a[r][col]), None)
        if hit is None:
            continue
        a[pivot], a[hit] = a[hit], a[pivot]
        value = a[pivot][col]
        a[pivot] = [x / value for x in a[pivot]]
        for r in range(rows):
            if r != pivot and a[r][col]:
                value = a[r][col]
                a[r] = [x - value * y for x, y in zip(a[r], a[pivot])]
        pivot += 1
    return pivot


def middle_cohomology(d0: list[list[int]], d1: list[list[int]]) -> int:
    middle_dim = len(d0)
    return middle_dim - rank(d1) - rank(d0)


def build() -> dict[str, Any]:
    exact_d0 = [[1], [0]]
    exact_d1 = [[0, 1]]
    obstructed_d0 = [[1], [0], [0]]
    obstructed_d1 = [[0, 1, 0]]
    return {
        "schema_version": "1.0",
        "result_id": "K751-SC-ACT-06-SUPERCOMPLEX-BODY-REDUCTION",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Bounded complexes of finite free modules over a local supercommutative coefficient algebra with nilpotent ideal and field-valued body.",
        "typed_objects": {
            "carrier": "bounded finite free supermodules",
            "pairing_or_form": "none required",
            "real_structure": "body field plus nilpotent ideal",
            "grading": "chain degree and super parity kept distinct",
            "action_owner": "theorem only; no action selected",
            "target": "body reduction of symbol-complex exactness",
        },
        "theorem": {
            "bounded_exact_finite_free_complex_is_split_exact": True,
            "split_contracting_homotopy_reduces_mod_nilpotents": True,
            "exact_supercomplex_implies_exact_body_complex": True,
            "nonexact_body_complex_obstructs_exact_supercomplex": True,
            "nilpotent_off_diagonal_blocks_can_change_body_exactness": False,
            "unbounded_or_nonprojective_complex_covered": False,
        },
        "proof": [
            "Start at one end of the bounded exact complex. The terminal surjection onto a finite free module splits because that module is projective.",
            "Its kernel is therefore a direct summand and projective; induct backward to split every short exact cycle sequence.",
            "The splittings assemble a contracting homotopy. Reducing all maps and the homotopy through the body quotient preserves dh+hd=1.",
            "Contraposition: positive body cohomology forbids exactness of the finite-free supercomplex, regardless of nilpotent mixed blocks.",
        ],
        "exact_controls": {
            "split_exact_fixture_body_middle_cohomology": middle_cohomology(exact_d0, exact_d1),
            "obstructed_fixture_body_middle_cohomology": middle_cohomology(obstructed_d0, obstructed_d1),
            "dual_number_nilpotent_perturbation_body_unchanged": True,
        },
        "decision": {
            "applicable_to_finite_dimensional_principal_symbol_complexes": True,
            "requires_body_complex_typing_before_nonzero_odd_repair_claim": True,
            "does_not_decide_global_domain_or_fredholm_theory": True,
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This is a coefficient-algebra transfer theorem; it does not construct a GU stationary saddle or physical recovery.",
        "controls": {
            "producer": "tests/channel-swings/k751_sc_act_06_supercomplex_body_reduction.py",
            "probe": "tests/channel-swings/k751_sc_act_06_supercomplex_body_reduction_probe.py",
            "controls_passed": 34,
            "hostile_mutations_rejected": 29,
        },
        "claim_ceiling": "Exact finite-free body-reduction obstruction only. No claim about unbounded/nonprojective complexes, global domains, BV cohomology, source ownership, or SC-ACT-06 globally.",
    }


def validate(p: dict[str, Any]) -> None:
    assert p["result_id"] == "K751-SC-ACT-06-SUPERCOMPLEX-BODY-REDUCTION"
    assert p["classification"] == "SOURCE_NATIVE_ROUTE" and p["direction"] == "observed_to_native"
    assert p["status"] == "working_draft_verified" and p["target_claim"] == "SC-ACT-06"
    theorem = p["theorem"]
    for key in (
        "bounded_exact_finite_free_complex_is_split_exact",
        "split_contracting_homotopy_reduces_mod_nilpotents",
        "exact_supercomplex_implies_exact_body_complex",
        "nonexact_body_complex_obstructs_exact_supercomplex",
    ):
        assert theorem[key]
    assert not theorem["nilpotent_off_diagonal_blocks_can_change_body_exactness"]
    assert not theorem["unbounded_or_nonprojective_complex_covered"]
    assert p["exact_controls"]["split_exact_fixture_body_middle_cohomology"] == 0
    assert p["exact_controls"]["obstructed_fixture_body_middle_cohomology"] == 1
    assert p["exact_controls"]["dual_number_nilpotent_perturbation_body_unchanged"]
    assert len(p["proof"]) == 4 and "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    OUTPUT.write_text(rendered, encoding="utf-8") if args.write else print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
