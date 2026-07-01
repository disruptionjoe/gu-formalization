"""GU-native loss channels for security-budget source-action tests.

This module is intentionally conservative. A loss channel may do one of two things:

1. compute from objects already exposed by ``lib.gu_bridge``; or
2. fail loudly with a named missing carrier.

It is not acceptable for a channel to be prose, taste, or a hidden target import.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from functools import lru_cache
import math
import re
from typing import Callable, Mapping, Sequence

import numpy as np

from lib import gu_bridge
from lib.security_budget import CandidateScore


EXPECTED_BARE_COMMUTATOR = 58.7215
EXPECTED_C2 = 155.3625
ANCHOR_TOL = 1e-2


@dataclass(frozen=True)
class SourceCandidate:
    """Minimal metadata for a proposed source extension."""

    name: str
    description: str = ""
    assumptions: Sequence[str] = ()
    metrics: Mapping[str, float] = field(default_factory=dict)

    def text_for_guards(self) -> str:
        return "\n".join([self.name, self.description, *self.assumptions])


@dataclass(frozen=True)
class LossReport:
    """A computed adversarial loss channel."""

    name: str
    value: float
    status: str
    carrier: str
    details: Mapping[str, object] = field(default_factory=dict)

    def is_fatal(self) -> bool:
        return math.isinf(self.value)


class MissingCarrierError(RuntimeError):
    """Raised when a loss channel has no GU-native computable carrier yet."""

    def __init__(self, channel: str, required_carrier: str, parent_object: str):
        self.channel = channel
        self.required_carrier = required_carrier
        self.parent_object = parent_object
        super().__init__(
            f"{channel} has no computable GU-native carrier yet; required carrier: "
            f"{required_carrier}; expected parent object: {parent_object}"
        )


TARGET_IMPORT_PATTERNS: tuple[tuple[str, str], ...] = (
    (r"\b24\s*/\s*8\b", "24/8 target normalization"),
    (r"\bch2\s*=\s*24\b", "ch2=24 target import"),
    (r"\bch2\s*\(\s*S_X\s*\)\s*\[\s*K3\s*\]\s*=\s*24\b", "ch2(S_X)[K3]=24 target import"),
    (r"\bchi\s*\(\s*K3\s*\)\s*=\s*24\b", "chi(K3)=24 generation input"),
    (r"\bassum(?:e|ed|ing)[-\s]+K3\b", "assumed-K3 input"),
    (r"\bflat\s+Ahat\s*=\s*3\b", "flat Ahat=3 target import"),
    (r"\bcontractible[-\s]*fiber\s*=>\s*pushforward\s*1\b", "contractible-fiber pushforward import"),
)

ACAUSAL_TRAP_PATTERNS: tuple[tuple[str, str], ...] = (
    (r"\bdrive\s+the\s+bare\s+(?:commutator|norm)\s+to\s+0\b", "drives bare commutator to zero"),
    (r"\bclean\s+decoupl(?:e|ing)\b", "clean decoupling trap"),
    (r"\btrivial\s+block[-\s]*subtraction\b", "trivial block-subtraction trap"),
    (r"\bsigma_c\s*=\s*-\s*\(?escape\s+block\)?\b", "sigma_c cancels escape block"),
)


def _candidate(candidate: SourceCandidate | None) -> SourceCandidate:
    return candidate if candidate is not None else SourceCandidate("unnamed")


def _matches(patterns: Sequence[tuple[str, str]], text: str) -> list[str]:
    found: list[str] = []
    for pattern, label in patterns:
        if re.search(pattern, text, flags=re.IGNORECASE):
            found.append(label)
    return found


def _missing(channel: str, required_carrier: str, parent_object: str) -> LossReport:
    raise MissingCarrierError(channel, required_carrier, parent_object)


def _cxi_mat(e: Sequence[np.ndarray], xi: np.ndarray) -> np.ndarray:
    return sum(xi[a] * e[a] for a in range(gu_bridge.N))


@lru_cache(maxsize=1)
def boundary_symbol_metrics() -> dict[str, object]:
    """Compute the currently available BV-to-boundary-symbol facts.

    The result is the executable core of the present boundary lesson:

    - the BV-to-boundary-Dirac map exists at the symbol/Hessian level;
    - the APS eta/index route fails because an anticommuting grading forces eta = 0;
    - C2 is carried as a Hilbert-Schmidt symbol norm, not as spectral asymmetry.
    """

    e, Gamma, Pi_RS, M_D = gu_bridge.constraint_objects()
    n = gu_bridge.N
    dim = gu_bridge.DIM
    xi = np.asarray(gu_bridge.XI, dtype=complex)
    q_boundary = np.eye(n * dim, dtype=complex) - Pi_RS

    bare = float(np.linalg.norm(Pi_RS @ M_D - M_D @ Pi_RS))
    c2 = float(np.linalg.norm(Gamma @ M_D @ Pi_RS))

    if abs(bare - EXPECTED_BARE_COMMUTATOR) > ANCHOR_TOL:
        raise RuntimeError(f"anti-trap anchor moved: bare commutator = {bare:.6f}")
    if abs(c2 - EXPECTED_C2) > ANCHOR_TOL:
        raise RuntimeError(f"C2 anchor moved: C2 = {c2:.6f}")

    escape = q_boundary @ M_D @ Pi_RS
    d_sigma = escape + escape.conj().T
    self_adjoint_error = float(np.linalg.norm(d_sigma - d_sigma.conj().T))

    grading = Pi_RS - q_boundary
    grading_square_error = float(np.linalg.norm(grading @ grading - np.eye(n * dim)))
    anticommutator_error = float(np.linalg.norm(grading @ d_sigma + d_sigma @ grading))

    evals = np.linalg.eigvalsh(d_sigma)
    tol = 1e-7 * (float(np.abs(evals).max()) + 1e-30)
    n_pos = int((evals > tol).sum())
    n_neg = int((evals < -tol).sum())
    n_zero = int((np.abs(evals) <= tol).sum())
    eta = n_pos - n_neg

    gamma_tight_error = float(np.linalg.norm(Gamma @ Gamma.conj().T - n * np.eye(dim)))
    q_frame_error = float(np.linalg.norm(q_boundary - Gamma.conj().T @ Gamma / n))

    b_kt = Gamma @ M_D @ Pi_RS
    m_kt = b_kt.conj().T @ b_kt
    ede = escape.conj().T @ escape
    mkt_norm = float(np.linalg.norm(m_kt))
    rel_mkt_dirac_square = float(np.linalg.norm(m_kt - n * ede)) / mkt_norm
    trace_mkt = float(np.trace(m_kt).real)
    c2_from_trace = float(np.sqrt(trace_mkt))

    c2_double = gu_bridge.C2(2.0 * xi)
    c2_degree_ratio = float(c2_double / c2)

    map_built = self_adjoint_error < 1e-10 and rel_mkt_dirac_square < 1e-10
    eta_forced_zero = anticommutator_error < 1e-10 and eta == 0
    section_connects = eta != 0
    c2_is_hs_symbol_norm = abs(c2_from_trace - c2) < 1e-6

    return {
        "bare_commutator": bare,
        "C2": c2,
        "C2_degree_ratio": c2_degree_ratio,
        "self_adjoint_error": self_adjoint_error,
        "grading_square_error": grading_square_error,
        "anticommutator_error": anticommutator_error,
        "n_pos": n_pos,
        "n_neg": n_neg,
        "n_zero": n_zero,
        "eta_D_sigma": eta,
        "gamma_tight_error": gamma_tight_error,
        "q_frame_error": q_frame_error,
        "rel_MKT_to_N_D_square": rel_mkt_dirac_square,
        "trace_MKT": trace_mkt,
        "C2_from_trace_MKT": c2_from_trace,
        "map_built": map_built,
        "eta_forced_zero": eta_forced_zero,
        "section_connects": section_connects,
        "C2_is_HS_symbol_norm": c2_is_hs_symbol_norm,
        "verdict": "BV_BOUNDARY_MAP_EXISTS_BUT_APS_INDEX_ROUTE_FAILS",
    }


def l_boundary_symbol(candidate: SourceCandidate | None = None) -> LossReport:
    """Loss for the already-built BV-to-boundary symbol carrier.

    Zero means the current bridge supports this carrier at the symbol/Hessian level.
    """

    del candidate
    metrics = boundary_symbol_metrics()
    loss = 0.0 if metrics["map_built"] and metrics["C2_is_HS_symbol_norm"] else 1.0
    return LossReport(
        name="L_boundary_symbol",
        value=loss,
        status="computed",
        carrier="D_Sigma = Q M_D Pi_RS + h.c.; M_KT = N*(D_Sigma^2)|surface",
        details=metrics,
    )


def l_boundary_index(candidate: SourceCandidate | None = None) -> LossReport:
    """Loss for using the current boundary operator as an APS index carrier.

    The value is one when the symbol exists but the spectral-section/index connection fails.
    This is a computed obstruction, not a missing carrier.
    """

    del candidate
    metrics = boundary_symbol_metrics()
    loss = 0.0 if metrics["section_connects"] else 1.0
    return LossReport(
        name="L_boundary_index",
        value=loss,
        status="computed",
        carrier="APS spectral section of D_Sigma",
        details=metrics,
    )


def l_target_import(candidate: SourceCandidate | None = None) -> LossReport:
    """Fatal loss for known target-import patterns."""

    c = _candidate(candidate)
    matches = _matches(TARGET_IMPORT_PATTERNS, c.text_for_guards())
    value = float("inf") if matches else 0.0
    return LossReport(
        name="L_target_import",
        value=value,
        status="computed",
        carrier="textual and metadata guard against known target imports",
        details={"matches": matches},
    )


def l_acausal_trap(candidate: SourceCandidate | None = None) -> LossReport:
    """Fatal loss for acausal decoupling and bare-commutator traps."""

    c = _candidate(candidate)
    matches = _matches(ACAUSAL_TRAP_PATTERNS, c.text_for_guards())
    bare = float(c.metrics.get("bare_commutator", gu_bridge.anchors()["bare_commutator"]))
    if bare < 1e-6:
        matches.append("bare commutator numerically driven to zero")
    elif abs(bare - EXPECTED_BARE_COMMUTATOR) > ANCHOR_TOL:
        matches.append("bare commutator moved from verified anchor")
    value = float("inf") if matches else 0.0
    return LossReport(
        name="L_acausal_trap",
        value=value,
        status="computed",
        carrier="anti-trap bare commutator guard",
        details={"bare_commutator": bare, "matches": matches},
    )


def l_anomaly(candidate: SourceCandidate | None = None) -> LossReport:
    del candidate
    return _missing(
        "L_anomaly",
        "anomaly polynomial / Green-Schwarz factorization computed from a candidate S_IG",
        "SPEC.md master-equation and anomaly-closure data",
    )


def l_rs_brst(candidate: SourceCandidate | None = None) -> LossReport:
    del candidate
    return _missing(
        "L_RS_BRST",
        "full BV bicomplex closure loss for the proposed source extension",
        "parent BV bicomplex plus candidate non-equivariant compensator closure",
    )


def l_theta_source(candidate: SourceCandidate | None = None) -> LossReport:
    del candidate
    return _missing(
        "L_theta_source",
        "theta/source-current law coupled to the candidate source action",
        "theta divergence-free and weak-field source-current objects",
    )


def l_weak_field(candidate: SourceCandidate | None = None) -> LossReport:
    del candidate
    return _missing(
        "L_weak_field",
        "weak-field Schwarzschild/GR recovery loss for the candidate source law",
        "parent weak-field recovery tests plus candidate source-current coupling",
    )


def l_families_pushforward(candidate: SourceCandidate | None = None) -> LossReport:
    del candidate
    return _missing(
        "L_families_pushforward",
        "families pushforward over GL(4,R)/O(3,1) or a controlled finite surrogate",
        "SPEC.md global object 5(i)",
    )


COMPUTABLE_CHANNELS: tuple[Callable[[SourceCandidate | None], LossReport], ...] = (
    l_boundary_symbol,
    l_boundary_index,
    l_target_import,
    l_acausal_trap,
)

MISSING_CARRIER_CHANNELS: tuple[Callable[[SourceCandidate | None], LossReport], ...] = (
    l_anomaly,
    l_rs_brst,
    l_theta_source,
    l_weak_field,
    l_families_pushforward,
)


def available_loss_reports(candidate: SourceCandidate | None = None) -> dict[str, LossReport]:
    """Compute every currently GU-native loss channel."""

    return {report.name: report for report in (channel(candidate) for channel in COMPUTABLE_CHANNELS)}


def candidate_score_from_available_losses(
    candidate: SourceCandidate,
    *,
    growth_value: float,
    validation_cost: float = 0.0,
    finalization_cost: float = 0.0,
) -> CandidateScore:
    """Build a ``CandidateScore`` from the channels that compute today."""

    reports = available_loss_reports(candidate)
    losses = {name: report.value for name, report in reports.items()}
    return CandidateScore(
        name=candidate.name,
        growth_value=growth_value,
        validation_cost=validation_cost,
        finalization_cost=finalization_cost,
        adversarial_losses=losses,
        hard_guards={
            "anti_import": not reports["L_target_import"].is_fatal(),
            "anti_trap_bare_commutator_preserved": not reports["L_acausal_trap"].is_fatal(),
            "boundary_symbol_carrier_exists": reports["L_boundary_symbol"].value == 0.0,
        },
    )
