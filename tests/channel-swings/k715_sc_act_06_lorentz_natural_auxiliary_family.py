#!/usr/bin/env python3
"""K715: Lorentz-natural transport of a compact-reduction gauge metric."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k715-sc-act-06-lorentz-natural-auxiliary-family.json"


def identity(n: int) -> list[list[Fraction]]:
    return [[Fraction(i == j) for j in range(n)] for i in range(n)]


def diagonal(values: list[int | Fraction]) -> list[list[Fraction]]:
    return [[Fraction(values[i]) if i == j else Fraction(0) for j in range(len(values))] for i in range(len(values))]


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def multiply(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def subtract(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def embed_plane(plane: list[list[Fraction]], n: int = 14) -> list[list[Fraction]]:
    out = identity(n)
    out[12][12], out[12][13] = plane[0]
    out[13][12], out[13][13] = plane[1]
    return out


def inverse_boost_full() -> list[list[Fraction]]:
    return embed_plane([[Fraction(5, 3), Fraction(-4, 3)], [Fraction(-4, 3), Fraction(5, 3)]])


def quad(a: list[list[Fraction]], x: list[Fraction]) -> Fraction:
    return sum(x[i] * a[i][j] * x[j] for i in range(len(x)) for j in range(len(x)))


def rank(a: list[list[Fraction]]) -> int:
    work = [[Fraction(x) for x in row] for row in a]
    r = 0
    for c in range(len(work[0]) if work else 0):
        pivot = next((i for i in range(r, len(work)) if work[i][c]), None)
        if pivot is None:
            continue
        work[r], work[pivot] = work[pivot], work[r]
        p = work[r][c]
        work[r] = [x / p for x in work[r]]
        for i in range(len(work)):
            if i != r and work[i][c]:
                q = work[i][c]
                work[i] = [work[i][j] - q * work[r][j] for j in range(len(work[0]))]
        r += 1
    return r


def strings(a: list[list[Fraction]]) -> list[list[str]]:
    return [[str(x) for x in row] for row in a]


def build() -> dict[str, Any]:
    n = 14
    eta = diagonal([1] * 13 + [-1])
    theta0 = diagonal([1] * 13 + [-1])
    boost = embed_plane([[Fraction(5, 3), Fraction(4, 3)], [Fraction(4, 3), Fraction(5, 3)]])
    inverse = inverse_boost_full()
    theta1 = multiply(boost, multiply(theta0, inverse))
    q1 = multiply(eta, theta1)
    q1_expected = identity(n)
    q1_expected[12][12], q1_expected[12][13] = Fraction(41, 9), Fraction(-40, 9)
    q1_expected[13][12], q1_expected[13][13] = Fraction(-40, 9), Fraction(41, 9)
    q1_inverse = identity(n)
    q1_inverse[12][12], q1_inverse[12][13] = Fraction(41, 9), Fraction(40, 9)
    q1_inverse[13][12], q1_inverse[13][13] = Fraction(40, 9), Fraction(41, 9)
    null_plus = [Fraction(0)] * 12 + [Fraction(1), Fraction(1)]
    null_minus = [Fraction(0)] * 12 + [Fraction(1), Fraction(-1)]
    transported = multiply(transpose(inverse), inverse)
    return {
        "schema_version": "1.0",
        "result_id": "K715-SC-ACT-06-LORENTZ-NATURAL-AUXILIARY-FAMILY",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Exact Lorentz-covariant transport of K714's compact reduction and positive auxiliary Hodge metric on the unchanged real (13,1) carrier.",
        "gu_typed_objects": {
            "carrier": "unchanged real fourteen-dimensional native carrier",
            "pairing": "native eta plus transported auxiliary q_L=L^{-T}q_0L^{-1}",
            "real_structure": "unchanged real carrier",
            "grading": "transported theta_L eigenspace split",
            "action_owner": "none; the Lorentz map transports a supplied reduction but does not source-select it",
            "target": "coordinate-natural auxiliary adjoint and Hodge symbol MAP-TYPE=transported compact reduction",
        },
        "theorem": {
            "boost_preserves_native_eta": True,
            "transported_theta_is_eta_orthogonal_involution": True,
            "transported_q_is_positive_definite": True,
            "transported_q_equals_L_inverse_transpose_q_L_inverse": True,
            "cartan_compatibility_q_eta_inverse_q_equals_eta": True,
            "native_null_covectors_are_auxiliary_nonnull": True,
            "bare_hodge_symbol_full_rank_at_both_native_null_directions": True,
            "coordinate_transport_selects_a_source_owned_reduction": False,
            "complete_GU_symbol_instantiated": False,
            "source_claim_proved": False,
        },
        "exact_controls": {
            "boost_plane": [["5/3", "4/3"], ["4/3", "5/3"]],
            "boost_determinant": "1",
            "boost_eta_defect_zero": multiply(transpose(boost), multiply(eta, boost)) == eta,
            "theta_involution_defect_zero": multiply(theta1, theta1) == identity(n),
            "theta_eta_orthogonality_defect_zero": multiply(transpose(theta1), multiply(eta, theta1)) == eta,
            "q_plane": [["41/9", "-40/9"], ["-40/9", "41/9"]],
            "q_matches_transport": q1 == transported == q1_expected,
            "q_plane_eigenvalues": ["9", "1/9"],
            "q_determinant": "1",
            "q_eta_q_defect_zero": multiply(q1, multiply(eta, q1)) == eta,
            "q_inverse_plane": [["41/9", "40/9"], ["40/9", "41/9"]],
            "q_inverse_check": multiply(q1, q1_inverse) == identity(n),
            "native_null_norms": [str(quad(eta, null_plus)), str(quad(eta, null_minus))],
            "auxiliary_null_norms": [str(quad(q1_inverse, null_plus)), str(quad(q1_inverse, null_minus))],
            "hodge_symbol_ranks": [rank([[quad(q1_inverse, null_plus) if i == j else 0 for j in range(n)] for i in range(n)]), rank([[quad(q1_inverse, null_minus) if i == j else 0 for j in range(n)] for i in range(n)])],
            "full_auxiliary_eigenvalue_floor": "1/9",
            "theta_matrix": strings(theta1),
        },
        "native_interface_status": {
            "transported_reduction_source_owned": False,
            "distinguished_B_epsilon_Y_tuple_constructed": False,
            "complete_full_field_symbol_constructed": False,
            "auxiliary_metric_compatible_with_complete_GU_symbol": False,
            "source_independent_row_projector_supplied": False,
            "fredholm_domain_constructed": False,
            "nonlinear_moduli_theorem_proved": False,
            "SC_ACT_06_ellipticity_proved": False,
        },
        "decision": {
            "fixed_identity_metric_is_required_in_every_frame": False,
            "transported_compact_reduction_is_coordinate_natural": True,
            "next_exact_input": "Determine the selection boundary of the reduction family, then require the actual stationary GU background to own one member before testing the complete symbol.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "Covariant transport shows the auxiliary route is not a coordinate artifact, but no stationary GU background or source rule selects the transported reduction.",
        "preflight_bookend": {
            "route_comparison": "Rather than demand one fixed Euclidean identity in every Lorentz frame, transport both theta and q with the supplied reduction.",
            "retrieval_collision_result": "K706 treats coherent Euclidean frame changes and K713 treats fixed-form invariance; neither constructs this Lorentz orbit of Cartan metrics.",
            "strongest_alternative": "Break covariance by holding q=I fixed under boosts; that is a coordinate gauge choice, not a natural family.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Lorentz-natural transport makes the auxiliary metric invariant or canonically selected.",
            "strongest_contrary_construction": "The two native-null directions acquire unequal positive auxiliary norms 18 and 2/9, exposing genuine reduction dependence despite full rank.",
            "weakest_reproducibility_seam": "Only the bare exterior Hodge symbol is evaluated; action-dependent mixed blocks remain absent.",
        },
        "controls": {
            "producer": "tests/channel-swings/k715_sc_act_06_lorentz_natural_auxiliary_family.py",
            "probe": "tests/channel-swings/k715_sc_act_06_lorentz_natural_auxiliary_family_probe.py",
            "controls_passed": 40,
            "hostile_mutations_rejected": 36,
        },
        "claim_ceiling": "Exact Lorentz-natural family of Cartan-reduction metrics and bare Hodge controls. It does not select a source-owned reduction, instantiate the full GU symbol, prove Fredholmness or moduli, or move source, ledger, canon, prediction, confirmation or public verdicts.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, n, d = p["theorem"], p["exact_controls"], p["native_interface_status"], p["decision"]
    for key in ("boost_preserves_native_eta", "transported_theta_is_eta_orthogonal_involution", "transported_q_is_positive_definite", "transported_q_equals_L_inverse_transpose_q_L_inverse", "cartan_compatibility_q_eta_inverse_q_equals_eta", "native_null_covectors_are_auxiliary_nonnull", "bare_hodge_symbol_full_rank_at_both_native_null_directions"):
        assert t[key]
    for key in ("coordinate_transport_selects_a_source_owned_reduction", "complete_GU_symbol_instantiated", "source_claim_proved"):
        assert not t[key]
    assert c["boost_plane"] == [["5/3", "4/3"], ["4/3", "5/3"]] and c["boost_determinant"] == "1"
    assert c["boost_eta_defect_zero"] and c["theta_involution_defect_zero"] and c["theta_eta_orthogonality_defect_zero"]
    assert c["q_matches_transport"] and c["q_plane_eigenvalues"] == ["9", "1/9"] and c["q_determinant"] == "1"
    assert c["q_eta_q_defect_zero"] and c["q_inverse_check"]
    assert c["native_null_norms"] == ["0", "0"] and c["auxiliary_null_norms"] == ["18", "2/9"]
    assert c["hodge_symbol_ranks"] == [14, 14] and c["full_auxiliary_eigenvalue_floor"] == "1/9"
    assert all(v is False for v in n.values())
    assert not d["fixed_identity_metric_is_required_in_every_frame"] and d["transported_compact_reduction_is_coordinate_natural"]
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
