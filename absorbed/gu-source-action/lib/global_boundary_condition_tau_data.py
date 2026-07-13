"""Global-boundary tau-data probe for the wall selector family.

The previous wall packet showed that spacelike wall involutions can create
nonzero tangent selectors in ``ker(Gamma)``, but the family is underdetermined.
This module asks the next narrower question: do the boundary/tau data currently
available inside the absorbed source-action bench force one wall, or does any
selection still depend on an externally supplied rule/current?
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
import sys

import numpy as np


SOURCE_ROOT = Path(__file__).resolve().parents[1]
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))

from lib.topological_wall_tau_selector import (  # noqa: E402
    TopologicalWallTauReport,
    TopologicalWallTauVerdict,
    WallSelectorCandidate,
    run_topological_wall_tau_selector,
)


class GlobalBoundaryTauVerdict(str, Enum):
    """Outcome labels for the global-boundary tau-data probe."""

    EXTERNALLY_KEYED_WALL_SELECTION_BLOCKED = (
        "externally_keyed_wall_selection_blocked"
    )
    FAILS = "fails"


@dataclass(frozen=True)
class CriterionChoice:
    """Selection made by one candidate scalar rule."""

    criterion: str
    selected_component: int
    selected_name: str
    score: float
    source_of_rule: str


@dataclass(frozen=True)
class ExternalCurrentChoice:
    """Selection induced by an externally supplied boundary/source current."""

    selected_component: int
    selected_name: str
    current_weight: float
    externally_keyed: bool


@dataclass(frozen=True)
class GlobalBoundaryTauReport:
    """Machine-checkable report for the boundary-condition selector blocker."""

    verdict: GlobalBoundaryTauVerdict
    wall_report: TopologicalWallTauReport
    local_criterion_choices: tuple[CriterionChoice, ...]
    external_current_choice: ExternalCurrentChoice | None
    boundary_current_declared_by_source_action: bool
    source_forced_unique_selector: bool
    next_progress_point: str

    @property
    def admissible_wall_count(self) -> int:
        return self.wall_report.admissible_count

    @property
    def local_scalar_rules_pick_multiple_components(self) -> bool:
        selected = {choice.selected_component for choice in self.local_criterion_choices}
        return len(selected) > 1

    @property
    def externally_supplied_current_can_pick_a_wall(self) -> bool:
        return self.external_current_choice is not None and self.external_current_choice.externally_keyed

    @property
    def selection_still_needs_source_current_data(self) -> bool:
        return (
            self.wall_report.verdict
            == TopologicalWallTauVerdict.NONZERO_WALL_SELECTORS_UNDERDETERMINED
            and self.admissible_wall_count == 9
            and self.local_scalar_rules_pick_multiple_components
            and not self.boundary_current_declared_by_source_action
            and not self.source_forced_unique_selector
        )


def _choose(
    candidates: tuple[WallSelectorCandidate, ...],
    criterion: str,
    key,
    *,
    prefer: str,
) -> CriterionChoice:
    """Choose a candidate by one scalar key."""

    if prefer == "min":
        selected = min(candidates, key=key)
    elif prefer == "max":
        selected = max(candidates, key=key)
    else:
        raise ValueError(f"unknown preference {prefer!r}")
    return CriterionChoice(
        criterion=criterion,
        selected_component=selected.reflected_component,
        selected_name=selected.name,
        score=float(key(selected)),
        source_of_rule="local_scalar_summary_not_a_source_action",
    )


def _local_criterion_choices(
    candidates: tuple[WallSelectorCandidate, ...],
) -> tuple[CriterionChoice, ...]:
    """Return deliberately simple local scalar rankings.

    These are not proposed as physical rules. They are a sanity check: the
    available finite-fiber summaries do not arrive with a canonical extremum
    principle, and different plausible summaries pick different walls.
    """

    first = min(candidates, key=lambda candidate: candidate.reflected_component)
    return (
        _choose(candidates, "min_selector_norm", lambda c: c.selector_norm, prefer="min"),
        _choose(candidates, "max_selector_norm", lambda c: c.selector_norm, prefer="max"),
        _choose(
            candidates,
            "min_projection_dependency_norm",
            lambda c: c.projection_dependency_norm,
            prefer="min",
        ),
        _choose(
            candidates,
            "max_raw_wall_noether_residual",
            lambda c: c.raw_wall_noether_residual,
            prefer="max",
        ),
        CriterionChoice(
            criterion="lexicographic_first_spacelike_wall",
            selected_component=first.reflected_component,
            selected_name=first.name,
            score=float(first.reflected_component),
            source_of_rule="bookkeeping_order_not_a_source_action",
        ),
    )


def _external_current_choice(
    candidates: tuple[WallSelectorCandidate, ...],
    boundary_current: np.ndarray | None,
) -> ExternalCurrentChoice | None:
    """Pick a wall by a supplied current, if the supplied current is unique."""

    if boundary_current is None:
        return None
    current = np.asarray(boundary_current, dtype=float)
    if current.shape != (9,):
        raise ValueError(f"boundary_current must have shape (9,), got {current.shape}")

    weights = np.abs(current)
    selected_index = int(np.argmax(weights))
    selected_weight = float(weights[selected_index])
    if selected_weight <= 0.0:
        return None
    if int(np.count_nonzero(np.isclose(weights, selected_weight))) != 1:
        return None

    selected = next(
        candidate for candidate in candidates if candidate.reflected_component == selected_index
    )
    return ExternalCurrentChoice(
        selected_component=selected.reflected_component,
        selected_name=selected.name,
        current_weight=selected_weight,
        externally_keyed=True,
    )


def run_global_boundary_tau_data(
    boundary_current: np.ndarray | None = None,
) -> GlobalBoundaryTauReport:
    """Run the boundary-data selector blocker probe."""

    wall_report = run_topological_wall_tau_selector()
    choices = _local_criterion_choices(wall_report.candidates)
    external_choice = _external_current_choice(wall_report.candidates, boundary_current)

    provisional = GlobalBoundaryTauReport(
        verdict=GlobalBoundaryTauVerdict.FAILS,
        wall_report=wall_report,
        local_criterion_choices=choices,
        external_current_choice=external_choice,
        boundary_current_declared_by_source_action=False,
        source_forced_unique_selector=False,
        next_progress_point="SOURCE-CURRENT-DERIVATIVE-DATA",
    )

    if provisional.selection_still_needs_source_current_data:
        verdict = GlobalBoundaryTauVerdict.EXTERNALLY_KEYED_WALL_SELECTION_BLOCKED
    else:
        verdict = GlobalBoundaryTauVerdict.FAILS

    return GlobalBoundaryTauReport(
        verdict=verdict,
        wall_report=wall_report,
        local_criterion_choices=choices,
        external_current_choice=external_choice,
        boundary_current_declared_by_source_action=False,
        source_forced_unique_selector=False,
        next_progress_point="SOURCE-CURRENT-DERIVATIVE-DATA",
    )


if __name__ == "__main__":
    print(run_global_boundary_tau_data())
