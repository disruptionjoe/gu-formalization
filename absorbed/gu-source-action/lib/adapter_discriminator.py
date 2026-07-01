"""First discriminator for the external-adapter steelman.

The test here is intentionally narrow. It asks whether a candidate adapter can
produce nonzero boundary/index behavior in the existing Cl(9,5) bridge while
also avoiding the two easy failures:

1. ordinary metric so(9,5) geometry, which the repo already showed gives zero;
2. arbitrary non-metric perturbation, which can move the index but has no source
   carrier.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import Callable, Sequence

import numpy as np

from lib import gu_bridge


ETA = np.array([1.0] * 9 + [-1.0] * 5)


@dataclass(frozen=True)
class AdapterCandidate:
    """A bounded candidate adapter class."""

    name: str
    shape: str
    source_carrier: str
    matrix_builder: Callable[[Sequence[np.ndarray]], np.ndarray]
    structured: bool
    metric_so95: bool
    arbitrary: bool


@dataclass(frozen=True)
class AdapterVerdict:
    """Computed discriminator verdict for one candidate."""

    name: str
    shape: str
    source_carrier: str
    sig_delta: int
    phs_break_norm: float
    nonzero_index: bool
    preserves_bare_anchor: bool
    structured: bool
    metric_so95: bool
    arbitrary: bool
    guard_status: str
    reason: str


def _herm(x: np.ndarray) -> np.ndarray:
    return 0.5 * (x + x.conj().T)


def _gdiag(x: np.ndarray, pi_rs: np.ndarray, q: np.ndarray) -> np.ndarray:
    return pi_rs @ x @ pi_rs + q @ x @ q


def _sig(x: np.ndarray) -> int:
    ev = np.linalg.eigvalsh(_herm(x))
    tol = 1e-7 * (float(np.abs(ev).max()) + 1e-30)
    return int((ev > tol).sum()) - int((ev < -tol).sum())


def _metric_generator(i: int, j: int) -> np.ndarray:
    m = np.zeros((gu_bridge.N, gu_bridge.N), dtype=complex)
    m[i, j] = ETA[j]
    m[j, i] = -ETA[i]
    return m


def _symmetric_pair(i: int, j: int) -> np.ndarray:
    m = np.zeros((gu_bridge.N, gu_bridge.N), dtype=complex)
    m[i, j] = 1.0
    m[j, i] = 1.0
    return m


def _directed_pair(i: int, j: int) -> np.ndarray:
    m = np.zeros((gu_bridge.N, gu_bridge.N), dtype=complex)
    m[i, j] = 1.0
    return m


def _diag_strain(weights: Sequence[float]) -> np.ndarray:
    return np.diag(np.asarray(weights, dtype=complex))


def _jfull(i: int, j: int, e128: Sequence[np.ndarray]) -> np.ndarray:
    sigma = 0.25 * (e128[i] @ e128[j] - e128[j] @ e128[i])
    return np.kron(_metric_generator(i, j), np.eye(gu_bridge.DIM)) + np.kron(
        np.eye(gu_bridge.N), sigma
    )


def _vector_only(a: np.ndarray) -> np.ndarray:
    return np.kron(a, np.eye(gu_bridge.DIM))


def _quaternionic_j(e128: Sequence[np.ndarray], seed: int = 1) -> np.ndarray:
    def phi(u: np.ndarray) -> np.ndarray:
        out = np.zeros_like(u)
        for a in range(gu_bridge.N):
            out += ETA[a] * (e128[a] @ u @ e128[a].conj())
        return out / gu_bridge.N

    rng = np.random.default_rng(seed)
    u = rng.standard_normal((gu_bridge.DIM, gu_bridge.DIM)) + 1j * rng.standard_normal(
        (gu_bridge.DIM, gu_bridge.DIM)
    )
    for _ in range(400):
        u = 0.5 * (u + phi(u))
        u /= np.linalg.norm(u)
    us, _, vs = np.linalg.svd(u)
    u = us @ vs
    return u / np.sqrt(abs(np.trace(u @ u.conj()) / gu_bridge.DIM))


@lru_cache(maxsize=1)
def _bridge_context() -> dict[str, np.ndarray | float]:
    e, gamma, pi_rs, m_d = gu_bridge.constraint_objects()
    q = np.eye(gu_bridge.N * gu_bridge.DIM, dtype=complex) - pi_rs
    g = pi_rs - q
    e128 = gu_bridge.gammas()
    jq = _quaternionic_j(e128)
    jf = np.kron(np.eye(gu_bridge.N), jq)
    cu = jf @ g.conj()
    bare = float(np.linalg.norm(pi_rs @ m_d - m_d @ pi_rs))
    c2 = float(np.linalg.norm(gamma @ m_d @ pi_rs))
    return {
        "pi_rs": pi_rs,
        "q": q,
        "cu": cu,
        "cu_dag": cu.conj().T,
        "e128": e128,
        "bare": bare,
        "c2": c2,
    }


def candidate_adapters() -> list[AdapterCandidate]:
    """Return the first bounded adapter classes to test."""

    return [
        AdapterCandidate(
            name="metric_selfdual_control",
            shape="ordinary metric so(9,5) self-dual connection",
            source_carrier="known metric gauge/spin geometry",
            matrix_builder=lambda e: _jfull(0, 1, e) + _jfull(2, 3, e),
            structured=True,
            metric_so95=True,
            arbitrary=False,
        ),
        AdapterCandidate(
            name="metric_random_control",
            shape="fixed linear combination of metric so(9,5) generators",
            source_carrier="known metric gauge/spin geometry",
            matrix_builder=lambda e: _jfull(0, 2, e)
            - 2.0 * _jfull(4, 9, e)
            + 0.5 * _jfull(7, 13, e),
            structured=True,
            metric_so95=True,
            arbitrary=False,
        ),
        AdapterCandidate(
            name="nonmetric_tracefree_strain",
            shape="trace-free symmetric strain on the vector/metric index",
            source_carrier="candidate source-side metric-strain adapter; no BV carrier yet",
            matrix_builder=lambda e: _vector_only(
                _diag_strain([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7])
            ),
            structured=True,
            metric_so95=False,
            arbitrary=False,
        ),
        AdapterCandidate(
            name="nonmetric_directed_mixing",
            shape="directed non-metric vector-index mixing from one spatial to one timelike direction",
            source_carrier="candidate source-side non-metric directed adapter; no BV carrier yet",
            matrix_builder=lambda e: _vector_only(_directed_pair(0, 9)),
            structured=True,
            metric_so95=False,
            arbitrary=False,
        ),
        AdapterCandidate(
            name="end_selector_strain",
            shape="rank-split end selector on vector directions 0..6 versus 7..13",
            source_carrier="candidate boundary/end-selector adapter; no holonomy carrier yet",
            matrix_builder=lambda e: _vector_only(
                _diag_strain([1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1])
            ),
            structured=True,
            metric_so95=False,
            arbitrary=False,
        ),
        AdapterCandidate(
            name="arbitrary_hlinear_noise_control",
            shape="deterministic dense H-linear non-algebra perturbation",
            source_carrier="none; pipeline sanity control only",
            matrix_builder=_arbitrary_hlinear_noise,
            structured=False,
            metric_so95=False,
            arbitrary=True,
        ),
    ]


def _arbitrary_hlinear_noise(e128: Sequence[np.ndarray]) -> np.ndarray:
    jq = _quaternionic_j(e128)
    jf = np.kron(np.eye(gu_bridge.N), jq)
    jfi = np.linalg.inv(jf)
    rng = np.random.default_rng(314159)
    r = rng.standard_normal((gu_bridge.N * gu_bridge.DIM, gu_bridge.N * gu_bridge.DIM)) + 1j * rng.standard_normal(
        (gu_bridge.N * gu_bridge.DIM, gu_bridge.N * gu_bridge.DIM)
    )
    # evaluate_adapter applies Herm(Gdiag(i*J)). Existing CONSTRUCT-03 arbitrary
    # breakers are of the form Herm(Gdiag(R_H-linear)), so return -i*R here.
    return -1j * 0.5 * (r + jf @ r.conj() @ jfi)


def evaluate_adapter(candidate: AdapterCandidate) -> AdapterVerdict:
    """Evaluate one adapter candidate against the boundary/index discriminator."""

    ctx = _bridge_context()
    pi_rs = ctx["pi_rs"]
    q = ctx["q"]
    cu = ctx["cu"]
    cu_dag = ctx["cu_dag"]
    e128 = ctx["e128"]
    bare = float(ctx["bare"])
    c2 = float(ctx["c2"])

    j = candidate.matrix_builder(e128)  # connection-like anti-Hermitian generator before i*
    delta = _herm(_gdiag(1j * j, pi_rs, q))
    sig_delta = _sig(delta)
    phs_break = float(np.linalg.norm(cu @ delta.conj() @ cu_dag + delta))
    preserves_anchors = abs(bare - 58.7215) < 1e-2 and abs(c2 - 155.3625) < 1e-2
    nonzero = sig_delta != 0

    if not preserves_anchors:
        status = "anchor_failed"
        reason = "bridge anchors moved"
    elif candidate.metric_so95 and nonzero:
        status = "unexpected_metric_positive"
        reason = "metric control should reproduce the zero-index result"
    elif candidate.metric_so95:
        status = "zero_metric_control"
        reason = "ordinary metric so(9,5) geometry preserves the PHS certificate and gives index zero"
    elif candidate.arbitrary and nonzero:
        status = "nonzero_but_arbitrary"
        reason = "dense non-algebra perturbation moves the index but has no source carrier"
    elif candidate.arbitrary:
        status = "arbitrary_zero"
        reason = "dense non-algebra perturbation failed to move the index in this seed"
    elif nonzero:
        status = "structured_nonmetric_signal_needs_carrier"
        reason = "structured non-metric candidate moves the index, but no BV/holonomy/source carrier is supplied"
    else:
        status = "structured_but_zero"
        reason = "structured non-metric candidate gives no boundary/index signal"

    return AdapterVerdict(
        name=candidate.name,
        shape=candidate.shape,
        source_carrier=candidate.source_carrier,
        sig_delta=sig_delta,
        phs_break_norm=phs_break,
        nonzero_index=nonzero,
        preserves_bare_anchor=preserves_anchors,
        structured=candidate.structured,
        metric_so95=candidate.metric_so95,
        arbitrary=candidate.arbitrary,
        guard_status=status,
        reason=reason,
    )


def run_discriminator() -> list[AdapterVerdict]:
    """Evaluate all first-pass adapter candidates."""

    return [evaluate_adapter(candidate) for candidate in candidate_adapters()]


def summarize_verdict(rows: Sequence[AdapterVerdict]) -> dict[str, object]:
    """Summarize whether the goal found a live adapter candidate."""

    structured_nonmetric = [r for r in rows if r.structured and not r.metric_so95 and not r.arbitrary]
    signals = [r for r in structured_nonmetric if r.nonzero_index]
    live = [
        r
        for r in signals
        if r.guard_status == "structured_nonmetric_signal_needs_carrier"
        and "no " not in r.source_carrier.lower()
    ]
    return {
        "candidate_count": len(rows),
        "metric_controls_zero": all((not r.nonzero_index) for r in rows if r.metric_so95),
        "structured_nonmetric_count": len(structured_nonmetric),
        "structured_nonmetric_signal_count": len(signals),
        "live_structured_candidate_count": len(live),
        "round_verdict": (
            "structured_nonmetric_signals_exist_but_no_source_carrier"
            if signals and not live
            else "one_live_structured_candidate"
            if live
            else "all_structured_candidates_zero"
        ),
    }
