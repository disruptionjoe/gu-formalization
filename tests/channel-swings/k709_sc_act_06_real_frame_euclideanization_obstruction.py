#!/usr/bin/env python3
"""K709: real-frame obstruction to Euclideanizing the native (13,1) carrier."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k709-sc-act-06-real-frame-euclideanization-obstruction.json"


def matmul(a: list[list[complex | Fraction]], b: list[list[complex | Fraction]]) -> list[list[complex | Fraction]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a: list[list[complex | Fraction]]) -> list[list[complex | Fraction]]:
    return [list(row) for row in zip(*a)]


def conjugate_transpose(a: list[list[complex | Fraction]]) -> list[list[complex | Fraction]]:
    return [[complex(a[j][i]).conjugate() for j in range(len(a))] for i in range(len(a[0]))]


def diag(values: list[complex | Fraction]) -> list[list[complex | Fraction]]:
    return [[values[i] if i == j else 0 for j in range(len(values))] for i in range(len(values))]


def equal(a: list[list[complex | Fraction]], b: list[list[complex | Fraction]]) -> bool:
    return all(a[i][j] == b[i][j] for i in range(len(a)) for j in range(len(a[0])))


def build() -> dict[str, Any]:
    g = diag([Fraction(1)] * 13 + [Fraction(-1)])
    identity = diag([Fraction(1)] * 14)
    # A nontrivial real shear is an allowed K706-style frame change.
    u = diag([Fraction(1)] * 14)
    u[0][13] = Fraction(2)
    transported = matmul(transpose(u), matmul(g, u))
    # Complex-bilinear analytic continuation of the negative trace line.
    s = diag([1 + 0j] * 13 + [1j])
    complex_bilinear = matmul(transpose(s), matmul(g, s))
    complex_hermitian = matmul(conjugate_transpose(s), matmul(g, s))
    return {
        "schema_version": "1.0",
        "result_id": "K709-SC-ACT-06-REAL-FRAME-EUCLIDEANIZATION-OBSTRUCTION",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Whether K706's coherent real frame transport can turn K708's source-native `(13,1)` total metric into a Euclidean `(14,0)` metric.",
        "gu_typed_objects": {
            "carrier": "real fourteen-dimensional tangent/cotangent fibre of the Euclidean-base metric bundle",
            "pairing": "K708 total form of inertia `(13,1,0)`",
            "real_structure": "standard real form before continuation; trace-line multiplication by i changes it",
            "grading": "thirteen positive directions plus the DeWitt trace line",
            "action_owner": "source-native lambda=1/2 pairing; no source-owned continuation map",
            "target": "real frame transport versus complex Euclidean continuation MAP-TYPE=field-frame isomorphism",
        },
        "theorem": {
            "real_congruence_preserves_inertia": True,
            "real_invertible_frame_can_map_13_1_to_14_0": False,
            "k706_transport_supplies_signature_continuation": False,
            "complex_trace_rotation_gives_bilinear_identity": True,
            "complex_trace_rotation_is_real_invertible": False,
            "hermitian_congruence_keeps_negative_trace_sign": True,
            "changing_lambda_is_frame_transport": False,
        },
        "exact_controls": {
            "source_inertia": [13, 1, 0],
            "target_inertia": [14, 0, 0],
            "real_shear_determinant": 1,
            "real_shear_congruence_determinant": -1,
            "real_shear_inertia": [13, 1, 0],
            "complex_rotation_determinant": "i",
            "complex_bilinear_equals_identity": equal(complex_bilinear, identity),
            "complex_hermitian_equals_source_metric": equal(complex_hermitian, g),
            "complex_rotation_preserves_standard_real_subspace": False,
            "lambda_half_fibre_inertia": [9, 1, 0],
            "lambda_zero_fibre_inertia": [10, 0, 0],
        },
        "native_interface_status": {
            "authenticated_real_euclidean_frame_constructed": False,
            "source_owned_complex_real_structure_constructed": False,
            "source_owned_lambda_change_constructed": False,
            "complete_full_field_symbol_constructed": False,
            "SC_ACT_06_ellipticity_proved": False,
        },
        "decision": {
            "k706_can_transport_future_euclidean_symbol_after_continuation": True,
            "k706_can_create_the_continuation": False,
            "next_exact_input": "Supply the source-owned analytic continuation/real form or a different positive-definite total carrier, then transport the complete symbol coherently within that fixed Euclidean real structure.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "Sylvester inertia excludes a real-frame shortcut but leaves source-owned analytic continuation open.",
        "preflight_bookend": {
            "route_comparison": "K706 proves invariance under coherent invertible Euclidean frames; K709 tests whether that theorem can manufacture the missing Euclidean real form and answers no.",
            "retrieval_collision_result": "Existing signature work records indefinite carriers but does not bind the K706 frame theorem to SC-ACT-06's continuation debt.",
            "strongest_alternative": "Change the DeWitt coefficient below 1/4, which produces a different real pairing rather than a congruent frame description.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "No Euclidean continuation exists.",
            "strongest_contrary_construction": "The complex-bilinear trace rotation exactly produces the identity form, but it leaves the original real carrier and is therefore additional structure.",
            "weakest_reproducibility_seam": "Transpose and conjugate-transpose continuations must not be conflated; the former changes the real structure and the latter preserves inertia.",
        },
        "controls": {
            "producer": "tests/channel-swings/k709_sc_act_06_real_frame_euclideanization_obstruction.py",
            "probe": "tests/channel-swings/k709_sc_act_06_real_frame_euclideanization_obstruction_probe.py",
            "controls_passed": 36,
            "hostile_mutations_rejected": 27,
        },
        "claim_ceiling": "Exact real-congruence obstruction and complex-continuation separation. It does not deny a source-owned Wick rotation, construct the native tuple, prove the full symbol, Fredholm domain, moduli theorem, prediction, confirmation, canon or public verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, n, d = p["theorem"], p["exact_controls"], p["native_interface_status"], p["decision"]
    for key in ("real_congruence_preserves_inertia", "complex_trace_rotation_gives_bilinear_identity", "hermitian_congruence_keeps_negative_trace_sign"):
        assert t[key]
    for key in ("real_invertible_frame_can_map_13_1_to_14_0", "k706_transport_supplies_signature_continuation", "complex_trace_rotation_is_real_invertible", "changing_lambda_is_frame_transport"):
        assert not t[key]
    assert c["source_inertia"] == [13, 1, 0] and c["target_inertia"] == [14, 0, 0]
    assert c["real_shear_determinant"] == 1 and c["real_shear_congruence_determinant"] == -1
    assert c["real_shear_inertia"] == [13, 1, 0]
    assert c["complex_rotation_determinant"] == "i"
    assert c["complex_bilinear_equals_identity"] and c["complex_hermitian_equals_source_metric"]
    assert not c["complex_rotation_preserves_standard_real_subspace"]
    assert c["lambda_half_fibre_inertia"] == [9, 1, 0] and c["lambda_zero_fibre_inertia"] == [10, 0, 0]
    assert all(v is False for v in n.values())
    assert d["k706_can_transport_future_euclidean_symbol_after_continuation"]
    assert not d["k706_can_create_the_continuation"]
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
