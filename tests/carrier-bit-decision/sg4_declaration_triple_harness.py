#!/usr/bin/env python3
"""SG4 declaration-triple harness for the carrier A / B / bare fork.

This is the executable shape demanded by the escape-corners campaign:
future source-action candidates must report a TRIPLE, not a single bit:

  1. invariance: does the quadratic/source form carry the linearized scalar-spinor
     odd variation?
  2. declaration: if no odd invariance is present, which field space is declared
     (`ker Gamma`, full vector-spinor, or bare unconstrained)?
  3. phase: unbroken/chiral, broken/super-Higgs, or massive/ungauged.

Hard guards run first. A candidate that imports the target or kills the bare
commutator anchor is rejected before any carrier reading is allowed.

Run from the repo root:

    python tests/carrier-bit-decision/sg4_declaration_triple_harness.py

This script does not build the source action and does not change any verdict. It
keeps SG4 as the decider by making the decision surface explicit and reusable.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from math import isclose


BARE_COMMUTATOR_ANCHOR = 58.7215
ANCHOR_TOL = 1e-3

TARGET_IMPORT_TOKENS = {
    "24/8=3",
    "chi(K3)=24",
    "ch2=24",
    "Ahat=3",
    "assumed K3",
    "fitted holonomy",
    "reverse-engineered rank",
    "post-hoc target normalization",
}


class Invariance(Enum):
    """Whether the built form carries the scalar-spinor odd variation."""

    PRESENT = "present"
    ABSENT = "absent"
    UNBUILT = "unbuilt"


class Declaration(Enum):
    """Field-space declaration if odd invariance does not auto-force one."""

    KER_GAMMA = "ker_gamma"
    FULL_VECTOR_SPINOR = "full_vector_spinor"
    BARE_UNCONSTRAINED = "bare_unconstrained"
    UNDECLARED = "undeclared"


class Phase(Enum):
    """Vacuum/phase register for the declared source-action sector."""

    UNBROKEN = "unbroken"
    BROKEN_SUPER_HIGGS = "broken_super_higgs"
    MASSIVE_UNGAUGED = "massive_ungauged"
    UNSELECTED = "unselected"


class Outcome(Enum):
    TARGET_IMPORT_FAIL = "target_import_fail"
    ACAUSAL_TRAP_FAIL = "acausal_trap_fail"
    OPEN_UNBUILT = "open_unbuilt"
    CARRIER_A_UNBROKEN = "carrier_a_unbroken"
    BARE_CONTROL_BROKEN = "bare_control_broken"
    CARRIER_B_MASSIVE = "carrier_b_massive"
    BARE_UNCONSTRAINED = "bare_unconstrained"
    OPEN_PHASE_UNSELECTED = "open_phase_unselected"


@dataclass(frozen=True)
class Candidate:
    name: str
    invariance: Invariance
    declaration: Declaration
    phase: Phase
    target_imports: tuple[str, ...] = ()
    bare_commutator_norm: float = BARE_COMMUTATOR_ANCHOR


@dataclass(frozen=True)
class TripleReport:
    candidate: str
    invariance: Invariance
    declaration: Declaration
    phase: Phase
    effective_declaration: Declaration
    outcome: Outcome
    index_density: int | None
    z24_class: tuple[int, int, int] | None
    reason: str
    canon_movement: bool = False


def guard_target_import(candidate: Candidate) -> tuple[bool, str]:
    hits = sorted(set(candidate.target_imports) & TARGET_IMPORT_TOKENS)
    if hits:
        return False, "forbidden target import(s): " + ", ".join(hits)
    return True, "no forbidden target imports"


def guard_bare_commutator(candidate: Candidate) -> tuple[bool, str]:
    if not isclose(candidate.bare_commutator_norm, BARE_COMMUTATOR_ANCHOR, abs_tol=ANCHOR_TOL):
        return (
            False,
            f"bare commutator anchor moved from {BARE_COMMUTATOR_ANCHOR} "
            f"to {candidate.bare_commutator_norm}",
        )
    return True, "bare commutator anchor preserved"


def effective_declaration(candidate: Candidate) -> Declaration:
    """Odd invariance auto-declares full vector-spinor field space."""
    if candidate.invariance is Invariance.PRESENT:
        return Declaration.FULL_VECTOR_SPINOR
    return candidate.declaration


def classify(candidate: Candidate) -> TripleReport:
    target_ok, target_reason = guard_target_import(candidate)
    if not target_ok:
        return TripleReport(
            candidate.name,
            candidate.invariance,
            candidate.declaration,
            candidate.phase,
            candidate.declaration,
            Outcome.TARGET_IMPORT_FAIL,
            None,
            None,
            target_reason,
        )

    anchor_ok, anchor_reason = guard_bare_commutator(candidate)
    if not anchor_ok:
        return TripleReport(
            candidate.name,
            candidate.invariance,
            candidate.declaration,
            candidate.phase,
            candidate.declaration,
            Outcome.ACAUSAL_TRAP_FAIL,
            None,
            None,
            anchor_reason,
        )

    if candidate.invariance is Invariance.UNBUILT:
        return TripleReport(
            candidate.name,
            candidate.invariance,
            candidate.declaration,
            candidate.phase,
            candidate.declaration,
            Outcome.OPEN_UNBUILT,
            None,
            None,
            "SG4 source action is unbuilt; invariance/declaration/phase cannot yet be read",
        )

    decl = effective_declaration(candidate)
    if decl is Declaration.FULL_VECTOR_SPINOR:
        if candidate.phase is Phase.UNBROKEN:
            return TripleReport(
                candidate.name,
                candidate.invariance,
                candidate.declaration,
                candidate.phase,
                decl,
                Outcome.CARRIER_A_UNBROKEN,
                -42,
                (0, 0, 0),
                "odd invariance auto-declares full field space; unbroken phase lands carrier A",
            )
        if candidate.phase is Phase.BROKEN_SUPER_HIGGS:
            return TripleReport(
                candidate.name,
                candidate.invariance,
                candidate.declaration,
                candidate.phase,
                decl,
                Outcome.BARE_CONTROL_BROKEN,
                -40,
                (0, 1, 2),
                "super-Higgs/goldstino return cancels the scalar-spinor subtraction; bare row",
            )
        return TripleReport(
            candidate.name,
            candidate.invariance,
            candidate.declaration,
            candidate.phase,
            decl,
            Outcome.OPEN_PHASE_UNSELECTED,
            None,
            None,
            "full field space is selected, but the unbroken/broken phase is not selected",
        )

    if decl is Declaration.KER_GAMMA:
        return TripleReport(
            candidate.name,
            candidate.invariance,
            candidate.declaration,
            candidate.phase,
            decl,
            Outcome.CARRIER_B_MASSIVE,
            -38,
            (0, 2, 1),
            "no odd invariance; gamma-trace-constrained massive/ungauged declaration lands carrier B",
        )

    if decl is Declaration.BARE_UNCONSTRAINED:
        return TripleReport(
            candidate.name,
            candidate.invariance,
            candidate.declaration,
            candidate.phase,
            decl,
            Outcome.BARE_UNCONSTRAINED,
            -40,
            (0, 1, 2),
            "bare unconstrained field space lands the control row",
        )

    return TripleReport(
        candidate.name,
        candidate.invariance,
        candidate.declaration,
        candidate.phase,
        decl,
        Outcome.OPEN_UNBUILT,
        None,
        None,
        "no field-space declaration supplied",
    )


def print_report(report: TripleReport) -> None:
    print(f"{report.candidate}")
    print(f"  invariance          : {report.invariance.value}")
    print(f"  surface declaration : {report.declaration.value}")
    print(f"  phase               : {report.phase.value}")
    print(f"  effective declaration: {report.effective_declaration.value}")
    print(f"  outcome             : {report.outcome.value}")
    print(f"  index density       : {report.index_density}")
    print(f"  Z/24 class          : {report.z24_class}")
    print(f"  reason              : {report.reason}")
    print(f"  canon movement      : {report.canon_movement}")


def main() -> None:
    print("=" * 78)
    print("SG4 declaration-triple harness")
    print("=" * 78)

    current = Candidate(
        name="current SG4 state",
        invariance=Invariance.UNBUILT,
        declaration=Declaration.UNDECLARED,
        phase=Phase.UNSELECTED,
    )
    controls = [
        current,
        Candidate(
            name="control: unbroken graded-IG A-door",
            invariance=Invariance.PRESENT,
            declaration=Declaration.UNDECLARED,
            phase=Phase.UNBROKEN,
        ),
        Candidate(
            name="control: broken/super-Higgs A-door",
            invariance=Invariance.PRESENT,
            declaration=Declaration.UNDECLARED,
            phase=Phase.BROKEN_SUPER_HIGGS,
        ),
        Candidate(
            name="control: massive ungauged ker-Gamma declaration",
            invariance=Invariance.ABSENT,
            declaration=Declaration.KER_GAMMA,
            phase=Phase.MASSIVE_UNGAUGED,
        ),
        Candidate(
            name="control: bare unconstrained declaration",
            invariance=Invariance.ABSENT,
            declaration=Declaration.BARE_UNCONSTRAINED,
            phase=Phase.UNSELECTED,
        ),
        Candidate(
            name="control: target import fail",
            invariance=Invariance.ABSENT,
            declaration=Declaration.KER_GAMMA,
            phase=Phase.MASSIVE_UNGAUGED,
            target_imports=("chi(K3)=24",),
        ),
        Candidate(
            name="control: acausal trap fail",
            invariance=Invariance.ABSENT,
            declaration=Declaration.KER_GAMMA,
            phase=Phase.MASSIVE_UNGAUGED,
            bare_commutator_norm=0.0,
        ),
    ]

    reports = [classify(candidate) for candidate in controls]
    for report in reports:
        print()
        print_report(report)

    expected = {
        "current SG4 state": Outcome.OPEN_UNBUILT,
        "control: unbroken graded-IG A-door": Outcome.CARRIER_A_UNBROKEN,
        "control: broken/super-Higgs A-door": Outcome.BARE_CONTROL_BROKEN,
        "control: massive ungauged ker-Gamma declaration": Outcome.CARRIER_B_MASSIVE,
        "control: bare unconstrained declaration": Outcome.BARE_UNCONSTRAINED,
        "control: target import fail": Outcome.TARGET_IMPORT_FAIL,
        "control: acausal trap fail": Outcome.ACAUSAL_TRAP_FAIL,
    }
    for report in reports:
        assert report.outcome is expected[report.candidate], report
        assert report.canon_movement is False, report

    # Core invariants from the campaign: the three physical rows stay distinct.
    by_name = {report.candidate: report for report in reports}
    assert by_name["control: unbroken graded-IG A-door"].z24_class == (0, 0, 0)
    assert by_name["control: broken/super-Higgs A-door"].z24_class == (0, 1, 2)
    assert by_name["control: massive ungauged ker-Gamma declaration"].z24_class == (0, 2, 1)

    print("\n" + "-" * 78)
    print("RESULT: SG4 triple harness OK")
    print("The current state remains OPEN_UNBUILT; controls discriminate A, B, bare,")
    print("target-import, and acausal-trap outcomes without moving canon or verdicts.")


if __name__ == "__main__":
    main()
