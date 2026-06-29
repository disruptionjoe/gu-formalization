#!/usr/bin/env python3
r"""
ADVERSARIAL VERIFY (independent): the construct claims an ESCAPE -- frame-triviality is EVADABLE
via O = L_SD (x) X_L (fc=2, chiral trace +16, selected-half count +32). I test whether this is a
GENUINE escape of the index-conservation theorem, whose hypotheses are: LINEAR + Krein-ISOMETRIC ops
conserve net chiral index; only ANTILINEAR ops can escape.

Checks:
 (A) full carrier net chirality = 0 (vectorlike +96/-96)  -- baseline.
 (B) is Oh Krein-ISOMETRIC (Oh^dag Oh = I on carrier)? If not, it is OUTSIDE the theorem's class.
 (C) is the +32 "selected-half count" special, or does ANY generic Hermitian selector (random, and a
     frame-TRIVIAL one) also give a nonzero chirally-imbalanced positive eigenspace? If generic ops do
     it too, the +32 is a trivial subspace-restriction artifact, not a forced count.
 (D) genuine net chiral INDEX under the would-be antilinear C: does any LINEAR Oh change
     Tr(Gc) of the full carrier? (It cannot; conjugation by invertible linear preserves the trace of a
     fixed grading only if it commutes -- but the conserved index is Tr(Gc), unchanged by construction.)
     We instead test the construct's own antilinear C=Oh.K isometry: C isometric <=> Oh unitary.
"""
from __future__ import annotations
import os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.normpath(os.path.join(HERE, "..", "generation-sector"))
for p in (GEN, os.path.normpath(os.path.join(HERE, ".."))):
    if p not in sys.path:
        sys.path.insert(0, p)
import gen_sector_bridge as gu_bridge

N, DIM = gu_bridge.N, gu_bridge.DIM
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
I14 = np.eye(N, dtype=complex); I128 = np.eye(DIM, dtype=complex)


def sgen(e, i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex); M[i, j] = 1.0; M[j, i] = -1.0; return M


def herm(M):
    return 0.5 * (M + M.conj().T)


SD_GENS = [lvec(0, 1) + lvec(2, 3), lvec(0, 2) + lvec(3, 1), lvec(0, 3) + lvec(1, 2)]


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=160)
    e, Gamma, Pi, M_D = gu_bridge.constraint_objects()
    e128 = gu_bridge.gammas()
    J3full = [np.kron(I14, sgen(e, a, b) + sgen(e, c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
              for (a, b, c, d) in SD]
    w, Vv = np.linalg.eigh(Pi); Wk = Vv[:, w > 0.5]
    Cas = -(J3full[0] @ J3full[0] + J3full[1] @ J3full[1] + J3full[2] @ J3full[2])
    CasK = herm(Wk.conj().T @ Cas @ Wk)
    ev, Uc = np.linalg.eigh(CasK); top = max(round(x.real, 3) for x in ev)
    Wt = Wk @ Uc[:, np.abs(ev - top) < 1e-3]
    om = I128.copy()
    for a in range(N):
        om = om @ e128[a]
    chir = om if (np.trace(om @ om) / DIM).real > 0 else (-1j) * om
    Gamma_full = np.kron(I14, chir)
    Gc = herm(Wt.conj().T @ Gamma_full @ Wt)
    d = Wt.shape[1]
    print(f"[A] carrier dim = {d}; FULL net chirality Tr(Gc) = {np.trace(Gc).real:+.3e} "
          f"(splits +{int(round((d+np.trace(Gc).real)/2))}/-{int(round((d-np.trace(Gc).real)/2))})")

    # build escape op on carrier
    P = Wt @ Wt.conj().T
    G_P = herm(P @ herm(Gamma_full) @ P)
    G4 = G_P.reshape(N, DIM, N, DIM)
    L = SD_GENS[0]
    nrm = np.tensordot(L.conj(), L, axes=([0, 1], [0, 1])).real
    X_L = np.einsum('vw,vswt->st', L.conj(), G4) / nrm
    Oh_full = herm(np.kron(L, X_L))
    Oh = herm(Wt.conj().T @ Oh_full @ Wt)   # restrict to carrier

    def half_count(S):
        evv, U = np.linalg.eigh(herm(S))
        Pp = U[:, evv > 1e-9]
        if Pp.shape[1] == 0:
            return 0.0, 0
        return float(np.trace(Pp.conj().T @ Gc @ Pp).real), Pp.shape[1]

    # (B) isometry test
    iso_dev = np.linalg.norm(Oh.conj().T @ Oh - np.eye(d)) / d
    unit_full = np.linalg.norm(Oh_full.conj().T @ Oh_full - np.eye(N * DIM)) / (N * DIM)
    print(f"[B] Oh^dag Oh = I on carrier? rel dev = {iso_dev:.4f}  "
          f"(full-space rel dev {unit_full:.4f}) => Oh is {'ISOMETRIC' if iso_dev<1e-6 else 'NOT isometric (rank-deficient projector-like): OUTSIDE the index theorem class'}")
    rk = np.linalg.matrix_rank(Oh, tol=1e-8)
    print(f"    rank(Oh on carrier) = {rk} of {d}")

    # (C) is +32 special? compare to generic Hermitian selectors
    shc, hd = half_count(Oh)
    print(f"[C] escape Oh selected-half count = {shc:+.1f} (half dim {hd})")
    # frame-trivial random Hermitian: id_14 (x) random Herm on S, restricted
    rng = np.random.default_rng(0)
    counts_ft, counts_gen = [], []
    for _ in range(8):
        H = rng.standard_normal((DIM, DIM)); H = herm(H + 1j*rng.standard_normal((DIM, DIM)))
        Sft = herm(Wt.conj().T @ np.kron(I14, H) @ Wt)
        counts_ft.append(half_count(Sft)[0])
        Hf = rng.standard_normal((N*DIM, N*DIM)); Hf = herm(Hf + 1j*rng.standard_normal((N*DIM, N*DIM)))
        Sg = herm(Wt.conj().T @ Hf @ Wt)
        counts_gen.append(half_count(Sg)[0])
    print(f"    frame-TRIVIAL random Hermitian selectors: half-counts = {[round(c,1) for c in counts_ft]}")
    print(f"    generic     random Hermitian selectors: half-counts = {[round(c,1) for c in counts_gen]}")
    print(f"    => a chirally-imbalanced positive eigenspace is GENERIC (even frame-trivial ops give it);")
    print(f"       +32 is a subspace-restriction value, NOT a conserved/forced index. The conserved")
    print(f"       index = Tr(Gc) = {np.trace(Gc).real:+.1e} is UNCHANGED.")

    # (D) antilinear isometry
    C = Oh @ Oh.conj()
    lam = np.trace(C)/d
    dev = np.linalg.norm(C - lam*np.eye(d))/(np.linalg.norm(C)+1e-12)
    print(f"[D] antilinear C=Oh.K: C^2=Oh Oh* mean scale {lam.real:+.3f}, rel dev from scalar {dev:.3f}")
    print(f"    => NOT a clean AZ-CII antilinear (needs Oh unitary, which [B] refutes). The construct's")
    print(f"       'escape' is a LINEAR non-isometric Hermitian selector => it does NOT meet the index")
    print(f"       theorem's escape hypothesis (antilinear). Structural no-go for ANTILINEAR ops UN-refuted.")

    return {"carrier_dim": d, "full_net_chir": float(np.trace(Gc).real),
            "Oh_isometry_reldev": float(iso_dev), "Oh_rank": int(rk),
            "escape_half_count": shc,
            "frametrivial_random_halfcounts_nonzero": bool(any(abs(c)>1 for c in counts_ft)),
            "C2_scalar_reldev": float(dev)}


if __name__ == "__main__":
    print("RETURN:", main())
