"""Compensator-adapter probes anchored to the RS escape block.

This is the second adapter discriminator. The first pass tested
connection-like candidates. This pass asks whether a source compensator can
touch the actual escape block

    E = (I - Pi_RS) M_D Pi_RS

without merely canceling the wall it is supposed to explain.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import Callable, Sequence

import numpy as np

from lib import gu_bridge


@dataclass(frozen=True)
class CompensatorCandidate:
    """A forced sigma_c shape built from the verified bridge objects."""

    name: str
    shape: str
    source_carrier: str
    matrix_builder: Callable[[dict[str, np.ndarray | float]], np.ndarray]
    structured: bool = True


@dataclass(frozen=True)
class CompensatorVerdict:
    """Computed verdict for one compensator candidate."""

    name: str
    shape: str
    source_carrier: str
    sig_delta: int
    escape_before: float
    escape_after: float
    escape_ratio: float
    total_commutator_norm: float
    preserves_bare_anchor: bool
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


@lru_cache(maxsize=1)
def _bridge_context() -> dict[str, np.ndarray | float]:
    _e, gamma, pi_rs, m_d = gu_bridge.constraint_objects()
    q = np.eye(gu_bridge.N * gu_bridge.DIM, dtype=complex) - pi_rs
    escape = q @ m_d @ pi_rs
    return {
        "gamma": gamma,
        "pi_rs": pi_rs,
        "q": q,
        "m_d": m_d,
        "escape": escape,
        "escape_dag": escape.conj().T,
        "bare": float(np.linalg.norm(pi_rs @ m_d - m_d @ pi_rs)),
        "c2": float(np.linalg.norm(gamma @ m_d @ pi_rs)),
        "escape_norm": float(np.linalg.norm(escape)),
    }


def candidate_compensators() -> list[CompensatorCandidate]:
    """Return the first forced compensator shapes to test."""

    return [
        CompensatorCandidate(
            name="full_escape_cancellation",
            shape="-E - E^dag, the direct cancellation of the RS escape channel",
            source_carrier="none; cancellation trap control",
            matrix_builder=lambda ctx: -(ctx["escape"] + ctx["escape_dag"]),
        ),
        CompensatorCandidate(
            name="half_escape_damping",
            shape="-0.5(E + E^dag), a partial compensating damper",
            source_carrier="boundary compensator ansatz; no BV carrier yet",
            matrix_builder=lambda ctx: -0.5 * (ctx["escape"] + ctx["escape_dag"]),
        ),
        CompensatorCandidate(
            name="quarter_escape_damping",
            shape="-0.25(E + E^dag), a weak compensating damper",
            source_carrier="boundary compensator ansatz; no BV carrier yet",
            matrix_builder=lambda ctx: -0.25 * (ctx["escape"] + ctx["escape_dag"]),
        ),
        CompensatorCandidate(
            name="antihermitian_escape_twist",
            shape="i(E - E^dag), a phase/twist of the escape channel",
            source_carrier="phase adapter ansatz; no holonomy carrier yet",
            matrix_builder=lambda ctx: 1j * (ctx["escape"] - ctx["escape_dag"]),
        ),
        CompensatorCandidate(
            name="imaginary_escape_completion",
            shape="i(E + E^dag), an imaginary Hermitian completion of the escape channel",
            source_carrier="phase adapter ansatz; no source-current law yet",
            matrix_builder=lambda ctx: 1j * (ctx["escape"] + ctx["escape_dag"]),
        ),
    ]


def evaluate_compensator(candidate: CompensatorCandidate) -> CompensatorVerdict:
    """Evaluate a compensator candidate against escape and index guards."""

    ctx = _bridge_context()
    gamma = ctx["gamma"]
    pi_rs = ctx["pi_rs"]
    q = ctx["q"]
    m_d = ctx["m_d"]
    bare = float(ctx["bare"])
    c2 = float(ctx["c2"])
    escape_before = float(ctx["escape_norm"])

    sigma = candidate.matrix_builder(ctx)
    m_eff = m_d + sigma
    escape_after = float(np.linalg.norm(q @ m_eff @ pi_rs))
    escape_ratio = escape_after / escape_before
    total_comm = float(np.linalg.norm(pi_rs @ m_eff - m_eff @ pi_rs))
    delta = _herm(_gdiag(1j * sigma, pi_rs, q))
    sig_delta = _sig(delta)
    preserves_anchors = abs(bare - 58.7215) < 1e-2 and abs(c2 - 155.3625) < 1e-2
    source_has_no_carrier = "no " in candidate.source_carrier.lower() or "none" in candidate.source_carrier.lower()

    if not preserves_anchors:
        status = "anchor_failed"
        reason = "the verified bare bridge anchors moved"
    elif escape_ratio < 1e-8:
        status = "clean_decoupling_trap"
        reason = "the candidate wins only by erasing the RS escape block"
    elif sig_delta != 0 and not source_has_no_carrier and escape_ratio > 0.5:
        status = "live_candidate_needs_closure_tests"
        reason = "the candidate changes the index discriminator without erasing the escape block"
    elif sig_delta != 0:
        status = "nonzero_but_missing_carrier"
        reason = "the candidate changes the index discriminator but has no source carrier"
    elif escape_ratio < 0.95:
        status = "damps_escape_without_index_signal"
        reason = "the candidate changes the escape strength but not the index discriminator"
    else:
        status = "escape_twist_without_index_signal"
        reason = "the candidate twists the escape channel but does not change the index discriminator"

    return CompensatorVerdict(
        name=candidate.name,
        shape=candidate.shape,
        source_carrier=candidate.source_carrier,
        sig_delta=sig_delta,
        escape_before=escape_before,
        escape_after=escape_after,
        escape_ratio=escape_ratio,
        total_commutator_norm=total_comm,
        preserves_bare_anchor=preserves_anchors,
        guard_status=status,
        reason=reason,
    )


def run_compensator_discriminator() -> list[CompensatorVerdict]:
    """Evaluate all first-pass compensator candidates."""

    return [evaluate_compensator(candidate) for candidate in candidate_compensators()]


def summarize_compensator_verdict(rows: Sequence[CompensatorVerdict]) -> dict[str, object]:
    """Summarize whether this pass found a non-arbitrary compensator."""

    live = [row for row in rows if row.guard_status == "live_candidate_needs_closure_tests"]
    traps = [row for row in rows if row.guard_status == "clean_decoupling_trap"]
    index_signals = [row for row in rows if row.sig_delta != 0]
    return {
        "candidate_count": len(rows),
        "clean_decoupling_trap_count": len(traps),
        "index_signal_count": len(index_signals),
        "live_candidate_count": len(live),
        "round_verdict": (
            "one_live_compensator_candidate"
            if live
            else "only_decoupling_or_zero_index_compensators"
        ),
    }
