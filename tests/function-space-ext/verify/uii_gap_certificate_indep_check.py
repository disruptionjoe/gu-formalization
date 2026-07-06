#!/usr/bin/env python3
# Independent re-check of uii_gap_certificate_validator.py. DIFFERENT substrate: instead
# of the hand-written 2x2 mass/coupling family, use rotated positive-definite real-symmetric
# 3x3 bases tensored with the H-line identity. Confirms the certificate-shape core:
# a uniform spectral gap gives the predicted bounded-transform gap, J transport is a
# separate OC2 side gate, and zero-gap / J-breaking controls are rejected.
import math
import numpy as np

NASSERT = 0
TOL = 1e-10


def check(condition, message):
    global NASSERT
    NASSERT += 1
    assert condition, message


def omega(dim):
    if dim % 2:
        raise ValueError("quaternionic model dimension must be even")
    j2 = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
    return np.kron(np.eye(dim // 2, dtype=complex), j2)


def h_linear_operator(base):
    return np.kron(base.astype(complex), np.eye(2, dtype=complex))


def rotated_positive_base(theta):
    c, s = math.cos(theta), math.sin(theta)
    rotation = np.array([[c, -s, 0.0], [s, c, 0.0], [0.0, 0.0, 1.0]])
    eigenvalues = np.diag([1.35 + 0.05 * c * c, 1.75 + 0.04 * s, 2.30 + 0.03 * c])
    return rotation @ eigenvalues @ rotation.T


def min_spectral_gap(operator):
    return float(np.min(np.abs(np.linalg.eigvalsh(operator))))


def bounded_transform(operator):
    eigvals, eigvecs = np.linalg.eigh(operator)
    transformed = eigvals / np.sqrt(1.0 + eigvals * eigvals)
    return (eigvecs * transformed) @ eigvecs.conj().T


def bounded_gap(operator):
    return min_spectral_gap(bounded_transform(operator))


def riesz_gap(delta):
    return delta / math.sqrt(1.0 + delta * delta)


def j_residual(operator):
    j = omega(operator.shape[0])
    return float(np.linalg.norm(operator @ j - j @ operator.conj()))


def summarize(operators):
    gaps = [min_spectral_gap(op) for op in operators]
    return {
        "uniform_delta": min(gaps),
        "uniform_riesz_gap": min(bounded_gap(op) for op in operators),
        "max_j_residual": max(j_residual(op) for op in operators),
    }


print("independent re-check: UII certificate shape on rotated positive H-linear bases")

operators = [h_linear_operator(rotated_positive_base(theta)) for theta in np.linspace(-1.1, 1.1, 7)]
summary = summarize(operators)
predicted = riesz_gap(summary["uniform_delta"])
print("  gapped family:")
print("    uniform_delta      = %.6f" % summary["uniform_delta"])
print("    uniform_riesz_gap  = %.6f" % summary["uniform_riesz_gap"])
print("    max_J_residual     = %.3e" % summary["max_j_residual"])
check(summary["uniform_delta"] > 1.30, "positive bases keep a uniform spectral gap")
check(abs(summary["uniform_riesz_gap"] - predicted) < 5e-10, "bounded-transform gap is Riesz gap")
check(summary["max_j_residual"] < TOL, "H-linear family transports J")

zero_gap = list(operators)
zero_gap[3] = h_linear_operator(np.diag([0.0, 1.6, 2.1]))
zero_summary = summarize(zero_gap)
print("  zero-gap control:")
print("    uniform_delta      = %.6f (expected fail)" % zero_summary["uniform_delta"])
check(zero_summary["uniform_delta"] == 0.0, "zero model must fail UII with delta = 0")
check(zero_summary["max_j_residual"] < TOL, "zero-gap control isolates the gap failure")

j_breaking = operators[0].copy()
j_breaking[0, 2] += 0.08
j_breaking[2, 0] += 0.08
print("  J-breaking control:")
print("    spectral_delta     = %.6f" % min_spectral_gap(j_breaking))
print("    J_residual         = %.3e (expected fail)" % j_residual(j_breaking))
check(min_spectral_gap(j_breaking) > 1.20, "J-breaking control remains spectrally gapped")
check(j_residual(j_breaking) > 1e-3, "J-breaking control fails the OC2 side gate")

print("INDEPENDENT CHECK PASS: UII gap, bounded-transform gap, and OC2 J gate; asserts %d" % NASSERT)
