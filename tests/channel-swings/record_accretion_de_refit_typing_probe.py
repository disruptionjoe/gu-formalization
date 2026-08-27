#!/usr/bin/env python3
"""M-H13 semantic-custody probe: a self-energy ratio is not an H(z) coefficient."""

from __future__ import annotations

import argparse
from dataclasses import dataclass, replace
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Sources:
    w187: str
    w154: str
    w230: str
    seat: str
    result: str


def load_sources() -> Sources:
    read = lambda p: (ROOT / p).read_text(encoding="utf-8")
    return Sources(
        w187=read("explorations/W187-gu-dressed-open-selfenergy-2026-07-14.md"),
        w154=read("explorations/W154-reverse-engineered-source-action-2026-07-14.md"),
        w230=read("explorations/W230-close-a4-derive-w154-2026-07-14.md"),
        seat=read("lab/process/anchor-council-2026-08-03/seat2-cosmology.md"),
        result=read("explorations/record-accretion-de-refit-typing-ceiling-2026-08-27.md"),
    )


def evaluate(src: Sources, emit: bool = True) -> list[str]:
    checks = [
        ("W187 types r as a self-energy magnitude ratio",
         "|Sigma_ext|/|Sigma_internal|" in src.w187),
        ("W187 labels the square-root growth law as a model",
         "the specific power is a" in src.w187 and "model" in src.w187),
        ("W154 proves monotone record accretion gives withdrawal",
         "monotone DECREASING" in src.w154 and "monotone withdrawal, no zero-crossing" in src.w154),
        ("W230 makes the record-current bridge conditional",
         "if and only if" in src.w230 and "c_kin = 0" in src.w230),
        ("the prior council explicitly rejects r as a dark-energy coefficient",
         "not a density, not an equation of state, and does not appear in `H(z)`" in src.seat),
        ("the prior council records that N(z) is absent from the DE pipeline",
         "There is no `N(z)` anywhere in the DE pipeline" in src.seat),
        ("the determination forbids the homonym refit",
         "HOMONYM_REFIT_NOT_LICENSED" in src.result),
        ("the determination names all three reopen owners",
         all(token in src.result for token in ("owned bridge", "owned `N(z)`", "coupling target"))),
    ]
    failures = [name for name, ok in checks if not ok]
    if emit:
        for name, ok in checks:
            print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    return failures


def selftest(src: Sources) -> bool:
    if evaluate(src):
        print("[FAIL] clean baseline is red; mutations are not bankable")
        return False
    mutations = [
        ("ratio-type", replace(src, w187=src.w187.replace("|Sigma_ext|/|Sigma_internal|", "|Sigma_ext|+|Sigma_internal|", 1))),
        ("model-grade", replace(src, w187=src.w187.replace("the specific power is a", "the specific power is exact", 1))),
        ("withdrawal", replace(src, w154=src.w154.replace("monotone withdrawal, no zero-crossing", "monotone rise", 1))),
        ("bridge-condition", replace(src, w230=src.w230.replace("if and only if", "regardless of whether"))),
        ("result-ceiling", replace(src, result=src.result.replace("HOMONYM_REFIT_NOT_LICENSED", "REFIT_LICENSED", 1))),
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
    src = load_sources()
    ok = selftest(src) if args.selftest else not evaluate(src)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
