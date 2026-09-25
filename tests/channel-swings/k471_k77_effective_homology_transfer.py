#!/usr/bin/env python3
"""K471 exact two-term effective-homology transfer."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from typing import Any


def q(value: Any) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise ValueError("exact rational input required")


def transfer(a: Any, b: Any, c: Any, t: Any) -> dict[str, Any]:
    aa, bb, cc, tt = map(q, (a, b, c, t))
    pivot = 1 + aa
    if pivot == 0:
        raise ValueError("contractible pivot is singular")
    effective = tt - cc * bb / pivot
    differential = ((pivot, bb), (cc, tt))
    inclusion_h1 = (-bb / pivot, Fraction(1))
    projection_h0 = (-cc / pivot, Fraction(1))
    homotopy = ((Fraction(1, 1) / pivot, Fraction(0)), (Fraction(0), Fraction(0)))
    lhs0 = (
        (differential[0][0] * homotopy[0][0], Fraction(0)),
        (differential[1][0] * homotopy[0][0] + projection_h0[0], projection_h0[1]),
    )
    lhs1 = (
        (homotopy[0][0] * differential[0][0], homotopy[0][0] * differential[0][1] + inclusion_h1[0]),
        (Fraction(0), inclusion_h1[1]),
    )
    if lhs0 != ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1))):
        raise ValueError("degree-zero retract identity failed")
    if lhs1 != ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1))):
        raise ValueError("degree-one retract identity failed")
    if differential[0][0] * inclusion_h1[0] + differential[0][1] != 0:
        raise ValueError("transferred inclusion is not a chain map")
    if differential[1][0] * inclusion_h1[0] + differential[1][1] != effective:
        raise ValueError("effective differential mismatch")
    return {
        "pivot": pivot,
        "effective": effective,
        "differential": differential,
        "inclusion_h1": inclusion_h1,
        "projection_h0": projection_h0,
        "homotopy": homotopy,
    }


def s(value: Any) -> Any:
    if isinstance(value, Fraction):
        return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    if isinstance(value, tuple):
        return [s(item) for item in value]
    return value


def demo() -> dict[str, Any]:
    result = transfer("1/2", "1/3", "1/4", "1")
    return {
        "schema_version": "1.0",
        "result_id": "K471-K77-EFFECTIVE-HOMOLOGY-TRANSFER",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "theorem": {
            "base_retract": "dh+hd=I-ip with ph=hi=h^2=0",
            "perturbed_differential": "D=d+delta with D^2=0",
            "invertibility": "1+delta h and 1+h delta invertible",
            "effective_differential": "d_H'=p(1+delta h)^(-1)delta i",
            "adapted_data": "i'=i-h(1+delta h)^(-1)delta i; p'=p-p delta(1+h delta)^(-1)h; h'=h(1+delta h)^(-1)",
            "conclusion": "the perturbed complex deformation retracts onto the effective homology complex",
            "smallness_is_sufficient_not_necessary": True,
            "closed_domain_preservation_still_required": True,
        },
        "exact_schur_control": {
            "a": "1/2",
            "b": "1/3",
            "c": "1/4",
            "t": "1",
            "pivot": s(result["pivot"]),
            "effective_differential": s(result["effective"]),
            "full_differential": s(result["differential"]),
            "adapted_inclusion_h1": s(result["inclusion_h1"]),
            "adapted_projection_h0": s(result["projection_h0"]),
            "adapted_homotopy": s(result["homotopy"]),
            "both_retract_identities_exact": True,
        },
        "native_status": {
            "actual_action_coefficients_present": False,
            "native_K77_packet_selected": False,
            "physical_cohomology_claimed": False,
        },
    }


def main() -> int:
    argparse.ArgumentParser().parse_args()
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
