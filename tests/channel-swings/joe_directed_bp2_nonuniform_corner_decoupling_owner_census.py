#!/usr/bin/env python3
"""BP2 exact conditional incidence and bounded owner-census certificate.

This probe does not choose or construct a decoupling or mass map. It accepts
B1P1's three-corner support theorem and asks a smaller algebraic question: if
a nonzero family row and an H210 stage are declared, what is the minimum
non-uniform incidence on M_3 tensor S_16?
"""

from __future__ import annotations

import argparse
import contextlib
from fractions import Fraction as F
import importlib.util
import io
from pathlib import Path
import sys


# Loading exact helper modules must leave the dependency checkout read-only.
sys.dont_write_bytecode = True


CHECKS: list[tuple[str, bool]] = []


def check(name: str, condition: object) -> None:
    CHECKS.append((name, bool(condition)))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load dependency: {path}")
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


def right_multiply(row: list[F], matrix: list[list[F]]) -> list[F]:
    return [sum(row[k] * matrix[k][j] for k in range(len(row)))
            for j in range(len(matrix[0]))]


def tensor_vectors(a: list[F], b: list[F]) -> list[F]:
    return [x * y for x in a for y in b]


def matvec(matrix: list[list[F | int]], vector: list[F]) -> list[F]:
    return [sum(F(x) * y for x, y in zip(row, vector)) for row in matrix]


def kernel_basis_for_row(row: list[F]) -> list[list[F]]:
    """Return two independent vectors in ker(row), without choosing semantics."""
    pivot = next(i for i, value in enumerate(row) if value)
    out: list[list[F]] = []
    for free in range(3):
        if free == pivot:
            continue
        vector = [F(0)] * 3
        vector[free] = F(1)
        vector[pivot] = -row[free] / row[pivot]
        out.append(vector)
    return out


def block_diagonal(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    aw = len(a[0]) if a else 0
    bw = len(b[0]) if b else 0
    return ([row + [0] * bw for row in a]
            + [[0] * aw + row for row in b])


def exact_incidence_checks(cb6, cb2) -> None:
    row = [F(2), F(-1), F(3)]
    kernel_basis = kernel_basis_for_row(row)
    check("nonzero family row has a two-dimensional kernel",
          cb6.rank([row]) == 1 and cb6.rank(kernel_basis) == 2)
    check("constructed kernel basis is annihilated by the row",
          all(sum(x * y for x, y in zip(row, vector)) == 0
              for vector in kernel_basis))

    for stage_rank in (0, 8, 12, 16):
        stage = cb6.diagonal_stage(16, stage_rank)
        composite = cb6.row_tensor_stage([int(x) for x in row], stage)
        observed_rank = cb6.rank(composite)
        check(f"rank(r tensor B) equals rank(B) at k={stage_rank}",
              observed_rank == stage_rank)
        check(f"kernel exact-sequence dimension at k={stage_rank}",
              48 - observed_rank == 32 + (16 - stage_rank))

        for family_vector in kernel_basis:
            for spin_index in (0, 7, 15):
                spin_vector = [F(0)] * 16
                spin_vector[spin_index] = F(1)
                domain_vector = tensor_vectors(family_vector, spin_vector)
                check(
                    f"K tensor S inclusion at k={stage_rank}, spin={spin_index}",
                    all(value == 0 for value in matvec(composite, domain_vector)),
                )

        # This q has row(q)=1 and therefore presents a generator of L=M_3/K.
        quotient_representative = [F(1, 2), F(0), F(0)]
        check(f"quotient generator normalized at k={stage_rank}",
              sum(x * y for x, y in zip(row, quotient_representative)) == 1)
        for spin_index in range(stage_rank, 16):
            spin_vector = [F(0)] * 16
            spin_vector[spin_index] = F(1)
            domain_vector = tensor_vectors(quotient_representative, spin_vector)
            check(f"L tensor ker(B) lifts into kernel at k={stage_rank}, spin={spin_index}",
                  all(value == 0 for value in matvec(composite, domain_vector)))

    basis = [
        [F(1), F(1), F(0)],
        [F(0), F(1), F(1)],
        [F(1), F(0), F(2)],
    ]
    check("family coordinate-change matrix is invertible", cb6.rank(basis) == 3)
    moved = right_multiply(row, basis)
    for stage_rank in (0, 8, 12, 16):
        stage = cb6.diagonal_stage(16, stage_rank)
        base_rank = cb6.rank(cb6.row_tensor_stage([int(x) for x in row], stage))
        moved_rank = cb6.rank(cb6.row_tensor_stage([int(x) for x in moved], stage))
        scaled_rank = cb6.rank(cb6.row_tensor_stage([6, -3, 9], stage))
        check(f"GL(3,Q) and row-line covariance at k={stage_rank}",
              base_rank == moved_rank == scaled_rank == stage_rank)

    stage12 = cb6.diagonal_stage(16, 12)
    one_half = cb6.row_tensor_stage([2, -1, 3], stage12)
    two_halves = block_diagonal(one_half, one_half)
    check("independent conjugate halves have direct-sum rank 2k",
          cb6.rank(two_halves) == 24)
    check("independent conjugate halves have kernel 2(48-k)",
          96 - cb6.rank(two_halves) == 72)

    check("equation-9.16 forward cells are exactly (1,2) and (0,3)",
          cb2.FORWARD == {(1, 2), (0, 3)})
    check("equation-9.16 reverse cells are exactly (3,0) and (2,1)",
          cb2.REVERSE == {(3, 0), (2, 1)})
    check("pp/mm positions remain wrong-channel controls",
          cb2.WRONG_PP_MM == {(0, 2), (1, 3)}
          and cb2.FORWARD.isdisjoint(cb2.WRONG_PP_MM))
    check("both forward arrows stay within their effective package",
          all(cb2.HALF[cb2.COLS[c]] == cb2.HALF[cb2.ROW_OUTPUT[r]]
              for r, c in cb2.FORWARD))
    check("pp/mm controls cross the effective packages",
          all(cb2.HALF[cb2.COLS[c]] != cb2.HALF[cb2.ROW_OUTPUT[r]]
              for r, c in cb2.WRONG_PP_MM))


def rsc1_wrong_direction_checks(rsc1) -> None:
    n = 5
    spin16 = rsc1.wts_spinor(+1, n)
    hw16 = (1,) * 5
    hw120 = (2, 2, 2, 0, 0)
    hw144 = (3, 1, 1, 1, 1)
    d16144 = rsc1.klimyk(hw144, spin16, n)
    d1616 = rsc1.klimyk(hw16, spin16, n)
    check("RSC1 wrong direction: mult(120,16 tensor 144)=0",
          d16144.get(hw120, 0) == 0)
    check("RSC1 positive control: mult(120,16 tensor 16)=1",
          d1616.get(hw120, 0) == 1)
    check("RSC1 detector distinguishes 144 from 16",
          d16144.get(hw120, 0) != d1616.get(hw120, 0))


OWNER_CENSUS = {
    # This is a bounded, cited artifact-status census, not a global no-go.
    "H210": (True, True, True, False, False, False),
    "H54": (False, False, False, False, False, False),
    "RSC1_120": (True, False, False, False, False, False),
    "FQZ_observation_lifts": (True, False, False, False, False, False),
    "density_dual_cell_reversal": (True, False, True, False, False, False),
}


def census_checks() -> None:
    # Columns: built relevant structure, right direction, right cells, owned
    # r, ALIGN, and phase. Non-port controls may occupy the first column while
    # still failing the direction/cell conjunction.
    viable = [name for name, facts in OWNER_CENSUS.items() if all(facts[:3])]
    closed = [name for name, facts in OWNER_CENSUS.items() if all(facts)]
    check("bounded inventory has exactly one direction-and-cell candidate",
          viable == ["H210"])
    check("bounded inventory has no fully owned route", closed == [])
    check("every enumerated candidate remains family-row blind",
          all(not facts[3] for facts in OWNER_CENSUS.values()))


REQUIRED_REPO_TOKENS = {
    "lab/active-research/joe-directed/bit1-price/b1p1-three-corner-support-prices-the-chiral-grant-2026-08-17.md": (
        "CHIRAL implies PRESENT implies carrier A",
        "mass map is non-uniform across the fermionic extension",
    ),
    "lab/active-research/joe-directed/high-energy-two-plus-one/cb1-h210-k77-rs-intertwiner-2026-08-16.md": (
        "r:M_3=C^3 -> C", "two-dimensional", "TYPE_MISSING",
    ),
    "lab/active-research/joe-directed/high-energy-two-plus-one/cb2-h210-equation916-cross-half-composition-2026-08-16.md": (
        "`(1,2)`", "`(0,3)`", "wrong PS products have invariant count zero",
    ),
    "lab/active-research/joe-directed/high-energy-two-plus-one/cb6-h210-three-horn-compatibility-2026-08-16.md": (
        "H210-ALIGN", "F_corr", "M_3", "Z/internal-144",
    ),
    "lab/active-research/joe-directed/high-energy-two-plus-one/he3-four-corner-partner-placement-and-family-rank-2026-08-16.md": (
        "source-owned family-row intertwiner", "TYPE_MISSING",
    ),
    "lab/active-research/joe-directed/rs-corner/rsc1-unique-channel-lives-on-the-gamma-trace-2026-08-17.md": (
        "16 (x) 144   contains the `120` with multiplicity  0",
        "16 (x) 16 = 10 (+) 120 (+) 126",
    ),
}


def repository_custody_checks(repo: Path) -> None:
    for relative, tokens in REQUIRED_REPO_TOKENS.items():
        text = (repo / relative).read_text(encoding="utf-8")
        check(f"repository custody tokens: {relative}",
              all(token in text for token in tokens))


FORBIDDEN_PROMOTIONS = (
    "selected_map", "massive_implies_b", "a_to_b_transition",
    "kernel_is_true_families", "quotient_is_imposter", "f_equals_144",
    "bars_identified", "low_phase_nonzero_incidence", "global_uniqueness",
    "action_derived", "vacuum_selected", "background_selected",
    "external_datum_built", "scale_fitted", "physical_quotient",
)


def validate_semantics(state: dict[str, bool]) -> None:
    if any(state.get(flag, False) for flag in FORBIDDEN_PROMOTIONS):
        raise AssertionError("forbidden semantic or ownership promotion")
    if state.get("imposter_semantics", False) and not state.get("align_declared", False):
        raise AssertionError("imposter semantics require declared H210-ALIGN")
    if state.get("phase_activation", False) and not state.get("phase_declared", False):
        raise AssertionError("cell activation requires a phase declaration")


def semantic_selftest() -> int:
    validate_semantics({})
    validate_semantics({"align_declared": True, "imposter_semantics": True})
    validate_semantics({"phase_declared": True, "phase_activation": True})
    mutants = [{flag: True} for flag in FORBIDDEN_PROMOTIONS]
    mutants += [{"imposter_semantics": True}, {"phase_activation": True}]
    fired = 0
    for mutant in mutants:
        try:
            validate_semantics(mutant)
        except AssertionError:
            fired += 1
        else:
            raise AssertionError(f"semantic mutant did not fire: {mutant}")
    return fired


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True,
                        help="read-only path to gu-formalization")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    repo = args.repo.resolve()

    cb6 = load_module("bp2_cb6", repo / "tests/channel-swings/joe_directed_cb6_h210_three_horn_compatibility_probe.py")
    cb2 = load_module("bp2_cb2", repo / "tests/channel-swings/joe_directed_cb2_h210_equation916_composition_probe.py")
    rsc1 = load_module("bp2_rsc1", repo / "tests/channel-swings/joe_directed_rsc1_unique_channel_lives_on_the_gamma_trace.py")

    exact_incidence_checks(cb6, cb2)
    rsc1_wrong_direction_checks(rsc1)
    census_checks()
    repository_custody_checks(repo)

    failed = [name for name, ok in CHECKS if not ok]
    for name, ok in CHECKS:
        print(f"{'PASS' if ok else 'FAIL'} {name}")
    print(f"BP2 exact/custody checks: {len(CHECKS) - len(failed)}/{len(CHECKS)}")
    if args.selftest:
        fired = semantic_selftest()
        expected = len(FORBIDDEN_PROMOTIONS) + 2
        print(f"PASS semantic mutants fired: {fired}/{expected}")
    print("BP2 verdict: CONDITIONAL_INCIDENCE_SURVIVES__OWNER_ROUTE_DEPENDENCY_FENCED")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
