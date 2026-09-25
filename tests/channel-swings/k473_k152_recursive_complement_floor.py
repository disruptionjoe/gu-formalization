#!/usr/bin/env python3
"""K473 recursive complete-complement lower-floor theorem."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import isqrt
from typing import Any


class CertificateError(ValueError):
    pass


def q(value: Any) -> Fraction:
    try:
        return value if isinstance(value, Fraction) else Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise CertificateError("exact rational input required") from exc


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def sqrt_interval(value: Any, bits: int = 96) -> tuple[Fraction, Fraction]:
    radicand = q(value)
    if radicand < 0:
        raise CertificateError("nonnegative radicand required")
    if radicand == 0:
        return Fraction(0), Fraction(0)
    scale = 1 << bits
    quotient = radicand.numerator * scale * scale // radicand.denominator
    lower_num = isqrt(quotient)
    lower = Fraction(lower_num, scale)
    upper = lower if lower * lower == radicand else Fraction(lower_num + 1, scale)
    if not lower * lower <= radicand <= upper * upper:
        raise AssertionError("square-root enclosure failed")
    return lower, upper


def recursive_floor(
    *,
    finite_slice_floor: Any,
    tail_floor: Any,
    cross_norm_upper: Any,
    target_threshold: Any,
    finite_slice_ref: str | None,
    complete_tail_ref: str | None,
    cross_block_ref: str | None,
    same_fixed_form: bool,
    complete_m_orthogonal_partition: bool,
    bits: int = 96,
) -> dict[str, Any]:
    refs = [finite_slice_ref, complete_tail_ref, cross_block_ref]
    if any(not isinstance(ref, str) or not ref.strip() for ref in refs):
        raise CertificateError("all proof references are required")
    if same_fixed_form is not True:
        raise CertificateError("all blocks must use the same fixed limiting form")
    if complete_m_orthogonal_partition is not True:
        raise CertificateError("finite slice plus tail must exhaust the complete M-complement")
    alpha, gamma = q(finite_slice_floor), q(tail_floor)
    mu, b = q(cross_norm_upper), q(target_threshold)
    if mu < 0:
        raise CertificateError("cross norm must be nonnegative")
    if not alpha > b or not gamma > b:
        raise CertificateError("both diagonal floors must exceed the target threshold")
    margin_product = (alpha - b) * (gamma - b)
    if not mu * mu < margin_product:
        raise CertificateError("strict Schur margin mu^2 < (alpha-b)(gamma-b) is required")
    disc = (alpha - gamma) ** 2 + 4 * mu * mu
    root_lo, root_hi = sqrt_interval(disc, bits)
    beta_lo = (alpha + gamma - root_hi) / 2
    beta_hi = (alpha + gamma - root_lo) / 2
    if not beta_lo > b:
        raise CertificateError("outward recursive floor does not exceed the target")
    return {
        "finite_slice_floor": qstr(alpha),
        "complete_tail_floor": qstr(gamma),
        "cross_norm_upper": qstr(mu),
        "target_threshold": qstr(b),
        "strict_margin_product": qstr(margin_product),
        "cross_norm_square": qstr(mu * mu),
        "recursive_floor_formula": "beta=(alpha+gamma-sqrt((alpha-gamma)^2+4*mu^2))/2",
        "discriminant": qstr(disc),
        "sqrt_outward_interval": [qstr(root_lo), qstr(root_hi)],
        "complete_complement_floor_outward_interval": [qstr(beta_lo), qstr(beta_hi)],
        "strict_beta_above_b": True,
        "same_fixed_limiting_form": True,
        "complete_M_orthogonal_partition": True,
        "proof_refs": {
            "finite_slice": finite_slice_ref,
            "complete_tail": complete_tail_ref,
            "cross_block": cross_block_ref,
        },
    }


def demo() -> dict[str, Any]:
    exact = recursive_floor(
        finite_slice_floor=3, tail_floor=6, cross_norm_upper=2,
        target_threshold=1, finite_slice_ref="control#F",
        complete_tail_ref="control#T", cross_block_ref="control#FRT",
        same_fixed_form=True, complete_m_orthogonal_partition=True,
    )
    outward = recursive_floor(
        finite_slice_floor=3, tail_floor=5, cross_norm_upper=1,
        target_threshold=Fraction(5, 2), finite_slice_ref="outward#F",
        complete_tail_ref="outward#T", cross_block_ref="outward#FRT",
        same_fixed_form=True, complete_m_orthogonal_partition=True, bits=16,
    )
    return {
        "schema_version": "1.0",
        "result_id": "K473-K152-RECURSIVE-COMPLEMENT-FLOOR",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "theorem": {
            "decomposition": "Q_M=F direct-sum_M T on the complete K162 complement",
            "premises": ["F R F>=alpha F_M", "T R T>=gamma T_M", "||F R T||<=mu"],
            "floor": "Q R Q>=beta Q_M with beta the lower two-block root",
            "target_test": "alpha>b, gamma>b, mu^2<(alpha-b)(gamma-b)",
            "sharp_for_scalar_two_block": True,
        },
        "exact_square_control": exact,
        "outward_nonsquare_control": outward,
        "native_release": {
            "finite_slice_packet_present": False,
            "complete_tail_packet_present": False,
            "cross_packet_present": False,
            "native_beta_emitted": False,
        },
    }


def main() -> int:
    argparse.ArgumentParser().parse_args()
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
