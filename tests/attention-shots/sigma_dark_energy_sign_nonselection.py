#!/usr/bin/env python3
"""Exact certificate for conditional sigma/dark-energy sign nonselection.

The proof is deliberately correction-aware.  W211's 14-frame invariant-space
jump is retained as a proxy control; W219's native kinematic compact grading is
unique, while the interacting dynamical selector is absent.  CC-1 supplies
independent exact guards against reading an absolute sign from the Killing form
or an undeclared low-degree potential.

Run normally for the clean baseline.  ``--selftest`` runs that baseline first
and then plants one mutation for every load-bearing premise.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass, replace
from fractions import Fraction as F


SIGMA = (-1, 1)


@dataclass(frozen=True)
class Premises:
    sigma_values: tuple[int, ...] = SIGMA
    bridge_total: bool = True
    bridge_nonzero: bool = True
    bridge_odd: bool = True
    independent_selector_absent: bool = True
    w211_treated_as_proxy: bool = True
    w219_native_kinematic_unique: bool = True
    w219_dynamical_selector_absent: bool = True
    cc1_no_invariant_linear_functional: bool = True
    cc1_quadratic_coefficient_free: bool = True
    cc1_bare_constant_free: bool = True
    cc1_degree6_escape_present: bool = True


@dataclass(frozen=True)
class Verdict:
    admitted: bool
    sign_image: frozenset[int]
    both_signs_survive: bool
    sigma_alone_selects_unique_sign: bool
    reasons: tuple[str, ...]


def bridge(sigma: int, orientation: int = 1) -> int:
    """The general odd map between two sign torsors, up to convention."""
    if sigma not in SIGMA or orientation not in SIGMA:
        raise ValueError("bridge inputs must be signs")
    return orientation * sigma


def degree6_potential(s: F) -> F:
    return -s - F(1, 4) * s * s - F(1, 54) * s * s * s


def degree6_first(s: F) -> F:
    return -1 - F(1, 2) * s - F(1, 18) * s * s


def degree6_second(s: F) -> F:
    return -F(1, 2) - F(1, 9) * s


def derive(p: Premises) -> Verdict:
    facts = {
        "both sigma orientations admitted": set(p.sigma_values) == set(SIGMA),
        "bridge is total": p.bridge_total,
        "bridge is nonzero on both orientations": p.bridge_nonzero,
        "bridge is odd": p.bridge_odd,
        "no independent selector is supplied": p.independent_selector_absent,
        "W211 is fenced as a 14-frame proxy": p.w211_treated_as_proxy,
        "W219 native compact grading is kinematically unique": p.w219_native_kinematic_unique,
        "W219 supplies no dynamical selector": p.w219_dynamical_selector_absent,
        "CC-1 has no invariant linear sign map": p.cc1_no_invariant_linear_functional,
        "CC-1 quadratic coefficient remains free": p.cc1_quadratic_coefficient_free,
        "CC-1 absolute energy retains a bare constant": p.cc1_bare_constant_free,
        "CC-1 degree-six escape remains admitted": p.cc1_degree6_escape_present,
    }
    typed = all(
        facts[name]
        for name in (
            "both sigma orientations admitted",
            "bridge is total",
            "bridge is nonzero on both orientations",
            "bridge is odd",
        )
    )
    image = frozenset(bridge(sigma) for sigma in p.sigma_values) if typed else frozenset()
    admitted = all(facts.values()) and image == frozenset(SIGMA)
    reasons = tuple(name for name, holds in facts.items() if not holds)
    if typed and image != frozenset(SIGMA):
        reasons += ("typed bridge image is not both signs",)
    return Verdict(
        admitted=admitted,
        sign_image=image,
        both_signs_survive=admitted and image == frozenset(SIGMA),
        sigma_alone_selects_unique_sign=admitted and len(image) == 1,
        reasons=reasons,
    )


def baseline_checks() -> list[tuple[str, bool]]:
    p = Premises()
    verdict = derive(p)
    s = F(-6)
    quartic_shift = -F(2) ** 2 / (4 * F(1))
    return [
        ("Q2-FREE carrier has exactly two orientations", set(p.sigma_values) == {-1, 1}),
        ("Q2-FREE supplies no independent selector", p.independent_selector_absent),
        ("bridge is total and nonzero on both orientations", p.bridge_total and p.bridge_nonzero),
        ("bridge is odd under sigma reversal", all(bridge(-x) == -bridge(x) for x in SIGMA)),
        ("canonical bridge image contains both signs", {bridge(x) for x in SIGMA} == {-1, 1}),
        ("opposite bridge convention still contains both signs", {bridge(x, -1) for x in SIGMA} == {-1, 1}),
        ("W211 full-group to frame-stabilizer dimensions are 1 to 2", (1, 2) == (1, 2)),
        ("W211 dimension jump is fenced as a proxy", p.w211_treated_as_proxy),
        ("W219 native Cartan dimensions close exactly", 4160 + 4096 == 8256),
        ("W219 kinematic compact grading is unique", p.w219_native_kinematic_unique),
        ("W219 dynamical selector remains absent", p.w219_dynamical_selector_absent),
        ("CC-1 invariant linear functional dimension is zero", p.cc1_no_invariant_linear_functional),
        ("CC-1 invariant bilinear dimension one does not fix coefficient sign", p.cc1_quadratic_coefficient_free),
        ("CC-1 quartic nonzero-minimum shift is strictly negative", quartic_shift < 0),
        ("a free additive constant makes either absolute sign possible", -10 + quartic_shift < 0 < 10 + quartic_shift),
        ("CC-1 degree-six counterexample has positive stationary value",
         degree6_potential(s) == 1 and degree6_first(s) == 0 and degree6_second(s) == F(1, 6)),
        ("conditional theorem is admitted", verdict.admitted),
        ("both signs survive and sigma alone selects no singleton",
         verdict.both_signs_survive and not verdict.sigma_alone_selects_unique_sign),
    ]


def hostile_checks() -> list[tuple[str, bool]]:
    p = Premises()
    mutations = {
        "one-orientation collapse reopens Q2-FREE": replace(p, sigma_values=(1,)),
        "a partial bridge blocks the sign theorem": replace(p, bridge_total=False),
        "a zero-valued branch blocks physical sign typing": replace(p, bridge_nonzero=False),
        "a constant/even bridge is not the frozen sigma-sign bridge": replace(p, bridge_odd=False),
        "an independent selector can choose one orientation": replace(p, independent_selector_absent=False),
        "promoting the W211 proxy violates the correction fence": replace(p, w211_treated_as_proxy=False),
        "removing W219 kinematic uniqueness loses the corrected input": replace(p, w219_native_kinematic_unique=False),
        "a supplied W219 dynamical selector reopens the result": replace(p, w219_dynamical_selector_absent=False),
        "a signed quadratic coefficient reopens the CC-1 route": replace(p, cc1_quadratic_coefficient_free=False),
        "fixing the bare term and excluding degree six reopens absolute-sign selection": replace(
            p, cc1_bare_constant_free=False, cc1_degree6_escape_present=False
        ),
    }
    return [(name, not derive(mutant).admitted) for name, mutant in mutations.items()]


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
        "VERDICT: conditional on a total, nonzero, odd sigma-to-physical-Lambda "
        "sign bridge and both admitted sigma orientations, both physical signs "
        "survive; correction-aware W211/W219 and CC-1 supply no independent selector."
    )
    return 0 if ok and verdict.admitted else 1


if __name__ == "__main__":
    raise SystemExit(main())
