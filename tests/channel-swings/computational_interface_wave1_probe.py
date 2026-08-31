#!/usr/bin/env python3
"""Exact controls for the computational-interface Wave 1 audit.

The finite model validates the audit machinery, not GU physics.
"""

from __future__ import annotations

import argparse
import copy
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Callable, Iterable


ROOT = Path(__file__).resolve().parents[2]
CHECKS: list[str] = []


def check(label: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(label)
    CHECKS.append(label)


@dataclass(frozen=True)
class Port:
    name: str
    admitted_external: bool
    kind: str
    witness: str
    cardinality: int | None = None


KNOWN_PORTS = (
    Port("chirality cell-selection", True, "TIEBREAKER", "net-chirality selector obstruction", 2),
    Port("causal orientation", True, "TIEBREAKER", "global orientation/section obstruction", 2),
    Port("stationary branch", True, "TIEBREAKER", "two surviving exact roots", 2),
    Port("W or mirror", True, "TIEBREAKER", "symmetric gate refusal", 2),
    Port("P1 orientation", True, "TIEBREAKER", "can orient but cannot select supplied line", 2),
    Port("generation count", True, "SETTING", "located-not-forced count freedom"),
    Port("absolute scale", True, "SETTING", "ratio-only scale freedom"),
    Port("boundary data", True, "SETTING", "positive-dimensional boundary moduli"),
    Port("balanced real-orbit seed R_0", True, "SETTING", "eight orbit types and no natural selector", 8),
    Port("observed trace right inverse j_B", False, "AUXILIARY_UNRESOLVED", "source/action/physical ownership open"),
    Port("54/210 family covector and coefficients", False, "IMPLEMENTATION_HOLE", "coefficient-complete source action open"),
    Port("B5 Gram/coefficient packet", False, "ADMISSION_UNRESOLVED", "EXTERNAL-VIA-GRAM packet remains fail-closed"),
)


def taxonomy_errors(ports: Iterable[Port]) -> list[str]:
    errors: list[str] = []
    for port in ports:
        if not port.admitted_external:
            continue
        if port.kind == "TIEBREAKER":
            if port.cardinality != 2:
                errors.append(f"{port.name}: tiebreaker is not binary")
            if not port.witness.strip():
                errors.append(f"{port.name}: missing obstruction/indifference witness")
        elif port.kind == "SETTING":
            if not port.witness.strip():
                errors.append(f"{port.name}: missing freedom witness")
        else:
            errors.append(f"{port.name}: admitted third type {port.kind}")
    return errors


def run_taxonomy_controls() -> None:
    check("PORT.baseline_has_no_admitted_third_type", taxonomy_errors(KNOWN_PORTS) == [])
    check(
        "PORT.unresolved_split_is_not_silently_counted",
        any(port.name.endswith("j_B") and not port.admitted_external for port in KNOWN_PORTS),
    )
    check(
        "PORT.post_spec_balanced_seed_is_caught_as_setting",
        any(port.name.endswith("R_0") and port.kind == "SETTING" and port.admitted_external for port in KNOWN_PORTS),
    )


BitState = tuple[int, int, int, int]


def flip(state: BitState, mask: tuple[int, int, int]) -> BitState:
    bit_0, bit_1, bit_2, setting = state
    mask_0, mask_1, mask_2 = mask
    return (bit_0 ^ mask_0, bit_1 ^ mask_1, bit_2 ^ mask_2, setting)


def orbit(state: BitState) -> frozenset[BitState]:
    return frozenset(flip(state, mask) for mask in product((0, 1), repeat=3))


def hidden_order_selector(states: list[BitState]) -> BitState:
    """Hostile implementation: an undeclared list order chooses a world."""
    return states[0]


def run_csp_controls() -> None:
    solutions = [
        (bit_0, bit_1, bit_2, setting)
        for bit_0, bit_1, bit_2 in product((0, 1), repeat=3)
        for setting in range(3)
    ]
    orbits = {orbit(state) for state in solutions}
    check("CSP.solution_count", len(solutions) == 24)
    check("CSP.setting_labels_exactly_three_symmetry_orbits", len(orbits) == 3)
    check("CSP.each_setting_orbit_has_eight_tied_representatives", {len(item) for item in orbits} == {8})
    check(
        "CSP.no_representative_is_fixed_by_the_full_flip_group",
        all(any(flip(state, mask) != state for mask in product((0, 1), repeat=3)) for state in solutions),
    )
    check("CSP.three_bits_plus_one_setting_select_one_world", (1, 0, 1, 2) in solutions)
    ordered = sorted(solutions)
    check(
        "CSP.hidden_solver_order_is_detected_as_an_undeclared_input",
        hidden_order_selector(ordered) != hidden_order_selector(list(reversed(ordered))),
    )


Vector = tuple[Fraction, Fraction]


def gamma(vector: Vector) -> Fraction:
    return vector[0]


def split(parameter: Fraction) -> Callable[[Fraction], Vector]:
    return lambda scalar: (scalar, parameter * scalar)


def subtract(left: Vector, right: Vector) -> Vector:
    return (left[0] - right[0], left[1] - right[1])


def projector(parameter: Fraction, vector: Vector) -> Vector:
    return subtract(vector, split(parameter)(gamma(vector)))


def run_split_controls() -> None:
    rationals = [Fraction(value) for value in range(-3, 4)]
    vectors = [(left, right) for left in rationals for right in rationals]
    first, second = Fraction(-2), Fraction(3)
    check("SPLIT.every_j_t_is_a_right_inverse", all(gamma(split(first)(value)) == value for value in rationals))
    check(
        "SPLIT.projector_difference_identity",
        all(
            subtract(projector(first, vector), projector(second, vector))
            == subtract(split(second)(gamma(vector)), split(first)(gamma(vector)))
            for vector in vectors
        ),
    )
    check(
        "SPLIT.distinct_right_inverses_give_distinct_maps",
        any(projector(first, vector) != projector(second, vector) for vector in vectors),
    )
    check(
        "SPLIT.all_projectors_land_in_the_common_kernel",
        all(gamma(projector(parameter, vector)) == 0 for parameter in (first, second) for vector in vectors),
    )
    check(
        "SPLIT.all_projectors_fix_exactly_the_common_kernel",
        all(
            (projector(parameter, vector) == vector) == (gamma(vector) == 0)
            for parameter in (first, second)
            for vector in vectors
        ),
    )
    kernel_samples = [(Fraction(0), value) for value in rationals]
    check(
        "SPLIT.common_kernel_is_split_independent_even_when_maps_are_not",
        all(projector(first, vector) == vector == projector(second, vector) for vector in kernel_samples),
    )


@dataclass(frozen=True)
class ActionCandidate:
    name: str
    admitted: bool
    owner_native: bool
    coefficient_complete: bool
    target_blind: bool
    full_euler_hilbert: bool
    n2_metric_stationary: bool | None = None
    n3_nongauge_hessian: bool | None = None


CURRENT_ACTIONS = (
    ActionCandidate("CBRS-1 first-action class", False, False, False, True, False),
    ActionCandidate("W154/W229 branch-3 transfer", False, False, True, True, False),
    ActionCandidate("residual-square deformation", False, True, True, True, False),
)


def action_screen(candidates: Iterable[ActionCandidate]) -> tuple[str, tuple[str, ...]]:
    eligible = tuple(
        candidate
        for candidate in candidates
        if candidate.admitted
        and candidate.owner_native
        and candidate.coefficient_complete
        and candidate.target_blind
        and candidate.full_euler_hilbert
    )
    if not eligible:
        return ("NO_ADMISSIBLE_CANDIDATE", ())
    passing = tuple(
        candidate.name
        for candidate in eligible
        if candidate.n2_metric_stationary is True and candidate.n3_nongauge_hessian is True
    )
    return (("SAT" if passing else "UNSAT_WITHIN_FROZEN_GRAMMAR"), passing)


def run_action_controls() -> None:
    verdict, passing = action_screen(CURRENT_ACTIONS)
    check("ACTION.current_named_grammar_has_no_admissible_candidate", verdict == "NO_ADMISSIBLE_CANDIDATE")
    check("ACTION.empty_grammar_is_not_reported_as_unsat", verdict != "UNSAT_WITHIN_FROZEN_GRAMMAR" and passing == ())
    control = ActionCandidate("positive evaluator control", True, True, True, True, True, True, True)
    check("ACTION.evaluator_positive_control", action_screen((control,)) == ("SAT", (control.name,)))


SOURCE_MARKERS = {
    "explorations/computational-interface-wave1-2026-08-31.md": (
        "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.",
        "An empty grammar is not an UNSAT result",
        "No source claim, ledger row, action owner",
    ),
    "CURRENT-STATE.yaml": (
        "action-root set is empty",
        "P_B = 1 - j_B Gamma_B",
        "right inverse j_B",
    ),
    "explorations/source-native-split-naturality-and-burnside-correspondence-composition-2026-08-31.md": (
        "P_j1 - P_j2 = (j2 - j1) Gamma",
        "if and only if `j1 = j2`",
    ),
    "explorations/conditional-build/selected-k100-rsap-balanced-order-parameter-owner-census-2026-08-15.md": (
        "eight `O(7,7)` orbit types",
        "balanced real-orbit seed R_0",
    ),
    "explorations/source-coefficient-packet-rank-certificate-2026-08-31.md": (
        "strict source matrix has zero equations",
        "No equation in the packet supplies a family",
    ),
}


def source_marker_errors(markers: dict[str, tuple[str, ...]]) -> list[str]:
    errors: list[str] = []
    for relative, expected in markers.items():
        text = (ROOT / relative).read_text(encoding="utf-8")
        for marker in expected:
            if marker not in text:
                errors.append(f"{relative}: missing {marker}")
    return errors


def run_selftest() -> None:
    third_type = KNOWN_PORTS + (Port("history update", True, "UPDATE", "irreversible external update"),)
    check("SELFTEST.third_type_mutation_is_caught", any("third type" in error for error in taxonomy_errors(third_type)))
    nonbinary = tuple(
        Port(port.name, port.admitted_external, port.kind, port.witness, 3 if port.name == "stationary branch" else port.cardinality)
        for port in KNOWN_PORTS
    )
    check("SELFTEST.nonbinary_tiebreaker_mutation_is_caught", any("not binary" in error for error in taxonomy_errors(nonbinary)))
    unwitnessed = tuple(
        Port(port.name, port.admitted_external, port.kind, "" if port.name == "absolute scale" else port.witness, port.cardinality)
        for port in KNOWN_PORTS
    )
    check("SELFTEST.unwitnessed_setting_mutation_is_caught", any("missing freedom" in error for error in taxonomy_errors(unwitnessed)))
    fake = ActionCandidate("synthetic ownerless candidate", True, False, True, True, True, True, True)
    check("SELFTEST.ownerless_action_mutation_stays_inadmissible", action_screen((fake,))[0] == "NO_ADMISSIBLE_CANDIDATE")
    failing = ActionCandidate("eligible N3 failure", True, True, True, True, True, True, False)
    check("SELFTEST.eligible_failed_candidate_reports_scoped_unsat", action_screen((failing,))[0] == "UNSAT_WITHIN_FROZEN_GRAMMAR")
    poisoned = copy.deepcopy(SOURCE_MARKERS)
    poisoned["CURRENT-STATE.yaml"] += ("THIS MARKER MUST NOT EXIST",)
    check("SELFTEST.source_currency_poison_is_caught", len(source_marker_errors(poisoned)) == 1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()

    run_taxonomy_controls()
    run_csp_controls()
    run_split_controls()
    run_action_controls()
    check("SOURCE.currency_markers_present", source_marker_errors(SOURCE_MARKERS) == [])
    if args.selftest:
        run_selftest()

    print(f"computational interface Wave 1: {len(CHECKS)}/{len(CHECKS)} exact controls passed")
    for label in CHECKS:
        print(f"  PASS: {label}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
