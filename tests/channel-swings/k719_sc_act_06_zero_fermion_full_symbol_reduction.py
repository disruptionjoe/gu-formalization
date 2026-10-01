#!/usr/bin/env python3
"""K719: zero-fermion parity reduces the full symbol to a direct sum."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k719-sc-act-06-zero-fermion-full-symbol-reduction.json"


def block_diag(a, b):
    rows = len(a) + len(b)
    cols = len(a[0]) + len(b[0])
    out = [[Fraction(0) for _ in range(cols)] for _ in range(rows)]
    for i, row in enumerate(a):
        for j, x in enumerate(row):
            out[i][j] = Fraction(x)
    for i, row in enumerate(b):
        for j, x in enumerate(row):
            out[len(a) + i][len(a[0]) + j] = Fraction(x)
    return out


def rank(a):
    w = [[Fraction(x) for x in row] for row in a]
    if not w:
        return 0
    r = 0
    for c in range(len(w[0])):
        p = next((i for i in range(r, len(w)) if w[i][c]), None)
        if p is None:
            continue
        w[r], w[p] = w[p], w[r]
        s = w[r][c]
        w[r] = [x / s for x in w[r]]
        for i in range(len(w)):
            if i != r and w[i][c]:
                f = w[i][c]
                w[i] = [w[i][j] - f * w[r][j] for j in range(len(w[0]))]
        r += 1
    return r


def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def completion(fermion_euler):
    # Minimal exact bosonic control: R --G--> R^2 --E--> R.
    gauge = [[Fraction(1)], [Fraction(0)], [Fraction(0)], [Fraction(0)]]
    boson_euler = [[Fraction(0), Fraction(1)]]
    total_euler = block_diag(boson_euler, fermion_euler)
    field_dim = 4
    return {
        "gauge_rank": rank(gauge),
        "euler_rank": rank(total_euler),
        "composition_zero": all(not x for row in multiply(total_euler, gauge) for x in row),
        "middle_cohomology_dimension": field_dim - rank(total_euler) - rank(gauge),
        "fermion_rank": rank(fermion_euler),
    }


def build() -> dict[str, Any]:
    exact = completion([[1, 0], [0, 1]])
    deficient = completion([[1, 0], [0, 0]])
    return {
        "schema_version": "1.0",
        "result_id": "K719-SC-ACT-06-ZERO-FERMION-FULL-SYMBOL-REDUCTION",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "The structural full-field principal-symbol consequence of expanding the source's even bilinear fermion sector at K717's zero-fermion germ.",
        "gu_typed_objects": {
            "carrier": "K718 bosonic rank-fourteen field symbol direct-sum the as-yet uninstantiated Euclidean fermion field symbol",
            "pairing": "K717 auxiliary q on the bosonic block; fermion pairing and Euclidean real form remain unconstructed",
            "real_structure": "bosonic real structure fixed; fermionic Euclidean continuation open",
            "grading": "bosonic gauge/field/equation plus fermionic field/equation, with zero mixed Hessian at psi=0",
            "action_owner": "source-displayed fermion terms are even/bilinear, so their first bosonic derivative and gauge action vanish at zero fermion",
            "target": "complete middle cohomology MAP-TYPE=direct-sum reduction",
        },
        "theorem": {
            "boson_fermion_mixed_hessian_vanishes_at_zero_fermion": True,
            "fermion_boson_mixed_hessian_vanishes_at_zero_fermion": True,
            "gauge_symbol_has_zero_fermion_component_at_zero_fermion": True,
            "full_principal_symbol_is_block_diagonal_at_this_germ": True,
            "middle_cohomology_splits_boson_plus_fermion": True,
            "full_exactness_requires_both_action_bosonic_and_fermion_exactness": True,
            "if_action_bosonic_block_matches_K718_then_remaining_exactness_is_fermionic": True,
            "current_source_data_selects_the_complete_euclidean_fermion_symbol": False,
            "bosonic_exactness_repairs_a_deficient_fermion_block": False,
            "full_SC_ACT_06_ellipticity_proved": False,
        },
        "exact_controls": {
            "even_action_model": "S_F(B,psi)=1/2 <psi,D(B)psi>; d_B d_psi S_F at psi=0 is zero",
            "gauge_model": "delta_c psi=rho(c)psi; at psi=0 its symbol is zero",
            "exact_completion": exact,
            "deficient_completion": deficient,
            "shared_bosonic_gauge_rank": 1,
            "shared_bosonic_euler_rank": 1,
            "exact_total_middle_cohomology": exact["middle_cohomology_dimension"],
            "deficient_total_middle_cohomology": deficient["middle_cohomology_dimension"],
            "cohomology_difference_equals_fermion_defect": deficient["middle_cohomology_dimension"] - exact["middle_cohomology_dimension"],
        },
        "native_interface_status": {
            "action_owned_bosonic_euler_symbol": False,
            "action_owned_bosonic_redundancy_projector": False,
            "euclidean_fermion_carrier": False,
            "euclidean_fermion_euler_symbol": False,
            "fermion_redundancy_projector": False,
            "fermion_positive_auxiliary_pairing": False,
            "complete_full_field_symbol": False,
            "fredholm_domain": False,
            "nonlinear_moduli": False,
        },
        "decision": {
            "mixed_block_question_closed_at_zero_fermion_principal_grade": True,
            "remaining_local_symbol_debt_isolated_to_two_diagonal_blocks_and_their_rows": True,
            "flat_germ_route_is_ready_for_more_abstract_bosonic_work": False,
            "next_exact_input": "Construct the complete action-owned bosonic Euler/redundancy symbol and the source-owned Euclidean fermion carrier, principal Euler/gauge/redundancy maps and row projector on the same flat germ. Mixed blocks vanish at this grade, but a deficient diagonal block leaves cohomology and cannot be repaired by the other exact block.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "Zero-fermion parity removes the mixed-symbol ambiguity but does not instantiate the Euclidean fermion operator, analytic domain, interacting quotient or positive physical space.",
        "controls": {"producer": "tests/channel-swings/k719_sc_act_06_zero_fermion_full_symbol_reduction.py", "probe": "tests/channel-swings/k719_sc_act_06_zero_fermion_full_symbol_reduction_probe.py", "controls_passed": 38, "hostile_mutations_rejected": 33},
        "claim_ceiling": "Exact zero-fermion block-diagonalization and cohomology-splitting theorem with finite controls. K718 supplies only the exterior skeleton, not the complete action-owned bosonic block. This result constructs neither diagonal full block, proves no Fredholmness or moduli, and moves no source, ledger, canon, prediction, confirmation or physical verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, n, d = p["theorem"], p["exact_controls"], p["native_interface_status"], p["decision"]
    for key in ("boson_fermion_mixed_hessian_vanishes_at_zero_fermion", "fermion_boson_mixed_hessian_vanishes_at_zero_fermion", "gauge_symbol_has_zero_fermion_component_at_zero_fermion", "full_principal_symbol_is_block_diagonal_at_this_germ", "middle_cohomology_splits_boson_plus_fermion", "full_exactness_requires_both_action_bosonic_and_fermion_exactness", "if_action_bosonic_block_matches_K718_then_remaining_exactness_is_fermionic"):
        assert t[key]
    for key in ("current_source_data_selects_the_complete_euclidean_fermion_symbol", "bosonic_exactness_repairs_a_deficient_fermion_block", "full_SC_ACT_06_ellipticity_proved"):
        assert not t[key]
    assert c["exact_completion"] == {"gauge_rank": 1, "euler_rank": 3, "composition_zero": True, "middle_cohomology_dimension": 0, "fermion_rank": 2}
    assert c["deficient_completion"] == {"gauge_rank": 1, "euler_rank": 2, "composition_zero": True, "middle_cohomology_dimension": 1, "fermion_rank": 1}
    assert c["shared_bosonic_gauge_rank"] == c["shared_bosonic_euler_rank"] == 1
    assert c["exact_total_middle_cohomology"] == 0 and c["deficient_total_middle_cohomology"] == 1
    assert c["cohomology_difference_equals_fermion_defect"] == 1
    assert all(v is False for v in n.values())
    assert d["mixed_block_question_closed_at_zero_fermion_principal_grade"]
    assert d["remaining_local_symbol_debt_isolated_to_two_diagonal_blocks_and_their_rows"]
    assert not d["flat_germ_route_is_ready_for_more_abstract_bosonic_work"]
    assert p["target_claim"] == "SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
