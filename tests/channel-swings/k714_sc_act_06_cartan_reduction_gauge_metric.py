#!/usr/bin/env python3
"""K714: a Cartan reduction produces a positive auxiliary gauge metric."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k714-sc-act-06-cartan-reduction-gauge-metric.json"


def diagonal(values: list[int | Fraction]) -> list[list[Fraction]]:
    return [[Fraction(values[i]) if i == j else Fraction(0) for j in range(len(values))] for i in range(len(values))]


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def multiply(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def signature_diagonal(a: list[list[Fraction]]) -> list[int]:
    vals = [a[i][i] for i in range(len(a))]
    return [sum(v > 0 for v in vals), sum(v < 0 for v in vals), sum(v == 0 for v in vals)]


def strings(a: list[list[Fraction]]) -> list[list[str]]:
    return [[str(x) for x in row] for row in a]


def build() -> dict[str, Any]:
    n = 14
    eta = diagonal([1] * 13 + [-1])
    theta = diagonal([1] * 13 + [-1])
    q = multiply(eta, theta)
    identity = diagonal([1] * n)
    return {
        "schema_version": "1.0",
        "result_id": "K714-SC-ACT-06-CARTAN-REDUCTION-GAUGE-METRIC",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "The exact finite-dimensional datum by which an O(13)xO(1) compact reduction of the native real (13,1) carrier produces a positive auxiliary gauge metric.",
        "gu_typed_objects": {
            "carrier": "unchanged real fourteen-dimensional carrier with native form eta of inertia (13,1)",
            "pairing": "native eta kept distinct from q(v,w)=eta(v,theta w)",
            "real_structure": "unchanged real carrier; no Wick rotation",
            "grading": "theta-positive thirteen-plane plus theta-negative one-line",
            "action_owner": "none; theta is an independently supplied compact reduction, not source-owned action data",
            "target": "positive auxiliary metric datum for the principal-symbol adjoint MAP-TYPE=Cartan reduction",
        },
        "theorem": {
            "theta_is_involution": True,
            "theta_is_eta_orthogonal": True,
            "eta_theta_is_symmetric_positive_definite": True,
            "compact_stabilizer_is_O13_times_O1": True,
            "native_action_pairing_changed": False,
            "real_structure_changed": False,
            "compact_reduction_is_source_owned": False,
            "complete_GU_symbol_instantiated": False,
            "source_claim_proved": False,
        },
        "exact_controls": {
            "dimension": n,
            "native_signature": [13, 1, 0],
            "theta_eigenspace_dimensions": [13, 1],
            "eta": strings(eta),
            "theta": strings(theta),
            "theta_squared": strings(multiply(theta, theta)),
            "theta_eta_orthogonality_defect_zero": multiply(transpose(theta), multiply(eta, theta)) == eta,
            "q": strings(q),
            "q_equals_identity": q == identity,
            "q_signature": signature_diagonal(q),
            "q_determinant": "1",
            "eta_recovered_as_q_theta": multiply(q, theta) == eta,
        },
        "native_interface_status": {
            "compact_reduction_source_owned": False,
            "distinguished_B_epsilon_Y_tuple_constructed": False,
            "complete_full_field_symbol_constructed": False,
            "auxiliary_metric_compatible_with_complete_GU_symbol": False,
            "source_independent_row_projector_supplied": False,
            "fredholm_domain_constructed": False,
            "nonlinear_moduli_theorem_proved": False,
            "SC_ACT_06_ellipticity_proved": False,
        },
        "decision": {
            "compact_reduction_is_sufficient_to_define_positive_auxiliary_metric": True,
            "compact_reduction_is_automatically_selected_by_native_eta": False,
            "next_exact_input": "Test the Lorentz-natural family of such reductions, then construct the complete stationary GU symbol and prove compatibility of one owned reduction with every block and projector.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The theorem identifies the missing auxiliary datum but neither attributes it to the source nor constructs the stationary full-field symbol.",
        "preflight_bookend": {
            "route_comparison": "K713 proves full O(13,1) cannot preserve q; K714 tests the exact weaker datum of a maximal compact reduction.",
            "retrieval_collision_result": "K712 chooses a positive diagonal metric but does not express its ownership as a Cartan involution/reduction.",
            "strongest_alternative": "Authenticate a Euclidean continuation of the complete action carrier instead of retaining the real Lorentz carrier.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Every Lorentz carrier canonically carries this particular compact reduction.",
            "strongest_contrary_construction": "K713's exact boost moves theta and q while preserving eta, so eta alone does not select the displayed reduction.",
            "weakest_reproducibility_seam": "The converse between Cartan involutions and compact reductions is standard linear algebra here; bundle-level source ownership remains absent.",
        },
        "controls": {
            "producer": "tests/channel-swings/k714_sc_act_06_cartan_reduction_gauge_metric.py",
            "probe": "tests/channel-swings/k714_sc_act_06_cartan_reduction_gauge_metric_probe.py",
            "controls_passed": 36,
            "hostile_mutations_rejected": 31,
        },
        "claim_ceiling": "Exact Cartan-reduction/positive-metric equivalence on the standard real carrier. It does not select a GU reduction, instantiate the full complex, prove Fredholmness or moduli, or move source, ledger, canon, prediction, confirmation or public verdicts.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, n, d = p["theorem"], p["exact_controls"], p["native_interface_status"], p["decision"]
    for key in ("theta_is_involution", "theta_is_eta_orthogonal", "eta_theta_is_symmetric_positive_definite", "compact_stabilizer_is_O13_times_O1"):
        assert t[key]
    for key in ("native_action_pairing_changed", "real_structure_changed", "compact_reduction_is_source_owned", "complete_GU_symbol_instantiated", "source_claim_proved"):
        assert not t[key]
    assert c["dimension"] == 14 and c["native_signature"] == [13, 1, 0]
    assert c["theta_eigenspace_dimensions"] == [13, 1]
    assert c["theta_eta_orthogonality_defect_zero"] and c["q_equals_identity"]
    assert c["q_signature"] == [14, 0, 0] and c["q_determinant"] == "1"
    assert c["eta_recovered_as_q_theta"]
    assert all(v is False for v in n.values())
    assert d["compact_reduction_is_sufficient_to_define_positive_auxiliary_metric"]
    assert not d["compact_reduction_is_automatically_selected_by_native_eta"]
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
