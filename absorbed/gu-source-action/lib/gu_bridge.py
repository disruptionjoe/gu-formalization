"""Bridge to the verified gu-formalization machinery.

The construction program builds ON the parent repo's adversarially-verified objects; it never re-derives them.
This module locates gu-formalization (env GU_FORMALIZATION_PATH, else the sibling ../gu-formalization),
imports its explicit Cl(9,5)=M(64,H) representation, and exposes the verified constraint setup + the
obstruction C2. Reproduces the parent anchors: bare ||[Pi_RS, M_D]|| = 58.7215, C2 = 155.3625.
"""

from __future__ import annotations

import os
import sys

import numpy as np

N = 14
DIM = 128
# The parent repo's fixed sample covector (defines M_D / Gamma; the C2 anchors are at this xi).
XI = np.array([1.0, 2.0, 3.0, 4.0, 0.5, 1.5, 2.5, 0.7,
               1.1, 0.3, 2.2, 1.7, 0.9, 1.3], dtype=complex)


def gu_formalization_path() -> str:
    """Locate the parent gu-formalization repo."""
    p = os.environ.get("GU_FORMALIZATION_PATH")
    if p and os.path.isdir(p):
        return p
    here = os.path.dirname(os.path.abspath(__file__))
    sibling = os.path.normpath(os.path.join(here, "..", "..", "gu-formalization"))
    if os.path.isdir(sibling):
        return sibling
    raise RuntimeError(
        "gu-formalization not found. Set GU_FORMALIZATION_PATH, or place this repo as a "
        "sibling of gu-formalization (../gu-formalization)."
    )


_GU = gu_formalization_path()
_TESTS = os.path.join(_GU, "tests")
if _TESTS not in sys.path:
    sys.path.insert(0, _TESTS)

import oq_rk1_cl95_explicit_rep as cl95  # noqa: E402  (the verified Cl(9,5)=M(64,H) rep)


def gammas():
    """The verified Cl(9,5) gamma matrices e[a] (signature (9,5))."""
    G = cl95.jordan_wigner_gammas(7)
    eta = [1] * 9 + [-1] * 5
    return [G[a] if eta[a] > 0 else 1j * G[a] for a in range(N)]


def constraint_objects(xi=None):
    """Return (e, Gamma, Pi_RS, M_D), the verified constraint setup.

    Gamma = hstack(e) is the gamma-trace map; Pi_RS the orthogonal projector onto ker(Gamma);
    M_D = id_14 (x) c(xi) the twisted Dirac symbol. Reproduces the parent anchors.
    """
    if xi is None:
        xi = XI
    e = gammas()
    Gamma = np.hstack(e)                                          # 128 x 1792
    Pi_RS = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
    cxi = sum(xi[a] * e[a] for a in range(N))
    M_D = np.kron(np.eye(N, dtype=complex), cxi)
    return e, Gamma, Pi_RS, M_D


def C2(xi=None) -> float:
    """The final obstruction C2 = ||Gamma . M_D . Pi_RS|| (bare 155.3625 at the repo xi)."""
    e, Gamma, Pi_RS, M_D = constraint_objects(xi)
    return float(np.linalg.norm(Gamma @ M_D @ Pi_RS))


def anchors() -> dict:
    """The verified anchors, recomputed live, for a bridge self-check."""
    e, Gamma, Pi_RS, M_D = constraint_objects()
    comm = float(np.linalg.norm(Pi_RS @ M_D - M_D @ Pi_RS))
    c2 = float(np.linalg.norm(Gamma @ M_D @ Pi_RS))
    return {"gu_path": _GU, "bare_commutator": comm, "C2": c2}
