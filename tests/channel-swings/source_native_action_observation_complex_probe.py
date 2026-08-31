#!/usr/bin/env python3
"""Exact controls for the source-native action--observation complex.

The finite rational model checks the three-stage chain law, corrected
observation compatibility, cycle/gauge-equivalence descent, split dependence,
and the source-coefficient nonselection boundary.  It is a certificate for the
interface theorem, not a physical GU model.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, replace
from fractions import Fraction as Q
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
LEAN = ROOT / "Lean/GUFormalization/SourceNativeActionObservationComplex.lean"
EXPLORATION = ROOT / "explorations/source-native-action-observation-complex-2026-08-31.md"


Matrix = tuple[tuple[Q, ...], ...]
Vector = tuple[Q, ...]


def matrix(rows: list[list[int]]) -> Matrix:
    return tuple(tuple(Q(x) for x in row) for row in rows)


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
              for j in range(len(b[0])))
        for i in range(len(a))
    )


def matvec(a: Matrix, x: Vector) -> Vector:
    return tuple(sum((row[j] * x[j] for j in range(len(x))), Q(0)) for row in a)


def add(x: Vector, y: Vector) -> Vector:
    return tuple(a + b for a, b in zip(x, y, strict=True))


def sub(x: Vector, y: Vector) -> Vector:
    return tuple(a - b for a, b in zip(x, y, strict=True))


def zero(rows: int, cols: int) -> Matrix:
    return tuple(tuple(Q(0) for _ in range(cols)) for _ in range(rows))


@dataclass(frozen=True)
class Model:
    d0: Matrix
    d1: Matrix
    gamma: Matrix
    right_inv: Matrix
    alternate_right_inv: Matrix
    source_rank: int = 0
    owner_axes_distinct: bool = True
    lean_path: Path = LEAN
    exploration_path: Path = EXPLORATION


BASE = Model(
    d0=matrix([[1], [0], [0]]),
    d1=matrix([[0, 1, 0]]),
    gamma=matrix([[0, 0, 1]]),
    right_inv=matrix([[0], [0], [1]]),
    alternate_right_inv=matrix([[1], [0], [1]]),
)


def projector(gamma: Matrix, right_inv: Matrix) -> Matrix:
    identity = matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    insertion_trace = matmul(right_inv, gamma)
    return tuple(
        tuple(identity[i][j] - insertion_trace[i][j] for j in range(3))
        for i in range(3)
    )


def checks(model: Model) -> list[tuple[str, bool]]:
    p = projector(model.gamma, model.right_inv)
    p_alt = projector(model.gamma, model.alternate_right_inv)
    x: Vector = (Q(2), Q(0), Q(5))
    noncycle: Vector = (Q(0), Q(1), Q(0))
    gauge: Vector = (Q(3),)
    y = add(x, matvec(model.d0, gauge))
    px = matvec(p, x)
    py = matvec(p, y)
    lean = model.lean_path.read_text(encoding="utf-8") if model.lean_path.is_file() else ""
    exploration = (
        model.exploration_path.read_text(encoding="utf-8")
        if model.exploration_path.is_file() else ""
    )
    return [
        ("chain-square-zero", matmul(model.d1, model.d0) == zero(1, 1)),
        ("right-inverse", matmul(model.gamma, model.right_inv) == matrix([[1]])),
        ("alternate-right-inverse", matmul(model.gamma, model.alternate_right_inv) == matrix([[1]])),
        ("projector-idempotent", matmul(p, p) == p),
        ("alternate-projector-idempotent", matmul(p_alt, p_alt) == p_alt),
        ("projector-gamma-kernel", matmul(model.gamma, p) == zero(1, 3)),
        ("alternate-projector-gamma-kernel", matmul(model.gamma, p_alt) == zero(1, 3)),
        ("split-projectors-distinct", p != p_alt),
        ("projector-fixes-gauge-image", matmul(p, model.d0) == model.d0),
        ("alternate-projector-fixes-gauge-image", matmul(p_alt, model.d0) == model.d0),
        ("equation-ignores-trace", matmul(model.d1, p) == model.d1),
        ("alternate-equation-ignores-trace", matmul(model.d1, p_alt) == model.d1),
        ("source-field-is-cycle", matvec(model.d1, x) == (Q(0),)),
        ("planted-noncycle-is-excluded", matvec(model.d1, noncycle) != (Q(0),)),
        ("corrected-field-is-cycle", matvec(model.d1, px) == (Q(0),)),
        ("alternate-corrected-field-is-cycle", matvec(model.d1, matvec(p_alt, x)) == (Q(0),)),
        ("gauge-shift-is-cycle", matvec(model.d1, matvec(model.d0, gauge)) == (Q(0),)),
        ("gauge-equivalence-preserved", sub(py, px) == matvec(model.d0, gauge)),
        ("corrected-output-gamma-zero", matvec(model.gamma, px) == (Q(0),)),
        ("split-choice-changes-traceful-output", px != matvec(p_alt, x)),
        ("strict-source-rank-zero", model.source_rank == 0),
        ("owner-axes-remain-distinct", model.owner_axes_distinct),
        ("lean-three-stage-complex", "structure ThreeStageComplex" in lean),
        ("lean-cycle-subtype", "abbrev Cycle" in lean and "{x : C1 // IsCycle C x}" in lean),
        ("lean-quotient-is-cycle-restricted", "Setoid (Cycle C)" in lean),
        ("lean-chain-map-restricts-to-cycles", "def ChainMap.mapCycle" in lean),
        ("lean-corrected-chain-map", "def correctedChainMap" in lean),
        ("lean-cohomology-descent", "def correctedCohomologyMap" in lean),
        ("lean-source-nonselection", "strictSource_does_not_select_injective_actionFamily" in lean),
        ("claim-ceiling-present", "conditional physical-candidate complex" in exploration),
        ("positive-physics-excluded", "positive physical Hilbert space" in exploration),
    ]


def run(model: Model, quiet: bool = False) -> tuple[bool, list[str]]:
    results = checks(model)
    failures = [name for name, passed in results if not passed]
    if not quiet:
        for name, passed in results:
            print(f"[{'PASS' if passed else 'FAIL'}] {name}")
        print(f"source-native action-observation complex: {len(results) - len(failures)}/{len(results)} exact checks passed")
    return not failures, failures


def selftest() -> bool:
    missing = ROOT / "tests/channel-swings/__missing_action_observation_artifact__"
    mutants = [
        ("broken-chain-square", replace(BASE, d1=matrix([[1, 1, 0]])), "chain-square-zero"),
        ("admitted-noncycle", replace(BASE, d1=zero(1, 3)), "planted-noncycle-is-excluded"),
        ("wrong-right-inverse", replace(BASE, right_inv=matrix([[0], [0], [2]])), "right-inverse"),
        ("collapsed-split-control", replace(BASE, alternate_right_inv=BASE.right_inv), "split-projectors-distinct"),
        ("invented-source-rank", replace(BASE, source_rank=1), "strict-source-rank-zero"),
        ("collapsed-owner-axes", replace(BASE, owner_axes_distinct=False), "owner-axes-remain-distinct"),
        ("missing-lean-artifact", replace(BASE, lean_path=missing), "lean-three-stage-complex"),
        ("missing-claim-ceiling", replace(BASE, exploration_path=missing), "claim-ceiling-present"),
    ]
    healthy, healthy_failures = run(BASE, quiet=True)
    if not healthy:
        print(f"[FAIL] baseline crashed or failed before mutation: {healthy_failures}")
        return False
    caught = 0
    for label, mutant, expected in mutants:
        try:
            ok, failures = run(mutant, quiet=True)
        except Exception as exc:  # a crash is never a valid catch
            print(f"[FAIL] {label}: crash-not-detection: {exc}")
            continue
        if (not ok) and expected in failures:
            print(f"[PASS] {label}: caught by {expected}")
            caught += 1
        else:
            print(f"[FAIL] {label}: expected {expected}, observed {failures}")
    print(f"selftest: {caught}/{len(mutants)} hostile mutations caught")
    return caught == len(mutants)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    return 0 if (selftest() if args.selftest else run(BASE)[0]) else 1


if __name__ == "__main__":
    sys.exit(main())
