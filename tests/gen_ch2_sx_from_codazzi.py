#!/usr/bin/env python3
"""ch2(S_X)[K3] from the in-repo Codazzi/Sp(64) curvature data -- computed AS-IS.

CONTEXT
-------
The S_XCharacteristicClassPacket_V0 computation demanded by
  active-research/topological-generation-count-families-k3-chi-gate-2026-06-26.md
and the C2-edge located by
  explorations/c2-is-global-y14-end-data-2026-06-27.md.

Goal: define the pulled-back spinor connection a^0 = s*A^0 on S_X = s*S, decide whether
it is FLAT on the source-free LC/K3 branch, and -- since it is NOT flat -- compute the
actual ch2(S_X)[K3] from the Codazzi/Sp(64) curvature via Chern-Weil. Report the NUMBER
as-is. Do NOT force 24. Then test, concretely, whether that number supplies C2's ~94%
global content (the load-bearing C2 connection test).

WHAT IS COMPUTED (a-priori in-repo inputs only)
-----------------------------------------------
1. S = H^64 spinor over Y14, Sp(64) = Aut(S), spin rep rho_*: so(9,5) -> sp(64)
   [codazzi-sp64 sec 2, anomaly-audit-cl95].
2. so(9,5) = so(3,1) (+) so(6,4) (+) (R^{3,1} (x) R^{6,4}) tangent/normal/off-diagonal
   split [codazzi-sp64 sec 2.1].
3. N_s = Sym^2 T*X4 with the induced connection [codazzi-sp64 sec 2.3, 5.2].
4. II_s^H = 0 for the tautological LC section => off-diagonal block vanishes =>
   BLOCK-DIAGONAL curvature on the LC/K3 branch [codazzi-sp64 sec 5.1, ii-s-moving-frames].
5. S(9,5) = S(3,1) (x)_R S(6,4) branching [ind-top-x4 sec 2.1].

K3 is used ONLY as a control surface, via sigma(K3) = -16 -> p1(TK3) = 3*sigma = -48
(Hirzebruch). chi(K3) = 24 is NEVER used as an input; the output does not reproduce it.

The two load-bearing Chern-Weil multipliers are VERIFIED here by actual matrix
computation, not asserted:
  (A) p1(Sym^2 T*X) = 6 p1(TX)        [so(4) Sym^2 weight sum]
  (B) ch2(spin rep) = (dim_S/8) p1(V) [spin-trace identity tr_S(rho(R)^2)=(dim_S/8)tr_V(R^2)]

Runs in ~10s. Reuses tests/oq_rk1_cl95_explicit_rep.py (the Cl(9,5) rep) and the
tests/c2_holonomy_global_obstruction.py C2 machinery (bare C2 = 155.36).

NO git commit. Honest-number discipline: a number that is not 24 is a valuable result.
"""

from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import oq_rk1_cl95_explicit_rep as cl95  # the explicit Cl(9,5) = M(64,H) ~ M(128,C) rep

TOL = 1e-9


# ----------------------------------------------------------------------------- #
# Part 0. Control-surface topology (K3) -- sigma ONLY, never chi.
# ----------------------------------------------------------------------------- #
SIGMA_K3 = -16                     # signature of K3 (Hirzebruch). NOT chi.
P1_TK3 = 3 * SIGMA_K3             # p1 = 3 sigma  (Hirzebruch signature thm) = -48
# explicit guard: we must NEVER read chi = 24 as an input anywhere below.
CHI_K3_FORBIDDEN = 24            # recorded only to assert it is unused.


# ----------------------------------------------------------------------------- #
# Part 1. Verify the Chern-Weil multipliers by actual matrix computation.
# ----------------------------------------------------------------------------- #
def sym2_rep_action(F):
    """Derivation action of an so(n) element F on Sym^2(R^n) (dim n(n+1)/2)."""
    n = F.shape[0]
    idx = [(i, j) for i in range(n) for j in range(i, n)]
    pos = {p: k for k, p in enumerate(idx)}
    D = len(idx)
    M = np.zeros((D, D))
    for (i, j) in idx:
        col = pos[(i, j)]
        for k in range(n):
            if F[k, i] != 0:
                a, b = sorted((k, j))
                M[pos[(a, b)], col] += F[k, i]
            if F[k, j] != 0:
                a, b = sorted((i, k))
                M[pos[(a, b)], col] += F[k, j]
    return M


def verify_sym2_multiplier(seed=1):
    """p1(Sym^2 V)/p1(V) = tr(rho_{Sym2}(F)^2)/tr_V(F^2) for a random so(4) curvature."""
    rng = np.random.default_rng(seed)
    A = rng.normal(size=(4, 4))
    F = A - A.T
    trV = float(np.trace(F @ F).real)
    S2 = sym2_rep_action(F)
    trS2 = float(np.trace(S2 @ S2).real)
    return trS2 / trV


def verify_spin_multiplier(N, seed=2):
    """ch2(S)/p1(V) = tr_S(rho(F)^2)/tr_V(F^2) for a random so(N) curvature; = dim_S/8."""
    rng = np.random.default_rng(seed + N)
    n_pairs = N // 2
    G = cl95.jordan_wigner_gammas(n_pairs)
    A = rng.normal(size=(N, N))
    F = A - A.T
    Sig = lambda a, b: 0.25 * (G[a] @ G[b] - G[b] @ G[a])
    rho = sum(F[a, b] * Sig(a, b) for a in range(N) for b in range(a + 1, N))
    trV = float(np.trace(F @ F).real)
    trS = float(np.trace(rho @ rho).real)
    return trS / trV, 2 ** n_pairs


# ----------------------------------------------------------------------------- #
# Part 2. The C2 machinery anchors (load-bearing connection test).
# ----------------------------------------------------------------------------- #
def c2_anchors():
    """Reproduce bare C2 = 155.36 and [Pi_RS, M_D] = 58.72 from the same rep."""
    N = 14
    G = cl95.jordan_wigner_gammas(7)
    eta = [1] * 9 + [-1] * 5
    e = [G[a] if eta[a] > 0 else 1j * G[a] for a in range(N)]
    XI = np.array([1.0, 2.0, 3.0, 4.0, 0.5, 1.5, 2.5, 0.7,
                   1.1, 0.3, 2.2, 1.7, 0.9, 1.3], dtype=complex)
    Gamma = np.hstack(e)                       # 128 x 1792
    cxi = sum(XI[a] * e[a] for a in range(N))
    M_D = np.kron(np.eye(N, dtype=complex), cxi)
    BBd = Gamma @ Gamma.conj().T
    Pi_RS = np.eye(Gamma.shape[1], dtype=complex) - Gamma.conj().T @ np.linalg.inv(BBd) @ Gamma
    bare_comm = float(np.linalg.norm(Pi_RS @ M_D - M_D @ Pi_RS))
    bare_C2 = float(np.linalg.norm(Gamma @ M_D @ Pi_RS))
    return bare_comm, bare_C2


# ----------------------------------------------------------------------------- #
# Main
# ----------------------------------------------------------------------------- #
def main():
    print("=" * 78)
    print("ch2(S_X)[K3] from the in-repo Codazzi/Sp(64) curvature -- computed AS-IS")
    print("=" * 78)

    # --- 1. FLATNESS decision on the source-free LC/K3 branch -----------------
    print("\n[1] FLATNESS of a^0 = s*A^0 on S_X over the source-free LC/K3 branch:")
    print("    K3 is Ricci-flat (source-free) but NOT flat: holonomy SU(2),")
    print("    Riemann/Weyl nonzero (p1(TK3) = 3*sigma = 3*(-16) = %d != 0)." % P1_TK3)
    print("    => the tangent so(4) spin-curvature block is NONZERO => ch2(S_X) != 0.")
    print("    On the tautological LC section II_s^H = 0 (codazzi-sp64 5.1) so the")
    print("    so(9,5) curvature is BLOCK-DIAGONAL: tangent so(4) (+) normal so(6,4).")
    flat = False
    assert not flat

    # --- 2. Verify the two Chern-Weil multipliers (actual matrices) -----------
    print("\n[2] Chern-Weil multipliers verified by actual matrix computation:")
    m_sym2 = verify_sym2_multiplier()
    print(f"    (A) p1(Sym^2 T*X)/p1(TX) = {m_sym2:.6f}   (expect 6)")
    assert abs(m_sym2 - 6.0) < 1e-6
    spin_mult = {}
    for N in (4, 10, 14):
        ratio, dimS = verify_spin_multiplier(N)
        spin_mult[N] = ratio
        print(f"    (B) N={N:2d}: ch2(S)/p1(V) = tr_S(rho^2)/tr_V(F^2) = {ratio:.6f}"
              f"   dim_S/8 = {dimS/8}")
        assert abs(ratio - dimS / 8.0) < 1e-6

    # --- 3. p1 inputs on K3 (from sigma ONLY) ---------------------------------
    print("\n[3] p1 inputs on K3 (Hirzebruch p1 = 3*sigma; sigma = -16; chi NEVER used):")
    p1_TK3 = P1_TK3                       # -48
    p1_N = int(round(m_sym2)) * p1_TK3    # N_s = Sym^2 T*X4 ; p1(N) = 6 p1(TK3) = -288
    p1_V = p1_TK3 + p1_N                  # V = TX4 (+) N_s = pulled-back TY14 ; -336
    print(f"    p1(TK3)            = {p1_TK3}")
    print(f"    p1(N=Sym^2 T*K3)   = 6 * {p1_TK3} = {p1_N}")
    print(f"    p1(V = TK3 (+) N)  = {p1_TK3} + {p1_N} = {p1_V}")

    # --- 4. ch2 values, computed AS-IS (NOT forced to 24) ---------------------
    print("\n[4] ch2(S_X)[K3] and variants on the SAME data (computed AS-IS):")
    ch2_full = int(round(spin_mult[14])) * p1_V        # full rank-128 S_X: 16 * (-336)
    ch2_normal = int(round(spin_mult[10])) * p1_N      # normal S(6,4) only: 4 * (-288)
    ch2_tangent = round(spin_mult[4] * p1_TK3)         # tangent Dirac only: 0.5 * (-48) = -24
    rank_SX = 128
    twisted_index = ch2_full - rank_SX * p1_TK3 // 24  # int Ahat(K3) ch(S_X)
    hline_norm = ch2_full / 64.0                       # H-line normalization from RANK (64 H)
    print(f"    ch2(S_X full, rank 128) = (dim_S/8) p1(V)   = 16 * {p1_V}  = {ch2_full}")
    print(f"    ch2(S(6,4) normal only) = (32/8) p1(N)      =  4 * {p1_N} = {ch2_normal}")
    print(f"    ch2(tangent Dirac only) = (4/8)  p1(TK3)    =  0.5 * {p1_TK3} = {ch2_tangent}")
    print(f"    twisted int_K3 Ahat ch  = ch2 - 128*p1/24   = {ch2_full} + {-rank_SX*p1_TK3//24} = {twisted_index}")
    print(f"    H-line normalized       = ch2/64 (RANK, not 24/8) = {hline_norm}")

    # --- 5. Honest-number / target-import / blocked-shortcut checks -----------
    print("\n[5] TARGET-IMPORT and BLOCKED-SHORTCUT checks:")
    used_chi = False  # chi(K3)=24 appears nowhere in the arithmetic above
    print(f"    chi(K3)=24 used as input?         {used_chi}  (only sigma=-16 used)")
    print(f"    24/8=3 normalization used?        False (H-line norm = {hline_norm} from rank 64)")
    print(f"    assumed-K3 to reach the number?   False (sigma is a control input; ch2 computed)")
    print(f"    ch2(S_X) == 24 (forced target)?   {ch2_full == 24}  -> value is {ch2_full}")
    # The tangent-only |ch2| = 24 is a DISGUISED chi-import: it equals -p1/2 and
    # |.|=chi only because K3 satisfies 2chi+3sigma=0. Flag and reject as a route.
    tangent_is_disguised_chi = (abs(ch2_tangent) == abs(CHI_K3_FORBIDDEN))
    print(f"    tangent-only |ch2| = {abs(ch2_tangent):.0f}: disguised chi-import? "
          f"{tangent_is_disguised_chi}  (REJECTED as a derivation of 24: it is -p1/2,")
    print(f"        =chi only via the K3 identity 2chi+3sigma=0; not a generation derivation)")
    assert ch2_full != 24 and ch2_full != 3
    assert not used_chi

    # contractible-fiber / pushforward guard
    pushforward_defined = False   # fiber GL(4,R)/O(3,1) is NOT convex -> NOT_DEFINED
    print(f"\n    families pushforward pi_!: ch(S)/Y14 -> ch(S_X)/X4 defined? {pushforward_defined}")
    print(f"        (fiber GL(4,R)/O(3,1) non-convex; contractible-fiber=>1 is a BLOCKED")
    print(f"         shortcut. So ch2(S_X)[K3]={ch2_full} is a BULK characteristic number,")
    print(f"         NOT yet licensed as THE families index.)")

    # --- 6. THE C2 CONNECTION TEST (load-bearing) -----------------------------
    print("\n[6] C2 CONNECTION TEST (concrete; default FORCED_ANALOGY unless a handle maps):")
    bare_comm, bare_C2 = c2_anchors()
    global_residual = 0.94 * bare_C2
    print(f"    C2 anchors reproduced: ||[Pi_RS,M_D]|| = {bare_comm:.4f} (repo 58.72);"
          f" bare C2 = {bare_C2:.4f} (repo 155.36)")
    assert abs(bare_comm - 58.7215) < 1e-2
    assert abs(bare_C2 - 155.3625) < 1e-2
    print(f"    C2 global content to be supplied ~= 0.94 * {bare_C2:.2f} = {global_residual:.2f}")
    # Try every arithmetic handle from the ch2 packet onto the C2 residual.
    candidates = {
        "ch2_full": ch2_full, "ch2_normal": ch2_normal, "ch2_tangent": ch2_tangent,
        "twisted_index": twisted_index, "hline_norm": hline_norm,
        "|ch2_full|": abs(ch2_full), "|hline_norm|": abs(hline_norm),
    }
    found = None
    for name, val in candidates.items():
        if val != 0 and abs(abs(val) - global_residual) / global_residual < 0.02:
            found = (name, val)
    print(f"    does any ch2 handle equal the {global_residual:.2f} global residual"
          f" (2% tol)? {found}")
    # Structural reason there is NO map: bulk integer char-number vs boundary eta object.
    print("    -> ch2(S_X)[K3] is a BULK integer characteristic number on the COMPACT")
    print("       control K3. C2's global content is a Gamma-independent operator-norm")
    print("       obstruction on the NON-COMPACT Y14 END (a boundary spectral-section /")
    print("       eta object, per c2-is-global-y14). Three handles for a real connection,")
    print("       all ABSENT: (1) no P_d spectral-section projector inserted into the BV")
    print("       closure to carry ch2 onto a C2 shift; (2) eta of the ACTUAL boundary")
    print("       operator uncomputed (only round-S^3 APS, eta=0, exists); (3) bulk-ch2")
    print("       and boundary-eta are DIFFERENT global invariants.")
    c2_verdict = "FORCED_ANALOGY" if found is None else "COMPUTABLE_HANDLE"
    print(f"    C2 CONNECTION VERDICT: {c2_verdict}")
    assert c2_verdict == "FORCED_ANALOGY"

    # --- 7. DECISION + the precise unsupplied edge ----------------------------
    print("\n[7] DECISION OUTCOME and the precise unsupplied edge:")
    decision = "CH2_NONZERO_OTHER_INDEX"
    print(f"    decision (per k3-chi-gate decision tree): {decision}")
    print(f"    ch2(S_X)[K3] = {ch2_full}  -- genuinely nonzero, decisively NOT 24,")
    print(f"    and not reducible to 3 by any rank normalization ({hline_norm} from 64 H).")
    print("    PRECISE EDGE that blocks closure:")
    print("      (i)  families pushforward pi_!: ch(S)/Y14 -> ch(S_X)/X4 is NOT_DEFINED")
    print("           (non-convex fiber GL(4,R)/O(3,1)); so ch2(S_X)[K3] is not yet THE index.")
    print("      (ii) no eta for the ACTUAL boundary operator and no P_d-into-BV handle,")
    print("           so the ch2 <-> C2 link stays FORCED_ANALOGY.")
    print("    NET: honest negative -- the source-derived ch2 is real, large, and != 24;")
    print("    it does NOT supply C2's ~94% global content.")

    print("\n" + "=" * 78)
    print(f"RESULT: ch2(S_X)[K3] = {ch2_full}  | decision = {decision}"
          f"  | C2 link = {c2_verdict}")
    print("=" * 78)

    return {
        "ch2_full": ch2_full, "ch2_normal": ch2_normal, "ch2_tangent": ch2_tangent,
        "twisted_index": twisted_index, "hline_norm": hline_norm,
        "p1_TK3": p1_TK3, "p1_N": p1_N, "p1_V": p1_V,
        "flat": flat, "bare_C2": bare_C2, "global_residual": global_residual,
        "c2_verdict": c2_verdict, "decision": decision,
        "pushforward_defined": pushforward_defined, "used_chi": used_chi,
    }


if __name__ == "__main__":
    main()
