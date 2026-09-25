#!/usr/bin/env python3
"""K477 recursive multilevel K152 complete-complement floor tree."""

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


def sqrt_interval(value: Any, bits: int = 80) -> tuple[Fraction, Fraction]:
    radicand = q(value)
    if radicand < 0 or bits < 1:
        raise CertificateError("nonnegative radicand and positive precision required")
    if radicand == 0:
        return Fraction(0), Fraction(0)
    scale = 1 << bits
    lower_num = isqrt(radicand.numerator * scale * scale // radicand.denominator)
    lower = Fraction(lower_num, scale)
    upper = lower if lower * lower == radicand else Fraction(lower_num + 1, scale)
    if not lower * lower <= radicand <= upper * upper:
        raise AssertionError("outward square-root enclosure failed")
    return lower, upper


def certify_tree(tree: dict[str, Any], target_threshold: Any, bits: int = 80) -> dict[str, Any]:
    """Certify every internal K473 composition in a complete binary block tree."""
    b = q(target_threshold)

    def walk(node: dict[str, Any], path: str) -> dict[str, Any]:
        if not isinstance(node, dict):
            raise CertificateError("every tree node must be a mapping")
        if "floor" in node:
            floor = q(node["floor"])
            ref = node.get("proof_ref")
            if not isinstance(ref, str) or not ref.strip():
                raise CertificateError("every leaf needs a proof reference")
            if not floor > b:
                raise CertificateError("every leaf floor must exceed the target")
            return {
                "path": path,
                "kind": "leaf",
                "floor_outward_interval": [qstr(floor), qstr(floor)],
                "strict_above_target": True,
                "proof_ref": ref,
                "leaf_count": 1,
                "internal_count": 0,
                "depth": 0,
            }
        if node.get("same_fixed_form") is not True or node.get("complete_partition") is not True:
            raise CertificateError("every internal split must be complete and use the same fixed form")
        if "left" not in node or "right" not in node:
            raise CertificateError("every internal node needs left and right children")
        mu = q(node.get("cross_norm_upper"))
        if mu < 0:
            raise CertificateError("cross norm must be nonnegative")
        left = walk(node["left"], f"{path}L")
        right = walk(node["right"], f"{path}R")
        alpha = q(left["floor_outward_interval"][0])
        gamma = q(right["floor_outward_interval"][0])
        margin = (alpha - b) * (gamma - b)
        if not mu * mu < margin:
            raise CertificateError("every internal node needs strict K473 margin")
        disc = (alpha - gamma) ** 2 + 4 * mu * mu
        root_lo, root_hi = sqrt_interval(disc, bits)
        beta_lo = (alpha + gamma - root_hi) / 2
        beta_hi = (alpha + gamma - root_lo) / 2
        if not beta_lo > b:
            raise CertificateError("outward internal floor does not exceed target")
        return {
            "path": path,
            "kind": "internal",
            "left": left,
            "right": right,
            "cross_norm_upper": qstr(mu),
            "strict_margin_product": qstr(margin),
            "cross_norm_square": qstr(mu * mu),
            "discriminant": qstr(disc),
            "sqrt_outward_interval": [qstr(root_lo), qstr(root_hi)],
            "floor_outward_interval": [qstr(beta_lo), qstr(beta_hi)],
            "strict_above_target": True,
            "same_fixed_form": True,
            "complete_partition": True,
            "leaf_count": left["leaf_count"] + right["leaf_count"],
            "internal_count": left["internal_count"] + right["internal_count"] + 1,
            "depth": max(left["depth"], right["depth"]) + 1,
        }

    result = walk(tree, "Q")
    return {"target_threshold": qstr(b), "root": result}


def demo() -> dict[str, Any]:
    tree = {
        "same_fixed_form": True,
        "complete_partition": True,
        "cross_norm_upper": "1/2",
        "left": {
            "same_fixed_form": True, "complete_partition": True, "cross_norm_upper": 2,
            "left": {"floor": 3, "proof_ref": "control#F1"},
            "right": {"floor": 6, "proof_ref": "control#F2"},
        },
        "right": {
            "same_fixed_form": True, "complete_partition": True, "cross_norm_upper": 2,
            "left": {"floor": 4, "proof_ref": "control#T1"},
            "right": {"floor": 7, "proof_ref": "control#T2"},
        },
    }
    return {
        "schema_version": "1.0",
        "result_id": "K477-K152-MULTILEVEL-COMPLEMENT-TREE",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "theorem": {
            "composition": "Apply K473 at every internal node of a complete M-orthogonal binary block tree.",
            "release": "The root is a complete-complement floor only when every leaf and internal strict margin is certified.",
            "ceiling": "A finite tree certificate cannot supply any missing native leaf floor or cross norm.",
        },
        "four_leaf_control": certify_tree(tree, 1, bits=32),
        "native_release": {
            "native_leaf_packets_present": False,
            "native_cross_packets_present": False,
            "native_complete_floor_emitted": False,
        },
    }


def main() -> int:
    argparse.ArgumentParser().parse_args()
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
