#!/usr/bin/env python3
"""Independent finite certificate for the Pati--Salam channel theorem.

The certificate freezes the already-derived D5 supports and held Pati--Salam
singlet counts, then checks only their exact logical composition. It does not
derive a Clebsch normalization, source coefficient, form-leg contraction,
physical vertex, family selector, mass, observed sector, or prediction.

Run normally for the clean baseline. The selftest option runs that baseline
first and then plants one mutation for every load-bearing premise or claim
fence.
"""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass, replace


Multiplicity = tuple[tuple[str, int], ...]


@dataclass(frozen=True)
class Premises:
    family_partner: Multiplicity = (
        ("45", 1), ("54", 1), ("210", 1), ("945", 1), ("1050", 1)
    )
    symmetric_adjoint: Multiplicity = (
        ("1", 1), ("54", 1), ("210", 1), ("770", 1)
    )
    alternating_adjoint: Multiplicity = (("45", 1), ("945", 1))
    ps_singlets: Multiplicity = (
        ("45", 0), ("54", 1), ("210", 1), ("945", 0), ("1050", 0)
    )
    paired_real_lines: bool = True
    source_one_form_leg_retained: bool = True
    source_selected_coefficient: bool = False
    source_selected_form_contraction: bool = False
    source_selected_family_covector: bool = False
    source_selected_physical_vertex: bool = False
    observed_sector_imported: bool = False


@dataclass(frozen=True)
class Verdict:
    admitted: bool
    symmetric_owners: frozenset[str]
    alternating_owners: frozenset[str]
    symmetric_ps_owners: frozenset[str]
    alternating_ps_owners: frozenset[str]
    reasons: tuple[str, ...]


def counter(rows: Multiplicity) -> Counter[str]:
    return Counter(dict(rows))


def support(rows: Multiplicity) -> frozenset[str]:
    return frozenset(name for name, multiplicity in rows if multiplicity)


def derive(p: Premises) -> Verdict:
    family = counter(p.family_partner)
    symmetric = counter(p.symmetric_adjoint)
    alternating = counter(p.alternating_adjoint)
    ps = dict(p.ps_singlets)

    symmetric_owners = support(p.family_partner) & support(p.symmetric_adjoint)
    alternating_owners = (
        support(p.family_partner) & support(p.alternating_adjoint)
    )
    symmetric_ps = frozenset(
        owner for owner in symmetric_owners if ps.get(owner, 0) > 0
    )
    alternating_ps = frozenset(
        owner for owner in alternating_owners if ps.get(owner, 0) > 0
    )

    facts = {
        "same-label family/partner support is exact": family
        == Counter({"45": 1, "54": 1, "210": 1, "945": 1, "1050": 1}),
        "symmetric adjoint-square support is exact": symmetric
        == Counter({"1": 1, "54": 1, "210": 1, "770": 1}),
        "alternating adjoint-square support is exact": alternating
        == Counter({"45": 1, "945": 1}),
        "Pati-Salam singlet counts are exact": ps
        == {"45": 0, "54": 1, "210": 1, "945": 0, "1050": 0},
        "complex cubic lines are paired into the real carrier":
        p.paired_real_lines,
        "the source one-form leg is retained": p.source_one_form_leg_retained,
        "no source coefficient is selected": not p.source_selected_coefficient,
        "no source form-leg contraction is selected":
        not p.source_selected_form_contraction,
        "no family covector is selected": not p.source_selected_family_covector,
        "no physical vertex is selected": not p.source_selected_physical_vertex,
        "no observed sector is imported": not p.observed_sector_imported,
        "symmetric owner intersection is exactly 54 and 210":
        symmetric_owners == frozenset({"54", "210"}),
        "alternating owner intersection is exactly 45 and 945":
        alternating_owners == frozenset({"45", "945"}),
        "symmetric Pati-Salam owners are exactly 54 and 210":
        symmetric_ps == frozenset({"54", "210"}),
        "alternating product has no Pati-Salam owner":
        alternating_ps == frozenset(),
    }
    return Verdict(
        admitted=all(facts.values()),
        symmetric_owners=symmetric_owners,
        alternating_owners=alternating_owners,
        symmetric_ps_owners=symmetric_ps,
        alternating_ps_owners=alternating_ps,
        reasons=tuple(name for name, holds in facts.items() if not holds),
    )


def baseline_checks() -> list[tuple[str, bool]]:
    p = Premises()
    family = counter(p.family_partner)
    symmetric = counter(p.symmetric_adjoint)
    alternating = counter(p.alternating_adjoint)
    ps = dict(p.ps_singlets)
    verdict = derive(p)
    dimensions = {"1": 1, "45": 45, "54": 54, "210": 210,
                  "770": 770, "945": 945, "1050": 1050}
    degree = lambda rows: sum(dimensions[name] * count for name, count in rows)
    return [
        ("16 tensor 144 support closes to dimension 2304",
         degree(p.family_partner) == 2304 == 16 * 144),
        ("Sym^2(45) support closes to dimension 1035",
         degree(p.symmetric_adjoint) == 1035 == 45 * 46 // 2),
        ("Lambda^2(45) support closes to dimension 990",
         degree(p.alternating_adjoint) == 990 == 45 * 44 // 2),
        ("adjoint squares close to the full tensor square",
         degree(p.symmetric_adjoint) + degree(p.alternating_adjoint) == 45 * 45),
        ("all frozen D5 support multiplicities are one",
         set(family.values()) == set(symmetric.values()) == set(alternating.values()) == {1}),
        ("the bare family/partner support contains no scalar", family["1"] == 0),
        ("the cubic adjoint 45 channel occurs once", family["45"] == 1),
        ("the cubic real line is conjugate-paired", p.paired_real_lines),
        ("the linear adjoint has no Pati-Salam singlet", ps["45"] == 0),
        ("symmetric intersection is exactly 54 and 210",
         verdict.symmetric_owners == frozenset({"54", "210"})),
        ("alternating intersection is exactly 45 and 945",
         verdict.alternating_owners == frozenset({"45", "945"})),
        ("54 has one Pati-Salam singlet", ps["54"] == 1),
        ("210 has one Pati-Salam singlet", ps["210"] == 1),
        ("945 has no Pati-Salam singlet", ps["945"] == 0),
        ("symmetric preserving owners are exactly 54 and 210",
         verdict.symmetric_ps_owners == frozenset({"54", "210"})),
        ("alternating preserving owner set is empty",
         verdict.alternating_ps_owners == frozenset()),
        ("source one-form leg remains explicit", p.source_one_form_leg_retained),
        ("no source coefficient or form contraction is selected",
         not p.source_selected_coefficient
         and not p.source_selected_form_contraction),
        ("no family, physical vertex, or observed sector is selected",
         not p.source_selected_family_covector
         and not p.source_selected_physical_vertex
         and not p.observed_sector_imported),
        ("the exact representation-channel theorem is admitted", verdict.admitted),
    ]


def hostile_checks() -> list[tuple[str, bool]]:
    p = Premises()
    mutations = {
        "removing 54 reopens the symmetric-owner theorem": replace(
            p, symmetric_adjoint=(("1", 1), ("210", 1), ("770", 1))
        ),
        "planting 945 in the symmetric square changes the channel split": replace(
            p, symmetric_adjoint=(
                ("1", 1), ("54", 1), ("210", 1), ("770", 1), ("945", 1)
            )
        ),
        "planting 210 in the alternating square changes the channel split": replace(
            p, alternating_adjoint=(("45", 1), ("210", 1), ("945", 1))
        ),
        "a Pati-Salam singlet in 45 reopens the linear obstruction": replace(
            p, ps_singlets=(
                ("45", 1), ("54", 1), ("210", 1), ("945", 0), ("1050", 0)
            )
        ),
        "removing the 210 singlet reopens the two-owner conclusion": replace(
            p, ps_singlets=(
                ("45", 0), ("54", 1), ("210", 0), ("945", 0), ("1050", 0)
            )
        ),
        "a 945 singlet reopens the alternating obstruction": replace(
            p, ps_singlets=(
                ("45", 0), ("54", 1), ("210", 1), ("945", 1), ("1050", 0)
            )
        ),
        "unpaired complex lines reopen the real-carrier statement": replace(
            p, paired_real_lines=False
        ),
        "discarding the one-form leg violates source typing": replace(
            p, source_one_form_leg_retained=False
        ),
        "a selected coefficient or contraction exceeds the frozen theorem": replace(
            p, source_selected_coefficient=True,
            source_selected_form_contraction=True
        ),
        "a selected family, physical vertex, or observed sector exceeds scope":
        replace(
            p, source_selected_family_covector=True,
            source_selected_physical_vertex=True,
            observed_sector_imported=True
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
        "VERDICT: the symmetric adjoint square reaches exactly 54 and 210, "
        "each with one Pati-Salam singlet; the alternating square reaches only "
        "45 and 945, both with none. This selects a representation-channel "
        "class, not a coefficient, source vertex, family, mass, or observable."
    )
    return 0 if ok and verdict.admitted else 1


if __name__ == "__main__":
    raise SystemExit(main())
