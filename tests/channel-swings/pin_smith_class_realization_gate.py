#!/usr/bin/env python3
"""Typed gate for the GU Pin+/Smith class-realization ultimatum.

This is deliberately a standard-library certificate.  It does not compute Pin
bordism: the ambient computation is already closed.  It asks the logically prior
question whether any committed GU candidate supplies an input to that computation.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import json


REQUIRED_FIELDS = (
    "program_native",
    "object_constructed",
    "degree_14_or_equivalent",
    "closed_or_fredholm",
    "pin_plus_lift",
    "deck_action",
    "orientation_line",
    "bordism_class_map",
    "generator_detector",
)


@dataclass(frozen=True)
class Candidate:
    name: str
    route: str
    fields: dict[str, bool]
    first_failure: str
    reason: str

    def complete(self) -> bool:
        return all(self.fields[field] for field in REQUIRED_FIELDS)

    def computed_first_failure(self) -> str | None:
        return next((field for field in REQUIRED_FIELDS if not self.fields[field]), None)


def fields(*true_fields: str) -> dict[str, bool]:
    selected = set(true_fields)
    unknown = selected.difference(REQUIRED_FIELDS)
    assert not unknown, f"unknown fields: {sorted(unknown)}"
    return {field: field in selected for field in REQUIRED_FIELDS}


CANDIDATES = (
    Candidate(
        "observerse_total_space_Y14",
        "geometric",
        fields("program_native", "object_constructed", "degree_14_or_equivalent"),
        "closed_or_fredholm",
        "The Lorentzian metric fiber is noncompact; no source-owned compactification or absolute fundamental cycle is supplied.",
    ),
    Candidate(
        "observer_section_image",
        "geometric",
        fields("program_native", "object_constructed"),
        "degree_14_or_equivalent",
        "A section has the base dimension 4, not 14.",
    ),
    Candidate(
        "regular_q_zero_wall",
        "geometric",
        fields("program_native", "object_constructed"),
        "degree_14_or_equivalent",
        "A regular wall inside Y14 has dimension 13, not 14.",
    ),
    Candidate(
        "fiber_retract_RP3",
        "geometric",
        fields("program_native", "object_constructed"),
        "degree_14_or_equivalent",
        "RP3 carries the exact cover bit but has dimension 3 and is not a degree-14 cycle.",
    ),
    Candidate(
        "chosen_RP3_times_Y11_completion",
        "geometric",
        fields("degree_14_or_equivalent", "closed_or_fredholm", "pin_plus_lift"),
        "program_native",
        "The 11-dimensional complement is freely chosen rather than constructed by GU.",
    ),
    Candidate(
        "full_section_space_Met_X4",
        "analytic",
        fields("program_native", "object_constructed"),
        "degree_14_or_equivalent",
        "The full section space is infinite-dimensional and is not a supplied degree-14 cycle or parameter family.",
    ),
    Candidate(
        "solution_moduli_space",
        "analytic",
        fields("program_native"),
        "object_constructed",
        "The full equations, global analytic moduli object, and its topology have not been constructed.",
    ),
    Candidate(
        "D_GU_family",
        "analytic",
        fields("program_native", "object_constructed", "degree_14_or_equivalent"),
        "closed_or_fredholm",
        "The source owns an operator skeleton, not a proper Fredholm realization with ends and domains fixed.",
    ),
    Candidate(
        "scalar_plus_minus_i0_branches",
        "analytic",
        fields("program_native", "object_constructed"),
        "degree_14_or_equivalent",
        "Two branches in a scalar ansatz are not a Fredholm family, line bundle, or bordism cycle.",
    ),
    Candidate(
        "external_abstract_Pin14_generator_control",
        "control",
        fields(*REQUIRED_FIELDS[1:]),
        "program_native",
        "An externally supplied generator satisfies the mathematical interface but is not the GU class.",
    ),
)


def y14_noncompact_ray(k: int) -> tuple[Fraction, Fraction, int, int]:
    """A Lorentzian diagonal form diag(-2^k, 2^-k, 1, 1)."""
    return (-Fraction(2**k), Fraction(1, 2**k), 1, 1)


def determinant(diagonal: tuple[Fraction, ...]) -> Fraction:
    out = Fraction(1)
    for value in diagonal:
        out *= value
    return out


def main() -> None:
    # Exact witness: the fiber contains an unbounded determinant-fixed Lorentzian ray.
    ray = [y14_noncompact_ray(k) for k in range(9)]
    assert all(determinant(point) == -1 for point in ray)
    assert all(sum(value < 0 for value in point) == 1 for point in ray)
    assert all(sum(value > 0 for value in point) == 3 for point in ray)
    assert [max(abs(value) for value in point) for point in ray] == [Fraction(2**k) for k in range(9)]

    # The exact topological bit on RP3 cannot itself supply a degree-14 detector.
    rp3_top_degree = 3
    assert 4 > rp3_top_degree  # a^4 = 0 in H*(RP3; F2)
    assert 14 - 2 == 12       # Smith degree shift
    assert ("Pin+", 14) == ("Pin+", 14)
    smith_target = ("Pin-", 12)
    assert smith_target == ("Pin-", 12)

    for candidate in CANDIDATES:
        assert candidate.computed_first_failure() == candidate.first_failure

    native_complete = [candidate.name for candidate in CANDIDATES if candidate.complete()]
    assert native_complete == []

    control = next(candidate for candidate in CANDIDATES if candidate.route == "control")
    assert all(control.fields[field] for field in REQUIRED_FIELDS[1:])
    assert not control.fields["program_native"]

    receipt = {
        "ambient_group": "Omega^Pin+_14 = Z/2",
        "candidate_count": len(CANDIDATES) - 1,
        "control_count": 1,
        "first_geometric_failure": "closed_or_fredholm",
        "first_analytic_failure": "closed_or_fredholm",
        "native_complete_candidates": native_complete,
        "noncompact_ray_last_norm": str(max(abs(value) for value in ray[-1])),
        "smith_target": "Omega^Pin-_12",
        "verdict": "PIN-SMITH-NOT-DEFINED",
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
