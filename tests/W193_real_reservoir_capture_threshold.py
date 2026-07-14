#!/usr/bin/env python3
r"""
W193 -- real-reservoir capture threshold for the open-Krein loop-unitarity toy-vs-general gate.

Purpose.  W187 used analytic square-root threshold self-energies.  W189/H21 asks for the cheapest
discharge of the toy-vs-general gate: one dressed r* computation for a real reservoir.  This script
replaces the square-root toy by a finite-quadrature Ohmic/Drude continuum reservoir and checks whether
the same qualitative capture threshold survives.

Scope.  This is finite-model evidence, not a class theorem and not a GU verdict.  It tests one
physically standard reservoir family:

    J(E) = (E - E0)^p exp(-(E - E0) / Lambda), E >= E0.

The load-bearing case is p=1, Lambda=2.5, internal threshold 0, source threshold 0.2, with the
Stelle ghost normalized to M=1.  The first capture threshold should track the on-shell width-balance
prediction

    r_width = sqrt(J_internal(M) / J_source(M)).

The script also keeps the honest finite-band warning: the real-reservoir finite model can have
additional resonance windows, so this does not prove monotone "all larger kappa works" behavior.
"""
from __future__ import annotations

import math

import numpy as np

M_DISC = 1.0
N_QUAD = 100
E_MAX = 4.0
CUTOFF = 2.5
POWER = 1.0
SOURCE_THRESHOLD = 0.2
SCALE = 0.35
G_KIN = 1.0
REAL_TOL = 1e-7

checks: list[tuple[str, bool, str]] = []


def log(message: str = "") -> None:
    print(message, flush=True)


def check(name: str, passed: bool, detail: str = "") -> None:
    checks.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))


def ohmic_drude_reservoir(threshold: float, e_max: float, n: int, power: float, cutoff: float) -> tuple[np.ndarray, np.ndarray]:
    edges = np.linspace(threshold, e_max, n + 1)
    energies = 0.5 * (edges[:-1] + edges[1:])
    d_energy = edges[1] - edges[0]
    shifted = np.maximum(energies - threshold, 0.0)
    density = (shifted ** power) * np.exp(-shifted / cutoff)
    return energies, np.sqrt(density * d_energy)


def spectral_density_at(mass: float, threshold: float, power: float, cutoff: float) -> float:
    if mass <= threshold:
        return 0.0
    shifted = mass - threshold
    return (shifted ** power) * math.exp(-shifted / cutoff)


E_INT, V_INT_BASE = ohmic_drude_reservoir(0.0, E_MAX, N_QUAD, POWER, CUTOFF)
E_SRC, V_SRC_BASE = ohmic_drude_reservoir(SOURCE_THRESHOLD, E_MAX + SOURCE_THRESHOLD, N_QUAD, POWER, CUTOFF)
V_INT = SCALE * V_INT_BASE
V_SRC = SCALE * V_SRC_BASE


def total_generator(kappa: float, source_sign: float = +1.0, positive_definite: bool = False) -> np.ndarray:
    """Finite Fano-Anderson generator.

    In the Krein case, the internal graviton continuum is opposite signed relative to the ghost and
    therefore couples antisymmetrically.  The favorable source reservoir is like signed and couples
    symmetrically.  A wrong-sign source is antisymmetric too.
    """

    n_total = 1 + len(E_INT) + len(E_SRC)
    generator = np.zeros((n_total, n_total))
    generator[0, 0] = M_DISC

    for idx, energy in enumerate(E_INT, start=1):
        coupling = G_KIN * V_INT[idx - 1]
        generator[idx, idx] = energy
        if positive_definite:
            generator[0, idx] = coupling
            generator[idx, 0] = coupling
        else:
            generator[0, idx] = -coupling
            generator[idx, 0] = +coupling

    offset = 1 + len(E_INT)
    for j, energy in enumerate(E_SRC):
        idx = offset + j
        coupling = kappa * V_SRC[j]
        generator[idx, idx] = energy
        generator[0, idx] = coupling
        generator[idx, 0] = coupling if positive_definite else source_sign * coupling

    return generator


def krein_metric(source_sign: float = +1.0) -> np.ndarray:
    # Ghost and favorable source reservoir are like signed (-1); internal continuum is opposite (+1).
    # For the wrong-sign source control, the source reservoir is treated as opposite signed.
    source_krein = -1.0 if source_sign > 0 else +1.0
    signs = [-1.0] + [+1.0] * len(E_INT) + [source_krein] * len(E_SRC)
    return np.diag(signs)


def max_imag(generator: np.ndarray) -> float:
    return float(np.max(np.abs(np.linalg.eigvals(generator).imag)))


def is_real(kappa: float, source_sign: float = +1.0) -> bool:
    return max_imag(total_generator(kappa, source_sign=source_sign)) < REAL_TOL


def first_capture_threshold() -> float:
    # This bracket intentionally locates the first real-spectrum window.  Later finite-band windows
    # are checked separately and are not used to assert monotone all-kappa capture.
    lo = 1.0
    hi = 1.2
    assert not is_real(lo), "lower bracket should still be complex"
    assert is_real(hi), "upper bracket should have entered the first capture window"
    for _ in range(36):
        mid = 0.5 * (lo + hi)
        if is_real(mid):
            hi = mid
        else:
            lo = mid
    return hi


def main() -> int:
    log("=" * 88)
    log("W193 -- real-reservoir capture threshold (Ohmic/Drude finite continuum)")
    log("=" * 88)

    generator = total_generator(0.8)
    k_metric = krein_metric()
    pseudo_error = float(np.max(np.abs(k_metric @ generator - generator.T @ k_metric)))
    check(
        "PC1 Krein generator is K-pseudo-Hermitian",
        pseudo_error < 1e-12,
        f"residual={pseudo_error:.1e}",
    )

    source_off_imag = max_imag(total_generator(0.0))
    check(
        "PC2 source-off kinematic continuum is pathological",
        source_off_imag > 0.1,
        f"max imaginary part={source_off_imag:.3f}",
    )

    j_internal = spectral_density_at(M_DISC, 0.0, POWER, CUTOFF)
    j_source = spectral_density_at(M_DISC, SOURCE_THRESHOLD, POWER, CUTOFF)
    r_width = math.sqrt(j_internal / j_source)
    r_numeric = first_capture_threshold()
    below_imag = max_imag(total_generator(0.97 * r_numeric))
    above_imag = max_imag(total_generator(1.03 * r_numeric))
    check(
        "G1 first capture threshold tracks spectral-density width balance",
        abs(r_numeric - r_width) < 0.03 and 1.0 < r_numeric < 1.15,
        f"r_numeric={r_numeric:.4f}, r_width={r_width:.4f}",
    )
    check(
        "G2 threshold is a real transition, complex below and real above",
        below_imag > 1e-3 and above_imag < REAL_TOL,
        f"below={below_imag:.3e}, above={above_imag:.3e}",
    )

    wrong_sign_imags = [max_imag(total_generator(kappa, source_sign=-1.0)) for kappa in [1.2, 2.0, 5.0, 10.0]]
    check(
        "G3 wrong-sign reservoir is not rescued by magnitude",
        all(value > 0.1 for value in wrong_sign_imags),
        "max imaginary parts=" + ", ".join(f"{value:.3f}" for value in wrong_sign_imags),
    )

    window_values = {
        1.2: max_imag(total_generator(1.2)),
        2.5: max_imag(total_generator(2.5)),
        3.0: max_imag(total_generator(3.0)),
    }
    check(
        "G4 finite-band warning is real: capture is not a monotone all-kappa theorem",
        window_values[1.2] < REAL_TOL and window_values[2.5] > 1e-3 and window_values[3.0] < REAL_TOL,
        "imag(1.2,2.5,3.0)=" + ", ".join(f"{window_values[k]:.3e}" for k in [1.2, 2.5, 3.0]),
    )

    positive_imags = [
        max_imag(total_generator(kappa, positive_definite=True))
        for kappa in [0.0, 0.5, 1.2, 3.0]
    ]
    check(
        "NC1 positive-definite analog stays real",
        all(value < REAL_TOL for value in positive_imags),
        "max imaginary parts=" + ", ".join(f"{value:.1e}" for value in positive_imags),
    )

    log("")
    log("SYNTHESIS")
    log(f"  Ohmic/Drude source threshold = {SOURCE_THRESHOLD}; r_width = {r_width:.4f}; first r_numeric = {r_numeric:.4f}.")
    log("  The W187 sign/capture structure survives one non-square-root continuum reservoir.")
    log("  The finite-band warning prevents promotion to a generic monotone class theorem.")
    log("  H21 is advanced, not closed. No claim-status, canon, verdict, or public-posture change.")

    passed = sum(1 for _, ok, _ in checks if ok)
    log("")
    log(f"W193 RESULT: {passed}/{len(checks)} checks passed.")
    if passed != len(checks):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
