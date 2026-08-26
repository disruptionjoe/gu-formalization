#!/usr/bin/env python3
"""M-S3: exceptional-point monodromy versus the PU ghost grading.

The equal-frequency Pais--Uhlenbeck Hamiltonian is even in the frequency
splitting epsilon.  Its analytic base coordinate is therefore
delta=epsilon^2.  A loop around delta=0 returns the matrix Hamiltonian but
changes epsilon to -epsilon, so the two n=1 eigenbranches may exchange.

This certificate freezes the oscillator basis, transports the two branches
by biorthogonal overlap, and compares the endpoint permutation with the
measured Krein-sign grading.  It is a toy-model result, not a GU action,
source claim, count, prediction, or physical Hilbert-space construction.
"""

from __future__ import annotations

import importlib.util
from math import pi
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "tests/big-swing/vg_v4_quantize_break_commuting_square.py"
SPEC = importlib.util.spec_from_file_location("vg_v4_base", BASE)
assert SPEC and SPEC.loader
VG = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VG)

FAILURES: list[str] = []
CHECKS = 0


def check(label: str, condition: object, detail: str = "") -> None:
    global CHECKS
    CHECKS += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'}: {label}{' -- ' + detail if detail else ''}")
    if not ok:
        FAILURES.append(label)


def fixed_basis_hamiltonian(n: int, epsilon: complex) -> tuple[np.ndarray, np.ndarray]:
    """Return H(epsilon) in one epsilon-independent oscillator basis."""
    z, pz, parity_z = VG.osc(n, 2.0)
    y, py, _ = VG.osc(n, 2.0)
    identity = np.eye(n, dtype=complex)
    z_op, pz_op = np.kron(z, identity), np.kron(pz, identity)
    y_op, py_op = np.kron(identity, y), np.kron(identity, py)
    w1, w2 = 1.0 + epsilon, 1.0 - epsilon
    hamiltonian = (
        1j * (pz_op @ y_op)
        + py_op @ py_op / 2
        + (w1**2 + w2**2) * (y_op @ y_op) / 2
        + (w1 * w2) ** 2 * (z_op @ z_op) / 2
    )
    return hamiltonian, np.kron(parity_z, identity)


def low_pair(hamiltonian: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    eigenvalues, eigenvectors = np.linalg.eig(hamiltonian)
    selected = np.argsort(np.abs(eigenvalues - 2.0))[:2]
    eigenvalues, eigenvectors = eigenvalues[selected], eigenvectors[:, selected]
    eigenvectors /= np.linalg.norm(eigenvectors, axis=0, keepdims=True)
    order = np.argsort(eigenvalues.real)
    return eigenvalues[order], eigenvectors[:, order]


def transport(n: int, delta_radius: float, turns: int) -> dict[str, object]:
    epsilon0 = delta_radius**0.5
    h0, eta = fixed_basis_hamiltonian(n, epsilon0)
    e0, v0 = low_pair(h0)
    eigenvalues, vectors = e0.copy(), v0.copy()
    steps = 96 * turns
    max_step_condition = 0.0

    for step in range(1, steps + 1):
        delta_angle = 2 * pi * turns * step / steps
        epsilon = epsilon0 * np.exp(0.5j * delta_angle)
        hamiltonian, _ = fixed_basis_hamiltonian(n, epsilon)
        candidate_values, candidates = low_pair(hamiltonian)
        overlap = np.abs(np.linalg.pinv(vectors) @ candidates)
        if overlap[0, 0] + overlap[1, 1] < overlap[0, 1] + overlap[1, 0]:
            candidates = candidates[:, [1, 0]]
            candidate_values = candidate_values[[1, 0]]
        coefficients = np.diag(np.linalg.pinv(vectors) @ candidates)
        candidates *= np.exp(-1j * np.angle(coefficients))[None, :]
        max_step_condition = max(max_step_condition, float(np.linalg.cond(candidates)))
        eigenvalues, vectors = candidate_values, candidates

    epsilon_end = epsilon0 * np.exp(1j * pi * turns)
    h_end, _ = fixed_basis_hamiltonian(n, epsilon_end)
    endpoint = np.linalg.pinv(v0) @ vectors
    krein_norms = np.real(np.diag(v0.conj().T @ eta @ v0))
    parity = np.diag(np.sign(krein_norms))
    return {
        "n": n,
        "delta_radius": delta_radius,
        "turns": turns,
        "h_closure": float(np.linalg.norm(h_end - h0)),
        "initial_values": e0,
        "final_values": eigenvalues,
        "endpoint_abs": np.abs(endpoint),
        "parity": parity,
        "krein_norms": krein_norms,
        "pair_condition": float(np.linalg.cond(v0)),
        "max_step_condition": max_step_condition,
    }


swap = np.array([[0.0, 1.0], [1.0, 0.0]])
identity = np.eye(2)
records = []

print("M-S3 exceptional-point monodromy certificate")
print("fixed PU oscillator basis; analytic coordinate delta=epsilon^2")
for n in (10, 12):
    for radius in (0.04, 0.09):
        one = transport(n, radius, 1)
        two = transport(n, radius, 2)
        records.append((one, two))
        one_matrix = one["endpoint_abs"]
        two_matrix = two["endpoint_abs"]
        parity = one["parity"]
        print(
            f"N={n} radius={radius:.2f}: cond(start)={one['pair_condition']:.3f}, "
            f"max cond(path)={one['max_step_condition']:.3f}, "
            f"one-loop swap residual={np.linalg.norm(one_matrix-swap):.3e}, "
            f"two-loop identity residual={np.linalg.norm(two_matrix-identity):.3e}"
        )
        check("one loop returns the fixed-basis Hamiltonian", one["h_closure"] < 1e-12)
        check("two loops return the fixed-basis Hamiltonian", two["h_closure"] < 1e-12)
        check("one loop swaps the two continuously tracked branches",
              np.linalg.norm(one_matrix - swap) < 2e-10)
        check("one loop is not the identity",
              np.linalg.norm(one_matrix - identity) > 1.9)
        check("two loops restore branch identity",
              np.linalg.norm(two_matrix - identity) < 2e-10)
        check("the two starting Krein signs are opposite",
              np.prod(np.sign(one["krein_norms"])) == -1)
        check("the swap anticommutes with the measured ghost grading",
              np.linalg.norm(swap @ parity + parity @ swap) < 1e-12)
        check("the monodromy is not the diagonal ghost-parity operator",
              np.linalg.norm(one_matrix - np.abs(parity)) > 1.9)
        check("reported pair conditioning remains finite",
              one["pair_condition"] < 20 and one["max_step_condition"] < 100)

check("both truncations and both radii give the same one-loop permutation",
      all(np.linalg.norm(one["endpoint_abs"] - swap) < 2e-10 for one, _ in records))
check("both truncations and both radii give the same two-loop return",
      all(np.linalg.norm(two["endpoint_abs"] - identity) < 2e-10 for _, two in records))

print(f"M-S3 verdict: {CHECKS-len(FAILURES)}/{CHECKS} checks passed")
print("one EP loop exchanges the two opposite-Krein branches; it does not equal")
print("the diagonal ghost parity. Instead it conjugates/exchanges the ghost labels.")
if FAILURES:
    print("failures:", ", ".join(FAILURES))
    raise SystemExit(1)
