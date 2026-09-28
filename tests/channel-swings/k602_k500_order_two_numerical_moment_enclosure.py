#!/usr/bin/env python3
"""K602 outward enclosure of K601's three common order-two moments."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from decimal import Decimal, localcontext
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k602-k500-order-two-numerical-moment-enclosure.json"
PRECISION = 50


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K180 = load("k180_for_k602", "k180_order_two_outward_exchange_kernel.py")


def cyclic_kernel(p: Decimal, q: Decimal) -> Decimal:
    """Raw G^2 cyclic kernel before its (2*pi)^-1 normalization."""
    first = Decimal(256) + K180.energy(p)
    return Decimal(1) / (first * (first + K180.energy(q)))


def cyclic_tail_bound(cutoff: Decimal) -> Decimal:
    """Full-plane integral bound for h^2 outside [-T,T]^2.

    On the y-tail, h^2 <= (256+E_x)^-2 E_y^-2.  On the x-tail,
    integrating (256+E_x+E_y)^-2 in y first gives 2(256+E_x)^-1.
    The two resulting elementary bounds are deliberately union-bounded.
    """
    y_tail = Decimal(1) / (Decimal(64) * cutoff)
    x_tail = Decimal(2) / (cutoff + Decimal(256)) ** 2
    return x_tail + y_tail


def outward_certificate() -> dict[str, Any]:
    with localcontext() as context:
        context.prec = PRECISION
        points = K180.dyadic_mesh()
        n_lower_raw = n_upper_raw = Decimal(0)
        a_lower_raw = a_upper_raw = Decimal(0)
        for x0, x1 in zip(points, points[1:]):
            dx = x1 - x0
            for y0, y1 in zip(points, points[1:]):
                area = dx * (y1 - y0)
                h_high_raw = cyclic_kernel(x0, y0)
                h_low_raw = cyclic_kernel(x1, y1)
                g_high_raw = K180.common_kernel(x0, y0)
                g_low_raw = K180.common_kernel(x1, y1)
                h_high = h_high_raw + K180.rounding_guard(h_high_raw)
                h_low = max(Decimal(0), h_low_raw - K180.rounding_guard(h_low_raw))
                g_high = g_high_raw + K180.rounding_guard(g_high_raw)
                g_low = max(Decimal(0), g_low_raw - K180.rounding_guard(g_low_raw))
                n_lower_raw += area * h_low * h_low
                n_upper_raw += area * h_high * h_high
                a_lower_raw += area * h_low * g_low
                a_upper_raw += area * h_high * g_high

        cutoff = points[-1]
        n_tail_raw = cyclic_tail_bound(cutoff)
        h_normalization = (Decimal(2) * K180.PI) ** 2
        cross_normalization = (Decimal(2) * K180.PI) ** 3
        n_lower = Decimal(4) * n_lower_raw / h_normalization
        n_upper = (Decimal(4) * n_upper_raw + n_tail_raw) / h_normalization

        k180 = json.loads(
            (ROOT / "lab/process/k180-order-two-outward-exchange-kernel-wave.json").read_text()
        )["outward_evaluation"]
        b_lower = Decimal(k180["single_kernel_norm_squared_lower"])
        b_upper = Decimal(k180["single_kernel_norm_squared_upper"])
        b_tail = Decimal(k180["full_raw_tail_upper"]) / (Decimal(2) * K180.PI) ** 4
        n_tail = n_tail_raw / h_normalization
        cross_tail = min((n_tail * b_upper).sqrt(), (n_upper * b_tail).sqrt())
        a_lower = Decimal(4) * a_lower_raw / cross_normalization
        a_upper = Decimal(4) * a_upper_raw / cross_normalization + cross_tail

        q00_lower = max(Decimal(0), b_lower / n_upper - (a_upper / n_lower) ** 2)
        q00_upper = b_upper / n_lower - (a_lower / n_upper) ** 2
        q10_direct_lower = max(
            Decimal(0), b_lower / n_upper - (a_upper / (Decimal(2) * n_lower)) ** 2
        )
        q10_cauchy_lower = Decimal(3) * b_lower / (Decimal(4) * n_upper)
        q10_lower = max(q10_direct_lower, q10_cauchy_lower)
        q10_upper = b_upper / n_lower - (a_lower / (Decimal(2) * n_upper)) ** 2
        difference_lower = Decimal(3) * a_lower**2 / (Decimal(4) * n_upper**2)
        difference_upper = Decimal(3) * a_upper**2 / (Decimal(4) * n_lower**2)

        return {
            "mesh_subdivisions_per_octave": K180.SUBDIVISIONS,
            "mesh_octaves": K180.OCTAVES,
            "positive_axis_cutoff": str(cutoff),
            "positive_quadrant_cells": (len(points) - 1) ** 2,
            "decimal_precision": PRECISION,
            "cyclic_finite_raw_interval": [str(n_lower_raw), str(n_upper_raw)],
            "cyclic_full_raw_tail_upper": str(n_tail_raw),
            "cross_finite_raw_interval": [str(a_lower_raw), str(a_upper_raw)],
            "cross_full_tail_upper_by_cauchy": str(cross_tail),
            "n_interval": [str(n_lower), str(n_upper)],
            "a_interval": [str(a_lower), str(a_upper)],
            "b_interval_reused_from_K180": [str(b_lower), str(b_upper)],
            "cauchy_consistency": a_upper**2 <= n_upper * b_upper,
            "q00_truncation_leakage_square_interval": [str(q00_lower), str(q00_upper)],
            "q10_q01_truncation_leakage_square_interval": [str(q10_lower), str(q10_upper)],
            "q10_minus_q00_interval": [str(difference_lower), str(difference_upper)],
            "q10_strict_lower_uses_cauchy": str(q10_cauchy_lower),
        }


def build() -> dict[str, Any]:
    certificate = outward_certificate()
    n0, n1 = map(Decimal, certificate["n_interval"])
    a0, a1 = map(Decimal, certificate["a_interval"])
    b0, b1 = map(Decimal, certificate["b_interval_reused_from_K180"])
    return {
        "schema_version": "1.0",
        "result_id": "K602-K500-ORDER-TWO-NUMERICAL-MOMENT-ENCLOSURE",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "K601's three common order-two q00/q10/q01 cyclic/action moments on the fixed K139--K179 equal-coupling point control.",
        "gu_typed_objects": {
            "cyclic_vector": "one normalized K177 order-two G^2 path kernel",
            "action_vector": "its same-signature K179 older-letter exchange kernel",
            "pairing": "positive physical Fock Hilbert pairing in one fixed impurity/exterior signature",
            "result": "order-two moment enclosure MAP-TYPE=outward-integral-certificate",
            "target": "the order-two contribution to K599's N, A_F and B_F moments",
        },
        "analytic_reduction": {
            "cyclic_kernel": "h(p,q)=(2*pi)^-1/[(256+E_p)(256+E_p+E_q)]",
            "exchange_kernel": "g(p,q)=(2*pi)^-2 K180.common_kernel(p,q)",
            "n": "int_R2 h^2",
            "a": "int_R2 h*g",
            "b": "int_R2 g^2",
            "coordinatewise_positive_and_decreasing": True,
            "b_reused_without_requadrature": True,
            "tail_rule": "cyclic tail is analytic; cross tail uses Cauchy on the common outside-box domain",
        },
        "outward_evaluation": certificate,
        "seed_moment_intervals": {
            "q00": {"N_2": [str(2*n0), str(2*n1)], "A_2": [str(2*a0), str(2*a1)], "B_2": [str(2*b0), str(2*b1)]},
            "q10": {"N_2": [str(2*n0), str(2*n1)], "A_2": [str(-a1), str(-a0)], "B_2": [str(2*b0), str(2*b1)]},
            "q01": {"N_2": [str(2*n0), str(2*n1)], "A_2": [str(-a1), str(-a0)], "B_2": [str(2*b0), str(2*b1)]},
        },
        "decision": {
            "K601_order_two_moments_numerically_enclosed": True,
            "K180_exchange_norm_reused_once": True,
            "q10_q01_order_two_leakage_strictly_positive_numerically": Decimal(certificate["q10_q01_truncation_leakage_square_interval"][0]) > 0,
            "complete_finite_K456_moments_emitted": False,
            "complete_K500_uniform_leakage_emitted": False,
            "native_noncyclic_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "Evaluate the surviving order-three-through-twelve cyclic/action signature blocks from K603, compose their finite N/A_F/B_F intervals, then apply K599 with K574's tail once and prove a uniform supported-level bound.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Certified outward numerical intervals for K601's three common order-two moments and the q00/q10/q01 truncation leakages only. Higher-order interference, complete finite moments, K574 tail composition, a uniform K500 bound, the noncyclic floor, K473, K152 and all source, ledger, canon, paper, public, novelty and physical conclusions remain open.",
    }


def validate(payload: dict[str, Any]) -> None:
    c = payload["outward_evaluation"]
    n0, n1 = map(Decimal, c["n_interval"])
    a0, a1 = map(Decimal, c["a_interval"])
    b0, b1 = map(Decimal, c["b_interval_reused_from_K180"])
    assert Decimal(0) < n0 <= n1 and Decimal(0) < a0 <= a1 and Decimal(0) < b0 <= b1
    assert c["cauchy_consistency"]
    assert Decimal(c["q10_q01_truncation_leakage_square_interval"][0]) > 0
    d = payload["decision"]
    assert d["K601_order_two_moments_numerically_enclosed"] and d["K180_exchange_norm_reused_once"]
    assert not any(d[key] for key in ("complete_finite_K456_moments_emitted", "complete_K500_uniform_leakage_emitted", "native_noncyclic_floor_emitted", "K473_released", "native_K152_interval_emitted"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
