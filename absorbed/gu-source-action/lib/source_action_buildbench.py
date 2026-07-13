"""Source-action candidate buildbench.

This module is the candidate ledger for the 2026-07-10 source-action hourly
plan. It forces each candidate to declare its field space, invariance
assumption, phase, hard-guard status, computable loss channels, and named
missing carriers.

After the topological-wall tau selector attempt, the default A-door row advances
to the global-boundary-condition tau-data handoff. Wall-like data can generate
nonzero tangent selectors, but the current repo still lacks a GU-native boundary
condition that selects one wall/tangent map uniquely.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping, Sequence

from lib import loss_channels as lc


class FieldSpaceDeclaration(str, Enum):
    """Declared SG4/source-action field space."""

    UNDECLARED = "undeclared"
    FULL_VECTOR_SPINOR = "full_vector_spinor"
    GAMMA_KERNEL = "gamma_kernel"
    BARE_UNCONSTRAINED = "bare_unconstrained"
    BOUNDARY_EXTERNAL = "boundary_external"
    SELECTOR_NOT_ACTION = "selector_not_action"


class InvarianceAssumption(str, Enum):
    """The invariance premise a candidate is trying to use."""

    UNSPECIFIED = "unspecified"
    ODD_SCALAR_SPINOR_A_DOOR = "odd_scalar_spinor_a_door"
    ANCHOR_SCALE_A_DOOR_PARTIAL = "anchor_scale_a_door_partial"
    H_LINEAR_NON_EQUIVARIANT = "h_linear_non_equivariant"
    BOUNDARY_SPECTRAL_SECTION = "boundary_spectral_section"
    AVAILABLE_LOSS_ONLY_SECURITY_BUDGET = "available_loss_only_security_budget"
    BARE_CONTROL = "bare_control"


class CandidatePhase(str, Enum):
    """Where the candidate sits in the hourly-progress sequence."""

    BUILD_BENCH = "build_bench"
    A_DOOR_FORK = "a_door_fork"
    BV_CLOSURE = "bv_closure"
    SOURCE_NOETHER_TAU = "source_noether_tau"
    DERIVATIVE_TAU_HOMOMORPHISM = "derivative_tau_homomorphism"
    GLOBAL_BOUNDARY_CONDITION_TAU = "global_boundary_condition_tau"
    BOUNDARY_BRIDGE = "boundary_bridge"
    DOWNSTREAM_SELECTOR = "downstream_selector"
    CONTROL = "control"


class BuildbenchVerdict(str, Enum):
    """Non-promotional buildbench classification."""

    HARD_GUARD_FAILED = "hard_guard_failed"
    READY_FOR_ANCHOR_SCALE_A_DOOR = "ready_for_anchor_scale_a_door"
    MISSING_CARRIER_BLOCKED = "missing_carrier_blocked"
    BOUNDARY_INDEX_WALL = "boundary_index_wall"
    DOWNSTREAM_PREMATURE = "downstream_premature"
    CONTROL_ROW = "control_row"


@dataclass(frozen=True)
class BuildbenchCandidate:
    """A source-action candidate with its required declaration triple."""

    name: str
    description: str
    field_space: FieldSpaceDeclaration
    invariance: InvarianceAssumption
    phase: CandidatePhase
    assumptions: Sequence[str] = ()
    metrics: Mapping[str, float] = field(default_factory=dict)

    def as_source_candidate(self) -> lc.SourceCandidate:
        return lc.SourceCandidate(
            name=self.name,
            description=self.description,
            assumptions=self.assumptions,
            metrics=self.metrics,
        )

    def effective_field_space(self) -> FieldSpaceDeclaration:
        """Apply the SG4 declaration-triple rule used by the hourly plan.

        The A-door is an odd scalar-spinor fork. Until the anchor-scale test
        says otherwise, that premise must be treated as a full vector-spinor
        field-space declaration rather than a hidden gamma-kernel projection.
        """

        if (
            self.field_space == FieldSpaceDeclaration.UNDECLARED
            and self.invariance == InvarianceAssumption.ODD_SCALAR_SPINOR_A_DOOR
        ):
            return FieldSpaceDeclaration.FULL_VECTOR_SPINOR
        return self.field_space


@dataclass(frozen=True)
class MissingCarrier:
    """A named loss channel that has no GU-native carrier yet."""

    channel: str
    required_carrier: str
    parent_object: str


@dataclass(frozen=True)
class BuildbenchReport:
    """Complete non-promotional report for one candidate."""

    candidate: BuildbenchCandidate
    effective_field_space: FieldSpaceDeclaration
    hard_guards: Mapping[str, bool]
    computable_losses: Mapping[str, float]
    missing_carriers: Sequence[MissingCarrier]
    verdict: BuildbenchVerdict
    next_action: str

    def hard_guard_failures(self) -> tuple[str, ...]:
        return tuple(name for name, passed in self.hard_guards.items() if not passed)

    def missing_channel_names(self) -> tuple[str, ...]:
        return tuple(carrier.channel for carrier in self.missing_carriers)


def _missing_carriers(candidate: lc.SourceCandidate) -> tuple[MissingCarrier, ...]:
    missing: list[MissingCarrier] = []
    for channel in lc.MISSING_CARRIER_CHANNELS:
        try:
            channel(candidate)
        except lc.MissingCarrierError as exc:
            missing.append(
                MissingCarrier(
                    channel=exc.channel,
                    required_carrier=exc.required_carrier,
                    parent_object=exc.parent_object,
                )
            )
    return tuple(missing)


def _next_action(candidate: BuildbenchCandidate, verdict: BuildbenchVerdict) -> str:
    if verdict == BuildbenchVerdict.HARD_GUARD_FAILED:
        return "discard or rewrite candidate before doing more source-action work"
    if verdict == BuildbenchVerdict.READY_FOR_ANCHOR_SCALE_A_DOOR:
        return "run the anchor-scale A-door test at the actual representation/Krein/H-linear scale"
    if verdict == BuildbenchVerdict.BOUNDARY_INDEX_WALL:
        return "do not use the current boundary symbol as an APS index; wait for a BV-to-boundary-Dirac bridge"
    if verdict == BuildbenchVerdict.DOWNSTREAM_PREMATURE:
        return "defer selection until declaration, A-door, BV closure, and bridge candidates exist"
    if candidate.phase == CandidatePhase.GLOBAL_BOUNDARY_CONDITION_TAU:
        return "supply the concrete global boundary condition or source current that selects one wall/tangent map"
    if candidate.phase == CandidatePhase.DERIVATIVE_TAU_HOMOMORPHISM:
        return "supply derivative-level tau/d_aleph data that selects the tangent part without reverting to a fixed projector"
    if candidate.phase == CandidatePhase.SOURCE_NOETHER_TAU:
        return "derive the projected BV/KT gauge differential from a source-level Noether/tau carrier"
    if candidate.phase == CandidatePhase.BV_CLOSURE:
        return "supply a non-equivariant anti-trap compensator plus full BV/Koszul-Tate closure"
    return "record the named missing carriers and keep the next hourly run on the earliest open fork"


def evaluate_candidate(candidate: BuildbenchCandidate) -> BuildbenchReport:
    """Evaluate one candidate against current hard guards and loss channels."""

    source_candidate = candidate.as_source_candidate()
    reports = lc.available_loss_reports(source_candidate)
    losses = {name: report.value for name, report in reports.items()}
    missing = _missing_carriers(source_candidate)

    hard_guards = {
        "field_space_declared_or_auto_declared": (
            candidate.effective_field_space() != FieldSpaceDeclaration.UNDECLARED
        ),
        "anti_import": not reports["L_target_import"].is_fatal(),
        "anti_trap_bare_commutator_preserved": not reports["L_acausal_trap"].is_fatal(),
    }

    if not all(hard_guards.values()):
        verdict = BuildbenchVerdict.HARD_GUARD_FAILED
    elif candidate.phase == CandidatePhase.A_DOOR_FORK:
        verdict = BuildbenchVerdict.READY_FOR_ANCHOR_SCALE_A_DOOR
    elif candidate.phase == CandidatePhase.DOWNSTREAM_SELECTOR:
        verdict = BuildbenchVerdict.DOWNSTREAM_PREMATURE
    elif losses["L_boundary_index"] > 0.0 and candidate.phase == CandidatePhase.BOUNDARY_BRIDGE:
        verdict = BuildbenchVerdict.BOUNDARY_INDEX_WALL
    elif candidate.phase == CandidatePhase.CONTROL:
        verdict = BuildbenchVerdict.CONTROL_ROW
    elif missing:
        verdict = BuildbenchVerdict.MISSING_CARRIER_BLOCKED
    else:
        verdict = BuildbenchVerdict.MISSING_CARRIER_BLOCKED

    return BuildbenchReport(
        candidate=candidate,
        effective_field_space=candidate.effective_field_space(),
        hard_guards=hard_guards,
        computable_losses=losses,
        missing_carriers=missing,
        verdict=verdict,
        next_action=_next_action(candidate, verdict),
    )


def default_buildbench_candidates() -> tuple[BuildbenchCandidate, ...]:
    """Current source-action candidates to classify for the hourly handoff."""

    return (
        BuildbenchCandidate(
            name="sg4-topological-wall-tau-underdetermined",
            description=(
                "The topology/wall lens generates nonzero tangent selectors that "
                "pass finite-fiber Noether, H-linear, Krein, and anchor checks, "
                "but the wall family remains underdetermined."
            ),
            field_space=FieldSpaceDeclaration.FULL_VECTOR_SPINOR,
            invariance=InvarianceAssumption.ANCHOR_SCALE_A_DOOR_PARTIAL,
            phase=CandidatePhase.GLOBAL_BOUNDARY_CONDITION_TAU,
            assumptions=(
                "No forbidden target numerology, fitted holonomy, or fitted rank is used.",
                "The bare commutator anchor is preserved.",
                "The raw gauge map remains second-class before projection.",
                "The projected finite-fiber BV/Koszul-Tate bicomplex closes.",
                "The finite-fiber tau multiplier derives the projection as a Schur complement.",
                "Noether leaves arbitrary tangent maps in ker Gamma unselected.",
                "Spacelike wall involutions generate nonzero tangent selectors.",
                "The current data do not select one wall/tangent map uniquely.",
                "A global boundary-condition/source-current carrier remains open.",
            ),
        ),
        BuildbenchCandidate(
            name="non-equivariant-compensator-bv-closure",
            description=(
                "The known necessary compensator lane, treated as a BV-closure "
                "candidate rather than as a completed source action."
            ),
            field_space=FieldSpaceDeclaration.FULL_VECTOR_SPINOR,
            invariance=InvarianceAssumption.H_LINEAR_NON_EQUIVARIANT,
            phase=CandidatePhase.BV_CLOSURE,
            assumptions=(
                "No target normalization is used.",
                "The bare commutator anchor is preserved.",
                "Arbitrary H-linear index movement is not source-action evidence.",
                "The compensator must couple to non-vacuous BV bicomplex closure.",
            ),
        ),
        BuildbenchCandidate(
            name="boundary-spectral-section-bridge",
            description=(
                "The currently computed BV-to-boundary symbol, kept separate from "
                "the missing APS/index bridge."
            ),
            field_space=FieldSpaceDeclaration.BOUNDARY_EXTERNAL,
            invariance=InvarianceAssumption.BOUNDARY_SPECTRAL_SECTION,
            phase=CandidatePhase.BOUNDARY_BRIDGE,
            assumptions=(
                "No Euler-characteristic shortcut or K3 import is used.",
                "The bare commutator anchor is preserved.",
                "A fixed boundary spectral section is not treated as closed internal S_IG data.",
            ),
        ),
        BuildbenchCandidate(
            name="available-loss-only-security-budget",
            description=(
                "The minimax/security-budget selector over currently computable "
                "losses, before enough real candidate channels exist."
            ),
            field_space=FieldSpaceDeclaration.SELECTOR_NOT_ACTION,
            invariance=InvarianceAssumption.AVAILABLE_LOSS_ONLY_SECURITY_BUDGET,
            phase=CandidatePhase.DOWNSTREAM_SELECTOR,
            assumptions=(
                "No target normalization is used.",
                "The bare commutator anchor is preserved.",
                "No candidate-specific anomaly, RS/BRST, theta/source, weak-field, or "
                "families-pushforward carrier is supplied.",
            ),
        ),
    )


def run_default_buildbench() -> tuple[BuildbenchReport, ...]:
    return tuple(evaluate_candidate(candidate) for candidate in default_buildbench_candidates())


def buildbench_summary(reports: Sequence[BuildbenchReport]) -> dict[str, object]:
    """Small summary for packet tests and hourly handoff."""

    hard_failures = {
        report.candidate.name: report.hard_guard_failures()
        for report in reports
        if report.hard_guard_failures()
    }
    ready_for_anchor = [
        report.candidate.name
        for report in reports
        if report.verdict == BuildbenchVerdict.READY_FOR_ANCHOR_SCALE_A_DOOR
    ]
    missing_by_candidate = {
        report.candidate.name: report.missing_channel_names()
        for report in reports
        if report.missing_carriers
    }
    next_point = (
        "ANCHOR-SCALE-A-DOOR"
        if ready_for_anchor
        else "GLOBAL-BOUNDARY-CONDITION-TAU-DATA"
        if any(
            report.candidate.phase == CandidatePhase.GLOBAL_BOUNDARY_CONDITION_TAU
            for report in reports
        )
        else "DERIVATIVE-TAU-HOMOMORPHISM"
        if any(
            report.candidate.phase == CandidatePhase.DERIVATIVE_TAU_HOMOMORPHISM
            for report in reports
        )
        else "SOURCE-NOETHER-TAU-CARRIER"
        if any(report.candidate.phase == CandidatePhase.SOURCE_NOETHER_TAU for report in reports)
        else "MINIMAL-BV-CLOSURE"
        if any(report.candidate.phase == CandidatePhase.BV_CLOSURE for report in reports)
        else "SOURCE-ACTION-BUILDBENCH"
    )
    return {
        "candidate_count": len(reports),
        "hard_failures": hard_failures,
        "ready_for_anchor_scale_a_door": tuple(ready_for_anchor),
        "missing_by_candidate": missing_by_candidate,
        "next_hourly_progress_point": next_point,
    }
