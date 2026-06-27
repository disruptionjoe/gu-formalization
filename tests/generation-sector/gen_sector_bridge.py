"""Generation-sector bridge (parent-local).

Self-contained version of the gu-source-action `lib/gu_bridge.py`, co-located in gu-formalization so
the migrated generation-sector audit tests (step1..step11, CONSTRUCT-01..07) run directly against this
repo's own verified Cl(9,5)=M(64,H) representation (`tests/oq_rk1_cl95_explicit_rep.py`). Reproduces the
anchors: bare ||[Pi_RS, M_D]|| = 58.7215, C2 = 155.3625.

These tests were developed in the child repo gu-source-action (CONSTRUCT-01..07) but they are AUDIT
results about GU's structure, not construction of the missing object, so they belong here with the rest
of the reconstruction+audit. See `../../canon/no-go-quaternionic-parity-generation-sector.md`.
"""
from __future__ import annotations

import os
import sys

import numpy as np

# the verified rep lives one directory up, in gu-formalization/tests/
_PARENT_TESTS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
if _PARENT_TESTS not in sys.path:
    sys.path.insert(0, _PARENT_TESTS)

import oq_rk1_cl95_explicit_rep as cl95  # noqa: E402  (the verified Cl(9,5)=M(64,H) rep)

N = 14
DIM = 128
XI = np.array([1.0, 2.0, 3.0, 4.0, 0.5, 1.5, 2.5, 0.7,
               1.1, 0.3, 2.2, 1.7, 0.9, 1.3], dtype=complex)


def gammas():
    """The verified Cl(9,5) gamma matrices e[a] (signature (9,5))."""
    G = cl95.jordan_wigner_gammas(7)
    eta = [1] * 9 + [-1] * 5
    return [G[a] if eta[a] > 0 else 1j * G[a] for a in range(N)]


def constraint_objects(xi=None):
    """Return (e, Gamma, Pi_RS, M_D), the verified constraint setup (reproduces the anchors)."""
    if xi is None:
        xi = XI
    e = gammas()
    Gamma = np.hstack(e)
    Pi_RS = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
    cxi = sum(xi[a] * e[a] for a in range(N))
    M_D = np.kron(np.eye(N, dtype=complex), cxi)
    return e, Gamma, Pi_RS, M_D


def C2(xi=None) -> float:
    e, Gamma, Pi_RS, M_D = constraint_objects(xi)
    return float(np.linalg.norm(Gamma @ M_D @ Pi_RS))


def anchors() -> dict:
    e, Gamma, Pi_RS, M_D = constraint_objects()
    comm = float(np.linalg.norm(Pi_RS @ M_D - M_D @ Pi_RS))
    c2 = float(np.linalg.norm(Gamma @ M_D @ Pi_RS))
    return {"bare_commutator": comm, "C2": c2}
