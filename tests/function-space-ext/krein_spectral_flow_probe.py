"""
WC-FUNCTION-SPACE-EXT first finite-Galerkin probe.

This script models the finite-dimensional part of the function-space obstruction named in
NEXT-STEPS.md: can a Krein-compatible family exhibit nonzero net chiral spectral flow?

It does NOT prove a function-space theorem. It checks a small Galerkin model with:

  W = W_+ (+) W_-
  Gamma = diag(+1 on W_+, -1 on W_-)
  K = [[0, I], [I, 0]]

so W_+ and W_- are K-isotropic and K pairs the two chirality sectors. The modeled
K-self-adjointness condition is D^T K = K D. For diagonal Galerkin boundary operators,
that condition forces every + chirality eigenvalue to be paired with a - chirality
eigenvalue of the same value. Hence a zero crossing in the modeled class has zero net
chiral contribution: +1 and -1 cross together with the same orientation.

The controls are:

  1. A paired K-compatible crossing family: net chiral spectral flow is zero.
  2. A pure Krein-isometric conjugacy family: the spectrum is constant, so no spectral flow
     is created by changing carrier frame.
  3. A one-sided crossing family: net chiral flow is nonzero, but K-self-adjointness fails.

The point is to sharpen the next theorem target, not to close WC-FUNCTION-SPACE-EXT.
"""

from __future__ import annotations

import numpy as np


N = 8
TOL = 1e-10


def krein_form(n: int = N) -> np.ndarray:
    z = np.zeros((n, n))
    i = np.eye(n)
    return np.block([[z, i], [i, z]])


def grading(n: int = N) -> np.ndarray:
    return np.diag(np.r_[np.ones(n), -np.ones(n)])


K = krein_form()
GAMMA = grading()


def k_selfadjoint_residual(d: np.ndarray) -> float:
    return float(np.linalg.norm(d.T @ K - K @ d) / max(1.0, np.linalg.norm(d)))


def gamma_cross_residual() -> float:
    return float(np.linalg.norm(GAMMA @ K + K @ GAMMA))


def paired_operator(t: float) -> np.ndarray:
    """K-self-adjoint diagonal toy family with paired + and - chirality eigenvalues."""
    lam = np.array(
        [
            t - 0.65,
            t + 0.40,
            1.25,
            -1.75,
            2.50,
            -2.25,
            3.00,
            -3.50,
        ]
    )
    return np.diag(np.r_[lam, lam])


def bad_one_sided_operator(t: float) -> np.ndarray:
    """Control family with an unpaired + chirality crossing."""
    plus = np.array([t - 0.10, 1.10, -1.30, 1.70, -2.10, 2.70, -3.10, 3.70])
    minus = np.array([0.80, 1.20, -1.40, 1.80, -2.20, 2.80, -3.20, 3.80])
    return np.diag(np.r_[plus, minus])


def crossing_contributions(family, roots: list[float], eps: float = 1e-5) -> list[tuple[float, int, int]]:
    """
    Return (root, chirality, orientation) for simple sign changes at known roots.

    chirality is +1 for W_+ and -1 for W_-.
    orientation is +1 for negative-to-positive and -1 for positive-to-negative.
    """
    out: list[tuple[float, int, int]] = []
    for root in roots:
        left = np.diag(family(root - eps))
        right = np.diag(family(root + eps))
        for idx, (a, b) in enumerate(zip(left, right)):
            if abs(a) < TOL or abs(b) < TOL:
                raise AssertionError("eps too small for crossing orientation check")
            if a * b < 0:
                chirality = 1 if idx < N else -1
                orientation = 1 if a < 0 < b else -1
                out.append((root, chirality, orientation))
    return out


def net_chiral_flow(contribs: list[tuple[float, int, int]]) -> int:
    return int(sum(chirality * orientation for _, chirality, orientation in contribs))


def block_rotation_generator(n: int = N) -> np.ndarray:
    """A K-skew and Euclidean-skew generator X with X^2 = -I."""
    if n % 2:
        raise ValueError("n must be even")
    j2 = np.array([[0.0, 1.0], [-1.0, 0.0]])
    j = np.kron(np.eye(n // 2), j2)
    z = np.zeros((n, n))
    return np.block([[z, j], [j, z]])


X = block_rotation_generator()


def krein_rotation(t: float) -> np.ndarray:
    # Since X^2 = -I, exp(tX) = cos(t) I + sin(t) X.
    return np.cos(t) * np.eye(2 * N) + np.sin(t) * X


def conjugacy_family(t: float) -> np.ndarray:
    vals = np.array([-4.0, -3.0, -2.0, -1.0, 1.0, 2.0, 3.0, 4.0])
    d0 = np.diag(np.r_[vals, vals])
    u = krein_rotation(t)
    return u.T @ d0 @ u


def assert_krein_rotation() -> None:
    for t in np.linspace(0.0, 1.2, 7):
        u = krein_rotation(float(t))
        iso = np.linalg.norm(u.T @ K @ u - K)
        orth = np.linalg.norm(u.T @ u - np.eye(2 * N))
        assert iso < 1e-12, iso
        assert orth < 1e-12, orth


def run() -> None:
    print("[setup]")
    print(f"  ||Gamma K + K Gamma|| = {gamma_cross_residual():.1e}")
    assert gamma_cross_residual() < 1e-12

    print("\n[1] paired K-compatible crossing family")
    paired_roots = [0.65, -0.40]
    paired_residuals = [k_selfadjoint_residual(paired_operator(t)) for t in [-0.8, -0.4, 0.0, 0.65, 0.9]]
    paired_contribs = crossing_contributions(paired_operator, paired_roots)
    paired_flow = net_chiral_flow(paired_contribs)
    print(f"  max K-self-adjoint residual = {max(paired_residuals):.1e}")
    print(f"  crossing contributions = {paired_contribs}")
    print(f"  net chiral spectral flow = {paired_flow:+d}")
    assert max(paired_residuals) < 1e-12
    assert paired_flow == 0

    print("\n[2] pure Krein-isometric conjugacy family")
    assert_krein_rotation()
    base = np.linalg.eigvalsh(conjugacy_family(0.0))
    max_drift = 0.0
    max_kres = 0.0
    for t in np.linspace(0.0, 1.2, 13):
        d = conjugacy_family(float(t))
        max_drift = max(max_drift, float(np.max(np.abs(np.linalg.eigvalsh(d) - base))))
        max_kres = max(max_kres, k_selfadjoint_residual(d))
    print(f"  max eigenvalue drift under U(t)^-1 D0 U(t) = {max_drift:.1e}")
    print(f"  max K-self-adjoint residual = {max_kres:.1e}")
    assert max_drift < 1e-12
    assert max_kres < 1e-12

    print("\n[3] one-sided chiral-flow control")
    bad_residuals = [k_selfadjoint_residual(bad_one_sided_operator(t)) for t in [-0.2, 0.1, 0.4]]
    bad_contribs = crossing_contributions(bad_one_sided_operator, [0.10])
    bad_flow = net_chiral_flow(bad_contribs)
    print(f"  min K-self-adjoint residual = {min(bad_residuals):.1e}")
    print(f"  crossing contributions = {bad_contribs}")
    print(f"  net chiral spectral flow = {bad_flow:+d}")
    assert min(bad_residuals) > 1e-2
    assert bad_flow == 1

    print(
        "\nVERDICT: in this finite-Galerkin model, Krein-compatible paired crossings and "
        "Krein-isometric conjugacy do not produce net chiral spectral flow; the nonzero "
        "control leaves the modeled Krein-compatible class. WC-FUNCTION-SPACE-EXT remains open."
    )


if __name__ == "__main__":
    run()
