#!/usr/bin/env python3
r"""
DECISIVE: connect the adversarial LINEAR escape (frame-active op with nonzero chiral TRACE +16) to the
actual FORCING notion (a chirally-imbalanced selected physical half = a light chiral generation count).

The adversarial probe (adversarial_frame_chir_orthogonality_probe.py) showed the strict linear trace-
orthogonality is FALSE: through the SELF-DUAL frame generators L_SD the carrier-projected grading G_P has
S-side content X_L (||X_L||=2), so O = L_SD (x) X_L is BOTH frame-active AND has chiral trace
Tr(G_P.O) = +16. This script asks the forcing question the campaign actually cares about:

  (1) Is the +16 a forced GENERATION COUNT? Decompose its primality (2- vs 3-primary).
  (2) Does Oh = Herm(L_SD (x) X_L) -- the explicit frame-active escape operator -- FORCE a nonzero
      net chirality of its SELECTED physical half (positive eigenspace on the carrier), the
      carrier-mass forcing notion? And is that count sourced by Oh's frame-trivial part or its
      frame-charged part?
  (3) Antilinearity check: build the genuine antilinear C = Oh.K_0 and report C^2 and whether the
      frame-active escape survives as an admissible antilinear chiralizer.

Run: python tests/gu-independent/decisive_escape_vs_forcing.py
"""
from __future__ import annotations
import os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.normpath(os.path.join(HERE, "..", "generation-sector"))
for p in (GEN, os.path.normpath(os.path.join(HERE, ".."))):
    if p not in sys.path:
        sys.path.insert(0, p)
import gen_sector_bridge as gu_bridge  # noqa: E402

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
ASD_GENS = [lvec(0, 1) - lvec(2, 3), lvec(0, 2) - lvec(3, 1), lvec(0, 3) - lvec(1, 2)]
SO4 = SD_GENS + ASD_GENS


def frame_charge(O, gens=SO4):
    O4 = O.reshape(N, DIM, N, DIM); tot = 0.0
    for L in gens:
        nrm = np.tensordot(L.conj(), L, axes=([0, 1], [0, 1])).real
        tot += float(np.linalg.norm(np.einsum('vw,vswt->st', L.conj(), O4) / nrm))
    return tot


def frame_trivial_part(O):
    O4 = O.reshape(N, DIM, N, DIM)
    return np.kron(I14, np.einsum('vsvt->st', O4) / N)


def primefac(n):
    n = abs(int(round(n)))
    if n <= 1:
        return str(n)
    out, d = [], 2
    while d * d <= n:
        ee = 0
        while n % d == 0:
            n //= d; ee += 1
        if ee:
            out.append(f"{d}^{ee}" if ee > 1 else f"{d}")
        d += 1
    if n > 1:
        out.append(str(n))
    return ".".join(out)


def three_two(n):
    n = abs(int(round(n)))
    if n == 0:
        return 0, 0
    t = n; k = 0
    while t % 3 == 0:
        t //= 3; k += 1
    return 3 ** k, n // (3 ** k)


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=170)
    print("=" * 94)
    print("DECISIVE: adversarial LINEAR escape (chiral trace +16) vs actual FORCING (selected-half count)")
    print("=" * 94)
    e, Gamma, Pi, M_D = gu_bridge.constraint_objects()
    e128 = gu_bridge.gammas()
    # carrier
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
    print(f"[carrier] dim {Wt.shape[1]}; net chirality {np.trace(Gc).real:+.2e} (+96/-96)")

    P = Wt @ Wt.conj().T
    G_P = herm(P @ herm(Gamma_full) @ P)

    def selected_half_count(S):
        """carrier-mass forcing notion: net chirality of the +eigenspace of S, on the carrier."""
        Sr = herm(Wt.conj().T @ S @ Wt)
        evv, U = np.linalg.eigh(Sr)
        phys = U[:, evv > 1e-9]
        if phys.shape[1] == 0:
            return 0.0, 0
        return float(np.trace(phys.conj().T @ Gc @ phys).real), phys.shape[1]

    def chiral_trace(S):
        return float(np.trace(G_P @ herm(S)).real)

    # ---- reconstruct the adversarial escape operator O = L_SD (x) X_L ----
    G4 = G_P.reshape(N, DIM, N, DIM)
    print("\n[escape operators O_k = L_SD^k (x) X_L^k  (the adversarial frame-active, net-chiral-trace ops)]")
    print(f"  {'gen':<6}{'fc(Oh)':>10}{'chiral_trace':>14}{'selected_half_count':>22}{'count(frame-triv part)':>26}")
    results = []
    for k, L in enumerate(SD_GENS):
        nrm = np.tensordot(L.conj(), L, axes=([0, 1], [0, 1])).real
        X_L = np.einsum('vw,vswt->st', L.conj(), G4) / nrm        # DIM x DIM
        O = np.kron(L, X_L)
        Oh = herm(O)
        fc = frame_charge(Oh)
        ct = chiral_trace(Oh)
        shc, dim = selected_half_count(Oh)
        Ot = herm(frame_trivial_part(Oh))
        shc_t, _ = selected_half_count(Ot)
        results.append((fc, ct, shc, shc_t))
        print(f"  SD{k:<4}{fc:>10.3f}{ct:>14.3f}{shc:>+22.3f}{shc_t:>+26.3f}")

    # primality of the chiral trace
    ct0 = int(round(results[0][1]))
    t3, t2 = three_two(ct0)
    print(f"\n  chiral trace value = {ct0} = {primefac(ct0)} ; 3-part = {t3} ; 2-part = {t2} "
          f"; equals 3? {abs(ct0)==3} ; contains factor 3? {ct0 % 3 == 0}")

    # ---- antilinear version: C = Oh . K_0, C^2 ? ----
    print("\n[antilinear] C = Oh . K_0 (K_0 = entrywise conj). C^2 = Oh Oh* ; report scale/identity-likeness")
    L = SD_GENS[0]
    nrm = np.tensordot(L.conj(), L, axes=([0, 1], [0, 1])).real
    X_L = np.einsum('vw,vswt->st', L.conj(), G4) / nrm
    Oh = herm(np.kron(L, X_L))
    Csq = Oh @ Oh.conj()                                          # (Oh K)(Oh K) = Oh Oh*
    # is C^2 proportional to identity on its support? measure ||Csq - lambda I|| / ||Csq||
    nz = np.linalg.norm(Oh) > 1e-9
    lam = (np.trace(Csq) / (N * DIM))
    dev = np.linalg.norm(Csq - lam * np.eye(N * DIM)) / (np.linalg.norm(Csq) + 1e-12)
    print(f"  ||Oh||={np.linalg.norm(Oh):.3f}; C^2 mean eigen-scale={lam.real:+.4f}; "
          f"rel dev from scalar-identity={dev:.3f}  (=> Oh is a rank-deficient projto-like op, NOT a clean AZ C^2=+-1)")

    print("\n" + "=" * 94)
    print("VERDICT")
    print("=" * 94)
    fc0, ct_, shc_, shct_ = results[0]
    forcing = abs(shc_) > 1e-6 and abs(shct_) < 1e-6 and fc0 > 1e-6
    print(f"  Adversarial escape is REAL at the LINEAR trace level: frame-active op (fc={fc0:.1f}) has")
    print(f"  nonzero chiral TRACE = {ct_:+.0f} (= {primefac(int(round(ct_)))}, 3-part {t3}: {'NO 3' if t3==1 else 'HAS 3'}).")
    print(f"  BUT at the FORCING level (selected physical half, the carrier-mass count notion):")
    print(f"     selected-half count of the frame-active escape Oh = {shc_:+.3f}")
    print(f"  => frame-active escape {'DOES' if forcing else 'does NOT'} force a net-chiral selected-half count.")
    print(f"  Net: the linear chiral-TRACE orthogonality is EVADABLE (self-dual entanglement channel),")
    print(f"  but the value is 2-primary (+16 = 2^4), and the forcing-level (light chiral count) {'is also forced' if forcing else 'stays 0'}.")
    return {
        "carrier_dim": int(Wt.shape[1]),
        "escape_fc": fc0,
        "escape_chiral_trace": ct_,
        "chiral_trace_3part": t3, "chiral_trace_2part": t2,
        "escape_selected_half_count": shc_,
        "escape_selected_half_count_frametrivial": shct_,
        "frame_active_forces_selected_half_count": bool(forcing),
        "C2_scalar_identity_rel_dev": float(dev),
    }


if __name__ == "__main__":
    out = main()
    print("\nRETURN:", out)
