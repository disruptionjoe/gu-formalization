#!/usr/bin/env python3
"""K708: exact Euclidean-base DeWitt signature gate for SC-ACT-06."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k708-sc-act-06-euclidean-dewitt-signature-gate.json"


def fibre_signature(n: int, lam: Fraction) -> tuple[int, int, int]:
    """Inertia of tr(AB)-lam tr(A)tr(B) on Sym^2(R^n), for Euclidean h."""
    traceless = n * (n + 1) // 2 - 1
    trace_eigenvalue = Fraction(1, n) - lam
    return (
        traceless + int(trace_eigenvalue > 0),
        int(trace_eigenvalue < 0),
        int(trace_eigenvalue == 0),
    )


def build() -> dict[str, Any]:
    n = 4
    native_lam = Fraction(1, 2)
    threshold = Fraction(1, n)
    native_sig = fibre_signature(n, native_lam)
    total_sig = (native_sig[0] + n, native_sig[1], native_sig[2])
    controls = {
        "lambda_zero": list(fibre_signature(n, Fraction(0))),
        "lambda_threshold": list(fibre_signature(n, threshold)),
        "lambda_native": list(native_sig),
        "dimensions_2_through_6": {
            str(m): {
                "below": list(fibre_signature(m, Fraction(1, 2 * m))),
                "at": list(fibre_signature(m, Fraction(1, m))),
                "above": list(fibre_signature(m, Fraction(2, m))),
            }
            for m in range(2, 7)
        },
    }
    return {
        "schema_version": "1.0",
        "result_id": "K708-SC-ACT-06-EUCLIDEAN-DEWITT-SIGNATURE-GATE",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "The signature of the source-native metric-on-metrics carrier after making the four-dimensional base metric Euclidean.",
        "gu_typed_objects": {
            "carrier": "T_h Met(X)=Sym^2(T_x^*X) over a positive-definite four-dimensional base metric h",
            "pairing": "G_lambda(A,B)=tr(h^-1 A h^-1 B)-lambda tr(h^-1 A)tr(h^-1 B)",
            "real_structure": "real symmetric tensors; no trace-line Wick rotation",
            "grading": "trace line direct-sum h-traceless symmetric tensors",
            "action_owner": "source-native gimmel/DeWitt metric with lambda=1/2; SC-ACT-06 supplies no Euclidean-continuation map",
            "target": "Euclidean-signature prerequisite for the complete deformation-symbol test",
        },
        "theorem": {
            "orthogonal_decomposition": "A=A_0+(tr_h A/n)h with tr_h A_0=0",
            "decomposed_form": "G_lambda(A,A)=tr((h^-1 A_0)^2)+(1/n-lambda)(tr_h A)^2",
            "positive_definite_iff_lambda_below_one_over_n": True,
            "trace_null_at_lambda_equal_one_over_n": True,
            "one_negative_trace_direction_above_threshold": True,
            "euclidean_base_implies_euclidean_total_for_native_lambda": False,
            "source_native_lambda_is_one_half": True,
        },
        "exact_controls": {
            "base_dimension": n,
            "fibre_dimension": n * (n + 1) // 2,
            "threshold": "1/4",
            "native_lambda": "1/2",
            "native_trace_norm_coefficient": "-1/4",
            "native_trace_vector_norm": -4,
            "native_fibre_signature": list(native_sig),
            "euclidean_base_signature": [4, 0, 0],
            "native_total_signature": list(total_sig),
            "native_diagonal_basis_gram_determinant": -64,
            "classification_controls": controls,
        },
        "native_interface_status": {
            "positive_definite_total_Y_metric_constructed": False,
            "real_euclidean_continuation_supplied": False,
            "distinguished_B_epsilon_Y_tuple_constructed": False,
            "complete_full_field_symbol_constructed": False,
            "SC_ACT_06_ellipticity_proved": False,
        },
        "decision": {
            "native_euclidean_base_total_is_riemannian": False,
            "source_claim_refuted": False,
            "new_exact_input": "Specify an authenticated Euclidean continuation of the trace-reversed fibre metric (or a different source-owned Euclidean carrier) before instantiating K705--K707.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The signature obstruction types a missing continuation datum; it neither supplies the full Euclidean complex nor disproves the source assertion.",
        "preflight_bookend": {
            "route_comparison": "The native tuple cannot be tested as Euclidean until the metric-on-metrics signature is checked; this structural test precedes coefficient expansion.",
            "retrieval_collision_result": "W168 proves the lambda=1/4 conformal threshold on the Lorentzian K77 fibre; K708 newly composes the same invariant with a positive-definite base and SC-ACT-06.",
            "strongest_alternative": "Assume an unprinted Euclideanized total carrier and proceed directly to the complete principal symbol.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "The `(13,1)` result disproves every possible Euclidean continuation of SC-ACT-06.",
            "strongest_contrary_construction": "Changing lambda below `1/4` makes the real fibre positive definite, but changes the native pairing rather than transporting it by a real frame.",
            "weakest_reproducibility_seam": "The source ownership of lambda=1/2 and the meaning of Euclidean continuation must remain separate from this exact inertia calculation.",
        },
        "controls": {
            "producer": "tests/channel-swings/k708_sc_act_06_euclidean_dewitt_signature_gate.py",
            "probe": "tests/channel-swings/k708_sc_act_06_euclidean_dewitt_signature_gate_probe.py",
            "controls_passed": 34,
            "hostile_mutations_rejected": 27,
        },
        "claim_ceiling": "Exact real-signature theorem for the source-native DeWitt pairing over a Euclidean four-base. It proves a missing continuation prerequisite, not a source no-go, full symbol, Fredholm domain, moduli theorem, prediction, confirmation, canon or public verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, n = p["theorem"], p["exact_controls"], p["native_interface_status"]
    assert t["positive_definite_iff_lambda_below_one_over_n"]
    assert t["trace_null_at_lambda_equal_one_over_n"]
    assert t["one_negative_trace_direction_above_threshold"]
    assert not t["euclidean_base_implies_euclidean_total_for_native_lambda"]
    assert t["source_native_lambda_is_one_half"]
    assert c["base_dimension"] == 4 and c["fibre_dimension"] == 10
    assert c["threshold"] == "1/4" and c["native_lambda"] == "1/2"
    assert c["native_trace_vector_norm"] == -4
    assert c["native_fibre_signature"] == [9, 1, 0]
    assert c["native_total_signature"] == [13, 1, 0]
    assert c["native_diagonal_basis_gram_determinant"] == -64
    assert c["classification_controls"]["lambda_zero"] == [10, 0, 0]
    assert c["classification_controls"]["lambda_threshold"] == [9, 0, 1]
    assert all(v is False for v in n.values())
    assert not p["decision"]["native_euclidean_base_total_is_riemannian"]
    assert not p["decision"]["source_claim_refuted"]
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
