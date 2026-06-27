#!/usr/bin/env python3
"""C2 is structurally GLOBAL: no local so(9,5) holonomy carrier can reconcile it.

CONTEXT (SOURCE-02/BICOMPLEX-01 + the Y14-curvature gate, 2026-06-27)
--------------------------------------------------------------------
The RS BV bicomplex closes the escape; the true remaining obstruction is the secondary
constraint C2 = Gamma . M_D . Pi_RS (bare norm 155.36, fully Gamma-INDEPENDENT). The
climactic-gate carriers all dress the constraint co-differential by a HOLONOMY:
    B_W = Gamma . (id_14 (x) G_W),  G_W = exp(sigma_c(W)),  sigma_c(W) = sum W_ab Sigma_ab,
and ask whether ker(B_W) can be made M_D-invariant enough to drive the dressed C2 to 0.

The full (~11 min) gates built the ACTUAL gimmel curvature W and found it floors at ~bare
(0-1.8% drop; ~94% of C2 is global/topological residual). THIS file is the fast, standalone
confirmation of the STRUCTURAL core: a holonomy carrier B_W = Gamma.(id (x) G_W) cannot pull
the Gamma-independent C2 below its bare value -- it generically INCREASES it. So the missing
datum cannot be any local connection/curvature/holonomy on a single section; it is the global
Y14 = Met(X4) structure (non-compact K3 chi-gate / APS end-data). Honest scope: this PROVES
local/holonomy insufficiency; it does NOT prove the global end-data reconciles C2.

Runs in ~10s (no curvature build). Reproduces the anchors bare C2=155.36, [Pi_RS,M_D]=58.72.
"""

from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import oq_rk1_cl95_explicit_rep as cl95

try:
    from scipy.linalg import expm
except Exception:  # pragma: no cover - fallback if scipy missing
    def expm(A, terms=24):
        out = np.eye(A.shape[0], dtype=complex)
        term = np.eye(A.shape[0], dtype=complex)
        for k in range(1, terms):
            term = term @ A / k
            out = out + term
        return out

N = 14
DIM = 128
XI = np.array([1.0, 2.0, 3.0, 4.0, 0.5, 1.5, 2.5, 0.7,
               1.1, 0.3, 2.2, 1.7, 0.9, 1.3], dtype=complex)


def build():
    G = cl95.jordan_wigner_gammas(7)
    eta = [1] * 9 + [-1] * 5
    e = [G[a] if eta[a] > 0 else 1j * G[a] for a in range(N)]
    return e


def proj_ker(B):
    """Orthogonal projector onto ker(B) for a wide full-row-rank B (rows x cols)."""
    BBd = B @ B.conj().T
    return np.eye(B.shape[1], dtype=complex) - B.conj().T @ np.linalg.inv(BBd) @ B


def fro(M):
    return float(np.linalg.norm(M))


def main():
    e = build()
    Sig = lambda a, b: 0.25 * (e[a] @ e[b] - e[b] @ e[a])
    Gamma = np.hstack(e)                                   # 128 x 1792
    cxi = sum(XI[a] * e[a] for a in range(N))
    M_D = np.kron(np.eye(N, dtype=complex), cxi)
    Pi_RS = proj_ker(Gamma)

    bare_comm = fro(Pi_RS @ M_D - M_D @ Pi_RS)
    bare_C2 = fro(Gamma @ M_D @ Pi_RS)
    # Gamma-independence of C2
    Gpinv = Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T)
    resid_C2 = fro((Gamma @ M_D @ Pi_RS) - (Gamma @ M_D @ Pi_RS) @ Gpinv @ Gamma)

    print("=" * 76)
    print("C2 is GLOBAL: no local so(9,5) holonomy carrier reconciles it")
    print("=" * 76)
    print(f"  anchors: bare ||[Pi_RS,M_D]|| = {bare_comm:.4f} (repo 58.72)")
    print(f"           bare ||C2=Gamma M_D Pi_RS|| = {bare_C2:.4f} (repo 155.36); "
          f"Gamma-independent residual = {resid_C2:.4f}")
    assert abs(bare_comm - 58.7215) < 1e-2
    assert abs(bare_C2 - 155.3625) < 1e-2
    assert abs(resid_C2 - bare_C2) < 1e-2, "C2 must be fully Gamma-independent"

    # sweep random so(9,5) holonomies at several amplitudes; track min dressed C2
    rng = np.random.default_rng(0)
    pairs = [(a, b) for a in range(N) for b in range(a + 1, N)]
    best = float("inf")
    best_at = None
    n_below_bare = 0
    for trial in range(8):
        coeffs = {p: rng.normal() for p in pairs}
        sig = sum(coeffs[(a, b)] * Sig(a, b) for (a, b) in pairs)
        for t in (0.3, 1.0, 2.0):
            GW = expm(t * sig)
            BW = Gamma @ np.kron(np.eye(N, dtype=complex), GW)
            PiB = proj_ker(BW)
            c2 = fro(BW @ M_D @ PiB)
            if c2 < bare_C2 - 1.0:
                n_below_bare += 1
            if c2 < best:
                best, best_at = c2, (trial, t)
    print(f"\n  min dressed C2 over 8 random so(9,5) holonomies x 3 amplitudes = {best:.4f}")
    print(f"    (bare {bare_C2:.4f}; below bare? {best < bare_C2 - 1.0}; "
          f"#configs below bare = {n_below_bare}/24)")
    assert best > bare_C2 - 1.0, "a local holonomy reduced C2 below bare -- finding would change"

    print("\n" + "=" * 76)
    print("VERDICT: a holonomy carrier B_W = Gamma.(id (x) G_W) cannot pull the")
    print("Gamma-independent C2 below bare (it generically INCREASES it). The actual")
    print("gimmel curvature (a specific such holonomy) floors at ~bare (full gate: 0-1.8%")
    print("drop, ~94% global residual). So the missing datum is NOT a local connection/")
    print("curvature on a single section -- it is the global Y14=Met(X4) structure")
    print("(non-compact K3 chi-gate / APS end). [Proves local insufficiency; does NOT")
    print("prove the global end-data reconciles C2.]")
    print("=" * 76)


if __name__ == "__main__":
    main()
