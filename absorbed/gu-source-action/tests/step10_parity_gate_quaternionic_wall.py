#!/usr/bin/env python3
"""STEP 10 / CONSTRUCT-06 - the PARITY GATE, corrected: the wall is UNDER-DETERMINATION, not impossibility.

The 113-persona Hegelian pass collapsed the search to one reframed invariant - quaternionic-linearity
(commuting with the phase-unique J_quat of M(64,H)) - and nominated a J-antilinear carrier as the only
escape to an ODD generation index. A first draft of this step claimed a UNIVERSAL parity wall ("no
a-priori carrier reaches an odd index"). Adversarial verification REFUTED that universal with a one-line
counterexample, and this corrected step records the honest, narrower, verified truth.

Carriers Delta = herm(Pi M Pi + Q M Q) [G-diagonal Hermitian, a-priori]. Split by J_quat via
S(Delta) = J_quat.Delta.J_quat^{-1}. Three classes, each VERIFIED here:

  (1) J-LINEAR carriers (S=+Delta) -- the PHYSICAL gauge/spin/metric-connection class (every connection
      in C-05 lives here): index forced EVEN by quaternionic Kramers, AT ALL RANKS. Concretely the
      J-linear projection of a rank-r object gives sig = 2r (it DOUBLES): jlin(rank-1)->2, rank-3->6,
      rank-5->10. This is the genuine, real wall, and it is exactly the physically-intended class.
  (2) J-ANTILINEAR carriers (S=-Delta): index IDENTICALLY 0, non-vacuous (||Delta|| ~ 1180). The one
      nominated escape gives zero (antiunitary conjugation forces an exactly +/- symmetric spectrum).
  (3) GENERIC / LOW-RANK carriers (no J-linearity imposed): NO parity protection. A rank-r positive
      kernel carrier gives sig = r EXACTLY -- so rank-1->1, rank-3->3, rank-5->5: ODD indices, INCLUDING
      3, ARE REACHABLE. (The first draft's "even only" was an artifact of sampling full-rank random
      carriers, whose signature is trivially even.)

CORRECTED VERDICT. "3" is NOT parity-forbidden and NOT impossible: a rank-3 a-priori carrier gives
index 3 directly. The genuine obstruction is UNDER-DETERMINATION: the rep does not FORCE the rank/index
to be 3 -- choosing rank 3 is a free choice = the forbidden import. Two real sub-walls survive: physical
CONNECTIONS are forced even (so the natural gauge/spin objects cannot give an odd 3), and the pure
J-antilinear class gives 0. But the index over all a-priori carriers is FREE. So the campaign's true
statement is not "GU cannot produce 3" but "GU under-determines the count; nothing internal forces 3;
an honest 3 requires a CANONICAL selector (the unbuilt S_IG membrane) that pins the rank/index a-priori
without choosing it." This is weaker than WALL-PERMANENT and is the precise, honest standing.

Guards: M_D / bare commutator untouched; carriers a-priori; J_quat is the phase-unique structure (step9).
Run: python tests/step10_parity_gate_quaternionic_wall.py
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from lib import gu_bridge  # noqa: E402

N, DIM = gu_bridge.N, gu_bridge.DIM
ETA = np.array([1.0] * 9 + [-1.0] * 5)


def quaternionic_J(e128, seed=1):
    def Phi(U):
        out = np.zeros_like(U)
        for a in range(N):
            out += ETA[a] * (e128[a] @ U @ e128[a].conj())
        return out / N
    rng = np.random.default_rng(seed)
    U = rng.standard_normal((DIM, DIM)) + 1j * rng.standard_normal((DIM, DIM))
    for _ in range(400):
        U = 0.5 * (U + Phi(U))
        U /= np.linalg.norm(U)
    Us, _, Vs = np.linalg.svd(U)
    U = Us @ Vs
    return U / np.sqrt(abs(np.trace(U @ U.conj()) / DIM))


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=170)
    e, Gamma, Pi, M_D = gu_bridge.constraint_objects()
    Q = np.eye(N * DIM, dtype=complex) - Pi
    e128 = gu_bridge.gammas()
    bare = float(np.linalg.norm(Pi @ M_D - M_D @ Pi))
    C2 = float(np.linalg.norm(Gamma @ M_D @ Pi))
    print(f"[anchors] bare={bare:.4f} (58.7215)  C2={C2:.4f} (155.3625)")
    assert abs(bare - 58.7215) < 1e-2 and abs(C2 - 155.3625) < 1e-2

    U = quaternionic_J(e128, seed=1)
    Uf = np.kron(np.eye(N), U)
    Ufi = np.linalg.inv(Uf)

    def sig(A):
        ev = np.linalg.eigvalsh(0.5 * (A + A.conj().T))
        tol = 1e-7 * np.abs(ev).max()
        return int((ev > tol).sum()) - int((ev < -tol).sum())

    def gd(X):
        return Pi @ X @ Pi + Q @ X @ Q

    def herm(X):
        return 0.5 * (X + X.conj().T)

    def Sop(X):
        return Uf @ X.conj() @ Ufi

    def jlin(X):
        return 0.5 * (X + Sop(X))

    def janti(X):
        return 0.5 * (X - Sop(X))

    # orthonormal basis of ker(Gamma) (the constraint surface) for low-rank carriers
    w, V = np.linalg.eigh(Pi)
    Wk = V[:, w > 0.5]                            # 1792 x 1664

    # ---- (3) LOW-RANK generic carriers: sig = r, ODD reachable (the counterexample) ----
    rng = np.random.default_rng(5)
    print("\n=== (3) generic low-rank a-priori carriers (kernel PSD projectors): sig = r ===")
    lowrank = {}
    for r in [1, 2, 3, 5]:
        cols = rng.choice(Wk.shape[1], r, replace=False)
        Wr = Wk[:, cols]
        M = Wr @ Wr.conj().T                      # rank-r PSD, supported in ker(Gamma)
        D = herm(gd(M))
        s = sig(D)
        lowrank[r] = s
        print(f"  rank-{r}: sig = {s}   (gd-fixed resid {np.linalg.norm(gd(M) - M):.0e})  "
              f"{'<-- ODD, and 3 IS REACHABLE' if r == 3 else ''}")

    # ---- (1) J-LINEAR (physical connection) carriers: forced EVEN (doubling: 2r) ----
    print("\n=== (1) J-linear (physical connection) carriers: forced EVEN by Kramers (sig = 2r) ===")
    jlin_sig = {}
    for r in [1, 3, 5]:
        cols = rng.choice(Wk.shape[1], r, replace=False)
        Wr = Wk[:, cols]
        D = herm(gd(jlin(Wr @ Wr.conj().T)))
        jlin_sig[r] = sig(D)
        print(f"  jlin(rank-{r}): sig = {sig(D)}   (= 2r, EVEN)")
    # plus full-rank J-linear stay on the 4Z ladder (matches C-03)
    jl_full = []
    for _ in range(4):
        R = rng.standard_normal((N * DIM, N * DIM)) + 1j * rng.standard_normal((N * DIM, N * DIM))
        jl_full.append(sig(herm(gd(jlin(R)))))
    print(f"  full-rank J-linear sig = {sorted(jl_full)} (4Z)")

    # ---- (2) J-ANTILINEAR carriers: identically 0, non-vacuous ----
    print("\n=== (2) J-antilinear carriers: identically 0 (non-vacuous) ===")
    anti_sig, anti_nrm = [], []
    for _ in range(4):
        R = rng.standard_normal((N * DIM, N * DIM)) + 1j * rng.standard_normal((N * DIM, N * DIM))
        Da = herm(gd(janti(R)))
        anti_sig.append(sig(Da)); anti_nrm.append(float(np.linalg.norm(Da)))
    print(f"  sig = {anti_sig}  ||Delta|| ~ {np.mean(anti_nrm):.0f} (non-vacuous)")

    # ---- VERDICT ----
    odd_reachable = (lowrank[3] == 3)
    jlinear_even = all(s % 2 == 0 for s in list(jlin_sig.values()) + jl_full)
    antilinear_zero = all(s == 0 for s in anti_sig) and np.mean(anti_nrm) > 1.0
    print("\n=== VERDICT (corrected) ===")
    print(f"3 IS REACHABLE by a rank-3 a-priori carrier (sig=3)?       {odd_reachable}")
    print(f"physical J-linear (connection) carriers forced EVEN?        {jlinear_even}")
    print(f"pure J-antilinear carriers give 0 (non-vacuous)?            {antilinear_zero}")
    print("\nReading: '3' is NOT impossible -- a rank-3 carrier gives index 3 directly. The genuine")
    print("obstruction is UNDER-DETERMINATION: nothing in the rep FORCES the rank/index to be 3;")
    print("choosing rank 3 is the forbidden import. Two real sub-walls survive (physical connections")
    print("are forced even; pure J-antilinear gives 0), but the index over a-priori carriers is FREE.")
    print("Honest standing: not 'GU cannot produce 3', but 'GU under-determines the count; an honest 3")
    print("requires a CANONICAL selector (the unbuilt S_IG membrane) that pins the rank a-priori.'")

    assert abs(bare - 58.7215) < 1e-2 and abs(C2 - 155.3625) < 1e-2, "anchors moved"
    assert odd_reachable, "a rank-3 a-priori carrier must give index 3 (odd IS reachable)"
    assert all(lowrank[r] == r for r in lowrank), "rank-r kernel PSD carrier must give sig = r"
    assert jlinear_even, "J-linear (physical connection) carriers must be forced even"
    assert antilinear_zero, "J-antilinear carriers must give a non-vacuous zero index"

    return {
        "bare": bare, "C2": C2,
        "lowrank_sig_eq_rank": lowrank, "three_reachable": odd_reachable,
        "jlinear_even": jlinear_even, "jlin_doubling": jlin_sig,
        "antilinear_zero": antilinear_zero, "antilinear_norm": float(np.mean(anti_nrm)),
        "verdict": "under-determination, not impossibility; canonical selector required",
    }


if __name__ == "__main__":
    main()
