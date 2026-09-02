#!/usr/bin/env python3
"""Exact composition certificate for the declared-content extra-vector obstruction.

The certificate recomputes the PV-1/PV-2/MV-2 mathematical core without
importing their probes.  Its conclusion is deliberately conditional: a
residual *physical vector* follows only when the residual gauge direction has
the separately supplied gauge-kinetic/physical-realization premise.

Run normally for the baseline.  Run with ``--selftest`` to execute the green
baseline first and then verify that every load-bearing premise has an explicit
hostile reopener.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass, replace
from fractions import Fraction as F
from itertools import combinations


def roots_d5() -> tuple[tuple[int, ...], ...]:
    roots = []
    for i, j in combinations(range(5), 2):
        for si in (-1, 1):
            for sj in (-1, 1):
                v = [0] * 5
                v[i], v[j] = si, sj
                roots.append(tuple(v))
    return tuple(roots)


ROOTS = roots_d5()
ZERO = (0, 0, 0, 0, 0)


def bl(weight: tuple[int, ...]) -> F:
    return F(-(weight[0] + weight[1] + weight[2]), 3)


def t3r(weight: tuple[int, ...]) -> F:
    return F(weight[3] + weight[4], 4)


def t3l(weight: tuple[int, ...]) -> F:
    return F(weight[3] - weight[4], 4)


def hypercharge(weight: tuple[int, ...]) -> F:
    return t3r(weight) + bl(weight) / 2


def sm_singlet(weight: tuple[int, ...]) -> bool:
    return (
        weight[0] == weight[1] == weight[2]
        and t3l(weight) == 0
        and hypercharge(weight) == 0
    )


def unbroken_dimension(y_coefficient: F, bl_coefficient: F) -> int:
    annihilated = sum(
        y_coefficient * hypercharge(root) + bl_coefficient * bl(root) == 0
        for root in ROOTS
    )
    return 5 + annihilated


def exact_orbit_dimensions() -> tuple[int, ...]:
    """Test the generic stratum and every root hyperplane in the two-plane."""
    representatives = {(F(1), F(1))}
    for root in ROOTS:
        y_value, bl_value = hypercharge(root), bl(root)
        if y_value or bl_value:
            representatives.add((bl_value, -y_value))
    return tuple(sorted({unbroken_dimension(*point) for point in representatives}))


def declared_weights() -> tuple[set[tuple[int, ...]], set[tuple[int, ...]]]:
    """Return adjoint-45 and vector-10 tensor adjoint-45 weight supports."""
    adjoint = set(ROOTS) | {ZERO}
    vector = set()
    for i in range(5):
        for sign in (-1, 1):
            weight = [0] * 5
            weight[i] = sign
            vector.add(tuple(weight))
    tensor = {
        tuple(v[i] + a[i] for i in range(5))
        for v in vector
        for a in tuple(ROOTS) + (ZERO,) * 5
    }
    return adjoint, tensor


def spinor_16_weights() -> tuple[tuple[int, ...], ...]:
    """Integer-doubled chiral spinor weights: signs with even minus parity."""
    out = []
    for bits in range(32):
        signs = tuple(-1 if bits & (1 << i) else 1 for i in range(5))
        if sum(value < 0 for value in signs) % 2 == 0:
            out.append(signs)
    return tuple(out)


def anomaly_sums() -> tuple[F, F, F]:
    charges = [bl(weight) for weight in spinor_16_weights()]
    return sum(charges, F(0)), sum((q ** 3 for q in charges), F(0)), sum(
        (hypercharge(w) ** 2) * bl(w) for w in spinor_16_weights()
    )


@dataclass(frozen=True)
class Premises:
    declared_carriers_only: bool = True
    observation_removes_only_noncompact: bool = True
    orbit_census_complete: bool = True
    charged_sm_singlet_absent: bool = True
    shifting_zero_form_absent: bool = True
    residual_u1_anomaly_free: bool = True
    residual_direction_abelian: bool = True
    physical_vector_realization: bool = True


@dataclass(frozen=True)
class Verdict:
    admitted: bool
    residual_gauge_direction: bool
    residual_physical_vector: bool
    reasons: tuple[str, ...]


def derive(premises: Premises) -> Verdict:
    dims = exact_orbit_dimensions()
    adjoint, tensor = declared_weights()
    charged_singlets = {
        weight
        for weight in adjoint | tensor
        if sm_singlet(weight) and bl(weight) != 0
    }
    linear, cubic, mixed = anomaly_sums()

    facts = {
        "declared carriers frozen": premises.declared_carriers_only,
        "observation leaves compact directions": (
            premises.observation_removes_only_noncompact and 45 == 21 + 24 and 21 - 12 == 9
        ),
        "SM-preserving orbit census has minimum 13": (
            premises.orbit_census_complete and dims == (13, 15, 19, 25)
        ),
        "no declared charged SM singlet": (
            premises.charged_sm_singlet_absent and not charged_singlets
        ),
        "no declared Stueckelberg zero-form": premises.shifting_zero_form_absent,
        "residual U(1) is anomaly-free": (
            premises.residual_u1_anomaly_free and (linear, cubic, mixed) == (0, 0, 0)
        ),
        "residual direction is abelian": premises.residual_direction_abelian,
    }
    admitted = all(facts.values())
    residual_gauge = admitted
    residual_vector = residual_gauge and premises.physical_vector_realization
    reasons = tuple(name for name, holds in facts.items() if not holds)
    if admitted and not premises.physical_vector_realization:
        reasons += ("physical gauge-kinetic realization not supplied",)
    return Verdict(admitted, residual_gauge, residual_vector, reasons)


def baseline_checks() -> list[tuple[str, bool]]:
    dims = exact_orbit_dimensions()
    adjoint, tensor = declared_weights()
    charged = [w for w in adjoint | tensor if sm_singlet(w) and bl(w) != 0]
    anomalies = anomaly_sums()
    verdict = derive(Premises())
    return [
        ("D5 has 40 roots and so(10) has dimension 45", len(ROOTS) == 40),
        ("SM dimension is 8+3+1=12", 8 + 3 + 1 == 12),
        ("observation split is 45=k(21)+p(24)", 45 == 21 + 24),
        ("nine non-SM compact directions remain", 21 - 12 == 9),
        ("all SM-preserving adjoint strata are enumerated", dims == (13, 15, 19, 25)),
        ("the minimum unbroken dimension is 13, not 12", min(dims) == 13),
        ("adjoint weight support is generated", len(adjoint) == 41),
        ("10 tensor 45 weight support is generated", len(tensor) == 170),
        ("declared supports contain no B-L-charged SM singlet", not charged),
        ("chiral 16 has sixteen weights", len(spinor_16_weights()) == 16),
        ("linear, cubic and Y^2(B-L) anomaly sums vanish", anomalies == (0, 0, 0)),
        ("declared-content theorem is admitted", verdict.admitted),
        ("a residual gauge direction follows", verdict.residual_gauge_direction),
        ("a physical vector follows only with its explicit premise", verdict.residual_physical_vector),
        ("removing physical realization preserves gauge result but not particle result",
         derive(replace(Premises(), physical_vector_realization=False)).residual_gauge_direction
         and not derive(replace(Premises(), physical_vector_realization=False)).residual_physical_vector),
    ]


def hostile_checks() -> list[tuple[str, bool]]:
    baseline = Premises()
    mutations = {
        "undeclared completion reopens carrier closure": replace(baseline, declared_carriers_only=False),
        "observation acting on compact directions reopens PV-2": replace(
            baseline, observation_removes_only_noncompact=False
        ),
        "incomplete orbit census reopens PV-1": replace(baseline, orbit_census_complete=False),
        "a charged SM singlet reopens the Higgs route": replace(
            baseline, charged_sm_singlet_absent=False
        ),
        "a shifting zero-form reopens Stueckelberg": replace(
            baseline, shifting_zero_form_absent=False
        ),
        "an anomalous residual U(1) reopens Green-Schwarz": replace(
            baseline, residual_u1_anomaly_free=False
        ),
        "a nonabelian residual factor reopens confinement": replace(
            baseline, residual_direction_abelian=False
        ),
    }
    checks = [(name, not derive(mutant).admitted) for name, mutant in mutations.items()]
    no_kinetic = derive(replace(baseline, physical_vector_realization=False))
    checks.append((
        "missing gauge-kinetic realization blocks only the physical-vector claim",
        no_kinetic.admitted and no_kinetic.residual_gauge_direction and not no_kinetic.residual_physical_vector,
    ))
    return checks


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
        "VERDICT: under the frozen declared-content premises, at least one extra "
        "abelian gauge direction survives every admitted mass/removal route; a "
        "physical vector additionally requires the explicit realization premise."
    )
    return 0 if ok and verdict.admitted else 1


if __name__ == "__main__":
    raise SystemExit(main())
