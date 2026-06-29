#!/usr/bin/env python3
"""CAPSTONE -- the MASSIVE case: decoupling to ZERO, not three.

THE GATE (computed-on-substrate)
--------------------------------
The order-3 carrier Lambda^2_+ = the 192-dim j=1 generation triplet of ker(Gamma) inside V (x) S is
VECTORLIKE: Krein signature exactly (+96, -96), chirality split exactly (+96, -96), net chirality 0
(canon/source-action-seiberg-witten-RESULTS.md; tests/source-action/verify_C_seesaw.py). A vectorlike pair
has NO chiral protection, so it generically admits a DIRAC MASS term

        S_mass = m * (generation . mirror) + h.c.   ==>   D_m = [[ 0 , m B ],[ m B^dag , 0 ]]

a chirality-FLIPPING (Clifford-odd) operator connecting the 96 chirality-(+) generation modes to the 96
chirality-(-) mirror modes. This script TURNS ON that mass, sweeps m over many decades, and reports, as a
function of m:

  (1) the LIGHT-spectrum count below a fixed physical cutoff Lambda -- how many carrier modes stay light;
  (2) the NET CHIRALITY of the light (sub-cutoff) sector -- the chiral generation count that survives;
  (3) the kernel index ind = dim ker_+(D_m) - dim ker_-(D_m) -- the topologically protected chiral number.

THE CLAIM UNDER TEST
--------------------
  - MASSIVE (m > 0): the 96 (+) modes pair with the 96 (-) modes, every mode lifts to mass ~ m, and the
    number of net chiral generations massless below m is ZERO.  Massive does NOT give 3 -- it gives 0.
  - MASSLESS (m = 0): all 192 stay light, but net chirality is STILL 0 (= a located modulus, not 3 chiral).
  - To keep 3 LIGHT AND CHIRAL you would need an operator that breaks the +96/-96 balance (a chiral
    projection). The campaign proved the only such operator (the antilinear chiralizer C = J_quat . G) is
    FRAME-TRIVIAL (frame charge 0.00, selector-arena). This script does NOT supply such an operator; it
    confirms that without one, the carrier decouples to 0, not 3.

We test TWO Dirac masses to show the result is GENERIC, not an artifact of one choice:
  (A) a substrate Dirac leg: the chirality-flip block of c(e_a) compressed to the triplet (Clifford-odd,
      exactly the shiab-type Dirac mass), and
  (B) a generic full-rank random Krein-Hermitian flip block (the "generic mass term").

Self-contained substrate builder copied from tests/source-action/verify_C_seesaw.py (verified: (9,5),
ker(Gamma) Casimir split, j=1 triplet 192-dim, Krein (+96,-96)). Only running code decides.
"""
from __future__ import annotations

import json
import numpy as np

N, DIM = 14, 128
TOL = 1e-7
TIMELIKE = {4, 5, 6, 7, 8}
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]


# ----------------------------------------------------------------- substrate (copied, verified)
def jw(n):
    I = np.eye(2, dtype=complex)
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    G = []
    for k in range(n):
        L, R = [s3] * k, [I] * (n - 1 - k)
        for mid in (s1, s2):
            o = np.array([[1 + 0j]])
            for m in L + [mid] + R:
                o = np.kron(o, m)
            G.append(o)
    return G


def sgen(e, i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex)
    M[i, j] = 1
    M[j, i] = -1
    return M


def build_substrate(timelike=TIMELIKE):
    base = jw(7)
    I128, I14 = np.eye(DIM, dtype=complex), np.eye(N, dtype=complex)
    e = [(1j * base[a] if a in timelike else base[a]) for a in range(N)]
    spacelike = [a for a in range(N) if a not in timelike]

    Gamma = np.hstack(e)
    Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
    Jfull = [np.kron(I14, sgen(e, a, b) + sgen(e, c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
             for (a, b, c, d) in SD]
    Sig = [sgen(e, a, b) + sgen(e, c, d) for (a, b, c, d) in SD]
    w, Vv = np.linalg.eigh(Pi)
    Wker = Vv[:, w > 0.5]
    Cas = -(Jfull[0] @ Jfull[0] + Jfull[1] @ Jfull[1] + Jfull[2] @ Jfull[2])
    CasK = Wker.conj().T @ Cas @ Wker
    CasK = 0.5 * (CasK + CasK.conj().T)
    cev, cU = np.linalg.eigh(CasK)
    Wt = Wker @ cU[:, np.abs(cev - 8.0) < 1e-3]                       # 1792 x 192  (j=1 triplet)

    bS = I128.copy()
    for s in spacelike:
        bS = bS @ e[s]
    if np.linalg.norm(bS.conj().T + bS) < 1e-9:
        bS = 1j * bS
    bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
    etaV = np.diag([(-1.0 if a in timelike else 1.0) for a in range(N)]).astype(complex)
    K = np.kron(etaV, bS)

    om = I128.copy()
    for a in range(N):
        om = om @ e[a]
    om2 = (np.trace(om @ om) / DIM).real
    chir14 = np.kron(I14, om if om2 > 0 else (-1j) * om)
    return e, K, Jfull, Sig, Wt, chir14


def net_chirality(P, chir_tr):
    """net chirality (n_+ - n_-) carried by the column space of P, w.r.t. omega_14."""
    if P.shape[1] == 0:
        return 0, 0, 0
    c = 0.5 * (P.conj().T @ chir_tr @ P + (P.conj().T @ chir_tr @ P).conj().T)
    ce = np.linalg.eigvalsh(c)
    npos = int((ce > 0.5).sum())
    nneg = int((ce < -0.5).sum())
    return npos, nneg, npos - nneg


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=120)
    out = {}
    print("=" * 94)
    print("CAPSTONE -- the MASSIVE case: a carrier Dirac mass decouples to ZERO light chiral, not three")
    print("=" * 94)

    e, K, Jfull, Sig, Wt, chir14 = build_substrate()
    d = Wt.shape[1]

    # chirality projectors on the triplet
    chir_tr = 0.5 * (Wt.conj().T @ chir14 @ Wt + (Wt.conj().T @ chir14 @ Wt).conj().T)
    ev14, U14 = np.linalg.eigh(chir_tr)
    Pp, Pm = U14[:, ev14 > 0.5], U14[:, ev14 < -0.5]
    nplus, nminus = Pp.shape[1], Pm.shape[1]

    # Krein form on the triplet (for the signature readout)
    Kr = 0.5 * (Wt.conj().T @ K @ Wt + (Wt.conj().T @ K @ Wt).conj().T)
    ksig = np.linalg.eigvalsh(Kr)
    kpos, kneg = int((ksig > 1e-9).sum()), int((ksig < -1e-9).sum())

    print(f"carrier dim                = {d}   (expected 192, the j=1 generation triplet)")
    print(f"chirality split (omega_14) = (+{nplus}, -{nminus})   net chirality = {nplus - nminus}")
    print(f"Krein signature            = (+{kpos}, -{kneg})   net = {kpos - kneg}")
    print(f"  => VECTORLIKE: equal +/-, no chiral protection, Dirac mass is symmetry-ALLOWED.")
    out["carrier_dim"] = d
    out["chirality_split"] = [nplus, nminus]
    out["chirality_net"] = nplus - nminus
    out["krein_signature"] = [kpos, kneg]

    # ------------------------------------------------------------------ build two Dirac masses
    # (A) substrate Dirac leg: chirality-flip block of c(e_a), Clifford-odd (the shiab-type Dirac mass).
    I14 = np.eye(N, dtype=complex)
    best_a, best_flip, BA = None, -1.0, None
    for a in [0, 1, 2, 3, 9, 12]:
        Bsub = Wt.conj().T @ np.kron(I14, e[a]) @ Wt
        Bsub = 0.5 * (Bsub + Bsub.conj().T)
        Bflip = Pp.conj().T @ Bsub @ Pm           # 96 x 96 chirality-flip block
        fn = float(np.linalg.norm(Bflip))
        if fn > best_flip:
            best_a, best_flip, BA = a, fn, Bflip
    # normalize to operator norm 1 so "m" is the literal mass scale
    BA = BA / np.linalg.svd(BA, compute_uv=False)[0]
    rankA = int(np.linalg.matrix_rank(BA, tol=TOL))
    sA = np.linalg.svd(BA, compute_uv=False)

    # (B) generic full-rank random flip block (the generic mass term)
    rng = np.random.default_rng(0)
    BB = rng.standard_normal((nplus, nminus)) + 1j * rng.standard_normal((nplus, nminus))
    BB = BB / np.linalg.svd(BB, compute_uv=False)[0]
    rankB = int(np.linalg.matrix_rank(BB, tol=TOL))
    sB = np.linalg.svd(BB, compute_uv=False)

    print(f"\nDirac mass (A) substrate leg c(e{best_a}) flip block: shape {BA.shape}, rank {rankA}, "
          f"sigma in [{sA.min():.3f}, {sA.max():.3f}]")
    print(f"Dirac mass (B) generic random flip block          : shape {BB.shape}, rank {rankB}, "
          f"sigma in [{sB.min():.3f}, {sB.max():.3f}]")
    out["diracA_gamma"] = best_a
    out["diracA_rank"] = rankA
    out["diracB_rank"] = rankB

    # The mass operator D_m = [[0, m B],[m B^dag, 0]]; its eigenvalues are {+/- m sigma_i(B)}.
    # number massless (zero modes) = total - 2*rank(B) ; net chirality of kernel = index.
    def sweep(B, label):
        rank = int(np.linalg.matrix_rank(B, tol=TOL))
        s = np.linalg.svd(B, compute_uv=False)
        # build the fold once symbolically; eigenvalues scale linearly with m, so just scale sigma.
        # kernel: zero modes. On chirality (+) side: dim ker of B (cols), on (-) side: dim ker of B^dag.
        ker_plus = nplus - rank        # uncoupled (+) modes (always massless)
        ker_minus = nminus - rank      # uncoupled (-) modes (always massless)
        idx = ker_plus - ker_minus     # net chiral index of the protected massless kernel
        print("\n" + "-" * 94)
        print(f"SWEEP, Dirac mass {label}:  D_m = [[0, m B],[m B^dag, 0]],  rank(B) = {rank}")
        print("-" * 94)
        print(f"  fixed cutoff Lambda = {LAM};  total carrier modes = {2 * rank + ker_plus + ker_minus}")
        print(f"  {'m':>10} | {'#light(<L)':>10} | {'#massive':>9} | {'net chir(light)':>15} | "
              f"{'kernel index':>12}")
        rows = []
        for m in MS:
            eig = np.concatenate([m * s, -m * s,
                                  np.zeros(ker_plus + ker_minus)])
            light = int((np.abs(eig) < LAM).sum())
            massive = int((np.abs(eig) >= LAM).sum())
            # net chirality of the light (sub-cutoff) sector:
            # the protected massless kernel contributes idx; the light part of the massive ladder is
            # chirality-balanced (each pair {+,-} shares one (+) and one (-) mode). So net chiral(light)=idx
            # whenever m>0 lifts all coupled modes above cutoff, else = full net = 0.
            if m == 0.0:
                net_light = nplus - nminus      # everything light: net = 0 (vectorlike)
            else:
                # coupled modes with m*sigma < Lambda are still light but come in balanced +/- pairs
                net_light = idx                 # only the uncoupled kernel is unbalanced -> = idx
            rows.append((m, light, massive, net_light, idx))
            print(f"  {m:10.2e} | {light:10d} | {massive:9d} | {net_light:15d} | {idx:12d}")
        return {"rank": rank, "ker_plus": ker_plus, "ker_minus": ker_minus,
                "index": idx, "rows": [list(r) for r in rows]}

    out["sweepA"] = sweep(BA, f"(A) substrate c(e{best_a})")
    out["sweepB"] = sweep(BB, "(B) generic random")

    # ------------------------------------------------------------------ explicit-fold confirmation
    # Re-confirm the m>0 count by actually diagonalizing the full 192x192 fold at one representative m,
    # rather than trusting the singular-value shortcut.
    print("\n" + "-" * 94)
    print("EXPLICIT FOLD CHECK (diagonalize the full 192x192 D_m; no singular-value shortcut)")
    print("-" * 94)
    for label, B in [("A", BA), ("B", BB)]:
        D = np.zeros((d, d), dtype=complex)
        D[:nplus, nplus:] = B
        D[nplus:, :nplus] = B.conj().T
        for mtest in [0.0, 1e-3, 1e-1, 1e3]:
            Dm = mtest * D
            ev = np.linalg.eigvalsh(0.5 * (Dm + Dm.conj().T))
            light = int((np.abs(ev) < LAM).sum())
            # net chirality of the light eigenspace, measured directly via omega_14
            light_vecs = np.linalg.eigh(0.5 * (Dm + Dm.conj().T))[1][:, np.abs(ev) < LAM]
            npos, nneg, netc = net_chirality(light_vecs, chir_tr)
            print(f"  mass {label}, m={mtest:8.1e}: #light(<{LAM})={light:3d}  "
                  f"light chirality (+{npos},-{nneg}) net={netc}")

    print("\n" + "=" * 94)
    print("VERDICT")
    print("=" * 94)
    iA, iB = out["sweepA"]["index"], out["sweepB"]["index"]
    print(f"  - carrier is vectorlike (+{nplus},-{nminus}); Dirac mass symmetry-ALLOWED (no protection).")
    print(f"  - m = 0 : all {d} modes light, net chirality 0  -> a LOCATED modulus, NOT 3.")
    print(f"  - m > 0 : all coupled modes lift to mass ~ m and DECOUPLE above m; light net chirality")
    print(f"            = kernel index = {iA} (substrate leg) / {iB} (generic) -- ZERO, not 3.")
    print(f"  - To force 3 light AND chiral you must break the +{nplus}/-{nminus} balance (a chiral")
    print(f"    projection). The only such operator (C = J_quat . G) is frame-trivial (charge 0.00).")
    print(f"  => MASSIVE decouples to 0 light chiral generations; MASSLESS leaves a 0-net-chiral modulus.")
    print(f"     NEITHER yields 3. Located-not-forced, re-confirmed on the substrate.")
    print("=" * 94)

    out["verdict"] = {
        "massless_light": d, "massless_net_chirality": nplus - nminus,
        "massive_light_net_chirality_A": iA, "massive_light_net_chirality_B": iB,
        "forces_three": False,
    }
    with open("tests/carrier-mass/decoupling_results.json", "w") as f:
        json.dump(out, f, indent=2)
    return out


# fixed physical cutoff and mass sweep (decades around the cutoff)
LAM = 1e-2
MS = [0.0, 1e-6, 1e-4, 1e-2, 1e-1, 1.0, 1e2, 1e6]

if __name__ == "__main__":
    main()
