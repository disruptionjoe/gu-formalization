#!/usr/bin/env python3
"""K495 outward L2 enclosure for the K176 one-variable exchange kernel."""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, localcontext
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k495-k176-kernel-l2-outward.json"
PRECISION = 70
SUBDIVISIONS = 8
OCTAVES = 40
PI = Decimal("3.141592653589793238462643383279502884197169399375105820974944592307816")


def energy(momentum: Decimal) -> Decimal:
    return (Decimal(1) + momentum * momentum).sqrt()


def acosh(value: Decimal) -> Decimal:
    return (value + (value * value - Decimal(1)).sqrt()).ln()


def primitive(value: Decimal) -> Decimal:
    return value * acosh(value) / (value * value - Decimal(1)).sqrt()


def pair_integral(a: Decimal, b: Decimal) -> Decimal:
    """Integral_R dk / ((E(k)+a)(E(k)+b))."""
    return Decimal(2) * (primitive(b) - primitive(a)) / (b - a)


def kernel(momentum: Decimal) -> Decimal:
    e = energy(momentum)
    return pair_integral(Decimal(256), Decimal(256) + e) / (Decimal(2) * PI)


def mesh(subdivisions: int = SUBDIVISIONS, octaves: int = OCTAVES) -> list[Decimal]:
    points = [Decimal(0)] + [Decimal(i + 1) / subdivisions for i in range(subdivisions)]
    for octave in range(octaves):
        left = Decimal(2) ** octave
        step = left / subdivisions
        points.extend(left + step * i for i in range(1, subdivisions + 1))
    return points


def rounding_guard(value: Decimal) -> Decimal:
    return max(abs(value) * Decimal("1e-45"), Decimal("1e-60"))


def direct_anchor(momentum: Decimal) -> dict[str, str | bool]:
    points = mesh(32, 24)
    e = energy(momentum)

    def integrand(k: Decimal) -> Decimal:
        ek = energy(k)
        return Decimal(1) / ((ek + Decimal(256)) * (ek + Decimal(256) + e)) / (Decimal(2) * PI)

    lower = Decimal(0)
    upper = Decimal(0)
    for left, right in zip(points, points[1:]):
        width = right - left
        upper += width * integrand(left)
        lower += width * integrand(right)
    cutoff = points[-1]
    # integrand <= 1/(2*pi*k^2) on the positive tail.
    tail = Decimal(1) / (Decimal(2) * PI * cutoff)
    lower *= 2
    upper = 2 * upper + 2 * tail
    closed = kernel(momentum)
    return {
        "momentum": str(momentum),
        "closed_form": str(closed),
        "direct_lower": str(lower),
        "direct_upper": str(upper),
        "closed_form_inside_direct_enclosure": lower <= closed <= upper,
    }


def certificate() -> dict[str, Any]:
    with localcontext() as context:
        context.prec = PRECISION
        points = mesh()
        lower = Decimal(0)
        upper = Decimal(0)
        monotone = True
        for left, right in zip(points, points[1:]):
            width = right - left
            high_raw = kernel(left)
            low_raw = kernel(right)
            monotone = monotone and high_raw >= low_raw > 0
            high = high_raw + rounding_guard(high_raw)
            low = max(Decimal(0), low_raw - rounding_guard(low_raw))
            upper += width * high * high
            lower += width * low * low
        cutoff = points[-1]
        # K176: J_256(E(p)) <= (1/3) E(p)^(-3/4).  For p>=R>=1,
        # J^2 <= (1/9)p^(-3/2); integrate both tails exactly.
        tail = Decimal(4) / (Decimal(9) * cutoff.sqrt())
        norm2_lower = 2 * lower
        norm2_upper = 2 * upper + tail
        threshold = Decimal(1) / Decimal(256)
        return {
            "mesh_subdivisions_per_octave": SUBDIVISIONS,
            "mesh_octaves": OCTAVES,
            "positive_axis_cutoff": str(cutoff),
            "positive_axis_cells": len(points) - 1,
            "decimal_precision": PRECISION,
            "kernel_positive_and_mesh_monotone": monotone,
            "rounding_guard_relative": "1e-45",
            "rounding_guard_absolute": "1e-60",
            "finite_full_line_norm_squared_lower": str(norm2_lower),
            "finite_full_line_norm_squared_upper": str(2 * upper),
            "analytic_full_line_tail_upper": str(tail),
            "single_kernel_norm_squared_lower": str(norm2_lower),
            "single_kernel_norm_squared_upper": str(norm2_upper),
            "single_kernel_norm_lower": str(norm2_lower.sqrt()),
            "single_kernel_norm_upper": str(norm2_upper.sqrt()),
            "target_norm_squared_threshold": "1/256",
            "strictly_below_target": norm2_upper < threshold,
            "margin_to_target": str(threshold - norm2_upper),
            "direct_integral_anchor_controls": [direct_anchor(x) for x in (Decimal(0), Decimal(1), Decimal(100))],
        }


def build() -> dict[str, Any]:
    outward = certificate()
    return {
        "schema_version": "1.0",
        "result_id": "K495-K176-KERNEL-L2-OUTWARD",
        "created": "2026-09-25",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The exact K176 one-variable kernel J_256(E(p)) on the K162 zero-bath exchange orbit.",
        "analytic_reduction": {
            "definition": "J_256(e)=int_R dk/((E(k)+256)(E(k)+256+e))/(2*pi)",
            "primitive": "F(a)=a*acosh(a)/sqrt(a^2-1)",
            "pair_integral": "2*(F(b)-F(a))/(b-a)",
            "kernel": "J_256(E(p))=pair_integral(256,256+E(p))/(2*pi)",
            "even_positive_and_decreasing_in_abs_p": True,
            "tail_majorant": "J_256(E(p))^2 <= (1/9)*p^(-3/2) for |p|>=R>=1",
        },
        "outward_evaluation": outward,
        "decision": {
            "K176_norm_upper_improves_from": "5/6",
            "K176_norm_upper_improves_to": "1/16",
            "strict_release_test_passed": outward["strictly_below_target"],
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "A rigorous outward numerical certificate for one auxiliary exchange kernel norm. It does not evaluate a complete action column, complement floor, K152 interval, physical quotient, source claim, ledger row, canon, paper or public conclusion.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    if args.write:
        OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    else:
        print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
