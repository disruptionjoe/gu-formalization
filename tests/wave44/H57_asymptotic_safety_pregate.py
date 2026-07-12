#!/usr/bin/env python3
"""
Wave 44 -- H57 asymptotic-safety pre-gate.

This is a contract test for the next H57 flow, not a fixed-point computation.

H56 already settled the power-counting question as RENORMALIZABLE-BUT-POSITIVITY-OPEN.
H57 is a different question: does the GU operator content admit an asymptotic-safety
fixed point under a functional-RG truncation?

The gate below makes three distinctions executable:

1. Power counting is not an asymptotic-safety result.
2. A gravity-only FRG scan is not a GU scan; the constrained RS carrier and Krein
   separation must be present.
3. A valid H57 work packet can be ready for a flow build while still explicitly
   failing the "fixed point demonstrated" result gate.

No claim status, canon verdict, public posture, generation count, or source-action
truth is changed by this script. Deterministic; exit 0 on success.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite


REQUIRED_OPERATORS = frozenset(
    {
        "dimensionless_newton_coupling",
        "cosmological_coupling",
        "weyl_squared_coupling",
        "rs_ker_gamma_kinetic",
        "curvature_rs_nonminimal_coupling",
        "krein_parity_separation",
    }
)

RUNNING_COUPLINGS = frozenset(
    {
        "dimensionless_newton_coupling",
        "cosmological_coupling",
        "weyl_squared_coupling",
        "rs_ker_gamma_kinetic",
        "curvature_rs_nonminimal_coupling",
    }
)

REQUIRED_WORK_PACKET_OUTPUTS = frozenset(
    {
        "truncation_operator_basis",
        "beta_function_targets",
        "fixed_point_search_plan",
        "stability_matrix_plan",
        "relevant_direction_count_plan",
        "krein_positivity_separation_note",
    }
)


@dataclass(frozen=True)
class Submission:
    name: str
    operators: frozenset[str]
    outputs: frozenset[str]
    computed_beta_functions: frozenset[str]
    fixed_point_residuals: dict[str, float]
    critical_exponents: tuple[float, ...]
    claims_uv_complete: bool = False
    claims_loop_positivity: bool = False


def missing(have: frozenset[str], need: frozenset[str]) -> list[str]:
    return sorted(need - have)


def work_packet_failures(submission: Submission) -> list[str]:
    failures: list[str] = []
    missing_ops = missing(submission.operators, REQUIRED_OPERATORS)
    missing_outputs = missing(submission.outputs, REQUIRED_WORK_PACKET_OUTPUTS)
    if missing_ops:
        failures.append(f"missing required operators: {missing_ops}")
    if missing_outputs:
        failures.append(f"missing required work-packet outputs: {missing_outputs}")
    if submission.claims_uv_complete:
        failures.append("work packet claims UV completeness before beta functions exist")
    if submission.claims_loop_positivity:
        failures.append("work packet conflates AS coupling flow with Krein loop positivity")
    return failures


def result_claim_failures(submission: Submission) -> list[str]:
    failures: list[str] = []
    missing_ops = missing(submission.operators, REQUIRED_OPERATORS)
    missing_betas = missing(submission.computed_beta_functions, RUNNING_COUPLINGS)
    missing_residuals = missing(frozenset(submission.fixed_point_residuals), RUNNING_COUPLINGS)
    if missing_ops:
        failures.append(f"missing required operators: {missing_ops}")
    if missing_betas:
        failures.append(f"missing computed beta functions: {missing_betas}")
    if missing_residuals:
        failures.append(f"missing fixed-point residuals: {missing_residuals}")
    if any(abs(v) > 1e-9 for v in submission.fixed_point_residuals.values()):
        failures.append("fixed-point residuals are not zero within tolerance")
    if not submission.critical_exponents:
        failures.append("missing stability-matrix critical exponents")
    if any(not isfinite(v) for v in submission.critical_exponents):
        failures.append("critical exponents must be finite")
    if submission.claims_loop_positivity:
        failures.append("AS fixed point cannot by itself claim Krein loop positivity")
    return failures


def check(name: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    print(f"  [{status}] {name}" + (f" -- {detail}" if detail else ""))
    if not condition:
        raise AssertionError(name)


def expect_failure(name: str, failures: list[str], expected_fragment: str) -> None:
    joined = " | ".join(failures)
    check(name, bool(failures) and expected_fragment in joined, joined)


def main() -> int:
    print("== Wave 44 / H57 asymptotic-safety pre-gate ==")

    h56_power_counting = Submission(
        name="H56 power-counting carve",
        operators=frozenset(
            {
                "weyl_squared_coupling",
                "rs_ker_gamma_kinetic",
                "krein_parity_separation",
            }
        ),
        outputs=frozenset(),
        computed_beta_functions=frozenset(),
        fixed_point_residuals={},
        critical_exponents=(),
    )

    gravity_only_frg = Submission(
        name="gravity-only AS scan",
        operators=frozenset(
            {
                "dimensionless_newton_coupling",
                "cosmological_coupling",
                "weyl_squared_coupling",
            }
        ),
        outputs=REQUIRED_WORK_PACKET_OUTPUTS,
        computed_beta_functions=frozenset(
            {
                "dimensionless_newton_coupling",
                "cosmological_coupling",
                "weyl_squared_coupling",
            }
        ),
        fixed_point_residuals={
            "dimensionless_newton_coupling": 0.0,
            "cosmological_coupling": 0.0,
            "weyl_squared_coupling": 0.0,
        },
        critical_exponents=(2.1, -1.4),
    )

    h57_minimal_work_packet = Submission(
        name="H57 minimal GU FRG work packet",
        operators=REQUIRED_OPERATORS,
        outputs=REQUIRED_WORK_PACKET_OUTPUTS,
        computed_beta_functions=frozenset(),
        fixed_point_residuals={},
        critical_exponents=(),
    )

    expect_failure(
        "H56 power-counting is rejected as an H57 result",
        result_claim_failures(h56_power_counting),
        "missing computed beta functions",
    )
    expect_failure(
        "gravity-only AS scan is rejected as a GU scan",
        result_claim_failures(gravity_only_frg),
        "missing required operators",
    )

    work_failures = work_packet_failures(h57_minimal_work_packet)
    check(
        "H57 minimal packet is ready as a bounded next flow build",
        not work_failures,
        "operator basis + output plan present; no UV or positivity verdict claimed",
    )

    expect_failure(
        "H57 minimal packet is not accepted as a demonstrated fixed point",
        result_claim_failures(h57_minimal_work_packet),
        "missing computed beta functions",
    )

    h57_gaps = result_claim_failures(h57_minimal_work_packet)
    check(
        "H57 next required data are beta functions, fixed-point residuals, and exponents",
        all(
            any(fragment in failure for failure in h57_gaps)
            for fragment in (
                "missing computed beta functions",
                "missing fixed-point residuals",
                "missing stability-matrix critical exponents",
            )
        ),
        "the pre-gate keeps H57 open and names the exact missing outputs",
    )

    print()
    print("H57 PRE-GATE VERDICT: READY_FOR_FRG_BUILD / FIXED_POINT_NOT_COMPUTED")
    print("Binding next move: compute beta functions for the full GU truncation, then search fixed points.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
