#!/usr/bin/env python3
"""K1818: restart-safe whole-line stationary rejection on K1816 candidates.

K1816's complete uniform order-eight value bank certifies 26 leaves and leaves
52 method-indeterminate. This producer evaluates the full Fisher objective,
not the fixed-score lower witness, with an order-eight leaf-centered Taylor
jet. It composes each compact gradient/Hessian enclosure with K1786's
analytic whole-line tails and rejects a candidate whenever either gradient
component excludes zero. Atomic checkpoints preserve every completed leaf;
retention is method indeterminacy, never evidence for another stationary
point.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import sys
from functools import cache
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path

from flint import arb

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1818-full-fisher-slab-three-stationary-cover.json"
CHECKPOINT_DIR = ROOT / "_local/k1818-stationary-checkpoints"

PARAMETER_ORDER = 8
CELL_HALF_WIDTH = F(1, 4)
OBSERVATION_ORDER = 14


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


base = load(
    "k1811_for_k1818",
    ROOT / "tests/channel-swings/k1811_full_fisher_slab_three_anchored_score_bank.py",
)
leaf_bank = load(
    "k1816_for_k1818",
    ROOT / "tests/channel-swings/k1816_full_fisher_slab_three_leafwise_score_bank.py",
)


def configure() -> None:
    base.m.PARAMETER_ORDER = PARAMETER_ORDER
    base.m.P.order = PARAMETER_ORDER
    base.m.CELL_HALF_WIDTH = CELL_HALF_WIDTH
    base.m.OBSERVATION_ORDER = OBSERVATION_ORDER
    leaf_bank.ensure_backends()
    leaf_bank.m.PARAMETER_ORDER = PARAMETER_ORDER
    leaf_bank.m.P.order = PARAMETER_ORDER
    leaf_bank.m.CELL_HALF_WIDTH = CELL_HALF_WIDTH
    leaf_bank.m.OBSERVATION_ORDER = OBSERVATION_ORDER
    leaf_bank.MARGIN_METHOD = "absolute"


def symmetric_ball(text: str) -> arb:
    value = arb(text)
    return arb(0, value.upper())


@cache
def point_jet():
    configure()
    print("K1818: computing shared order-eight anchor jet", file=sys.stderr, flush=True)
    return base.compact_jet(
        base.ANCHOR_T,
        base.ANCHOR_T,
        base.ANCHOR_Z,
        base.ANCHOR_Z,
    )


@cache
def input_rows() -> list[dict]:
    """Load K1816's tracked complete final-configuration bank."""
    configure()
    certificate = json.loads(leaf_bank.ARTIFACT.read_text())["certificate"]
    rows = certificate.get("leaves", [])
    if [row.get("leaf") for row in rows] != list(range(78)):
        raise ValueError("K1818 requires K1816's tracked complete 78-leaf uniform bank")
    return rows


@cache
def candidate_leaf_ids() -> list[int]:
    return [
        row["leaf"]
        for row in input_rows()
        if not row["decision"]["compact_cross_margin_positive"]
    ]


@cache
def leaf_boxes():
    return [(None, tuple(F(value) for value in row["box"])) for row in input_rows()]


@cache
def partition_digest() -> str:
    return json.loads(leaf_bank.ARTIFACT.read_text())["certificate"]["input_partition_digest"]


def checkpoint_path(leaf_id: int) -> Path:
    return CHECKPOINT_DIR / (
        f"leaf-{leaf_id:03d}-order-{PARAMETER_ORDER:02d}"
        f"-cell-{CELL_HALF_WIDTH.numerator}-{CELL_HALF_WIDTH.denominator}"
        f"-observation-{OBSERVATION_ORDER:02d}-remainder-anchor-hull.json"
    )


def bernstein_checkpoint_path(leaf_id: int) -> Path:
    return CHECKPOINT_DIR / (
        f"leaf-{leaf_id:03d}-order-{PARAMETER_ORDER:02d}"
        f"-cell-{CELL_HALF_WIDTH.numerator}-{CELL_HALF_WIDTH.denominator}"
        f"-observation-{OBSERVATION_ORDER:02d}-remainder-anchor-hull-bernstein.json"
    )


def atomic_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    temporary.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    os.replace(temporary, path)


def affine_power_to_bernstein_range(
    coefficients: dict[tuple[int, int], arb],
    x_lo: arb,
    x_hi: arb,
    y_lo: arb,
    y_hi: arb,
    degree: int,
) -> arb:
    """Enclose a bivariate power polynomial by tensor Bernstein coefficients."""
    transformed: dict[tuple[int, int], arb] = {}
    for (i, j), coefficient in coefficients.items():
        for k in range(i + 1):
            for ell in range(j + 1):
                key = (k, ell)
                transformed[key] = transformed.get(key, arb(0)) + (
                    coefficient
                    * arb(comb(i, k))
                    * x_lo ** (i - k)
                    * (x_hi - x_lo) ** k
                    * arb(comb(j, ell))
                    * y_lo ** (j - ell)
                    * (y_hi - y_lo) ** ell
                )
    bernstein = []
    for i in range(degree + 1):
        for j in range(degree + 1):
            value = arb(0)
            for k in range(i + 1):
                for ell in range(j + 1):
                    value += (
                        transformed.get((k, ell), arb(0))
                        * arb(comb(i, k))
                        / arb(comb(degree, k))
                        * arb(comb(j, ell))
                        / arb(comb(degree, ell))
                    )
            bernstein.append(value)
    lower = min(value.lower() for value in bernstein)
    upper = max(value.upper() for value in bernstein)
    return arb((lower + upper) / 2, (upper - lower) / 2)


def derivative_polynomial_bernstein(
    point,
    derivative_jet,
    dt_lo: F,
    dt_hi: F,
    dz_lo: F,
    dz_hi: F,
    axis_counts: tuple[int, int],
) -> arb:
    """Range the anchored Taylor polynomial without repeated-variable wrapping."""
    at, az = axis_counts
    maximum_degree = PARAMETER_ORDER - at - az - 1
    coefficients = {}
    for (i, j), coefficient in point.c.items():
        if i < at or j < az or (i - at) + (j - az) > maximum_degree:
            continue
        factor = factorial(i) // factorial(i - at)
        factor *= factorial(j) // factorial(j - az)
        coefficients[(i - at, j - az)] = arb(factor) * coefficient
    aq = base.m.aq
    polynomial = affine_power_to_bernstein_range(
        coefficients,
        aq(dt_lo),
        aq(dt_hi),
        aq(dz_lo),
        aq(dz_hi),
        maximum_degree,
    )
    remainder = arb(0)
    for (i, j), coefficient in derivative_jet.c.items():
        if i < at or j < az or i + j != PARAMETER_ORDER:
            continue
        factor = factorial(i) // factorial(i - at)
        factor *= factorial(j) // factorial(j - az)
        term = (
            arb(factor)
            * abs(coefficient)
            * max(abs(base.m.aq(dt_lo)), abs(base.m.aq(dt_hi))) ** (i - at)
            * max(abs(base.m.aq(dz_lo)), abs(base.m.aq(dz_hi))) ** (j - az)
        )
        remainder += arb(term.upper())
    return polynomial + arb(0, remainder)


def compute_leaf(leaf_id: int) -> dict:
    configure()
    candidates = candidate_leaf_ids()
    if leaf_id not in candidates:
        raise ValueError(f"leaf {leaf_id} is not a K1816 value-indeterminate candidate")
    _, box = leaf_boxes()[leaf_id]
    t_lo, t_hi, z_lo, z_hi = box
    print(
        f"K1818 candidate leaf {leaf_id:02d}: order-eight full-objective jet",
        file=sys.stderr,
        flush=True,
    )
    center = point_jet()
    derivative_hull = (
        min(t_lo, base.ANCHOR_T),
        max(t_hi, base.ANCHOR_T),
        min(z_lo, base.ANCHOR_Z),
        max(z_hi, base.ANCHOR_Z),
    )
    derivative_jet = base.compact_jet(*derivative_hull)
    base.tails.CENTER_T = (t_lo + t_hi) / 2
    base.tails.RADIUS_T = (t_hi - t_lo) / 2
    base.tails.CENTER_Z = (z_lo + z_hi) / 2
    base.tails.RADIUS_Z = (z_hi - z_lo) / 2
    tails = base.tails.compute()["absolute_two_tail_bounds"]
    dt = base.offset_ball(t_lo - base.ANCHOR_T, t_hi - base.ANCHOR_T)
    dz = base.offset_ball(z_lo - base.ANCHOR_Z, z_hi - base.ANCHOR_Z)
    gradient = [
        base.derivative_polynomial(center, derivative_jet, dt, dz, (1, 0))
        + symmetric_ball(tails["gradient"]["t"]),
        base.derivative_polynomial(center, derivative_jet, dt, dz, (0, 1))
        + symmetric_ball(tails["gradient"]["z"]),
    ]
    hessian = [
        [
            base.derivative_polynomial(center, derivative_jet, dt, dz, (2, 0))
            + symmetric_ball(tails["hessian"]["tt"]),
            base.derivative_polynomial(center, derivative_jet, dt, dz, (1, 1))
            + symmetric_ball(tails["hessian"]["tz"]),
        ],
        [
            base.derivative_polynomial(center, derivative_jet, dt, dz, (1, 1))
            + symmetric_ball(tails["hessian"]["tz"]),
            base.derivative_polynomial(center, derivative_jet, dt, dz, (0, 2))
            + symmetric_ball(tails["hessian"]["zz"]),
        ],
    ]
    determinant = hessian[0][0] * hessian[1][1] - hessian[0][1] ** 2
    rejected_by = [
        axis
        for axis, value in zip(("t", "z"), gradient)
        if not value.contains(0)
    ]
    payload = {
        "schema_version": "1.0",
        "claim_id": "K1818",
        "leaf": leaf_id,
        "input_partition_digest": partition_digest(),
        "input_k1816_checkpoint_digest": input_rows()[leaf_id]["checkpoint_digest"],
        "box": [str(value) for value in box],
        "configuration": {
            "parameter_taylor_order": PARAMETER_ORDER,
            "cell_half_width": str(CELL_HALF_WIDTH),
            "observation_taylor_order": OBSERVATION_ORDER,
            "compact_cell_count": 2 * int(base.m.RADIUS / CELL_HALF_WIDTH),
            "parameter_remainder_domain": "axis-aligned hull of the K1787 anchor and exact target leaf",
            "parameter_remainder_hull": [str(value) for value in derivative_hull],
            "whole_line_tail_method": "K1786 analytic value-gradient-Hessian majorant on the exact leaf",
        },
        "certificate": {
            "whole_line_gradient": {
                "t": base.m.enc(gradient[0]),
                "z": base.m.enc(gradient[1]),
            },
            "whole_line_hessian": {
                "tt": base.m.enc(hessian[0][0]),
                "tz": base.m.enc(hessian[0][1]),
                "zz": base.m.enc(hessian[1][1]),
                "determinant": base.m.enc(determinant),
            },
        },
        "decision": {
            "stationary_rejected": bool(rejected_by),
            "rejected_by": rejected_by,
            "strictly_convex": bool(hessian[0][0] > 0 and determinant > 0),
            "retained_leaf_means_additional_stationary_point": False,
        },
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["checkpoint_digest"] = hashlib.sha256(canonical).hexdigest()
    return payload


def compute_leaf_bernstein(leaf_id: int) -> dict:
    """Re-evaluate one corrected leaf with Bernstein-ranged Taylor polynomials."""
    configure()
    candidates = candidate_leaf_ids()
    if leaf_id not in candidates:
        raise ValueError(f"leaf {leaf_id} is not a K1816 value-indeterminate candidate")
    _, box = leaf_boxes()[leaf_id]
    t_lo, t_hi, z_lo, z_hi = box
    print(
        f"K1818 candidate leaf {leaf_id:02d}: anchor-hull Bernstein range",
        file=sys.stderr,
        flush=True,
    )
    center = point_jet()
    derivative_hull = (
        min(t_lo, base.ANCHOR_T),
        max(t_hi, base.ANCHOR_T),
        min(z_lo, base.ANCHOR_Z),
        max(z_hi, base.ANCHOR_Z),
    )
    derivative_jet = base.compact_jet(*derivative_hull)
    base.tails.CENTER_T = (t_lo + t_hi) / 2
    base.tails.RADIUS_T = (t_hi - t_lo) / 2
    base.tails.CENTER_Z = (z_lo + z_hi) / 2
    base.tails.RADIUS_Z = (z_hi - z_lo) / 2
    tails = base.tails.compute()["absolute_two_tail_bounds"]
    dt_lo, dt_hi = t_lo - base.ANCHOR_T, t_hi - base.ANCHOR_T
    dz_lo, dz_hi = z_lo - base.ANCHOR_Z, z_hi - base.ANCHOR_Z

    def bounded(axis_counts: tuple[int, int], tail: str) -> arb:
        return derivative_polynomial_bernstein(
            center,
            derivative_jet,
            dt_lo,
            dt_hi,
            dz_lo,
            dz_hi,
            axis_counts,
        ) + symmetric_ball(tail)

    gradient = [
        bounded((1, 0), tails["gradient"]["t"]),
        bounded((0, 1), tails["gradient"]["z"]),
    ]
    hessian = [
        [
            bounded((2, 0), tails["hessian"]["tt"]),
            bounded((1, 1), tails["hessian"]["tz"]),
        ],
        [
            bounded((1, 1), tails["hessian"]["tz"]),
            bounded((0, 2), tails["hessian"]["zz"]),
        ],
    ]
    determinant = hessian[0][0] * hessian[1][1] - hessian[0][1] ** 2
    rejected_by = [
        axis
        for axis, value in zip(("t", "z"), gradient)
        if not value.contains(0)
    ]
    payload = {
        "schema_version": "1.0",
        "claim_id": "K1818",
        "leaf": leaf_id,
        "input_partition_digest": partition_digest(),
        "input_k1816_checkpoint_digest": input_rows()[leaf_id]["checkpoint_digest"],
        "box": [str(value) for value in box],
        "configuration": {
            "parameter_taylor_order": PARAMETER_ORDER,
            "cell_half_width": str(CELL_HALF_WIDTH),
            "observation_taylor_order": OBSERVATION_ORDER,
            "compact_cell_count": 2 * int(base.m.RADIUS / CELL_HALF_WIDTH),
            "parameter_remainder_domain": "axis-aligned hull of the K1787 anchor and exact target leaf",
            "parameter_remainder_hull": [str(value) for value in derivative_hull],
            "polynomial_range_method": "tensor Bernstein coefficients after exact affine substitution",
            "whole_line_tail_method": "K1786 analytic value-gradient-Hessian majorant on the exact leaf",
        },
        "certificate": {
            "whole_line_gradient": {
                "t": base.m.enc(gradient[0]),
                "z": base.m.enc(gradient[1]),
            },
            "whole_line_hessian": {
                "tt": base.m.enc(hessian[0][0]),
                "tz": base.m.enc(hessian[0][1]),
                "zz": base.m.enc(hessian[1][1]),
                "determinant": base.m.enc(determinant),
            },
        },
        "decision": {
            "stationary_rejected": bool(rejected_by),
            "rejected_by": rejected_by,
            "strictly_convex": bool(hessian[0][0] > 0 and determinant > 0),
            "retained_leaf_means_additional_stationary_point": False,
        },
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["checkpoint_digest"] = hashlib.sha256(canonical).hexdigest()
    return payload


def load_checkpoint(leaf_id: int) -> dict | None:
    path = checkpoint_path(leaf_id)
    if not path.exists():
        return None
    data = json.loads(path.read_text())
    canonical = dict(data)
    digest = canonical.pop("checkpoint_digest")
    encoded = json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()
    if hashlib.sha256(encoded).hexdigest() != digest:
        raise ValueError(f"checkpoint digest mismatch: {path}")
    _, box = leaf_boxes()[leaf_id]
    if data["leaf"] != leaf_id or data["box"] != [str(value) for value in box]:
        raise ValueError(f"checkpoint identity mismatch: {path}")
    if data["input_partition_digest"] != partition_digest():
        raise ValueError(f"checkpoint partition mismatch: {path}")
    if data["input_k1816_checkpoint_digest"] != input_rows()[leaf_id]["checkpoint_digest"]:
        raise ValueError(f"checkpoint K1816 provenance mismatch: {path}")
    hull = (
        min(box[0], base.ANCHOR_T),
        max(box[1], base.ANCHOR_T),
        min(box[2], base.ANCHOR_Z),
        max(box[3], base.ANCHOR_Z),
    )
    if data["configuration"].get("parameter_remainder_hull") != [str(value) for value in hull]:
        raise ValueError(f"checkpoint remainder hull mismatch: {path}")
    return data


def load_bernstein_checkpoint(leaf_id: int) -> dict | None:
    path = bernstein_checkpoint_path(leaf_id)
    if not path.exists():
        return None
    data = json.loads(path.read_text())
    canonical = dict(data)
    digest = canonical.pop("checkpoint_digest")
    encoded = json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()
    if hashlib.sha256(encoded).hexdigest() != digest:
        raise ValueError(f"checkpoint digest mismatch: {path}")
    _, box = leaf_boxes()[leaf_id]
    if data["leaf"] != leaf_id or data["box"] != [str(value) for value in box]:
        raise ValueError(f"checkpoint identity mismatch: {path}")
    if data["input_partition_digest"] != partition_digest():
        raise ValueError(f"checkpoint partition mismatch: {path}")
    if data["input_k1816_checkpoint_digest"] != input_rows()[leaf_id]["checkpoint_digest"]:
        raise ValueError(f"checkpoint K1816 provenance mismatch: {path}")
    hull = (
        min(box[0], base.ANCHOR_T),
        max(box[1], base.ANCHOR_T),
        min(box[2], base.ANCHOR_Z),
        max(box[3], base.ANCHOR_Z),
    )
    if data["configuration"].get("parameter_remainder_hull") != [str(value) for value in hull]:
        raise ValueError(f"checkpoint remainder hull mismatch: {path}")
    if data["configuration"].get("polynomial_range_method") != (
        "tensor Bernstein coefficients after exact affine substitution"
    ):
        raise ValueError(f"checkpoint polynomial range mismatch: {path}")
    return data


def ensure_leaf(leaf_id: int, replay: bool) -> dict:
    cached = load_checkpoint(leaf_id)
    if cached is not None and not replay:
        print(f"K1818 candidate leaf {leaf_id:02d}: checkpoint reused", file=sys.stderr)
        return cached
    computed = compute_leaf(leaf_id)
    atomic_json(checkpoint_path(leaf_id), computed)
    return computed


def ensure_bernstein_leaf(leaf_id: int, replay: bool) -> dict:
    cached = load_bernstein_checkpoint(leaf_id)
    if cached is not None and not replay:
        print(f"K1818 candidate leaf {leaf_id:02d}: Bernstein checkpoint reused", file=sys.stderr)
        return cached
    computed = compute_leaf_bernstein(leaf_id)
    atomic_json(bernstein_checkpoint_path(leaf_id), computed)
    return computed


def combined(rows: list[dict]) -> dict:
    rows = sorted(rows, key=lambda row: row["leaf"])
    candidates = candidate_leaf_ids()
    return {
        "input_partition_digest": partition_digest(),
        "candidate_leaf_count": len(candidates),
        "candidate_leaf_ids": candidates,
        "completed_leaf_count": len(rows),
        "completed_leaf_ids": [row["leaf"] for row in rows],
        "stationary_rejected_leaf_ids": [
            row["leaf"] for row in rows if row["decision"]["stationary_rejected"]
        ],
        "stationary_retained_leaf_ids": [
            row["leaf"] for row in rows if not row["decision"]["stationary_rejected"]
        ],
        "checkpoint_digests": {
            str(row["leaf"]): row["checkpoint_digest"] for row in rows
        },
        "leaves": rows,
    }


def artifact_data(rows: list[dict]) -> dict:
    complete_bank = combined(rows)
    certificate = {key: value for key, value in complete_bank.items() if key != "leaves"}
    certificate["stationary_rejection_evidence"] = [
        row for row in complete_bank["leaves"] if row["decision"]["stationary_rejected"]
    ]
    complete = certificate["completed_leaf_ids"] == certificate["candidate_leaf_ids"]
    rejected = certificate["stationary_rejected_leaf_ids"]
    retained = certificate["stationary_retained_leaf_ids"]
    title = (
        "The complete slab-three whole-line gradient bank classifies "
        f"{len(rejected)} stationary-free leaves and retains {len(retained)} candidates"
    )
    return {
        "schema_version": "1.0",
        "claim_id": "K1818",
        "status": "active_research",
        "title": title,
        "inputs": ["K1786", "K1787", "K1816"],
        "backend": "python-flint==0.9.0",
        "certificate": certificate,
        "decision": {
            "complete_candidate_leaf_bank_computed": complete,
            "analytic_whole_line_gradient_and_hessian_tails_composed": True,
            "stationary_rejected_leaf_count": len(rejected),
            "stationary_retained_leaf_count": len(retained),
            "retained_leaf_means_additional_stationary_point": False,
            "named_local_stationary_point_preserved": 50 in retained,
            "complete_stationary_cover": complete and not retained,
            "global_optimizer_proved": False,
        },
        "scope_guard": (
            "Gradient exclusion closes only the named rejected leaves. Retention is interval-method "
            "indeterminacy, not evidence of another stationary point; the K1787 local stationary "
            "box lies inside retained leaf 50. The residual leaves, exposed boundary and global "
            "optimizer admission remain open."
        ),
    }


def validate_current(data: dict) -> list[tuple[str, bool]]:
    certificate = data["certificate"]
    rows = certificate["stationary_rejection_evidence"]
    k1816 = json.loads(leaf_bank.ARTIFACT.read_text())["certificate"]
    k1816_rows = {row["leaf"]: row for row in k1816["leaves"]}
    candidates = [
        row["leaf"]
        for row in k1816["leaves"]
        if not row["decision"]["compact_cross_margin_positive"]
    ]
    digests_valid = True
    provenance_valid = True
    boxes_valid = True
    gradient_exclusions_valid = True
    for row in rows:
        canonical = dict(row)
        digest = canonical.pop("checkpoint_digest")
        encoded = json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()
        digests_valid &= hashlib.sha256(encoded).hexdigest() == digest
        provenance_valid &= (
            row["input_k1816_checkpoint_digest"]
            == k1816_rows[row["leaf"]]["checkpoint_digest"]
        )
        boxes_valid &= row["box"] == [str(value) for value in leaf_boxes()[row["leaf"]][1]]
        excluded_axes = [
            axis
            for axis in ("t", "z")
            if not arb(row["certificate"]["whole_line_gradient"][axis]).contains(0)
        ]
        gradient_exclusions_valid &= (
            row["decision"]["stationary_rejected"]
            and row["decision"]["rejected_by"] == excluded_axes
            and bool(excluded_axes)
        )
    rejected = certificate["stationary_rejected_leaf_ids"]
    retained = certificate["stationary_retained_leaf_ids"]
    return [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1818"),
        ("inputs", data["inputs"] == ["K1786", "K1787", "K1816"]),
        ("partition", certificate["input_partition_digest"] == partition_digest()),
        ("52 candidates", candidates == list(range(13, 65))),
        ("complete candidate ids", certificate["completed_leaf_ids"] == candidates),
        ("embedded checkpoint digests", digests_valid),
        ("K1816 provenance", provenance_valid),
        ("exact leaf boxes", boxes_valid),
        ("gradient exclusions semantic", gradient_exclusions_valid),
        ("rejected evidence", [row["leaf"] for row in rows] == rejected and all(row["decision"]["stationary_rejected"] for row in rows)),
        ("complete classification", sorted(rejected + retained) == candidates),
        ("rejected count", data["decision"]["stationary_rejected_leaf_count"] == len(rejected)),
        ("retained count", data["decision"]["stationary_retained_leaf_count"] == len(retained)),
        ("dynamic title", data["title"] == (
            "The complete slab-three whole-line gradient bank classifies "
            f"{len(rejected)} stationary-free leaves and retains {len(retained)} candidates"
        )),
        ("retention fenced", not data["decision"]["retained_leaf_means_additional_stationary_point"]),
        ("local stationary leaf preserved", data["decision"]["named_local_stationary_point_preserved"] and 50 in retained),
        ("stationary cover open", not data["decision"]["complete_stationary_cover"]),
        ("global withheld", not data["decision"]["global_optimizer_proved"]),
    ]


def validate_legacy(data: dict) -> list[tuple[str, bool]]:
    certificate = data["certificate"]
    return [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1818"),
        ("78 leaves", certificate["leaf_count"] == 78),
        ("two leaves complete", certificate["completed_leaf_ids"] == [0, 1]),
        ("76 leaves remain", certificate["remaining_leaf_count"] == 76),
        ("stationary cover open", not data["decision"]["complete_stationary_cover"]),
        ("global withheld", not data["decision"]["global_optimizer_proved"]),
    ]


def validate_correction(data: dict) -> list[tuple[str, bool]]:
    certificate = data["certificate"]
    return [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1818"),
        ("partition", certificate["input_partition_digest"] == partition_digest()),
        ("invalidated bank", certificate["invalidated_checkpoint_count"] == 52),
        ("invalidated exclusions", certificate["invalidated_stationary_rejected_leaf_ids"] == [13, 27, 28, 39, 40, 41, 42, 52, 53, 64]),
        ("corrected domain", certificate["corrected_parameter_remainder_domain"] == "axis-aligned hull of the K1787 anchor and exact target leaf"),
        ("no stationary exclusions", data["decision"]["stationary_rejected_leaf_count"] == 0),
        ("all candidates reopened", data["decision"]["stationary_retained_leaf_count"] == 52),
        ("stationary cover open", not data["decision"]["complete_stationary_cover"]),
        ("global withheld", not data["decision"]["global_optimizer_proved"]),
    ]


def validate_bernstein_kernel() -> list[tuple[str, bool]]:
    bilinear = affine_power_to_bernstein_range(
        {(0, 0): arb(1), (1, 0): arb(2), (0, 1): arb(3), (1, 1): arb(4)},
        arb(0),
        arb(1),
        arb(0),
        arb(1),
        6,
    )
    signed = affine_power_to_bernstein_range(
        {(1, 0): arb(1), (0, 1): arb(-1)},
        arb(-1),
        arb(2),
        arb(-3),
        arb(4),
        5,
    )
    return [
        ("Bernstein bilinear lower endpoint", bilinear.contains(arb(1)) and bilinear > 0),
        ("Bernstein bilinear upper endpoint", bilinear.contains(arb(10)) and bilinear < 11),
        ("Bernstein signed rectangle", signed.contains(arb(-5)) and signed.contains(arb(5))),
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--leaf", type=int, action="append", default=[])
    parser.add_argument("--bernstein-leaf", type=int, action="append", default=[])
    parser.add_argument("--resume-bank", action="store_true")
    parser.add_argument("--resume-bernstein-bank", action="store_true")
    parser.add_argument("--max-new", type=int)
    parser.add_argument("--replay", action="store_true")
    parser.add_argument("--summary", action="store_true")
    parser.add_argument("--print-artifact", action="store_true")
    args = parser.parse_args()

    if (
        not args.leaf
        and not args.bernstein_leaf
        and not args.resume_bank
        and not args.resume_bernstein_bank
    ):
        stored = json.loads(ARTIFACT.read_text())
        if "remainder_correction" in stored:
            checks = validate_correction(stored)
        elif "stationary_rejection_evidence" in stored["certificate"]:
            checks = validate_current(stored)
        else:
            checks = validate_legacy(stored)
        checks += validate_bernstein_kernel()
        for index, (label, ok) in enumerate(checks, 1):
            assert ok, label
            print(f"PASS {index:02d}: {label}")
        print(f"RESULT: PASS {len(checks)}/{len(checks)}")
        return

    use_bernstein = bool(args.bernstein_leaf or args.resume_bernstein_bank)
    selected = args.bernstein_leaf or args.leaf or candidate_leaf_ids()
    rows = []
    new_count = 0
    for leaf_id in selected:
        cached = (
            load_bernstein_checkpoint(leaf_id)
            if use_bernstein
            else load_checkpoint(leaf_id)
        )
        if cached is None or args.replay:
            if args.max_new is not None and new_count >= args.max_new:
                continue
            new_count += 1
        rows.append(
            ensure_bernstein_leaf(leaf_id, args.replay)
            if use_bernstein
            else ensure_leaf(leaf_id, args.replay)
        )
    if args.resume_bank:
        rows = [
            row
            for leaf_id in candidate_leaf_ids()
            if (row := load_checkpoint(leaf_id)) is not None
        ]
    if args.resume_bernstein_bank:
        rows = [
            row
            for leaf_id in candidate_leaf_ids()
            if (row := load_bernstein_checkpoint(leaf_id)) is not None
        ]
    data = artifact_data(rows) if args.print_artifact else combined(rows)
    if args.summary:
        if args.print_artifact:
            data["certificate"] = {
                key: value for key, value in data["certificate"].items()
                if key != "stationary_rejection_evidence"
            }
        else:
            data = {key: value for key, value in data.items() if key != "leaves"}
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
