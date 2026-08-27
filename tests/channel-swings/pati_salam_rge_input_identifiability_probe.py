#!/usr/bin/env python3
"""M-M22 exact input-identifiability probe for a Pati-Salam scale run."""

from __future__ import annotations

import argparse
from dataclasses import dataclass, replace
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Inputs:
    representation: str
    result: str
    low: tuple[F, F, F]
    ps: tuple[F, F, F]


def determinant(low: tuple[F, F, F], ps: tuple[F, F, F]) -> F:
    b1, b2, b3 = low
    b4, b_l, b_r = ps
    c12 = F(3, 5) * b_r + F(2, 5) * b4 - b_l
    c23 = b_l - b4
    return (b1 - b2) * c23 - (b2 - b3) * c12


def solve_logs(low: tuple[F, F, F], ps: tuple[F, F, F], a12: F = F(29), a23: F = F(21)) -> tuple[F, F]:
    b1, b2, b3 = low
    b4, b_l, b_r = ps
    m11, m12 = b1 - b2, F(3, 5) * b_r + F(2, 5) * b4 - b_l
    m21, m22 = b2 - b3, b_l - b4
    det = m11 * m22 - m21 * m12
    if det == 0:
        raise ValueError("rank-deficient scale system")
    return ((a12 * m22 - a23 * m12) / det,
            (m11 * a23 - m21 * a12) / det)


def load_inputs() -> Inputs:
    representation = (ROOT / "explorations/conditional-build/cb-a-representation-content-2026-08-05.md").read_text(encoding="utf-8")
    result = (ROOT / "explorations/pati-salam-rge-input-identifiability-2026-08-27.md").read_text(encoding="utf-8")
    return Inputs(
        representation=representation,
        result=result,
        low=(F(41, 10), F(-19, 6), F(-7)),
        ps=(F(-7), F(-3), F(11, 3)),
    )


def evaluate(inp: Inputs, emit: bool = True) -> list[str]:
    alt_ps = (F(-5), F(-2), F(7, 2))
    det = determinant(inp.low, inp.ps)
    distinct = det != 0 and determinant(inp.low, alt_ps) != 0 and solve_logs(inp.low, inp.ps) != solve_logs(inp.low, alt_ps)
    checks = [
        ("hypercharge matching weights sum to one", F(3, 5) + F(2, 5) == 1),
        ("standard unified normalization gives sin^2(theta_W)=3/8", (F(3, 5) / (1 + F(3, 5))) == F(3, 8)),
        ("owner evidence grades the absolute normalization BOUGHT",
         "`sin²θ_W = 3/8` at the unification boundary, is filed **BOUGHT**" in inp.representation),
        ("one-loop scale system is identifiable only after beta coefficients are supplied", det != 0),
        ("different admissible coefficient packets produce different scale logs", distinct),
        ("determination requires interval spectra and threshold matching",
         "interval mass spectrum" in inp.result and "threshold matching" in inp.result),
        ("determination requires two-loop matrices plus Yukawa/scalar inputs",
         "two-loop gauge matrices" in inp.result and "Yukawa and scalar-coupling inputs" in inp.result),
        ("determination records the pre-beta ceiling", "RGE_UNCOMPUTABLE_PREBETA" in inp.result),
    ]
    failures = [name for name, ok in checks if not ok]
    if emit:
        for name, ok in checks:
            print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    return failures


def selftest(inp: Inputs) -> bool:
    if evaluate(inp):
        print("[FAIL] clean baseline is red; mutations are not bankable")
        return False
    mutations = [
        ("bought-grade", replace(inp, representation=inp.representation.replace("is filed **BOUGHT**", "is filed **EARNED**", 1))),
        ("spectrum-owner", replace(inp, result=inp.result.replace("interval mass spectrum", "group labels alone", 1))),
        ("matching-owner", replace(inp, result=inp.result.replace("threshold matching", "threshold-free running", 1))),
        ("two-loop-owner", replace(inp, result=inp.result.replace("two-loop gauge matrices", "one-loop labels", 1))),
        ("ceiling", replace(inp, result=inp.result.replace("RGE_UNCOMPUTABLE_PREBETA", "RGE_SCALES_COMPUTED"))),
    ]
    caught = 0
    for name, mutant in mutations:
        failures = evaluate(mutant, emit=False)
        ok = bool(failures)
        print(f"[{'PASS' if ok else 'FAIL'}] mutation {name} caught by genuine failing check"
              f"{': ' + failures[0] if failures else ''}")
        caught += int(ok)
    print(f"SUMMARY: 8/8 baseline checks; {caught}/{len(mutations)} mutations caught")
    return caught == len(mutations)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    inp = load_inputs()
    ok = selftest(inp) if args.selftest else not evaluate(inp)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
