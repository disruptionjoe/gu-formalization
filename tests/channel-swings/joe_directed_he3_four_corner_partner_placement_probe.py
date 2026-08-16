#!/usr/bin/env python3
"""HE-3: exact four-corner partner placement and family-rank controls.

This probe composes two already-owned ingredients without replacing either:

1. HE-1's exact complex D5 weight arithmetic for 16, 16bar, 144, and
   144bar along Spin(10) -> Pati-Salam -> Standard Model.
2. The source-aligned (7,7) carrier-horn census from referee_legA2_verify.py:
   the source-stated effective half has three spin-1/2 family units in one 16
   and a dark gamma-traceless 144bar; its conjugate half reverses both labels.

The complex branching facts are horn-robust.  The assignment of those modules
to an effective physical half, and any interpretation as a mass, are not.
Nothing here computes a generation index, net chirality, real-form bilinear,
operator domain, quotient, background, scale, threshold, or observable.
"""
from __future__ import annotations

from fractions import Fraction as F
import contextlib
import importlib.util
import io
from pathlib import Path


CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    CHECKS.append((name, bool(ok)))


# Reuse the exact, positive-controlled D5 engine rather than copy its weight
# conventions.  HE-1 prints a report and exits; both are contained here.
REPO = Path(__file__).resolve().parents[2]
HE1_PATH = REPO / "tests/channel-swings/joe_directed_imposter_separation_probe.py"
spec = importlib.util.spec_from_file_location("he1_exact_engine", HE1_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"cannot load HE-1 exact engine: {HE1_PATH}")
he1 = importlib.util.module_from_spec(spec)
captured = io.StringIO()
he1_exit = None
with contextlib.redirect_stdout(captured):
    try:
        spec.loader.exec_module(he1)
    except SystemExit as exc:
        he1_exit = exc.code

check("HE-1 dependency reruns cleanly (62/62 exact checks)", he1_exit == 0)


def ladder(left, right) -> tuple[int, int, int]:
    """(Spin(10), PS, SM) singlet multiplicities, all exact."""
    product = he1.tensor(left, right)
    return (
        he1.invariants(product, he1.SO10),
        he1.invariants(product, he1.PS),
        he1.invariants(product, he1.SM, extra_zero=(he1.hyper,)),
    )


LADDERS = {
    "16 x 144": ladder(he1.C16, he1.W144),
    "16 x 144bar": ladder(he1.C16, he1.W144B),
    "16bar x 144": ladder(he1.C16B, he1.W144),
    "16bar x 144bar": ladder(he1.C16B, he1.W144B),
}

check("all four tensor products have dimension 16*144 = 2304",
      all(sum(he1.tensor(a, b).values()) == 2304 for a, b in (
          (he1.C16, he1.W144),
          (he1.C16, he1.W144B),
          (he1.C16B, he1.W144),
          (he1.C16B, he1.W144B),
      )))
check("cross-half ladder: Inv(16 x 144) = (0, 2, 11)",
      LADDERS["16 x 144"] == (0, 2, 11))
check("same-effective-half ladder: Inv(16 x 144bar) = (0, 0, 3)",
      LADDERS["16 x 144bar"] == (0, 0, 3))
check("conjugate same-effective-half ladder: Inv(16bar x 144) = (0, 0, 3)",
      LADDERS["16bar x 144"] == (0, 0, 3))
check("conjugate cross-half ladder: Inv(16bar x 144bar) = (0, 2, 11)",
      LADDERS["16bar x 144bar"] == (0, 2, 11))
check("complex-conjugation control pairs the four ladders",
      LADDERS["16 x 144"] == LADDERS["16bar x 144bar"]
      and LADDERS["16 x 144bar"] == LADDERS["16bar x 144"])
check("Spin(10) has no bare singlet in any of the four products",
      all(values[0] == 0 for values in LADDERS.values()))
check("at Pati-Salam exactly the two cross-half products open two channels",
      [name for name, values in LADDERS.items() if values[1] == 2]
      == ["16 x 144", "16bar x 144bar"])
check("same-effective-half products first acquire channels only below PS",
      LADDERS["16 x 144bar"][1:] == (0, 3)
      and LADDERS["16bar x 144"][1:] == (0, 3))


# Direct branching-content controls.  These distinguish the placement result
# from a numerical coincidence in the invariant counter.
PS144B = he1.ps_content(he1.W144B)
check("144 contains each conjugate-family PS block once",
      len(he1.PS16B) == 2
      and all(he1.PS144.get(block, 0) == 1 for block in he1.PS16B))
check("144bar contains each family PS block once",
      len(he1.PS16) == 2
      and all(PS144B.get(block, 0) == 1 for block in he1.PS16))
check("wrong-half PS family blocks are absent in both orientations",
      all(he1.PS144.get(block, 0) == 0 for block in he1.PS16)
      and all(PS144B.get(block, 0) == 0 for block in he1.PS16B))


# Source-aligned (7,7) horn.  This is a typed premise from the corrected
# source census, not a new derivation and not a claim about a generation index.
SOURCE_EFFECTIVE_HALF_77 = ("16", "16", "16", "144bar")
CONJUGATE_EFFECTIVE_HALF_77 = ("16bar", "16bar", "16bar", "144")
check("source-aligned (7,7) effective-half premise carries 3 x 16 plus 144bar",
      SOURCE_EFFECTIVE_HALF_77.count("16") == 3
      and SOURCE_EFFECTIVE_HALF_77.count("144bar") == 1)
check("its conjugate effective half carries 3 x 16bar plus 144",
      CONJUGATE_EFFECTIVE_HALF_77.count("16bar") == 3
      and CONJUGATE_EFFECTIVE_HALF_77.count("144") == 1)
check("the PS partner for either family sector lies across, not within, that half",
      LADDERS["16 x 144"][1] == 2
      and LADDERS["16 x 144bar"][1] == 0
      and LADDERS["16bar x 144bar"][1] == 2
      and LADDERS["16bar x 144"][1] == 0)


def matrix_rank(rows: list[list[F]]) -> int:
    """Exact Gaussian rank over Q."""
    if not rows:
        return 0
    matrix = [[F(value) for value in row] for row in rows]
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("ragged matrix")
    rank = 0
    for column in range(width):
        pivot = next((r for r in range(rank, len(matrix))
                      if matrix[r][column] != 0), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        scale = matrix[rank][column]
        matrix[rank] = [value / scale for value in matrix[rank]]
        for r in range(len(matrix)):
            if r == rank or matrix[r][column] == 0:
                continue
            factor = matrix[r][column]
            matrix[r] = [value - factor * pivot_value
                         for value, pivot_value in zip(matrix[r], matrix[rank])]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def right_multiply(rows: list[list[F]], basis: list[list[F]]) -> list[list[F]]:
    """Change family basis on the three columns."""
    return [[sum(F(row[k]) * F(basis[k][j]) for k in range(len(basis)))
             for j in range(len(basis[0]))] for row in rows]


# Two PS invariant blocks give two a priori distinct rows in three-family
# space.  Multiplicity fixes the number of rows, not their relative direction.
ALIGNED = [[F(1), F(2), F(-1)], [F(2), F(4), F(-2)]]
INDEPENDENT = [[F(1), F(0), F(0)], [F(0), F(1), F(0)]]
ONE_CHANNEL = [[F(1), F(-1), F(2)], [F(0), F(0), F(0)]]
ZERO = [[F(0), F(0), F(0)], [F(0), F(0), F(0)]]
FAMILY_BASIS_CHANGE = [
    [F(1), F(1), F(0)],
    [F(0), F(1), F(1)],
    [F(1), F(0), F(1)],
]

check("planted proportional PS rows have rank 1 and leave a two-dimensional kernel",
      matrix_rank(ALIGNED) == 1 and 3 - matrix_rank(ALIGNED) == 2)
check("planted independent PS rows have rank 2 and leave only a one-dimensional kernel",
      matrix_rank(INDEPENDENT) == 2 and 3 - matrix_rank(INDEPENDENT) == 1)
check("one active channel also has rank 1; channel count alone does not identify its origin",
      matrix_rank(ONE_CHANNEL) == 1 and 3 - matrix_rank(ONE_CHANNEL) == 2)
check("zero rows have rank 0 and leave all three family directions untouched",
      matrix_rank(ZERO) == 0 and 3 - matrix_rank(ZERO) == 3)
check("family-basis changes preserve aligned and independent ranks",
      matrix_rank(FAMILY_BASIS_CHANGE) == 3
      and matrix_rank(right_multiply(ALIGNED, FAMILY_BASIS_CHANGE)) == 1
      and matrix_rank(right_multiply(INDEPENDENT, FAMILY_BASIS_CHANGE)) == 2)
check("the same two-channel multiplicity permits rank 1 and rank 2 controls",
      len(ALIGNED) == len(INDEPENDENT) == LADDERS["16 x 144"][1]
      and matrix_rank(ALIGNED) != matrix_rank(INDEPENDENT))


# The repository/source supplies no family-space rows for these two PS
# contractions.  Keep absence typed rather than filling it with a fit.
SOURCE_FAMILY_ROW_MATRIX = None
check("TYPE_MISSING: source family-row matrix is not supplied",
      SOURCE_FAMILY_ROW_MATRIX is None)


print("HE-3 four-corner invariant ladders (Spin(10), PS, SM):")
for name, values in LADDERS.items():
    print(f"  {name:20s} -> {values}")
print()
print("Source-aligned (7,7) effective-half premise:")
print(f"  source-stated half : {SOURCE_EFFECTIVE_HALF_77}")
print(f"  conjugate half     : {CONJUGATE_EFFECTIVE_HALF_77}")
print("  PS partner placement: CROSS-HALF only")
print()
print("Exact two-channel family-rank controls (three family columns):")
for name, rows in (("aligned", ALIGNED), ("independent", INDEPENDENT),
                   ("one-channel", ONE_CHANNEL), ("zero", ZERO)):
    rank = matrix_rank(rows)
    print(f"  {name:12s}: rank={rank}, kernel dimension={3-rank}, rows={rows}")
print()
print("HE-3 boundary: BRIDGE_OR_SEMANTIC_BOUNDARY")
print("  TYPE_MISSING: source-owned family-row alignment/intertwiner")
print("  TYPE_MISSING: effective-half selector and physical operator placement")
print("  SOURCE_SILENT: background, scale, threshold, quotient, and observable")
print("  No generation-index or chirality/parity inference is made.")
print()

passed = sum(1 for _, ok in CHECKS if ok)
for name, ok in CHECKS:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print(f"\n{passed}/{len(CHECKS)} exact checks passed")
raise SystemExit(0 if passed == len(CHECKS) else 1)
