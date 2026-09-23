#!/usr/bin/env python3
"""Exact quotient-descent versus representative-slice controls.

The packet separates two laws that act on the same corrected projector:

* quotient descent only requires projected gauge shifts to remain gauge shifts;
* a carrier-valued representative selector must kill gauge shifts.

All arithmetic is exact rational arithmetic.  The finite fixtures certify the
logical distinction; they are not a physical K77 complex.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/corrected-observation-quotient-slice-compatibility.json"

Matrix = tuple[tuple[Q, ...], ...]
Vector = tuple[Q, ...]


def matrix(rows: list[list[int]]) -> Matrix:
    return tuple(tuple(Q(value) for value in row) for row in rows)


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(len(right))), Q(0))
            for j in range(len(right[0]))
        )
        for i in range(len(left))
    )


def matvec(left: Matrix, right: Vector) -> Vector:
    return tuple(
        sum((left[i][j] * right[j] for j in range(len(right))), Q(0))
        for i in range(len(left))
    )


def add(left: Vector, right: Vector) -> Vector:
    return tuple(a + b for a, b in zip(left, right, strict=True))


def sub(left: Vector, right: Vector) -> Vector:
    return tuple(a - b for a, b in zip(left, right, strict=True))


def identity(size: int) -> Matrix:
    return tuple(
        tuple(Q(int(i == j)) for j in range(size))
        for i in range(size)
    )


def subtract(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[i][j] - right[i][j] for j in range(len(left[0])))
        for i in range(len(left))
    )


def zero(rows: int, columns: int) -> Matrix:
    return tuple(tuple(Q(0) for _ in range(columns)) for _ in range(rows))


def digest(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


GAMMA = matrix([[0, 0, 1]])
RIGHT_INVERSE = matrix([[0], [0], [1]])
PROJECTOR = subtract(identity(3), matmul(RIGHT_INVERSE, GAMMA))

# The August quotient fixture: the gauge image lies inside ker(Gamma), so P
# fixes it.  Carrier outputs change under gauge shifts, but their quotient
# classes agree.
QUOTIENT_GAUGE = matrix([[1], [0], [0]])

# The physical-slice fixture: the gauge image is the trace-lift complement, so
# P kills it and carrier-valued representatives are constant on gauge cosets.
SLICE_GAUGE = RIGHT_INVERSE


def matrix_rows(value: Matrix) -> list[list[str]]:
    return [[str(item) for item in row] for row in value]


def build() -> dict[str, Any]:
    sample = (Q(2), Q(3), Q(5))
    parameter = (Q(7),)
    quotient_shift = matvec(QUOTIENT_GAUGE, parameter)
    slice_shift = matvec(SLICE_GAUGE, parameter)
    projected = matvec(PROJECTOR, sample)
    projected_quotient_shift = sub(
        matvec(PROJECTOR, add(sample, quotient_shift)), projected
    )
    projected_slice_shift = sub(
        matvec(PROJECTOR, add(sample, slice_shift)), projected
    )

    quotient_fixed = matmul(PROJECTOR, QUOTIENT_GAUGE) == QUOTIENT_GAUGE
    quotient_killed = matmul(PROJECTOR, QUOTIENT_GAUGE) == zero(3, 1)
    slice_fixed = matmul(PROJECTOR, SLICE_GAUGE) == SLICE_GAUGE
    slice_killed = matmul(PROJECTOR, SLICE_GAUGE) == zero(3, 1)

    theorem_controls = {
        "right_inverse": matmul(GAMMA, RIGHT_INVERSE) == matrix([[1]]),
        "projector_idempotent": matmul(PROJECTOR, PROJECTOR) == PROJECTOR,
        "projector_gamma_zero": matmul(GAMMA, PROJECTOR) == zero(1, 3),
        "quotient_fixture_projector_fixes_gauge_image": quotient_fixed,
        "quotient_fixture_projector_does_not_kill_nonzero_gauge_image": not quotient_killed,
        "quotient_fixture_carrier_output_changes_by_same_gauge_image": projected_quotient_shift == quotient_shift,
        "quotient_fixture_output_classes_agree": projected_quotient_shift == matvec(QUOTIENT_GAUGE, parameter),
        "slice_fixture_projector_kills_gauge_image": slice_killed,
        "slice_fixture_projector_does_not_fix_nonzero_gauge_image": not slice_fixed,
        "slice_fixture_carrier_representative_is_coset_constant": projected_slice_shift == (Q(0), Q(0), Q(0)),
        "fix_and_kill_same_image_forces_zero": (
            not (quotient_fixed and quotient_killed)
            and not (slice_fixed and slice_killed)
            and matmul(PROJECTOR, zero(3, 1)) == zero(3, 1)
        ),
    }
    if not all(theorem_controls.values()):
        raise AssertionError("quotient/slice exact theorem controls failed")

    return {
        "schema_version": "1.0",
        "result_id": "CORRECTED-OBSERVATION-QUOTIENT-SLICE-COMPATIBILITY",
        "created": "2026-09-23",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "typed_objects": {
            "carrier": "abstract observed field carrier B=Q^3 in the independence fixtures; actual K77 carrier remains uninstantiated",
            "contraction": "Gamma:B->S",
            "right_inverse": "j:S->B with Gamma*j=1",
            "corrected_projector": "P=1-j*Gamma",
            "quotient_descent_gauge_image": "im(d0_target) contained in ker(Gamma), tested by d0_target=(1,0,0)^T",
            "representative_slice_gauge_image": "im(d_action)=im(j), tested by d_action=(0,0,1)^T",
            "pairing": "none added; the prior Green-self-adjoint condition remains independent",
            "real_structure": "rational real fixture only; no K77 real/Krein physical structure inferred",
        },
        "exact_laws": {
            "quotient_descent": "P d0_action = d0_target u for a named gauge-parameter map u; the carrier output may change, but only by a target gauge image",
            "same_complex_quotient_descent": "P(im d0) subset im d0; the August fixture uses the stronger P d0=d0",
            "unquotiented_representative_selection": "P d_action=0, equivalently im(d_action) subset ker(P)=im(j)",
            "full_trace_sized_slice": "if Gamma restricted to im(d_action) is an isomorphism onto S, representative selection forces im(d_action)=im(j)",
            "fix_kill_incompatibility": "if P d0=d0 and P d0=0 for the same differential, then d0=0",
        },
        "fixtures": {
            "gamma": matrix_rows(GAMMA),
            "right_inverse": matrix_rows(RIGHT_INVERSE),
            "projector": matrix_rows(PROJECTOR),
            "quotient_descent_gauge": matrix_rows(QUOTIENT_GAUGE),
            "representative_slice_gauge": matrix_rows(SLICE_GAUGE),
            "sample": [str(value) for value in sample],
            "gauge_parameter": [str(value) for value in parameter],
            "fixture_sha256": digest({
                "gamma": matrix_rows(GAMMA),
                "right_inverse": matrix_rows(RIGHT_INVERSE),
                "projector": matrix_rows(PROJECTOR),
                "quotient_gauge": matrix_rows(QUOTIENT_GAUGE),
                "slice_gauge": matrix_rows(SLICE_GAUGE),
            }),
        },
        "theorem_controls": theorem_controls,
        "owner_audit": {
            "august_action_observation_complex": "valid conditional map between middle cohomology quotients; its finite fixture fixes a nonzero observed gauge image and therefore is not a carrier-valued gauge-slice representative selector",
            "september_corrected_slice_criterion": "valid same-carrier representative-selection criterion; it requires the action gauge image to lie in im(j), with equality in the full trace-sized case",
            "composition_status": "not yet instantiated on one K77 carrier; no same-carrier action differential, Green form and analytic domain have been supplied",
            "correction_status": "semantic reclassification only; neither predecessor theorem is retracted",
        },
        "decision": {
            "quotient_descent_and_representative_selection_distinguished": True,
            "august_fixture_reclassified_as_quotient_descent_only": True,
            "same_nonzero_gauge_image_cannot_be_both_fixed_and_killed": True,
            "typed_K77_action_observation_bridge_constructed": False,
            "physical_quotient_constructed": False,
            "green_domain_closed": False,
            "next_exact_input": "supply one same-carrier K77 action differential and observed differential together with a map u, then test P*d_action=d0_target*u; only if a carrier-valued slice is intended also test P*d_action=0 and the prior Green/domain law",
        },
        "release_test": {
            "all_exact_controls_pass": all(theorem_controls.values()),
            "quotient_fixture_is_nontrivial": QUOTIENT_GAUGE != zero(3, 1),
            "slice_fixture_is_nontrivial": SLICE_GAUGE != zero(3, 1),
            "quotient_and_slice_gauge_images_are_distinct": QUOTIENT_GAUGE != SLICE_GAUGE,
            "predecessor_quotient_theorem_not_retracted": True,
            "predecessor_slice_theorem_not_retracted": True,
            "source_ledger_canon_paper_status_unchanged": True,
            "physical_claim_not_emitted": True,
        },
        "ledger_effect": {
            "changed": False,
            "reason": "The result classifies an internal semantic seam and supplies no source-owned K77 differential, physical quotient, state space or observable.",
        },
        "source_routing": {
            "source_claims": ["SC-ACT-01", "SC-ACT-02", "SC-ACT-06", "SC-GEN-02", "SC-GEN-03", "SC-GEN-54", "SC-CHI-01", "SC-CHI-51"],
            "polarity_change": "none",
            "route": "SOURCE_NATIVE_ROUTE",
        },
        "claim_ceiling": "Exact linear-algebra separation of quotient descent from carrier-valued gauge-slice representative selection for a supplied split corrected projector. It proves that the August condition P d0=d0 preserves a nonzero gauge image for descent to a target quotient, while the September physical-slice condition P d_action=0 kills a gauge image so representatives are constant on cosets; imposing both on the same nonzero differential is impossible. The result reclassifies one finite fixture without retracting either predecessor theorem. It does not supply a same-carrier K77 action differential, Green form, analytic domain, physical quotient, family/chirality interpretation, source/ledger move, canon, paper, public posture or GU verdict.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    controls = payload["theorem_controls"]
    if len(controls) != 11 or not all(controls.values()):
        raise AssertionError("quotient/slice theorem-control bank changed")
    decision = payload["decision"]
    if not (
        decision["quotient_descent_and_representative_selection_distinguished"]
        and decision["august_fixture_reclassified_as_quotient_descent_only"]
        and decision["same_nonzero_gauge_image_cannot_be_both_fixed_and_killed"]
    ):
        raise AssertionError("quotient/slice decision lost")
    if any(
        decision[key]
        for key in (
            "typed_K77_action_observation_bridge_constructed",
            "physical_quotient_constructed",
            "green_domain_closed",
        )
    ):
        raise AssertionError("quotient/slice packet overclaims physical closure")
    if not all(payload["release_test"].values()):
        raise AssertionError("quotient/slice release test failed")
    if payload["ledger_effect"]["changed"]:
        raise AssertionError("internal seam may not move the physics ledger")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate_payload(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
