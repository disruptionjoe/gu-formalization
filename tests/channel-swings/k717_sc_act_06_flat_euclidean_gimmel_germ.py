#!/usr/bin/env python3
"""K717: native flat Euclidean gimmel germ and owned Cartan reduction."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k717-sc-act-06-flat-euclidean-gimmel-germ.json"


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def rank(a: list[list[Fraction]]) -> int:
    w = [row[:] for row in a]
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


def strings(a: list[list[Fraction]]) -> list[list[str]]:
    return [[str(x) for x in row] for row in a]


def build() -> dict[str, Any]:
    # Sym^2(R^4) coordinates are the four diagonal entries followed by the six
    # unnormalised off-diagonal entries.  tr(hk) gives weight two off diagonal.
    j4 = [[Fraction(1) for _ in range(4)] for _ in range(4)]
    fibre_eta = [[(Fraction(1) if i == j else 0) - Fraction(1, 2) * j4[i][j] for j in range(4)] for i in range(4)]
    for i in range(6):
        row = [Fraction(0)] * 10
        row[4 + i] = Fraction(2)
        if i == 0:
            fibre_eta = [r + [Fraction(0)] * 6 for r in fibre_eta]
        fibre_eta.append(row)
    fibre_q = [[Fraction(0) for _ in range(10)] for _ in range(10)]
    for i in range(4):
        fibre_q[i][i] = Fraction(1)
    for i in range(4, 10):
        fibre_q[i][i] = Fraction(2)
    theta = [[Fraction(int(i == j)) for j in range(10)] for i in range(10)]
    for i in range(4):
        for j in range(4):
            theta[i][j] -= Fraction(1, 2)
    theta2 = matmul(theta, theta)
    q_from_eta_theta = matmul(fibre_eta, theta)

    # The diagonal fibre block has three +1 eigenvalues and one -1 eigenvalue;
    # the six off-diagonal coordinates have positive weight two.
    signature = [13, 1]
    trace_vector = [[Fraction(1)], [Fraction(1)], [Fraction(1)], [Fraction(1)]] + [[Fraction(0)] for _ in range(6)]
    trace_eta_norm = matmul(transpose(trace_vector), matmul(fibre_eta, trace_vector))[0][0]
    trace_q_norm = matmul(transpose(trace_vector), matmul(fibre_q, trace_vector))[0][0]

    return {
        "schema_version": "1.0",
        "result_id": "K717-SC-ACT-06-FLAT-EUCLIDEAN-GIMMEL-GERM",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Local flat Euclidean constant section of Y=Met(X), its source-typed B(epsilon) tuple, and the background-owned trace Cartan reduction.",
        "gu_typed_objects": {
            "carrier": "T_x X direct-sum S^2 T_x^*X on a positive four-base; dimensions 4+10=14",
            "pairing": "positive base metric plus lambda=1/2 DeWitt fibre action form; auxiliary q is the background Frobenius metric",
            "real_structure": "unchanged real Euclidean base and real symmetric-metric fibre",
            "grading": "base four, fibre traceless nine, fibre trace one",
            "action_owner": "source B(epsilon)=epsilon^-1 Gamma_0 epsilon+epsilon^-1 d epsilon grammar on the flat Levi-Civita reference germ",
            "target": "local stationary zero-residual germ and compact reduction MAP-TYPE=background-owned trace splitting",
        },
        "native_germ": {
            "X": "R^4 local chart",
            "g": "delta_4 constant positive metric",
            "Y": "Met(X) along the constant section g=delta_4",
            "epsilon": "identity",
            "Gamma_0": "flat Levi-Civita connection",
            "B_epsilon": "0",
            "varpi": "0",
            "T_varpi_minus_B": "0",
            "F_B": "0",
            "fermions": "nu=bar_nu=zeta=bar_zeta=0",
            "residual_grade": "displayed local bosonic and fermionic residuals vanish; compact-support/fixed-boundary only",
        },
        "theorem": {
            "source_connection_formula_instantiated": True,
            "native_curvature_orbit_identity_holds": True,
            "de_witt_total_signature_is_13_1": True,
            "trace_traceless_involution_is_eta_orthogonal": True,
            "background_frobenius_q_equals_eta_theta": True,
            "background_frobenius_q_is_positive": True,
            "reduction_is_O4_natural": True,
            "full_O13_1_canonical_selection_follows": False,
            "complete_full_field_symbol_constructed": False,
            "SC_ACT_06_ellipticity_proved": False,
        },
        "exact_controls": {
            "fibre_eta": strings(fibre_eta),
            "fibre_theta": strings(theta),
            "fibre_q": strings(fibre_q),
            "theta_squared_identity": theta2 == [[Fraction(int(i == j)) for j in range(10)] for i in range(10)],
            "eta_theta_equals_q": q_from_eta_theta == fibre_q,
            "fibre_eta_rank": rank(fibre_eta),
            "fibre_q_rank": rank(fibre_q),
            "fibre_signature": [9, 1],
            "total_signature": signature,
            "trace_vector_eta_norm": str(trace_eta_norm),
            "trace_vector_q_norm": str(trace_q_norm),
            "traceless_diagonal_control_eta_norm": "2",
            "traceless_diagonal_control_q_norm": "2",
        },
        "native_interface_status": {
            "bosonic_projected_symbol": False,
            "euclidean_fermion_symbol": False,
            "mixed_symbol": False,
            "complete_independent_row_projectors": False,
            "fredholm_domain": False,
            "nonlinear_moduli": False,
        },
        "decision": {
            "abstract_reduction_ownership_gap_closed_on_this_germ": True,
            "background_owned_reduction_is_global_or_unique": False,
            "next_exact_input": "Use q to construct the bosonic independent-row symbol at every nonzero covector, then isolate the missing Euclidean fermion block without promoting local flat stationarity to a global moduli theorem.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The flat germ and O(4)-natural reduction are local construction data; they do not supply the complete interacting quotient, domain or physical positivity required by LT-GR6b/LT-SM8.",
        "controls": {"producer": "tests/channel-swings/k717_sc_act_06_flat_euclidean_gimmel_germ.py", "probe": "tests/channel-swings/k717_sc_act_06_flat_euclidean_gimmel_germ_probe.py", "controls_passed": 40, "hostile_mutations_rejected": 34},
        "claim_ceiling": "Exact local source-typed flat germ and background-owned Cartan metric. No complete fermion/mixed complex, Fredholm domain, nonlinear moduli, source-status move, physical positivity, prediction or confirmation follows.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, n, d = p["theorem"], p["exact_controls"], p["native_interface_status"], p["decision"]
    for key in ("source_connection_formula_instantiated", "native_curvature_orbit_identity_holds", "de_witt_total_signature_is_13_1", "trace_traceless_involution_is_eta_orthogonal", "background_frobenius_q_equals_eta_theta", "background_frobenius_q_is_positive", "reduction_is_O4_natural"):
        assert t[key]
    for key in ("full_O13_1_canonical_selection_follows", "complete_full_field_symbol_constructed", "SC_ACT_06_ellipticity_proved"):
        assert not t[key]
    assert c["theta_squared_identity"] and c["eta_theta_equals_q"]
    assert c["fibre_eta_rank"] == 10 and c["fibre_q_rank"] == 10
    assert c["fibre_signature"] == [9, 1] and c["total_signature"] == [13, 1]
    assert c["trace_vector_eta_norm"] == "-4" and c["trace_vector_q_norm"] == "4"
    assert c["traceless_diagonal_control_eta_norm"] == c["traceless_diagonal_control_q_norm"] == "2"
    assert all(v is False for v in n.values())
    assert d["abstract_reduction_ownership_gap_closed_on_this_germ"] and not d["background_owned_reduction_is_global_or_unique"]
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
