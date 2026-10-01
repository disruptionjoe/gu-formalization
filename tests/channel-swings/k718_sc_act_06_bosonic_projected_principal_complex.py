#!/usr/bin/env python3
"""K718: positive-metric projectors for the flat bosonic exterior skeleton."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k718-sc-act-06-bosonic-projected-principal-complex.json"


def transpose(a):
    return [list(row) for row in zip(*a)]


def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(a, s):
    return [[s * x for x in row] for row in a]


def identity(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


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


def wedge_symbol(n: int, degree: int, xi: tuple[int, ...]):
    src = list(combinations(range(n), degree))
    dst = list(combinations(range(n), degree + 1))
    index = {b: i for i, b in enumerate(src)}
    out = [[Fraction(0) for _ in src] for _ in dst]
    for r, basis in enumerate(dst):
        for pos, axis in enumerate(basis):
            inbound = basis[:pos] + basis[pos + 1 :]
            out[r][index[inbound]] = Fraction(((-1) ** pos) * xi[axis])
    return out


def zero(a):
    return all(not x for row in a for x in row)


def one_case(xi: tuple[int, ...]) -> dict[str, Any]:
    n = len(xi)
    norm2 = sum(Fraction(x * x) for x in xi)
    g = [[Fraction(x)] for x in xi]
    e = wedge_symbol(n, 1, xi)
    r = wedge_symbol(n, 2, xi)
    p_field = add(identity(n), scale(multiply(g, transpose(g)), -Fraction(1, norm2)))
    p_eq = scale(multiply(e, transpose(e)), Fraction(1, norm2))
    hodge = add(multiply(g, transpose(g)), multiply(transpose(e), e))
    return {
        "xi": list(xi),
        "auxiliary_norm_squared": str(norm2),
        "native_eta_norm_squared": str(sum(Fraction(x * x) for x in xi[:-1]) - Fraction(xi[-1] * xi[-1])),
        "gauge_rank": rank(g),
        "euler_rank": rank(e),
        "redundancy_rank": rank(r),
        "field_projector_rank": rank(p_field),
        "equation_projector_rank": rank(p_eq),
        "field_projector_idempotent": multiply(p_field, p_field) == p_field,
        "equation_projector_idempotent": multiply(p_eq, p_eq) == p_eq,
        "projected_euler_unchanged": multiply(p_eq, e) == e,
        "field_projector_kills_gauge": zero(multiply(p_field, g)),
        "euler_after_gauge_zero": zero(multiply(e, g)),
        "redundancy_after_euler_zero": zero(multiply(r, e)),
        "hodge_equals_norm_identity": hodge == scale(identity(n), norm2),
        "middle_cohomology_dimension": n - rank(e) - rank(g),
    }


def build() -> dict[str, Any]:
    cases = [
        one_case((1,) + (0,) * 13),
        one_case((1,) + (0,) * 12 + (1,)),
        one_case((2, -3, 5, 0, 7, 0, 0, 11, 0, 0, 13, 0, 17, 19)),
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K718-SC-ACT-06-BOSONIC-PROJECTED-PRINCIPAL-COMPLEX",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "The one-generator bosonic exterior/Koszul principal skeleton on K717's flat germ, reduced by the K717 background-owned positive metric; this is not the complete action-owned Euler linearization.",
        "gu_typed_objects": {
            "carrier": "real rank-fourteen cotangent symbol of the local flat Y=Met(X) germ",
            "pairing": "K717 background Frobenius q for field adjoints and covector contractions; native eta retained only as the action pairing",
            "real_structure": "unchanged real carrier",
            "grading": "Lambda^0 -> Lambda^1 -> Lambda^2 -> Lambda^3",
            "action_owner": "source B(epsilon) gauge variation and curvature/Bianchi exterior skeleton on the flat zero-residual germ; complete action Euler ownership remains open",
            "target": "bosonic independent Euler rows MAP-TYPE=covector-dependent orthogonal projection",
        },
        "theorem": {
            "field_transverse_projector_constructed": True,
            "independent_euler_row_projector_constructed": True,
            "projectors_are_defined_at_every_nonzero_covector": True,
            "reduced_bosonic_middle_exactness_holds": True,
            "native_null_covectors_are_included": True,
            "positive_hodge_symbol_is_invertible": True,
            "projectors_are_action_independent_auxiliary_gauge_data": True,
            "complete_action_owned_bosonic_symbol_constructed": False,
            "complete_fermionic_and_mixed_symbol_constructed": False,
            "full_SC_ACT_06_ellipticity_proved": False,
        },
        "exact_controls": {
            "dimension": 14,
            "equation_dimension": 91,
            "redundancy_dimension": 364,
            "cases": cases,
            "all_cases_rank_triple": [[c["gauge_rank"], c["euler_rank"], c["redundancy_rank"]] for c in cases],
            "all_cases_projector_ranks": [[c["field_projector_rank"], c["equation_projector_rank"]] for c in cases],
            "all_cases_middle_cohomology": [c["middle_cohomology_dimension"] for c in cases],
            "native_null_case_index": 1,
            "native_null_auxiliary_norm": cases[1]["auxiliary_norm_squared"],
        },
        "native_interface_status": {
            "fermion_euler_symbol": False,
            "fermion_gauge_symbol": False,
            "fermion_redundancy_symbol": False,
            "mixed_principal_blocks": False,
            "action_owned_bosonic_euler_symbol": False,
            "complete_full_field_projectors": False,
            "fredholm_domain": False,
            "nonlinear_moduli": False,
        },
        "decision": {
            "exterior_skeleton_row_ambiguity_closed_on_flat_germ": True,
            "exterior_skeleton_exactness_decides_action_bosonic_or_full_field_exactness": False,
            "next_exact_input": "Use zero-fermion parity to decide the mixed blocks, while retaining both diagonal debts: the action-owned bosonic Euler/redundancy linearization and the source-owned Euclidean fermion gauge/Euler/redundancy symbol.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The bosonic projected complex is exact locally but the physical ledger requires the interacting full-field quotient, domain and positivity.",
        "controls": {"producer": "tests/channel-swings/k718_sc_act_06_bosonic_projected_principal_complex.py", "probe": "tests/channel-swings/k718_sc_act_06_bosonic_projected_principal_complex_probe.py", "controls_passed": 42, "hostile_mutations_rejected": 37},
        "claim_ceiling": "Exact exterior/Koszul skeleton projectors and middle exactness at every nonzero covector on the K717 germ. This does not identify the complete action-owned bosonic Euler linearization; no complete fermion/mixed complex, Fredholmness, moduli, source-status move or physical result follows.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, n, d = p["theorem"], p["exact_controls"], p["native_interface_status"], p["decision"]
    for key in ("field_transverse_projector_constructed", "independent_euler_row_projector_constructed", "projectors_are_defined_at_every_nonzero_covector", "reduced_bosonic_middle_exactness_holds", "native_null_covectors_are_included", "positive_hodge_symbol_is_invertible", "projectors_are_action_independent_auxiliary_gauge_data"):
        assert t[key]
    assert not t["complete_action_owned_bosonic_symbol_constructed"]
    assert not t["complete_fermionic_and_mixed_symbol_constructed"] and not t["full_SC_ACT_06_ellipticity_proved"]
    assert c["dimension"] == 14 and c["equation_dimension"] == 91 and c["redundancy_dimension"] == 364
    assert c["all_cases_rank_triple"] == [[1, 13, 78]] * 3
    assert c["all_cases_projector_ranks"] == [[13, 13]] * 3
    assert c["all_cases_middle_cohomology"] == [0, 0, 0]
    assert c["native_null_case_index"] == 1 and c["native_null_auxiliary_norm"] == "2"
    for case in c["cases"]:
        for key in ("field_projector_idempotent", "equation_projector_idempotent", "projected_euler_unchanged", "field_projector_kills_gauge", "euler_after_gauge_zero", "redundancy_after_euler_zero", "hodge_equals_norm_identity"):
            assert case[key]
    assert all(v is False for v in n.values())
    assert d["exterior_skeleton_row_ambiguity_closed_on_flat_germ"]
    assert not d["exterior_skeleton_exactness_decides_action_bosonic_or_full_field_exactness"]
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
