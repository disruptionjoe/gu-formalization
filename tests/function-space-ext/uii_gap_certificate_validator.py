#!/usr/bin/env python3
"""Uniform Invertibility at Infinity (UII) certificate validator.

This is a finite certificate harness for the signed-readout OC1/OC2 gate. It
does not prove the actual GU non-compact operator is Fredholm. It checks the
shape a future asymptotic-operator certificate must have:

- a uniform lower spectral gap for the model operator at infinity,
- the corresponding bounded-transform gap,
- and, for OC2, transport of the quaternionic structure through the same gate.
"""

import math
import numpy as np

TOL = 1e-10
ASSERTS = 0


def check(condition, message):
    global ASSERTS
    ASSERTS += 1
    assert condition, message


def h_linear_asymptotic_model(mass, coupling):
    """A real self-adjoint 2x2 model tensored with H-line identity.

    In matrix form this is `A tensor I_2`, so it commutes with the standard
    quaternionic structure `J(v) = Omega conjugate(v)`.
    """
    base = np.array([[mass, coupling], [coupling, -mass]], dtype=float)
    return np.kron(base, np.eye(2, dtype=complex))


def quaternionic_omega(dim):
    if dim % 2 != 0:
        raise ValueError("quaternionic model dimension must be even")
    j2 = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
    return np.kron(np.eye(dim // 2, dtype=complex), j2)


def j_commutator_residual(operator):
    omega = quaternionic_omega(operator.shape[0])
    return float(np.linalg.norm(operator @ omega - omega @ operator.conj()))


def min_spectral_gap(operator):
    return float(np.min(np.abs(np.linalg.eigvalsh(operator))))


def bounded_transform(operator):
    eigvals, eigvecs = np.linalg.eigh(operator)
    transformed = eigvals / np.sqrt(1.0 + eigvals * eigvals)
    return (eigvecs * transformed) @ eigvecs.conj().T


def bounded_gap_from_operator(operator):
    return min_spectral_gap(bounded_transform(operator))


def riesz_gap(delta):
    return delta / math.sqrt(1.0 + delta * delta)


def certificate_summary(operators):
    gaps = [min_spectral_gap(op) for op in operators]
    f_gaps = [bounded_gap_from_operator(op) for op in operators]
    j_residuals = [j_commutator_residual(op) for op in operators]
    return {
        "uniform_delta": min(gaps),
        "uniform_riesz_gap": min(f_gaps),
        "max_j_residual": max(j_residuals),
    }


def assert_uii_certificate(operators, required_delta):
    summary = certificate_summary(operators)
    check(
        summary["uniform_delta"] >= required_delta,
        f"UII gap below requirement: {summary['uniform_delta']:.6g} < {required_delta:.6g}",
    )
    predicted = riesz_gap(summary["uniform_delta"])
    check(
        abs(summary["uniform_riesz_gap"] - predicted) < 5e-10,
        "bounded-transform gap must be delta/sqrt(1+delta^2)",
    )
    check(
        summary["max_j_residual"] < TOL,
        f"OC2 J-commutator residual too large: {summary['max_j_residual']:.3e}",
    )
    return summary


def main():
    print("=" * 86)
    print("SIGNED-READOUT OC1/OC2: UII GAP CERTIFICATE VALIDATOR")
    print("=" * 86)

    t_values = np.linspace(-1.0, 1.0, 9)
    gapped_family = [
        h_linear_asymptotic_model(mass=1.15 + 0.08 * math.cos(float(t)), coupling=0.25 * float(t))
        for t in t_values
    ]
    summary = assert_uii_certificate(gapped_family, required_delta=1.0)
    print("  gapped family:")
    print(f"    uniform_delta      = {summary['uniform_delta']:.6f}")
    print(f"    uniform_riesz_gap  = {summary['uniform_riesz_gap']:.6f}")
    print(f"    max_J_residual     = {summary['max_j_residual']:.3e}")

    zero_gap_family = list(gapped_family)
    zero_gap_family[4] = h_linear_asymptotic_model(mass=0.0, coupling=0.0)
    zero_gap_summary = certificate_summary(zero_gap_family)
    check(
        zero_gap_summary["uniform_delta"] == 0.0,
        "zero asymptotic model must fail UII with delta = 0",
    )
    print("  zero-gap control:")
    print(f"    uniform_delta      = {zero_gap_summary['uniform_delta']:.6f} (expected fail)")

    j_breaking = h_linear_asymptotic_model(mass=1.4, coupling=0.2).copy()
    j_breaking[0, 2] = 0.05
    j_breaking[2, 0] = 0.05
    check(min_spectral_gap(j_breaking) > 1.0, "J-breaking control should remain spectrally gapped")
    check(
        j_commutator_residual(j_breaking) > 1e-3,
        "J-breaking control must fail the OC2 H-linear side gate",
    )
    print("  J-breaking control:")
    print(f"    spectral_delta     = {min_spectral_gap(j_breaking):.6f}")
    print(f"    J_residual         = {j_commutator_residual(j_breaking):.3e} (expected fail)")

    print("#" * 86)
    print("# VERDICT: PASS. The harness accepts a uniformly gapped H-linear")
    print("# asymptotic family and rejects the zero-gap and J-breaking controls.")
    print(f"# hard asserts passed: {ASSERTS}")
    print("#" * 86)


if __name__ == "__main__":
    main()
