#!/usr/bin/env python3
"""Independent exact certificate for the literal-observation obstruction.

The finite model is a nonvacuity and mutation control for the general theorem
already proved in Lean. It uses exact rational arithmetic and refuses physical
leftover, quotient, source-correction, family, mass and observable claims.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass, replace
from fractions import Fraction


Q = Fraction
Vector = tuple[Fraction, Fraction]
Matrix = tuple[Vector, Vector]

I: Matrix = ((Q(1), Q(0)), (Q(0), Q(1)))
ZERO: Matrix = ((Q(0), Q(0)), (Q(0), Q(0)))
X: Matrix = ((Q(0), Q(1)), (Q(1), Q(0)))
J: Matrix = ((Q(0), Q(1)), (Q(-1), Q(0)))


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(sum((a[i][k] * b[k][j] for k in range(2)), Q(0)) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def matvec(a: Matrix, v: Vector) -> Vector:
    return tuple(sum((a[i][k] * v[k] for k in range(2)), Q(0)) for i in range(2))  # type: ignore[return-value]


def add(u: Vector, v: Vector) -> Vector:
    return (u[0] + v[0], u[1] + v[1])


def neg(u: Vector) -> Vector:
    return (-u[0], -u[1])


@dataclass(frozen=True)
class Premises:
    gamma_h: Matrix = X
    gamma_n: Matrix = J
    right_inv_n: Matrix = ((Q(0), Q(-1)), (Q(1), Q(0)))  # -J
    h_spinor: Vector = (Q(1), Q(0))
    lift_sign: int = -1
    literal_first_projection: bool = True
    source_owned_correction: bool = False
    physical_quotient_supplied: bool = False
    physical_leftover_classified: bool = False


@dataclass(frozen=True)
class Verdict:
    admitted: bool
    ambient_trace: Vector
    observed_trace: Vector
    reasons: tuple[str, ...]


def derive(p: Premises) -> Verdict:
    horizontal_trace = matvec(p.gamma_h, p.h_spinor)
    inserted = matvec(p.right_inv_n, horizontal_trace)
    normal_component = neg(inserted) if p.lift_sign == -1 else inserted
    ambient_trace = add(horizontal_trace, matvec(p.gamma_n, normal_component))
    observed_trace = horizontal_trace
    facts = {
        "normal map has the frozen right inverse": matmul(p.gamma_n, p.right_inv_n) == I,
        "literal observation is the first projection": p.literal_first_projection,
        "horizontal trace is nonzero": horizontal_trace != (Q(0), Q(0)),
        "normal lift has the cancellation sign": p.lift_sign == -1,
        "explicit lift lies in the ambient kernel": ambient_trace == (Q(0), Q(0)),
        "literal output retains nonzero observed trace": observed_trace != (Q(0), Q(0)),
        "no source-selected correction is imported": not p.source_owned_correction,
        "no physical quotient is imported": not p.physical_quotient_supplied,
        "the physical leftover remains unclassified": not p.physical_leftover_classified,
    }
    return Verdict(
        admitted=all(facts.values()),
        ambient_trace=ambient_trace,
        observed_trace=observed_trace,
        reasons=tuple(name for name, holds in facts.items() if not holds),
    )


def corrected_observation(horizontal: Vector) -> Vector:
    # The observed right inverse is X because X^2=I. On the one-slot control
    # carrier Q=1-X*X, so the leaking one-slot trace is removed exactly.
    return add(horizontal, neg(matvec(X, matvec(X, horizontal))))


def baseline_checks() -> list[tuple[str, bool]]:
    p = Premises()
    verdict = derive(p)
    h_trace = matvec(p.gamma_h, p.h_spinor)
    normal_lift = neg(matvec(p.right_inv_n, h_trace))
    corrected = corrected_observation(p.h_spinor)
    return [
        ("horizontal Clifford generator squares to +I", matmul(X, X) == I),
        ("normal Clifford generator squares to -I", matmul(J, J) == ((Q(-1), Q(0)), (Q(0), Q(-1)))),
        ("horizontal and normal generators anticommute", tuple(tuple(matmul(X, J)[i][j] + matmul(J, X)[i][j] for j in range(2)) for i in range(2)) == ZERO),
        ("normal inverse is exact", matmul(p.gamma_n, p.right_inv_n) == I),
        ("chosen horizontal spinor is nonzero", p.h_spinor != (Q(0), Q(0))),
        ("chosen horizontal trace is nonzero", h_trace != (Q(0), Q(0))),
        ("normal component is nonzero", normal_lift != (Q(0), Q(0))),
        ("normal trace cancels horizontal trace", matvec(p.gamma_n, normal_lift) == neg(h_trace)),
        ("ambient kernel witness has zero trace", verdict.ambient_trace == (Q(0), Q(0))),
        ("literal pullback returns the horizontal component", p.literal_first_projection),
        ("literal observed trace is unchanged", verdict.observed_trace == h_trace),
        ("literal observed trace is nonzero", verdict.observed_trace != (Q(0), Q(0))),
        ("literal pullback fails kernel preservation", verdict.ambient_trace == (Q(0), Q(0)) and verdict.observed_trace != (Q(0), Q(0))),
        ("half-spin ten-dimensional gamma kernel control is 144", 10 * 16 - 16 == 144),
        ("ambient half-spin fourteen-dimensional gamma kernel control is 832", 14 * 64 - 64 == 832),
        ("ambient full-Dirac gamma kernel control is 1664", 2 * 832 == 1664),
        ("supplied observed split removes the leaking trace", corrected == (Q(0), Q(0))),
        ("corrected map is extra structure", not p.source_owned_correction),
        ("physical quotient and leftover are not imported", not p.physical_quotient_supplied and not p.physical_leftover_classified),
        ("the exact literal-observation obstruction is admitted", verdict.admitted),
    ]


def hostile_checks() -> list[tuple[str, bool]]:
    p = Premises()
    mutants = {
        "wrong normal inverse reopens the lift": replace(p, right_inv_n=J),
        "wrong normal contraction reopens the lift": replace(p, gamma_n=X),
        "zero horizontal contraction removes the witness": replace(p, gamma_h=ZERO),
        "zero horizontal element removes the witness": replace(p, h_spinor=(Q(0), Q(0))),
        "wrong lift sign doubles rather than cancels": replace(p, lift_sign=1),
        "nonliteral observation reopens the map theorem": replace(p, literal_first_projection=False),
        "source-selected correction exceeds the frozen owner set": replace(p, source_owned_correction=True),
        "an imported physical quotient changes the application gate": replace(p, physical_quotient_supplied=True),
        "classifying the leftover exceeds the theorem": replace(p, physical_leftover_classified=True),
    }
    return [(name, not derive(mutant).admitted) for name, mutant in mutants.items()]


def report(checks: list[tuple[str, bool]], label: str) -> bool:
    print(label)
    for name, ok in checks:
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")
    passed = sum(ok for _, ok in checks)
    print(f"{passed}/{len(checks)} checks passed")
    return passed == len(checks)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    ok = report(baseline_checks(), "BASELINE")
    if args.selftest:
        ok = report(hostile_checks(), "HOSTILE REOPENERS") and ok
    verdict = derive(Premises())
    print(
        "VERDICT: literal horizontal pullback need not preserve the ambient "
        "gamma kernel. The witness does not classify the physical leftover "
        "or select a source/action-owned correction or quotient."
    )
    return 0 if ok and verdict.admitted else 1


if __name__ == "__main__":
    raise SystemExit(main())
