#!/usr/bin/env python3
"""K1816: restart-safe leafwise fixed-score bank on slab three.

K1813 measured that the fixed K1787-score witness loses its sign on a complete
K1794 parent almost entirely through the absolute degree-six remainder.  This
producer changes only that proved source of loss: it recenters a normalized
Arb jet on each exact K1796 leaf.  Each leaf is written
atomically to ignored local checkpoint storage, so interruption never turns a
partial bank into evidence and completed leaves are replayable without another
quadrature.
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
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1816-full-fisher-slab-three-leafwise-score-bank.json"
CHECKPOINT_DIR = ROOT / "_local/k1816-leafwise-score-checkpoints"


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


m = None
atlas = None

ANCHOR_T = F(265664669701527, 5000000000000000)
ANCHOR_Z = F(8805034043103, 15625000000000)
THRESHOLD = F(7958932265249, 50000000000000000000)
FIXED_SCORE_CACHE: dict[tuple[int, int, str], list[tuple[object, object]]] = {}
MARGIN_METHOD = "absolute"


class S:
    """Observation Taylor series with scalar Arb coefficients.

    K1807's fixed anchor score has no parameter dependence.  Computing it with
    the full bivariate parameter-jet algebra is exact but needlessly repeats
    zero nonconstant coefficients on every observation cell.  This scalar
    series is algebraically identical for that fixed-score subexpression and
    is lifted back into the parameter jet only after the score is formed.
    """

    def __init__(self, coefficients):
        self.c = [m.arb(value) for value in coefficients]

    @property
    def n(self):
        return len(self.c)

    @staticmethod
    def lift(value, n):
        if isinstance(value, S):
            assert value.n == n
            return value
        return S([value] + [0] * (n - 1))

    def __add__(self, other):
        other = self.lift(other, self.n)
        return S([self.c[index] + other.c[index] for index in range(self.n)])

    __radd__ = __add__

    def __neg__(self):
        return S([-value for value in self.c])

    def __sub__(self, other):
        return self + (-self.lift(other, self.n))

    def __rsub__(self, other):
        return self.lift(other, self.n) - self

    def __mul__(self, other):
        other = self.lift(other, self.n)
        return S([
            sum((self.c[k] * other.c[index - k]
                 for k in range(index + 1)), m.arb(0))
            for index in range(self.n)
        ])

    __rmul__ = __mul__

    def reciprocal(self):
        out = [1 / self.c[0]]
        for index in range(1, self.n):
            out.append(-sum((self.c[k] * out[index - k]
                             for k in range(1, index + 1)), m.arb(0)) / self.c[0])
        return S(out)

    def __truediv__(self, other):
        return self * self.lift(other, self.n).reciprocal()

    def __rtruediv__(self, other):
        return self.lift(other, self.n) / self

    def exp(self):
        out = [self.c[0].exp()]
        for index in range(1, self.n):
            out.append(sum((m.aq(k) * self.c[k] * out[index - k]
                            for k in range(1, index + 1)), m.arb(0)) / m.aq(index))
        return S(out)

    def sinh(self):
        return (self.exp() - (-self).exp()) / 2

    def cosh(self):
        return (self.exp() + (-self).exp()) / 2


def fq(value) -> F:
    return F(str(value))


def ensure_backends() -> None:
    global m, atlas
    if m is None:
        m = load(
            "k1807_for_k1816",
            ROOT / "tests/channel-swings/k1807_full_fisher_anchored_score_compact_taylor.py",
        )
        m.reference_witness_integrands = m.witness_integrands
        m.witness_integrands = witness_integrands
    if atlas is None:
        atlas = load(
            "k1804_for_k1816",
            ROOT / "tests/channel-swings/k1804_full_fisher_deduplicated_boundary_atlas.py",
        )


def fixed_anchor_score(y):
    """Evaluate K1787's fixed score without a vacuous parameter jet."""
    observation_center = y.c[0].constant
    cache_key = (
        m.P.order,
        y.n,
        observation_center.str(50, radius=True, more=True),
    )
    for cached_center, cached_score in FIXED_SCORE_CACHE.get(cache_key, []):
        if (cached_center.contains(observation_center)
                and observation_center.contains(cached_center)):
            return cached_score
    scalar_y = S([coefficient.constant for coefficient in y.c])
    t0, z0 = m.aq(ANCHOR_T), m.aq(ANCHOR_Z)
    c = 2 - m.aq(m.Q) / t0**2
    p = c / (c + z0**2)
    a = 1 - z0
    b = 1 + c / z0
    v = 1 - t0
    ra, rb, rt = a.sqrt(), b.sqrt(), t0.sqrt()
    ca, cb = rt * ra / v, rt * rb / v
    wa = p * (-t0 * a / (2 * v)).exp()
    wb = (1 - p) * (-t0 * b / (2 * v)).exp()
    denominator = wa * (ca * scalar_y).cosh() + wb * (cb * scalar_y).cosh()
    residual = (
        wa * ra * (ca * scalar_y).sinh()
        + wb * rb * (cb * scalar_y).sinh()
        - rt * scalar_y * denominator
    )
    score = rt * residual / (v * denominator)
    lifted = m.Y([m.P(coefficient) for coefficient in score.c])
    FIXED_SCORE_CACHE.setdefault(cache_key, []).append(
        (m.arb(observation_center), lifted)
    )
    return lifted


def witness_integrands(y, t, z):
    """K1807 witness with a scalar-only evaluation of the fixed score."""
    denominator, residual, gaussian, rt, rv, v = m.mixture_parts(y, t, z)
    h0 = fixed_anchor_score(y)
    normal = m.P((2 * m.arb.pi()).sqrt())
    a_integrand = rt * gaussian * residual * h0 / (v * rv * normal)
    b_integrand = gaussian * denominator * h0**2 / (rv * normal)
    return a_integrand, b_integrand


@cache
def leaves():
    ensure_backends()
    return tuple(
        (cell, tuple(fq(value) for value in box))
        for slab, cell, box in atlas.retained_boxes()
        if slab == 3
    )


def partition_digest() -> str:
    data = json.loads(
        (ROOT / "lab/process/k1796-full-fisher-retained-box-enclosure-bank.json").read_text()
    )
    return data["enclosure"]["partition_digest"]


def observation_config() -> dict:
    config = {
        "cell_half_width": str(m.CELL_HALF_WIDTH),
        "observation_taylor_order": m.OBSERVATION_ORDER,
        "compact_cell_count": 2 * int(m.RADIUS / m.CELL_HALF_WIDTH),
    }
    if MARGIN_METHOD != "absolute":
        config["margin_bound_method"] = MARGIN_METHOD
    return config


def bernstein_polynomial_lower(
    coefficients: dict[str, str],
    radius_t: F,
    radius_z: F,
    degree: int,
):
    """Lower-bound a centered bivariate power polynomial on its rectangle.

    Substitute ``dt=radius_t*(2*x-1)`` and
    ``dz=radius_z*(2*y-1)``, then convert the resulting power coefficients on
    ``[0,1]^2`` to the tensor Bernstein basis of bidegree ``(degree, degree)``.
    Every polynomial value lies in the convex hull of those coefficient
    intervals, so the smallest lower endpoint is a rigorous lower bound.  The
    separately enclosed total-degree remainder is composed by the caller.
    """
    power = {(a, b): m.arb(0) for a in range(degree + 1) for b in range(degree + 1)}
    for key, text in coefficients.items():
        i, j = (int(value) for value in key.split(","))
        if i + j > degree:
            continue
        scaled = m.arb(text) * m.aq(radius_t**i * radius_z**j)
        for a in range(i + 1):
            t_factor = F(comb(i, a) * 2**a * (-1) ** (i - a))
            for b in range(j + 1):
                z_factor = F(comb(j, b) * 2**b * (-1) ** (j - b))
                power[(a, b)] += scaled * m.aq(t_factor * z_factor)
    lower = None
    for i in range(degree + 1):
        for j in range(degree + 1):
            coefficient = m.arb(0)
            for a in range(i + 1):
                t_factor = F(comb(i, a), comb(degree, a))
                for b in range(j + 1):
                    z_factor = F(comb(j, b), comb(degree, b))
                    coefficient += power[(a, b)] * m.aq(t_factor * z_factor)
            candidate = m.arb(coefficient.lower())
            if lower is None or candidate < lower:
                lower = candidate
    assert lower is not None
    return lower


def validate_bernstein_transform() -> None:
    """Exact affine controls for the power-to-Bernstein conversion."""
    radius_t, radius_z = F(3, 10), F(1, 5)
    constant = bernstein_polynomial_lower({"0,0": "3"}, radius_t, radius_z, 3)
    affine = bernstein_polynomial_lower(
        {"0,0": "1", "1,0": "1", "0,1": "2"},
        radius_t,
        radius_z,
        3,
    )
    assert abs(constant - m.aq(3)) < m.arb("1e-70")
    assert abs(affine - m.aq(F(1) - radius_t - 2 * radius_z)) < m.arb("1e-70")


def compact_summary(certificate: dict, parameter_order: int) -> dict:
    config = observation_config()
    compact_bounds = dict(certificate["compact_bounds"])
    if MARGIN_METHOD == "bernstein":
        radius_t = F(certificate["radius"]["t"])
        radius_z = F(certificate["radius"]["z"])
        polynomial_lower = bernstein_polynomial_lower(
            certificate["center_normalized_coefficients"]["L"],
            radius_t,
            radius_z,
            parameter_order - 1,
        )
        remainder = certificate["degree_six_remainder_bounds"]["L"]
        margin_lower = polynomial_lower - m.arb(m.arb(remainder).upper())
        compact_bounds["cross_margin_absolute_lower"] = compact_bounds[
            "cross_margin_lower"
        ]
        compact_bounds["cross_margin_bernstein_polynomial_lower"] = m.enc(
            polynomial_lower
        )
        compact_bounds["cross_margin_lower"] = m.enc(margin_lower)
        compact_bounds["cross_margin_positive"] = bool(margin_lower > 0)
        compact_bounds["margin_bound_method"] = "bernstein"
    return {
        "rectangle": certificate["rectangle"],
        "center": certificate["center"],
        "radius": certificate["radius"],
        "anchor": certificate["anchor"],
        "threshold": certificate["threshold"],
        "window": certificate["window"],
        "cell_half_width": config["cell_half_width"],
        "observation_taylor_order": config["observation_taylor_order"],
        "parameter_taylor_order": certificate["parameter_taylor_order"],
        "compact_cell_count": config["compact_cell_count"],
        "compact_bounds": compact_bounds,
        f"degree_{parameter_order}_remainder_bounds": certificate[
            "degree_six_remainder_bounds"
        ],
    }


def checkpoint_path(leaf_id: int, parameter_order: int) -> Path:
    suffix = "" if parameter_order == 6 else f"-order-{parameter_order:02d}"
    config = observation_config()
    width = F(config["cell_half_width"])
    config_suffix = (
        f"-cell-{width.numerator}-{width.denominator}"
        f"-observation-{config['observation_taylor_order']:02d}"
    )
    if MARGIN_METHOD != "absolute":
        config_suffix += f"-margin-{MARGIN_METHOD}"
    return CHECKPOINT_DIR / f"leaf-{leaf_id:03d}{suffix}{config_suffix}.json"


def dyadic_intervals(lo: F, hi: F, depth: int) -> tuple[tuple[F, F], ...]:
    if depth < 1:
        raise ValueError("subdivision depth must be positive")
    count = 2**depth
    width = (hi - lo) / count
    return tuple((lo + index * width, lo + (index + 1) * width) for index in range(count))


def subdivision_boxes(
    leaf_id: int,
    axis: str,
    depth: int = 1,
) -> tuple[tuple[F, ...], ...]:
    """Bisect one exact K1796 leaf without changing its covered union."""
    if axis not in {"t", "z", "both"}:
        raise ValueError(f"unsupported subdivision axis: {axis}")
    _, box = leaves()[leaf_id]
    t_lo, t_hi, z_lo, z_hi = box
    t_intervals = dyadic_intervals(t_lo, t_hi, depth) if axis in {"t", "both"} else ((t_lo, t_hi),)
    z_intervals = dyadic_intervals(z_lo, z_hi, depth) if axis in {"z", "both"} else ((z_lo, z_hi),)
    return tuple(
        (child_t_lo, child_t_hi, child_z_lo, child_z_hi)
        for child_t_lo, child_t_hi in t_intervals
        for child_z_lo, child_z_hi in z_intervals
    )


def grid_boxes(
    leaf_id: int,
    t_depth: int,
    z_depth: int,
) -> tuple[tuple[F, ...], ...]:
    """Return a deterministic dyadic t-by-z grid over one exact leaf."""
    if t_depth < 0 or z_depth < 0 or t_depth + z_depth < 1:
        raise ValueError("grid subdivision requires nonnegative depths with a positive sum")
    _, box = leaves()[leaf_id]
    t_lo, t_hi, z_lo, z_hi = box
    t_intervals = dyadic_intervals(t_lo, t_hi, t_depth) if t_depth else ((t_lo, t_hi),)
    z_intervals = dyadic_intervals(z_lo, z_hi, z_depth) if z_depth else ((z_lo, z_hi),)
    return tuple(
        (child_t_lo, child_t_hi, child_z_lo, child_z_hi)
        for child_t_lo, child_t_hi in t_intervals
        for child_z_lo, child_z_hi in z_intervals
    )


def point_box(leaf_id: int, location: str) -> tuple[F, ...]:
    """Return a degenerate exact rational box for a route-changing control."""
    _, box = leaves()[leaf_id]
    t_lo, t_hi, z_lo, z_hi = box
    t_mid, z_mid = (t_lo + t_hi) / 2, (z_lo + z_hi) / 2
    points = {
        "lower-t-mid-z": (t_lo, t_lo, z_mid, z_mid),
        "center": (t_mid, t_mid, z_mid, z_mid),
        "lower-lower": (t_lo, t_lo, z_lo, z_lo),
        "lower-upper": (t_lo, t_lo, z_hi, z_hi),
    }
    if location not in points:
        raise ValueError(f"unsupported point location: {location}")
    return points[location]


def subdivision_checkpoint_path(
    leaf_id: int,
    axis: str,
    child: int,
    parameter_order: int,
    depth: int = 1,
) -> Path:
    suffix = "" if parameter_order == 6 else f"-order-{parameter_order:02d}"
    config = observation_config()
    width = F(config["cell_half_width"])
    config_suffix = (
        f"-cell-{width.numerator}-{width.denominator}"
        f"-observation-{config['observation_taylor_order']:02d}"
    )
    if MARGIN_METHOD != "absolute":
        config_suffix += f"-margin-{MARGIN_METHOD}"
    depth_suffix = "" if depth == 1 else f"-depth-{depth:02d}"
    return CHECKPOINT_DIR / (
        f"leaf-{leaf_id:03d}-split-{axis}{depth_suffix}-child-{child:02d}"
        f"{suffix}{config_suffix}.json"
    )


def grid_checkpoint_path(
    leaf_id: int,
    t_depth: int,
    z_depth: int,
    child: int,
    parameter_order: int,
) -> Path:
    suffix = "" if parameter_order == 6 else f"-order-{parameter_order:02d}"
    config = observation_config()
    width = F(config["cell_half_width"])
    config_suffix = (
        f"-cell-{width.numerator}-{width.denominator}"
        f"-observation-{config['observation_taylor_order']:02d}"
    )
    return CHECKPOINT_DIR / (
        f"leaf-{leaf_id:03d}-grid-t{t_depth:02d}-z{z_depth:02d}"
        f"-child-{child:03d}{suffix}{config_suffix}.json"
    )


def point_checkpoint_path(
    leaf_id: int,
    location: str,
    parameter_order: int,
) -> Path:
    suffix = "" if parameter_order == 6 else f"-order-{parameter_order:02d}"
    config = observation_config()
    width = F(config["cell_half_width"])
    config_suffix = (
        f"-cell-{width.numerator}-{width.denominator}"
        f"-observation-{config['observation_taylor_order']:02d}"
    )
    return CHECKPOINT_DIR / (
        f"leaf-{leaf_id:03d}-point-{location}{suffix}{config_suffix}.json"
    )


def atomic_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    temporary.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    os.replace(temporary, path)


def compute_box(
    leaf_id: int,
    parameter_order: int,
    box: tuple[F, ...],
    subdivision: dict | None = None,
) -> dict:
    ensure_backends()
    all_leaves = leaves()
    if not 0 <= leaf_id < len(all_leaves):
        raise ValueError(f"leaf id {leaf_id} outside 0..{len(all_leaves) - 1}")
    cell, parent_box = all_leaves[leaf_id]
    m.ANCHOR_T, m.ANCHOR_Z, m.THRESHOLD = ANCHOR_T, ANCHOR_Z, THRESHOLD
    m.PARAMETER_ORDER = parameter_order
    m.P.order = parameter_order
    m.T_LO, m.T_HI, m.Z_LO, m.Z_HI = box
    label = f"leaf {leaf_id:02d}/77"
    if subdivision is not None:
        label += (
            f" split-{subdivision['axis']}"
            f" child {subdivision['child'] + 1}/{subdivision['child_count']}"
        )
    print(
        f"K1816 {label}: order-{parameter_order} centered jet",
        file=sys.stderr,
        flush=True,
    )
    certificate = compact_summary(m.compute(), parameter_order)
    payload = {
        "schema_version": "1.0",
        "claim_id": "K1816",
        "leaf": leaf_id,
        "input_cell": cell,
        "input_partition_digest": partition_digest(),
        "box": [str(value) for value in box],
        "parameter_taylor_order": parameter_order,
        "observation_config": observation_config(),
        "certificate": certificate,
        "decision": {
            "compact_cross_margin_positive": certificate["compact_bounds"][
                "cross_margin_positive"
            ],
            "negative_margin_is_counterexample": False,
        },
    }
    if subdivision is not None:
        payload["subdivision"] = {
            **subdivision,
            "parent_box": [str(value) for value in parent_box],
        }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["checkpoint_digest"] = hashlib.sha256(canonical).hexdigest()
    return payload


def compute_leaf(leaf_id: int, parameter_order: int) -> dict:
    return compute_box(leaf_id, parameter_order, leaves()[leaf_id][1])


def load_checkpoint(leaf_id: int, parameter_order: int) -> dict | None:
    path = checkpoint_path(leaf_id, parameter_order)
    if not path.exists():
        return None
    data = json.loads(path.read_text())
    canonical = dict(data)
    digest = canonical.pop("checkpoint_digest")
    encoded = json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()
    if hashlib.sha256(encoded).hexdigest() != digest:
        raise ValueError(f"checkpoint digest mismatch: {path}")
    expected_cell, expected_box = leaves()[leaf_id]
    if data["leaf"] != leaf_id or data["input_cell"] != expected_cell:
        raise ValueError(f"checkpoint identity mismatch: {path}")
    if data["box"] != [str(value) for value in expected_box]:
        raise ValueError(f"checkpoint box mismatch: {path}")
    if data["input_partition_digest"] != partition_digest():
        raise ValueError(f"checkpoint partition mismatch: {path}")
    if data.get("observation_config") != observation_config():
        raise ValueError(f"checkpoint observation configuration mismatch: {path}")
    certificate_config = {
        key: data["certificate"][key]
        for key in (
            "cell_half_width",
            "observation_taylor_order",
            "compact_cell_count",
        )
    }
    if certificate_config != observation_config():
        raise ValueError(f"checkpoint certificate configuration mismatch: {path}")
    recorded_order = data.get(
        "parameter_taylor_order", data["certificate"]["parameter_taylor_order"]
    )
    if recorded_order != parameter_order:
        raise ValueError(f"checkpoint order mismatch: {path}")
    return data


def ensure_leaf(leaf_id: int, parameter_order: int, replay: bool) -> dict:
    cached = load_checkpoint(leaf_id, parameter_order)
    if cached is not None and not replay:
        print(f"K1816 leaf {leaf_id:02d}/77: checkpoint reused", file=sys.stderr)
        return cached
    computed = compute_leaf(leaf_id, parameter_order)
    atomic_json(checkpoint_path(leaf_id, parameter_order), computed)
    return computed


def load_subdivision_checkpoint(
    leaf_id: int,
    axis: str,
    child: int,
    parameter_order: int,
    depth: int = 1,
) -> dict | None:
    boxes = subdivision_boxes(leaf_id, axis, depth)
    if not 0 <= child < len(boxes):
        raise ValueError(f"subdivision child {child} outside 0..{len(boxes) - 1}")
    path = subdivision_checkpoint_path(leaf_id, axis, child, parameter_order, depth)
    if not path.exists():
        return None
    data = json.loads(path.read_text())
    canonical = dict(data)
    digest = canonical.pop("checkpoint_digest")
    encoded = json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()
    if hashlib.sha256(encoded).hexdigest() != digest:
        raise ValueError(f"checkpoint digest mismatch: {path}")
    expected_cell, parent_box = leaves()[leaf_id]
    expected_subdivision = {
        "axis": axis,
        "child": child,
        "child_count": len(boxes),
        "parent_box": [str(value) for value in parent_box],
    }
    if depth != 1:
        expected_subdivision["depth"] = depth
    if data["leaf"] != leaf_id or data["input_cell"] != expected_cell:
        raise ValueError(f"checkpoint identity mismatch: {path}")
    if data["box"] != [str(value) for value in boxes[child]]:
        raise ValueError(f"checkpoint box mismatch: {path}")
    if data.get("subdivision") != expected_subdivision:
        raise ValueError(f"checkpoint subdivision mismatch: {path}")
    if data["input_partition_digest"] != partition_digest():
        raise ValueError(f"checkpoint partition mismatch: {path}")
    if data.get("observation_config") != observation_config():
        raise ValueError(f"checkpoint observation configuration mismatch: {path}")
    if data.get("parameter_taylor_order") != parameter_order:
        raise ValueError(f"checkpoint order mismatch: {path}")
    return data


def ensure_subdivision_child(
    leaf_id: int,
    axis: str,
    child: int,
    parameter_order: int,
    replay: bool,
    depth: int = 1,
) -> dict:
    cached = load_subdivision_checkpoint(leaf_id, axis, child, parameter_order, depth)
    if cached is not None and not replay:
        print(
            f"K1816 leaf {leaf_id:02d} split-{axis} depth {depth} child {child}: checkpoint reused",
            file=sys.stderr,
        )
        return cached
    boxes = subdivision_boxes(leaf_id, axis, depth)
    subdivision = {"axis": axis, "child": child, "child_count": len(boxes)}
    if depth != 1:
        subdivision["depth"] = depth
    computed = compute_box(leaf_id, parameter_order, boxes[child], subdivision)
    atomic_json(
        subdivision_checkpoint_path(leaf_id, axis, child, parameter_order, depth),
        computed,
    )
    return computed


def load_grid_checkpoint(
    leaf_id: int,
    t_depth: int,
    z_depth: int,
    child: int,
    parameter_order: int,
) -> dict | None:
    boxes = grid_boxes(leaf_id, t_depth, z_depth)
    if not 0 <= child < len(boxes):
        raise ValueError(f"grid child {child} outside 0..{len(boxes) - 1}")
    path = grid_checkpoint_path(leaf_id, t_depth, z_depth, child, parameter_order)
    if not path.exists():
        return None
    data = json.loads(path.read_text())
    canonical = dict(data)
    digest = canonical.pop("checkpoint_digest")
    encoded = json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()
    if hashlib.sha256(encoded).hexdigest() != digest:
        raise ValueError(f"checkpoint digest mismatch: {path}")
    expected_cell, parent_box = leaves()[leaf_id]
    expected_subdivision = {
        "axis": "grid",
        "t_depth": t_depth,
        "z_depth": z_depth,
        "child": child,
        "child_count": len(boxes),
        "parent_box": [str(value) for value in parent_box],
    }
    if data["leaf"] != leaf_id or data["input_cell"] != expected_cell:
        raise ValueError(f"checkpoint identity mismatch: {path}")
    if data["box"] != [str(value) for value in boxes[child]]:
        raise ValueError(f"checkpoint box mismatch: {path}")
    if data.get("subdivision") != expected_subdivision:
        raise ValueError(f"checkpoint subdivision mismatch: {path}")
    if data["input_partition_digest"] != partition_digest():
        raise ValueError(f"checkpoint partition mismatch: {path}")
    if data.get("observation_config") != observation_config():
        raise ValueError(f"checkpoint observation configuration mismatch: {path}")
    if data.get("parameter_taylor_order") != parameter_order:
        raise ValueError(f"checkpoint order mismatch: {path}")
    return data


def ensure_grid_child(
    leaf_id: int,
    t_depth: int,
    z_depth: int,
    child: int,
    parameter_order: int,
    replay: bool,
) -> dict:
    cached = load_grid_checkpoint(
        leaf_id, t_depth, z_depth, child, parameter_order
    )
    if cached is not None and not replay:
        print(
            f"K1816 leaf {leaf_id:02d} grid t{t_depth} z{z_depth} child {child}: checkpoint reused",
            file=sys.stderr,
        )
        return cached
    boxes = grid_boxes(leaf_id, t_depth, z_depth)
    subdivision = {
        "axis": "grid",
        "t_depth": t_depth,
        "z_depth": z_depth,
        "child": child,
        "child_count": len(boxes),
    }
    computed = compute_box(leaf_id, parameter_order, boxes[child], subdivision)
    atomic_json(
        grid_checkpoint_path(leaf_id, t_depth, z_depth, child, parameter_order),
        computed,
    )
    return computed


def load_point_checkpoint(
    leaf_id: int,
    location: str,
    parameter_order: int,
) -> dict | None:
    box = point_box(leaf_id, location)
    path = point_checkpoint_path(leaf_id, location, parameter_order)
    if not path.exists():
        return None
    data = json.loads(path.read_text())
    canonical = dict(data)
    digest = canonical.pop("checkpoint_digest")
    encoded = json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()
    if hashlib.sha256(encoded).hexdigest() != digest:
        raise ValueError(f"checkpoint digest mismatch: {path}")
    expected_cell, parent_box = leaves()[leaf_id]
    expected_subdivision = {
        "axis": "point",
        "location": location,
        "child": 0,
        "child_count": 1,
        "parent_box": [str(value) for value in parent_box],
    }
    if data["leaf"] != leaf_id or data["input_cell"] != expected_cell:
        raise ValueError(f"checkpoint identity mismatch: {path}")
    if data["box"] != [str(value) for value in box]:
        raise ValueError(f"checkpoint box mismatch: {path}")
    if data.get("subdivision") != expected_subdivision:
        raise ValueError(f"checkpoint point mismatch: {path}")
    if data["input_partition_digest"] != partition_digest():
        raise ValueError(f"checkpoint partition mismatch: {path}")
    if data.get("observation_config") != observation_config():
        raise ValueError(f"checkpoint observation configuration mismatch: {path}")
    if data.get("parameter_taylor_order") != parameter_order:
        raise ValueError(f"checkpoint order mismatch: {path}")
    return data


def ensure_point(
    leaf_id: int,
    location: str,
    parameter_order: int,
    replay: bool,
) -> dict:
    cached = load_point_checkpoint(leaf_id, location, parameter_order)
    if cached is not None and not replay:
        print(
            f"K1816 leaf {leaf_id:02d} point {location}: checkpoint reused",
            file=sys.stderr,
        )
        return cached
    subdivision = {
        "axis": "point",
        "location": location,
        "child": 0,
        "child_count": 1,
    }
    computed = compute_box(
        leaf_id,
        parameter_order,
        point_box(leaf_id, location),
        subdivision,
    )
    canonical = dict(computed)
    canonical.pop("checkpoint_digest")
    margin = m.arb(computed["certificate"]["compact_bounds"]["cross_margin_lower"])
    computed["decision"]["fixed_witness_margin_strictly_negative"] = margin < 0
    canonical = dict(computed)
    canonical.pop("checkpoint_digest", None)
    encoded = json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()
    computed["checkpoint_digest"] = hashlib.sha256(encoded).hexdigest()
    atomic_json(point_checkpoint_path(leaf_id, location, parameter_order), computed)
    return computed


def combined_subdivisions(rows: list[dict]) -> dict:
    rows = sorted(rows, key=lambda row: (row["leaf"], row["subdivision"]["child"]))
    parent_rows: dict[int, list[dict]] = {}
    for row in rows:
        parent_rows.setdefault(row["leaf"], []).append(row)
    return {
        "input_partition_digest": partition_digest(),
        "completed_child_count": len(rows),
        "positive_child_count": sum(
            row["decision"]["compact_cross_margin_positive"] for row in rows
        ),
        "parent_results": {
            str(leaf_id): {
                "axis": children[0]["subdivision"]["axis"],
                "completed_child_count": len(children),
                "child_count": children[0]["subdivision"]["child_count"],
                "all_children_positive": (
                    len(children) == children[0]["subdivision"]["child_count"]
                    and all(
                        child["decision"]["compact_cross_margin_positive"]
                        for child in children
                    )
                ),
                "checkpoint_digests": {
                    str(child["subdivision"]["child"]): child["checkpoint_digest"]
                    for child in children
                },
            }
            for leaf_id, children in sorted(parent_rows.items())
        },
        "children": rows,
    }


def combined(rows: list[dict], parameter_order: int) -> dict:
    rows = sorted(rows, key=lambda row: row["leaf"])
    return {
        "input_partition_digest": partition_digest(),
        "observation_config": observation_config(),
        "parameter_taylor_order": parameter_order,
        "leaf_count": len(leaves()),
        "completed_leaf_count": len(rows),
        "completed_leaf_ids": [row["leaf"] for row in rows],
        "positive_compact_margin_count": sum(
            row["decision"]["compact_cross_margin_positive"] for row in rows
        ),
        "nonpositive_or_indeterminate_leaf_ids": [
            row["leaf"]
            for row in rows
            if not row["decision"]["compact_cross_margin_positive"]
        ],
        "checkpoint_digests": {
            str(row["leaf"]): row["checkpoint_digest"] for row in rows
        },
        "leaves": rows,
    }


def fallback_scouts() -> dict:
    """Collect the configuration-bound leaf-53 route discriminators."""
    scouts = []
    for path in sorted(CHECKPOINT_DIR.glob("leaf-053*.json")):
        data = json.loads(path.read_text())
        config = data.get("observation_config")
        if data.get("parameter_taylor_order") != 8 or config is None:
            continue
        if data.get("subdivision") is None and config["observation_taylor_order"] != 16:
            continue
        canonical = dict(data)
        digest = canonical.pop("checkpoint_digest")
        encoded = json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()
        if hashlib.sha256(encoded).hexdigest() != digest:
            raise ValueError(f"checkpoint digest mismatch: {path}")
        if data["input_partition_digest"] != partition_digest():
            raise ValueError(f"checkpoint partition mismatch: {path}")
        remainder_key = "degree_8_remainder_bounds"
        scouts.append({
            "checkpoint_file": path.name,
            "box": data["box"],
            "observation_config": config,
            "subdivision": data.get("subdivision"),
            "compact_cross_margin_lower": data["certificate"]["compact_bounds"][
                "cross_margin_lower"
            ],
            "degree_8_remainder_bounds": data["certificate"].get(remainder_key),
            "decision": data["decision"],
            "checkpoint_digest": digest,
        })
    point = next(
        (
            scout for scout in scouts
            if (scout.get("subdivision") or {}).get("location") == "lower-t-mid-z"
            and scout["observation_config"]["observation_taylor_order"] == 16
        ),
        None,
    )
    whole_order_sixteen = next(
        (
            scout for scout in scouts
            if scout.get("subdivision") is None
            and scout["observation_config"]["observation_taylor_order"] == 16
        ),
        None,
    )
    if point is None or whole_order_sixteen is None:
        raise ValueError("fallback scouts require the whole-leaf and exact-point controls")
    return {
        "leaf": 53,
        "scouts": scouts,
        "route_findings": {
            "whole_leaf_order_16_positive": whole_order_sixteen["decision"][
                "compact_cross_margin_positive"
            ],
            "exact_lower_t_mid_z_point_positive": point["decision"][
                "compact_cross_margin_positive"
            ],
            "exact_point_margin": point["compact_cross_margin_lower"],
            "fixed_witness_counterexample": False,
            "uniform_value_cover_complete": False,
            "next_route": "compose analytic tails and prioritize stationary/gradient rejection over deeper value subdivision",
        },
    }


def provisional_artifact() -> dict:
    """Embed the calibrated scouts and completed production leaves."""
    order_six = load_checkpoint(0, 6)
    order_eight = load_checkpoint(0, 8)
    order_seven = [
        row for leaf_id in range(len(leaves()))
        if (row := load_checkpoint(leaf_id, 7)) is not None
    ]
    if order_six is None or order_eight is None or len(order_seven) < 2:
        raise ValueError("K1816 provisional artifact requires 6/7/8 calibration and two order-seven leaves")
    return {
        "schema_version": "1.0",
        "claim_id": "K1816",
        "status": "active_research",
        "title": "Leafwise order-seven fixed-score calibration on the slab-three frontier",
        "inputs": ["K1787", "K1796", "K1806", "K1813"],
        "backend": "python-flint==0.9.0",
        "certificate": {
            "input_partition_digest": partition_digest(),
            "leaf_count": len(leaves()),
            "selected_parameter_order": 7,
            "fallback_parameter_order": 8,
            "completed_order_seven_leaf_count": len(order_seven),
            "completed_order_seven_leaf_ids": [row["leaf"] for row in order_seven],
            "order_six_leaf_zero": order_six,
            "order_seven_completed_leaves": order_seven,
            "order_eight_leaf_zero": order_eight,
            "measured_minutes_per_order_seven_leaf": "approximately 18",
            "estimated_remaining_serial_hours": "approximately 23",
            "resume_command": "UV_CACHE_DIR=/private/tmp/uv-cache-gu-science uv run --offline --with python-flint==0.9.0 --with sympy==1.14.0 python tests/channel-swings/k1816_full_fisher_slab_three_leafwise_score_bank.py --resume-bank --parameter-order 7 --summary",
        },
        "decision": {
            "leafwise_recentering_validated": True,
            "order_seven_selected_for_production": True,
            "order_eight_fallback_validated": True,
            "complete_compact_leaf_bank_computed": len(order_seven) == len(leaves()),
            "retained_leaf_means_counterexample": False,
            "whole_line_composition_separate": True,
            "global_optimizer_proved": False,
        },
        "scope_guard": "The first two order-seven leaves have strict compact margins. The remaining 76 leaves, whole-line tails, stationary rejection and exposed boundary still require completion before any global promotion.",
    }


def validate(data: dict) -> list[tuple[str, bool]]:
    certificate = data["certificate"]
    if "leaves" in certificate:
        leaves_data = certificate["leaves"]
        fallback = data["fallback_scouts"]
        return [
            ("schema", data["schema_version"] == "1.0"),
            ("claim", data["claim_id"] == "K1816"),
            ("partition", certificate["input_partition_digest"] == partition_digest()),
            ("uniform configuration", certificate["observation_config"] == {
                "cell_half_width": "1/4",
                "observation_taylor_order": 14,
                "compact_cell_count": 88,
            }),
            ("78 leaves", certificate["leaf_count"] == 78),
            ("complete leaf ids", certificate["completed_leaf_ids"] == list(range(78))),
            ("26 positive", certificate["positive_compact_margin_count"] == 26),
            ("exact indeterminate block", certificate["nonpositive_or_indeterminate_leaf_ids"] == list(range(13, 65))),
            ("no counterexample flags", all(
                not row["decision"]["negative_margin_is_counterexample"]
                for row in leaves_data
            )),
            ("complete uniform bank", data["decision"]["complete_compact_leaf_bank_computed"]),
            ("value cover open", not data["decision"]["complete_compact_value_cover"]),
            ("whole order sixteen indeterminate", not fallback["route_findings"]["whole_leaf_order_16_positive"]),
            ("exact point positive", fallback["route_findings"]["exact_lower_t_mid_z_point_positive"]),
            ("fixed witness not counterexample", not fallback["route_findings"]["fixed_witness_counterexample"]),
            ("global withheld", not data["decision"]["global_optimizer_proved"]),
        ]
    seven = certificate["order_seven_completed_leaves"]
    return [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1816"),
        ("partition", certificate["input_partition_digest"] == partition_digest()),
        ("78 leaves", certificate["leaf_count"] == 78),
        ("two production leaves", certificate["completed_order_seven_leaf_ids"] == [0, 1]),
        ("order seven positive", all(row["decision"]["compact_cross_margin_positive"] for row in seven)),
        ("sixth order indeterminate", not certificate["order_six_leaf_zero"]["decision"]["compact_cross_margin_positive"]),
        ("eighth order fallback positive", certificate["order_eight_leaf_zero"]["decision"]["compact_cross_margin_positive"]),
        ("bank incomplete", not data["decision"]["complete_compact_leaf_bank_computed"]),
        ("global withheld", not data["decision"]["global_optimizer_proved"]),
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--leaf", type=int, action="append", default=[])
    parser.add_argument("--subdivide-leaf", type=int, action="append", default=[])
    parser.add_argument(
        "--subdivision-axis",
        choices=("t", "z", "both"),
        default="both",
    )
    parser.add_argument("--subdivision-depth", type=int, default=1)
    parser.add_argument("--subdivision-child", type=int, action="append", default=[])
    parser.add_argument("--grid-t-depth", type=int)
    parser.add_argument("--grid-z-depth", type=int)
    parser.add_argument("--grid-child", type=int, action="append", default=[])
    parser.add_argument("--point-leaf", type=int, action="append", default=[])
    parser.add_argument(
        "--point-location",
        choices=("lower-t-mid-z", "center", "lower-lower", "lower-upper"),
        default="lower-t-mid-z",
    )
    parser.add_argument("--resume-bank", action="store_true")
    parser.add_argument("--max-new", type=int)
    parser.add_argument("--parameter-order", type=int, choices=(6, 7, 8), default=6)
    parser.add_argument(
        "--cell-half-width",
        default="1/16",
        help="positive rational observation Taylor cell half-width dividing 11",
    )
    parser.add_argument(
        "--observation-order",
        type=int,
        choices=(12, 14, 16, 18),
        default=12,
        help="even observation Taylor order used on every compact cell",
    )
    parser.add_argument(
        "--margin-method",
        choices=("absolute", "bernstein"),
        default="absolute",
        help="rigorous lower-bound method for the combined cross-margin polynomial",
    )
    parser.add_argument("--replay", action="store_true")
    parser.add_argument("--write-artifact", action="store_true")
    parser.add_argument("--write-provisional-artifact", action="store_true")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()

    ensure_backends()
    global MARGIN_METHOD
    MARGIN_METHOD = args.margin_method
    if MARGIN_METHOD == "bernstein":
        validate_bernstein_transform()
    m.CELL_HALF_WIDTH = F(args.cell_half_width)
    m.OBSERVATION_ORDER = args.observation_order
    if not 0 < m.CELL_HALF_WIDTH <= F(1, 4):
        raise ValueError("cell half-width must lie in (0,1/4]")
    if (m.RADIUS / m.CELL_HALF_WIDTH).denominator != 1:
        raise ValueError("cell half-width must divide the compact observation radius")

    if args.write_provisional_artifact:
        artifact = provisional_artifact()
        atomic_json(ARTIFACT, artifact)
        print(json.dumps(artifact, indent=2))
        return
    if args.point_leaf:
        if args.leaf or args.resume_bank or args.write_artifact or args.subdivide_leaf:
            raise ValueError(
                "point mode cannot be combined with leaf, subdivision, resume-bank, or write-artifact"
            )
        rows = [
            ensure_point(
                leaf_id,
                args.point_location,
                args.parameter_order,
                args.replay,
            )
            for leaf_id in args.point_leaf
        ]
        data = {
            "input_partition_digest": partition_digest(),
            "point_count": len(rows),
            "strictly_positive_count": sum(
                row["decision"]["compact_cross_margin_positive"] for row in rows
            ),
            "strictly_negative_fixed_witness_count": sum(
                row["decision"]["fixed_witness_margin_strictly_negative"] for row in rows
            ),
            "checkpoint_digests": {
                str(row["leaf"]): row["checkpoint_digest"] for row in rows
            },
            "points": rows,
        }
        if args.summary:
            data.pop("points")
        print(json.dumps(data, indent=2))
        return
    if args.subdivide_leaf:
        if args.leaf or args.resume_bank or args.write_artifact:
            raise ValueError(
                "subdivision mode cannot be combined with leaf, resume-bank, or write-artifact"
            )
        if (args.grid_t_depth is None) != (args.grid_z_depth is None):
            raise ValueError("grid-t-depth and grid-z-depth must be supplied together")
        rows = []
        for leaf_id in args.subdivide_leaf:
            grid_mode = args.grid_t_depth is not None
            boxes = (
                grid_boxes(leaf_id, args.grid_t_depth, args.grid_z_depth)
                if grid_mode
                else subdivision_boxes(
                    leaf_id,
                    args.subdivision_axis,
                    args.subdivision_depth,
                )
            )
            child_count = len(boxes)
            selected_children = (
                args.grid_child if grid_mode else args.subdivision_child
            ) or list(range(child_count))
            if any(child < 0 or child >= child_count for child in selected_children):
                raise ValueError(
                    f"subdivision child outside 0..{child_count - 1}"
                )
            for child in selected_children:
                if grid_mode:
                    row = ensure_grid_child(
                        leaf_id,
                        args.grid_t_depth,
                        args.grid_z_depth,
                        child,
                        args.parameter_order,
                        args.replay,
                    )
                else:
                    row = ensure_subdivision_child(
                        leaf_id,
                        args.subdivision_axis,
                        child,
                        args.parameter_order,
                        args.replay,
                        args.subdivision_depth,
                    )
                rows.append(row)
        data = combined_subdivisions(rows)
        if args.summary:
            data = {key: value for key, value in data.items() if key != "children"}
        print(json.dumps(data, indent=2))
        return
    if not args.leaf and not args.resume_bank:
        checks = validate(json.loads(ARTIFACT.read_text()))
        for index, (label, ok) in enumerate(checks, 1):
            assert ok, label
            print(f"PASS {index:02d}: {label}")
        print(f"RESULT: PASS {len(checks)}/{len(checks)}")
        return

    selected = args.leaf or list(range(len(leaves())))
    rows = []
    new_count = 0
    for leaf_id in selected:
        cached = load_checkpoint(leaf_id, args.parameter_order)
        if cached is None or args.replay:
            if args.max_new is not None and new_count >= args.max_new:
                continue
            new_count += 1
        rows.append(ensure_leaf(leaf_id, args.parameter_order, args.replay))

    if args.resume_bank:
        rows = [
            row
            for leaf_id in range(len(leaves()))
            if (row := load_checkpoint(leaf_id, args.parameter_order))
        ]
    data = combined(rows, args.parameter_order)
    if args.write_artifact:
        if data["completed_leaf_count"] != data["leaf_count"]:
            raise ValueError("refusing to write a partial K1816 artifact")
        artifact = {
            "schema_version": "1.0",
            "claim_id": "K1816",
            "status": "active_research",
            "title": "Leafwise recentered fixed-score bank on the complete slab-three frontier",
            "inputs": ["K1787", "K1796", "K1806", "K1813"],
            "backend": "python-flint==0.9.0",
            "certificate": data,
            "fallback_scouts": fallback_scouts(),
            "decision": {
                "complete_compact_leaf_bank_computed": True,
                "complete_compact_value_cover": data[
                    "positive_compact_margin_count"
                ] == data["leaf_count"],
                "retained_leaf_means_counterexample": False,
                "whole_line_composition_separate": True,
                "global_optimizer_proved": False,
            },
            "scope_guard": "The uniform bank is complete, but 52 leaves remain method-indeterminate. The exact positive boundary-point control rejects a fixed-witness counterexample while showing that deeper value subdivision is ill-conditioned; whole-line tails, stationary rejection and exposed-boundary closure remain required before global admission.",
        }
        atomic_json(ARTIFACT, artifact)
    if args.summary:
        data = {key: value for key, value in data.items() if key != "leaves"}
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
