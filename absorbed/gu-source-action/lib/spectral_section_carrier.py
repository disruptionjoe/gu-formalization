"""Spectral-section carrier discriminator for the GU source-action wall.

The temporal-issuance absorber warning is the methodological constraint here:
a fixed compatibility choice can look like source structure while remaining an
observer-side or fixed-H reconstruction. For GU, that means a spectral section
is not promoted just because it chooses many zero modes. It must create
nonzero spectral asymmetry in the nonzero boundary spectrum without moving the
verified anchors or erasing the RS escape channel.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import Callable, Sequence

import numpy as np

from lib import gu_bridge


ETA = np.array([1.0] * 9 + [-1.0] * 5)


@dataclass(frozen=True)
class SectionCandidate:
    """A candidate rule for selecting a boundary spectral section."""

    name: str
    shape: str
    source_carrier: str
    selector: Callable[[dict[str, np.ndarray | float]], np.ndarray]


@dataclass(frozen=True)
class SectionVerdict:
    """Computed verdict for one spectral-section rule."""

    name: str
    shape: str
    source_carrier: str
    selected_rank: int
    positive_selected: int
    negative_selected: int
    zero_selected: int
    nonzero_eta: int
    zero_mode_balance: int
    section_balance: int
    commutator_norm: float
    escape_ratio: float
    preserves_bare_anchor: bool
    absorber_status: str
    guard_status: str
    reason: str


def _signature_counts(evals: np.ndarray, tol: float) -> tuple[int, int, int]:
    pos = int((evals > tol).sum())
    neg = int((evals < -tol).sum())
    zero = int((np.abs(evals) <= tol).sum())
    return pos, neg, zero


@lru_cache(maxsize=1)
def _spectral_context() -> dict[str, np.ndarray | float]:
    _e, gamma, pi_rs, m_d = gu_bridge.constraint_objects()
    q = np.eye(gu_bridge.N * gu_bridge.DIM, dtype=complex) - pi_rs
    escape = q @ m_d @ pi_rs
    d_sigma = escape + escape.conj().T
    grading = pi_rs - q
    evals, evecs = np.linalg.eigh(d_sigma)
    tol = 1e-7 * max(float(np.abs(evals).max()), 1e-30)
    pos_mask = evals > tol
    neg_mask = evals < -tol
    zero_mask = np.abs(evals) <= tol
    eta_vec = np.kron(np.diag(ETA), np.eye(gu_bridge.DIM))
    pi_weight = np.real(np.einsum("ij,ji->i", evecs.conj().T @ pi_rs, evecs))
    eta_weight = np.real(np.einsum("ij,ji->i", evecs.conj().T @ eta_vec, evecs))
    return {
        "gamma": gamma,
        "pi_rs": pi_rs,
        "q": q,
        "m_d": m_d,
        "escape": escape,
        "d_sigma": d_sigma,
        "grading": grading,
        "evals": evals,
        "evecs": evecs,
        "tol": tol,
        "pos_mask": pos_mask,
        "neg_mask": neg_mask,
        "zero_mask": zero_mask,
        "pi_weight": pi_weight,
        "eta_weight": eta_weight,
        "bare": float(np.linalg.norm(pi_rs @ m_d - m_d @ pi_rs)),
        "c2": float(np.linalg.norm(gamma @ m_d @ pi_rs)),
        "escape_norm": float(np.linalg.norm(escape)),
        "anticomm_norm": float(np.linalg.norm(grading @ d_sigma + d_sigma @ grading)),
    }


def candidate_sections() -> list[SectionCandidate]:
    """Return the first candidate spectral-section carrier rules."""

    return [
        SectionCandidate(
            name="strict_positive_aps",
            shape="strictly positive spectral projection of D_Sigma",
            source_carrier="canonical APS boundary section",
            selector=lambda ctx: ctx["pos_mask"].copy(),
        ),
        SectionCandidate(
            name="nonnegative_zero_fill",
            shape="positive spectrum plus the full zero eigenspace",
            source_carrier="fixed zero-mode convention; fixed-H absorber candidate",
            selector=lambda ctx: np.logical_or(ctx["pos_mask"], ctx["zero_mask"]),
        ),
        SectionCandidate(
            name="rs_weighted_zero_fill",
            shape="positive spectrum plus zero modes with dominant Pi_RS weight",
            source_carrier="fixed RS projector rule; fixed compatibility absorber candidate",
            selector=lambda ctx: np.logical_or(
                ctx["pos_mask"], np.logical_and(ctx["zero_mask"], ctx["pi_weight"] > 0.5)
            ),
        ),
        SectionCandidate(
            name="normal_weighted_zero_fill",
            shape="positive spectrum plus zero modes with dominant normal Q weight",
            source_carrier="fixed normal-projector rule; fixed compatibility absorber candidate",
            selector=lambda ctx: np.logical_or(
                ctx["pos_mask"], np.logical_and(ctx["zero_mask"], ctx["pi_weight"] < 0.5)
            ),
        ),
        SectionCandidate(
            name="eta_weighted_zero_fill",
            shape="positive spectrum plus zero modes selected by positive (9,5) eta weight",
            source_carrier="fixed signature-weight rule; fixed latent-structure absorber candidate",
            selector=lambda ctx: np.logical_or(
                ctx["pos_mask"], np.logical_and(ctx["zero_mask"], ctx["eta_weight"] > 1e-9)
            ),
        ),
    ]


def evaluate_section(candidate: SectionCandidate) -> SectionVerdict:
    """Evaluate one spectral-section rule."""

    ctx = _spectral_context()
    pi_rs = ctx["pi_rs"]
    q = ctx["q"]
    m_d = ctx["m_d"]
    d_sigma = ctx["d_sigma"]
    evecs = ctx["evecs"]
    pos_mask = ctx["pos_mask"]
    neg_mask = ctx["neg_mask"]
    zero_mask = ctx["zero_mask"]
    escape_norm = float(ctx["escape_norm"])
    bare = float(ctx["bare"])
    c2 = float(ctx["c2"])

    selected = np.asarray(candidate.selector(ctx), dtype=bool)
    selected_rank = int(selected.sum())
    positive_selected = int(np.logical_and(selected, pos_mask).sum())
    negative_selected = int(np.logical_and(selected, neg_mask).sum())
    zero_selected = int(np.logical_and(selected, zero_mask).sum())
    nonzero_eta = positive_selected - int(np.logical_and(~selected, neg_mask).sum())
    zero_mode_balance = zero_selected - (int(zero_mask.sum()) - zero_selected)
    section_balance = selected_rank - (len(selected) - selected_rank)

    basis = evecs[:, selected]
    projector = basis @ basis.conj().T if selected_rank else np.zeros_like(d_sigma)
    commutator_norm = float(np.linalg.norm(projector @ d_sigma - d_sigma @ projector))
    escape_after = float(np.linalg.norm(q @ m_d @ pi_rs))
    escape_ratio = escape_after / escape_norm
    preserves_anchors = abs(bare - 58.7215) < 1e-2 and abs(c2 - 155.3625) < 1e-2
    zero_choice_only = zero_selected > 0 and nonzero_eta == 0

    if not preserves_anchors:
        absorber = "anchor_failed"
        status = "anchor_failed"
        reason = "the verified GU bridge anchors moved"
    elif escape_ratio < 1e-8:
        absorber = "decoupling_trap"
        status = "clean_decoupling_trap"
        reason = "the section is paired with a vanished RS escape channel"
    elif nonzero_eta != 0:
        absorber = "not_absorbed_yet"
        status = "live_candidate_needs_closure_tests"
        reason = "the section changes the nonzero spectral asymmetry"
    elif zero_choice_only:
        absorber = "fixed_projector_or_fixed_H_absorber"
        status = "zero_mode_choice_absorbed"
        reason = "the only asymmetry comes from a fixed zero-mode convention"
    else:
        absorber = "chiral_symmetry_zero"
        status = "symmetric_section_zero"
        reason = "the exact chiral grading pairs the nonzero boundary spectrum"

    return SectionVerdict(
        name=candidate.name,
        shape=candidate.shape,
        source_carrier=candidate.source_carrier,
        selected_rank=selected_rank,
        positive_selected=positive_selected,
        negative_selected=negative_selected,
        zero_selected=zero_selected,
        nonzero_eta=nonzero_eta,
        zero_mode_balance=zero_mode_balance,
        section_balance=section_balance,
        commutator_norm=commutator_norm,
        escape_ratio=escape_ratio,
        preserves_bare_anchor=preserves_anchors,
        absorber_status=absorber,
        guard_status=status,
        reason=reason,
    )


def run_section_discriminator() -> list[SectionVerdict]:
    """Evaluate all first-pass spectral-section carrier rules."""

    return [evaluate_section(candidate) for candidate in candidate_sections()]


def summarize_section_verdict(rows: Sequence[SectionVerdict]) -> dict[str, object]:
    """Summarize whether this pass found a live spectral-section carrier."""

    live = [row for row in rows if row.guard_status == "live_candidate_needs_closure_tests"]
    absorbed = [row for row in rows if row.guard_status == "zero_mode_choice_absorbed"]
    symmetric = [row for row in rows if row.guard_status == "symmetric_section_zero"]
    ctx = _spectral_context()
    pos, neg, zero = _signature_counts(ctx["evals"], float(ctx["tol"]))
    return {
        "candidate_count": len(rows),
        "d_sigma_positive_count": pos,
        "d_sigma_negative_count": neg,
        "d_sigma_zero_count": zero,
        "d_sigma_eta": pos - neg,
        "anticomm_norm": float(ctx["anticomm_norm"]),
        "live_candidate_count": len(live),
        "absorbed_zero_mode_choice_count": len(absorbed),
        "symmetric_zero_count": len(symmetric),
        "round_verdict": (
            "one_live_spectral_section_candidate"
            if live
            else "only_symmetric_or_fixed_zero_mode_sections"
        ),
    }
