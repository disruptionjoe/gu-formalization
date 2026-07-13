"""Topological-wall tau selector probe for the anchor-scale A-door.

This is an analogy-driven but GU-native finite-fiber test.  The Klein-bottle
cosmology lens suggests the mechanism class

    global topology -> wall/order parameter -> tangent/source selection.

Here we model the weakest version of that idea using spacelike reflection wall
involutions on the existing Cl(9,5) carrier.  The question is not whether such
walls can make tangent maps.  They can.  The question is whether the repo has
enough GU-native data to force a unique nonzero tangent selector instead of
choosing one wall and then projecting by hand.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
import itertools
import sys

import numpy as np


SOURCE_ROOT = Path(__file__).resolve().parents[1]
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))

from lib import gu_bridge  # noqa: E402
from lib.anchor_scale_a_door import ETA, quaternionic_J, spinor_krein_metric  # noqa: E402


ANCHOR_BARE_COMMUTATOR = 58.7215
ANCHOR_C2 = 155.3625
TOL = 1.0e-8


class TopologicalWallTauVerdict(str, Enum):
    """Outcome labels for the topological-wall tau selector probe."""

    NONZERO_WALL_SELECTORS_UNDERDETERMINED = (
        "nonzero_wall_selectors_underdetermined"
    )
    FAILS = "fails"


@dataclass(frozen=True)
class WallSelectorCandidate:
    """One wall-involution tangent selector candidate."""

    name: str
    reflected_component: int
    selector_norm: float
    selector_rank: int
    selector_noether_residual: float
    raw_wall_noether_residual: float
    projection_dependency_norm: float
    h_linear_defect: float
    krein_wall_residual: float
    involution_residual: float

    @property
    def admissible_finite_fiber_wall(self) -> bool:
        return (
            self.selector_norm > 1.0
            and self.selector_rank == gu_bridge.DIM
            and self.selector_noether_residual < TOL
            and self.h_linear_defect < 1.0e-7
            and self.krein_wall_residual < TOL
            and self.involution_residual < TOL
        )

    @property
    def still_uses_projection_repair(self) -> bool:
        return (
            self.raw_wall_noether_residual > 1.0
            and self.projection_dependency_norm > 1.0
        )


@dataclass(frozen=True)
class TopologicalWallTauReport:
    """Machine-checkable report for the wall/tau selector probe."""

    verdict: TopologicalWallTauVerdict
    candidates: tuple[WallSelectorCandidate, ...]
    admissible_count: int
    distinct_selector_count: int
    min_pairwise_selector_distance: float
    max_pairwise_selector_distance: float
    max_noether_residual: float
    max_h_linear_defect: float
    max_krein_wall_residual: float
    min_projection_dependency_norm: float
    bare_commutator_norm: float
    c2_norm: float
    source_forced_unique_selector: bool
    next_progress_point: str

    @property
    def nonzero_wall_selectors_exist(self) -> bool:
        return self.admissible_count > 0

    @property
    def wall_family_is_underdetermined(self) -> bool:
        return (
            self.admissible_count > 1
            and self.distinct_selector_count > 1
            and self.min_pairwise_selector_distance > 1.0
        )

    @property
    def wall_lens_still_needs_boundary_data(self) -> bool:
        return (
            self.nonzero_wall_selectors_exist
            and self.wall_family_is_underdetermined
            and not self.source_forced_unique_selector
        )


def _rank(matrix: np.ndarray, tol: float = 1.0e-8) -> int:
    return int(np.linalg.matrix_rank(matrix, tol=tol))


def _vector_spinor_injection(direction: np.ndarray, spin_dim: int) -> np.ndarray:
    """Return spinor -> vector-spinor injection psi |-> direction tensor psi."""

    vector_dim = int(direction.shape[0])
    injection = np.zeros((vector_dim * spin_dim, spin_dim), dtype=complex)
    for vector_index, coeff in enumerate(direction):
        start = vector_index * spin_dim
        injection[start : start + spin_dim, :] = coeff * np.eye(spin_dim)
    return injection


def _spacelike_wall_involution(
    component: int,
    spin_lift: np.ndarray,
) -> np.ndarray:
    """Build a spacelike reflection wall on the vector-spinor carrier."""

    reflection = np.eye(gu_bridge.N, dtype=complex)
    reflection[component, component] = -1.0
    return np.kron(reflection, spin_lift)


def _candidate_for_component(
    component: int,
    gamma_trace: np.ndarray,
    pi_rs: np.ndarray,
    raw_gauge: np.ndarray,
    spin_lift: np.ndarray,
    spinor_j: np.ndarray,
    krein_metric: np.ndarray,
) -> tuple[WallSelectorCandidate, np.ndarray]:
    wall = _spacelike_wall_involution(component, spin_lift)
    transformed = wall @ raw_gauge @ spin_lift.conj().T
    raw_wall_difference = transformed - raw_gauge
    selector = pi_rs @ raw_wall_difference

    vector_spinor_j = np.kron(np.eye(gu_bridge.N, dtype=complex), spinor_j)
    h_linear_defect = float(
        np.linalg.norm(vector_spinor_j @ selector.conj() - selector @ spinor_j)
    )

    candidate = WallSelectorCandidate(
        name=f"spacelike-reflection-wall-{component}",
        reflected_component=component,
        selector_norm=float(np.linalg.norm(selector)),
        selector_rank=_rank(selector),
        selector_noether_residual=float(np.linalg.norm(gamma_trace @ selector)),
        raw_wall_noether_residual=float(
            np.linalg.norm(gamma_trace @ raw_wall_difference)
        ),
        projection_dependency_norm=float(np.linalg.norm(raw_wall_difference - selector)),
        h_linear_defect=h_linear_defect,
        krein_wall_residual=float(np.linalg.norm(wall.conj().T @ krein_metric @ wall - krein_metric)),
        involution_residual=float(
            np.linalg.norm(wall @ wall - np.eye(wall.shape[0], dtype=complex))
        ),
    )
    return candidate, selector


def run_topological_wall_tau_selector(
    xi: np.ndarray | None = None,
) -> TopologicalWallTauReport:
    """Run the topology/wall-inspired tangent selector probe."""

    e, gamma_trace, pi_rs, mass_operator = gu_bridge.constraint_objects()
    spin_dim = gu_bridge.DIM
    vector_dim = gu_bridge.N

    if xi is None:
        xi = np.asarray(gu_bridge.XI, dtype=complex)
    else:
        xi = np.asarray(xi, dtype=complex)
    if xi.shape != (vector_dim,):
        raise ValueError(f"xi must have shape ({vector_dim},), got {xi.shape}")

    raw_gauge = _vector_spinor_injection(xi, spin_dim)
    spinor_j = quaternionic_J(e, seed=1)
    beta = spinor_krein_metric(e)
    krein_metric = np.kron(np.diag(ETA).astype(complex), beta)

    candidates: list[WallSelectorCandidate] = []
    selectors: list[np.ndarray] = []
    for component in range(9):  # spacelike reflections are genuine involutions here.
        candidate, selector = _candidate_for_component(
            component=component,
            gamma_trace=gamma_trace,
            pi_rs=pi_rs,
            raw_gauge=raw_gauge,
            spin_lift=e[component],
            spinor_j=spinor_j,
            krein_metric=krein_metric,
        )
        candidates.append(candidate)
        selectors.append(selector)

    pairwise_distances = [
        float(np.linalg.norm(left - right))
        for left, right in itertools.combinations(selectors, 2)
    ]
    min_pairwise = min(pairwise_distances) if pairwise_distances else 0.0
    max_pairwise = max(pairwise_distances) if pairwise_distances else 0.0
    distinct_selector_count = 1
    for selector in selectors[1:]:
        if all(np.linalg.norm(selector - earlier) > 1.0e-8 for earlier in selectors[:distinct_selector_count]):
            distinct_selector_count += 1

    admissible_count = sum(candidate.admissible_finite_fiber_wall for candidate in candidates)

    bare_commutator = pi_rs @ mass_operator - mass_operator @ pi_rs
    c2_operator = gamma_trace @ mass_operator @ pi_rs
    bare_commutator_norm = float(np.linalg.norm(bare_commutator))
    c2_norm = float(np.linalg.norm(c2_operator))

    anchors_preserved = (
        abs(bare_commutator_norm - ANCHOR_BARE_COMMUTATOR) < 1.0e-4
        and abs(c2_norm - ANCHOR_C2) < 1.0e-4
    )
    all_admissible_need_projection = all(
        candidate.still_uses_projection_repair for candidate in candidates
    )
    underdetermined = (
        admissible_count > 1
        and distinct_selector_count > 1
        and min_pairwise > 1.0
    )

    if anchors_preserved and admissible_count > 0 and underdetermined and all_admissible_need_projection:
        verdict = TopologicalWallTauVerdict.NONZERO_WALL_SELECTORS_UNDERDETERMINED
    else:
        verdict = TopologicalWallTauVerdict.FAILS

    return TopologicalWallTauReport(
        verdict=verdict,
        candidates=tuple(candidates),
        admissible_count=admissible_count,
        distinct_selector_count=distinct_selector_count,
        min_pairwise_selector_distance=min_pairwise,
        max_pairwise_selector_distance=max_pairwise,
        max_noether_residual=max(candidate.selector_noether_residual for candidate in candidates),
        max_h_linear_defect=max(candidate.h_linear_defect for candidate in candidates),
        max_krein_wall_residual=max(candidate.krein_wall_residual for candidate in candidates),
        min_projection_dependency_norm=min(
            candidate.projection_dependency_norm for candidate in candidates
        ),
        bare_commutator_norm=bare_commutator_norm,
        c2_norm=c2_norm,
        source_forced_unique_selector=False,
        next_progress_point="GLOBAL-BOUNDARY-CONDITION-TAU-DATA",
    )


if __name__ == "__main__":
    print(run_topological_wall_tau_selector())
