#!/usr/bin/env python3
"""Exact controls for the split corrected-observation projector.

The probe independently realizes the held Cl(1,1) leakage witness, applies
P = I - j Gamma on the observed one-form-spinor carrier, and checks the full
kernel/trace decomposition. Arithmetic is exact integer/rational arithmetic.
"""

from __future__ import annotations

from fractions import Fraction


CHECKS: list[tuple[str, bool]] = []


def check(name: str, condition: bool) -> None:
    CHECKS.append((name, bool(condition)))
    print(f"[{'PASS' if condition else 'FAIL'}] {name}")


def mat_vec(a: list[list[Fraction]], v: list[Fraction]) -> list[Fraction]:
    return [sum((x * y for x, y in zip(row, v)), Fraction(0)) for row in a]


def add(u: list[Fraction], v: list[Fraction]) -> list[Fraction]:
    return [x + y for x, y in zip(u, v)]


def sub(u: list[Fraction], v: list[Fraction]) -> list[Fraction]:
    return [x - y for x, y in zip(u, v)]


def scale(c: Fraction, v: list[Fraction]) -> list[Fraction]:
    return [c * x for x in v]


Q = Fraction
X = [[Q(0), Q(1)], [Q(1), Q(0)]]
J = [[Q(0), Q(1)], [Q(-1), Q(0)]]
ZERO2 = [Q(0), Q(0)]


# Observed carrier B = H* tensor S is represented as two spinor components,
# with gamma trace Gamma_B(b0,b1) = X b0 + J b1.  A right inverse inserts the
# trace through the non-null first covector: j(s) = (X s, 0), since X^2 = I.
def gamma_b(b: list[Fraction]) -> list[Fraction]:
    return add(mat_vec(X, b[:2]), mat_vec(J, b[2:]))


def right_inverse(s: list[Fraction]) -> list[Fraction]:
    return mat_vec(X, s) + ZERO2


def projector(b: list[Fraction]) -> list[Fraction]:
    return sub(b, right_inverse(gamma_b(b)))


print("Split corrected-observation exact controls")

for basis in ([Q(1), Q(0)], [Q(0), Q(1)]):
    check("RIGHT_INVERSE.gamma_j_identity", gamma_b(right_inverse(basis)) == basis)

samples = [
    [Q(1), Q(2), Q(3), Q(5)],
    [Q(-2), Q(7), Q(1), Q(-4)],
    [Q(0), Q(0), Q(0), Q(0)],
]
for sample in samples:
    corrected = projector(sample)
    trace = gamma_b(sample)
    check("PROJECTOR.output_gamma_zero", gamma_b(corrected) == ZERO2)
    check("PROJECTOR.idempotent", projector(corrected) == corrected)
    check("SPLIT.reconstructs_input", add(corrected, right_inverse(trace)) == sample)
    check("SPLIT.trace_coordinate_exact", gamma_b(right_inverse(trace)) == trace)


# Reproduce the prior literal-observation leakage witness.  Ambient horizontal
# and normal contractions are X and J.  Choose psi=e0 and normal coefficient
# phi=-J^{-1}X psi = J X psi because J^{-1}=-J.  Literal observation keeps
# only the horizontal component, represented in the first observed slot.
psi = [Q(1), Q(0)]
phi = mat_vec(J, mat_vec(X, psi))
ambient_trace = add(mat_vec(X, psi), mat_vec(J, phi))
literal_observed = psi + ZERO2
corrected_observed = projector(literal_observed)

check("LEAKAGE.ambient_witness_gamma_zero", ambient_trace == ZERO2)
check("LEAKAGE.literal_observed_trace_nonzero", gamma_b(literal_observed) != ZERO2)
check("CORRECTION.corrected_observed_trace_zero", gamma_b(corrected_observed) == ZERO2)
check("CORRECTION.removes_exact_trace_lift",
      add(corrected_observed, right_inverse(gamma_b(literal_observed))) == literal_observed)
check("CORRECTION.changes_leaking_literal_output", corrected_observed != literal_observed)


# Positive control: a hand-built kernel element is fixed.  Hostile controls:
# the identity map and the wrong-sign correction both retain/double trace.
kernel_sample = [Q(1), Q(0), Q(1), Q(0)]
check("POSITIVE.kernel_sample_is_gamma_zero", gamma_b(kernel_sample) == ZERO2)
check("POSITIVE.kernel_sample_fixed", projector(kernel_sample) == kernel_sample)

identity_hostile = literal_observed
wrong_sign_hostile = add(literal_observed, right_inverse(gamma_b(literal_observed)))
check("HOSTILE.identity_does_not_correct", gamma_b(identity_hostile) != ZERO2)
check("HOSTILE.wrong_sign_does_not_correct", gamma_b(wrong_sign_hostile) != ZERO2)

passed = sum(ok for _, ok in CHECKS)
print(f"source_native_corrected_observation_probe: {passed}/{len(CHECKS)} checks passed")
raise SystemExit(0 if passed == len(CHECKS) else 1)
