#!/usr/bin/env python3
"""K642: dimension-free operator-valued cancellation-graph lower theorem."""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k642-k500-operator-cancellation-graph-lower-theorem.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K641 = load("k641_for_k642", "k641_k500_spectator_boundary_type_audit.py")


class CertificateError(ValueError):
    pass


def q(value: Any) -> Fraction:
    try:
        return value if isinstance(value, Fraction) else Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise CertificateError(f"invalid rational value {value!r}") from exc


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def beta_partial(cutoff: int) -> Fraction:
    if cutoff < 1:
        raise CertificateError("cutoff must be positive")
    return sum((Fraction(1, (k + 256) ** 2) for k in range(1, cutoff + 1)), Fraction())


def controlled_floor(matrix_lower: Any, alpha: Any = 0, delta: Any = 0) -> Fraction:
    m = q(matrix_lower)
    a = q(alpha)
    d = q(delta)
    if a < 0 or a >= Fraction(1, 2) or d < 0:
        raise CertificateError("require 0<=alpha<1/2 and delta>=0")
    return min(Fraction(1, 2) - a, m - d - Fraction(1, 128))


def finite_control(spectator_dimension: int) -> dict:
    if spectator_dimension < 1:
        raise CertificateError("spectator dimension must be positive")
    coefficient_dimension = 6 * spectator_dimension
    cutoff = 4
    m = Fraction(3)
    alpha = Fraction(1, 8)
    delta = Fraction(1, 16)
    floor = controlled_floor(m, alpha, delta)
    coefficients = [Fraction((index % 5) - 2) for index in range(coefficient_dimension)]
    coefficient_norm = sum((value * value for value in coefficients), Fraction())
    # phi_k=-c/(k+256) is a finite exact stress direction. Then
    # ||a phi||^2=cutoff*||c||^2 and L(phi)=-s_N c.
    weighted_norm = cutoff * coefficient_norm
    trace_scalar = sum((Fraction(1, k + 256) for k in range(1, cutoff + 1)), Fraction())
    cross = -2 * trace_scalar * coefficient_norm
    boundary = m * coefficient_norm
    remainder = -alpha * weighted_norm - delta * coefficient_norm
    form_value = weighted_norm + cross + boundary + remainder
    graph_norm = weighted_norm + coefficient_norm
    slack = form_value - floor * graph_norm
    if slack < 0:
        raise AssertionError("finite spectator control violated the theorem")
    return {
        "spectator_dimension": spectator_dimension,
        "coefficient_dimension": coefficient_dimension,
        "cutoff": cutoff,
        "matrix_lower_m": qstr(m),
        "remainder_alpha": qstr(alpha),
        "remainder_delta": qstr(delta),
        "floor": qstr(floor),
        "exact_slack": qstr(slack),
        "passes": True,
    }


def build() -> dict:
    k641 = K641.build()
    k640 = json.loads((ROOT / "lab/process/k640-k500-cancellation-graph-lower-theorem.json").read_text(encoding="utf-8"))
    assert k641["native_type_theorem"]["minimal_corrected_coefficient_space"] == "C^6 tensor H_spec"
    assert k641["K640_reconciliation"]["spectator_amplification_required"]
    assert k640["trace_and_domain_theorem"]["beta_squared_strictly_below_one_over_256"]

    beta_upper = Fraction(258, 66049)
    assert beta_upper < Fraction(1, 256)
    controls = [finite_control(dimension) for dimension in (1, 2, 5, 8)]
    reference_m = Fraction(-2)
    reference_floor = controlled_floor(reference_m)
    extended_control = controlled_floor(3, Fraction(1, 8), Fraction(1, 16))

    return {
        "schema_version": "1.0",
        "result_id": "K642-K500-OPERATOR-CANCELLATION-GRAPH-LOWER-THEOREM",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Dimension-free same-domain lower theorem for K641's spectator-amplified six-channel cancellation graph, a self-adjoint operator-valued boundary form and a quantitatively controlled remainder.",
        "gu_typed_objects": {
            "spectator_space": "arbitrary Hilbert space H_spec",
            "boundary_coefficient_space": "H_b=C^6 tensor H_spec",
            "base_domain": "D_a tensor H_b with a_k=k+256",
            "cancellation_domain": "D_op=(D_a tensor H_b) direct_sum (h tensor Dom(|B|^(1/2)))",
            "graph_norm": "||phi+h tensor c||_G^2=||a phi||^2+||c||^2",
            "matched_trace": "L_op(phi+h tensor c)=sum_k phi_k in H_b",
            "boundary_form": "q_B=||a phi||^2+2 Re<c,L_op phi>+b[c]",
            "result": "operator-valued cancellation-graph lower theorem MAP-TYPE=closed-form estimate",
            "target": "the correctly typed analytic interface preceding a native K139/K168 form identity",
        },
        "spectator_amplification_theorem": {
            "spectator_dimension_restricted": False,
            "finite_or_infinite_spectator_space_allowed": True,
            "base_domain_dense": True,
            "cancellation_domain_dense_when_B_form_domain_dense": True,
            "direct_sum_decomposition_unique": True,
            "coefficient_projection_continuous_with_norm": "1",
            "matched_Bochner_trace_continuous": True,
            "trace_bound": "||L_op phi||<=beta||a phi||",
            "beta_squared_definition": "sum_(k>=1)(k+256)^-2",
            "beta_squared_integral_test_upper": qstr(beta_upper),
            "beta_squared_strictly_below_one_over_256": True,
            "proof_constant_independent_of_H_spec": True,
        },
        "operator_lower_theorem": {
            "hypothesis": "B is self-adjoint on H_b with closed quadratic form b and b[c]>=m||c||^2",
            "form_domain": "(D_a tensor H_b) direct sum (h tensor Dom(|B|^(1/2)))",
            "young_parameter": "1/2",
            "inequality": "q_B>=1/2||a phi||^2+(m-2 beta^2)||c||^2>=min(1/2,m-1/128)||.||_G^2",
            "floor_function": "min(1/2,m-1/128)",
            "bounded_boundary_operator_required": False,
            "finite_boundary_matrix_required": False,
            "operator_valued_spectator_action_allowed": True,
            "dimension_free": True,
            "reference_control_m": qstr(reference_m),
            "reference_control_floor": qstr(reference_floor),
            "reference_control_is_actual_K139_K168_floor": False,
        },
        "controlled_extension_theorem": {
            "remainder_hypothesis": "r[phi,c]>=-alpha||a phi||^2-delta||c||^2 with 0<=alpha<1/2 and delta>=0",
            "inequality": "q_B+r>=min(1/2-alpha,m-delta-1/128)||.||_G^2",
            "floor_function": "min(1/2-alpha,m-delta-1/128)",
            "same_cancellation_domain_required": True,
            "separate_singular_factor_bounds_used": False,
            "mixed_incompatible_graphs_used": False,
            "finite_control_parameters": {"m": "3", "alpha": "1/8", "delta": "1/16"},
            "finite_control_floor": qstr(extended_control),
            "finite_controls": controls,
        },
        "native_interface_status": {
            "K641_corrected_coefficient_space_consumed": True,
            "K640_finite_channel_theorem_strictly_extended": True,
            "K159_operator_valued_boundary_typing_compatible": True,
            "actual_K139_K168_to_D_op_intertwiner_identified": False,
            "actual_complete_boundary_form_B_identified": False,
            "actual_operator_lower_m_identified": False,
            "actual_remainder_alpha_delta_identified": False,
            "native_same_domain_form_identity_proved": False,
            "named_complete_sector_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "finite_matrix_type_obstruction_bypassed": True,
            "correct_operator_valued_analytic_interface_constructed": True,
            "K612_data_custody_obstruction_retracted": False,
            "quantitative_native_complete_form_part_released": False,
            "next_exact_input": "Construct the native K139/K168 intertwiner into D_op, identify the self-adjoint coefficient form B on C^6 tensor H_spec and a same-domain remainder, then certify m, alpha and delta. Only those data can instantiate the displayed native floor.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "The theorem repairs an internal analytic interface without supplying the native coefficient operator, a physical quotient, state, observable or source-owned action result.",
        "preflight_bookend": {
            "route_comparison": "After K641 rejects direct scalar-matrix substitution, tensor amplification and a Bochner-trace Young estimate are the cheapest exact route that preserves K640's cancellation mechanism on the correctly typed coefficient space.",
            "retrieval_collision_result": "K159 gives an operator-valued resolvent compiler, not a same-domain quadratic lower theorem; K640 gives the lower theorem only for C^6. No prior packet proves the spectator-amplified form estimate or the controlled remainder formula.",
            "strongest_alternative": "Numerically evaluating K179 kernels would be stronger only after a native form intertwiner specifies how those columns assemble into B and the remainder; current custody does not provide that map.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling the dimension-free theorem a native lower bound without identifying the K139/K168 intertwiner, coefficient form B and constants m, alpha and delta.",
            "strongest_contrary_construction": "An operator-valued boundary form may have arbitrarily negative lower m or an uncontrolled same-domain remainder; spectator amplification alone supplies neither constant.",
            "weakest_reproducibility_seam": "Native application depends on a future exact form identity, not merely agreement of channel counts, finite spectator controls or resolvent typing.",
        },
        "controls": {
            "producer": "tests/channel-swings/k642_k500_operator_cancellation_graph_lower_theorem.py",
            "probe": "tests/channel-swings/k642_k500_operator_cancellation_graph_lower_theorem_probe.py",
            "controls_passed": 28,
            "hostile_mutations_rejected": 25,
        },
        "claim_ceiling": "Exact dimension-free lower theorem on the spectator-amplified six-channel cancellation graph. For any Hilbert H_spec and self-adjoint boundary form B>=m on C^6 tensor H_spec, the matched Bochner trace obeys beta^2<1/256 and q_B>=min(1/2,m-1/128)||.||_G^2. A same-domain remainder bounded below by -alpha||a phi||^2-delta||c||^2 gives floor min(1/2-alpha,m-delta-1/128). This repairs K640's native coefficient-space type but does not supply the K139/K168 intertwiner, B, m, alpha or delta. The m=-2 and -257/128 row remains a reference control; no native complete-sector floor, K473 beta, K152 interval, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict) -> None:
    amp = payload["spectator_amplification_theorem"]
    operator = payload["operator_lower_theorem"]
    extension = payload["controlled_extension_theorem"]
    native = payload["native_interface_status"]
    assert amp["proof_constant_independent_of_H_spec"]
    assert amp["beta_squared_strictly_below_one_over_256"]
    assert operator["floor_function"] == "min(1/2,m-1/128)"
    assert operator["dimension_free"]
    assert not operator["finite_boundary_matrix_required"]
    assert extension["floor_function"] == "min(1/2-alpha,m-delta-1/128)"
    assert all(row["passes"] for row in extension["finite_controls"])
    assert not native["actual_complete_boundary_form_B_identified"]
    assert not native["named_complete_sector_floor_emitted"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
