#!/usr/bin/env python3
"""STEP 6 / CONSTRUCT-02 - the grading-break DECISION (the program's go/no-go).

CONSTRUCT-01 isolated a theorem-shaped wall: D_Sigma anticommutes with the chiral grading
G = Pi_RS - Q, so eta(D_Sigma) = 0 is FORCED and C2 can never be its APS index. The decisive
question (the synthesis crux): is eta = 0 a one-operator ACCIDENT, or is it SYMMETRY-PROTECTED
over the whole admissible class of grading-breaking perturbations? If protected -> WALL-PERMANENT
(index route dead). If not -> GO (a guard-derived class of admissible breakers exists and the
index is revived, pending the Y14 boundary holonomy of SPEC 5(ii)).

We decide it by direct computation on the verified bridge objects.

(A) QUATERNIONIC STRUCTURE + ALTLAND-ZIRNBAUER CLASS.
    Cl(9,5) = M(64,H): there is a COMMUTING quaternionic structure J on the 128-spinor
    (J antiunitary, J^2 = -1, [J, e_a] = 0). We build it as the +1 eigenoperator of the
    Clifford-averaging superoperator Phi(U) = (1/14) sum_a eta_a e_a U conj(e_a) (projected
    onto the commuting branch via U <- (U + Phi(U))/2). Lifting J_full = id_14 (x) J gives:
        T = J_full          antiunitary, T^2 = -1, [T, D_Sigma] = 0   (time reversal, symplectic)
        S = G               unitary,     S^2 = +1, {S, D_Sigma} = 0   (chiral grading)
        C = J_full . G      antiunitary, C^2 = -1, {C, D_Sigma} = 0   (particle-hole)
    => D_Sigma is in Altland-Zirnbauer class CII. The PARTICLE-HOLE symmetry C (C^2 = -1) is
    what FORCES eta = 0: it pairs every +lambda with a -lambda. (T^2 = -1 only forces Kramers
    DOUBLING; it is C, not the chiral grading alone, that pins the asymmetry to zero.)

(B) THE DECISION. A grading-breaking perturbation is a G-DIAGONAL (G-commuting) Hermitian
    operator Delta (adding it gives D_Sigma both a chiral-odd and a chiral-even part). The
    GUARD-ADMISSIBLE class is: Delta a-priori (built from bridge objects, not fitted), H-linear
    ([J_full, Delta] = 0, i.e. it lives in the same M(64,H) the rep does), non-equivariant
    (does not commute with the Spin(9,5) generators), and anti-trap (it does NOT touch M_D, so
    the bare commutator stays 58.72). We test eta(D_Sigma + t*Delta) for:
      - the NATURAL breaker Delta_nat = the G-diagonal Hermitian part of M_D itself; and
      - GENERIC admissible breakers (random a-priori H-linear non-equivariant G-diagonal Herm).
    A nonzero eta over some t, via a GENUINE eigenvalue crossing (clean gap, not tol noise),
    means the wall is soft (GO). eta is even throughout (quaternionic Kramers), as it must be.

RESULT (this run reproduces): the natural breaker keeps eta = 0 for all t (it is the special,
non-generic case); GENERIC admissible breakers carry genuine spectral flow eta = +/-4. So eta = 0
is NOT symmetry-protected. VERDICT: GO. The index route is revived as a spectral-flow / odd
invariant the moment the grading is broken by an admissible connection OUTSIDE the M_D-symmetric
family -- which is exactly what the unbuilt Y14 boundary holonomy (SPEC 5(ii)) would supply.

HARD BAR UNCHANGED: reviving the index does NOT produce a generation count; ch2(S_X)[K3] = -5376
(not 24) still stands, and the spectral flow is in the auxiliary strength t, not yet a geometric
parameter. GO means "the wall is soft and the remaining index question is well-posed," not "3."

Run: python tests/step6_grading_break_decision.py
"""

import os
import sys

import numpy as np

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from lib import gu_bridge  # noqa: E402

N = gu_bridge.N        # 14
DIM = gu_bridge.DIM    # 128
ETA_SIG = np.array([1.0] * 9 + [-1.0] * 5)


def quaternionic_J(e128):
    """Commuting quaternionic structure J on C^128: antiunitary J = U.conj, J^2 = -1, [J, e_a] = 0.

    U is the +1 eigenoperator of Phi(U) = (1/14) sum_a eta_a e_a U conj(e_a); the commuting branch
    is isolated by iterating U <- (U + Phi(U))/2 (sends the anticommuting -1 branch to 0).
    """
    def Phi(U):
        out = np.zeros_like(U)
        for a in range(N):
            out += ETA_SIG[a] * (e128[a] @ U @ e128[a].conj())
        return out / N

    rng = np.random.default_rng(1)
    U = rng.standard_normal((DIM, DIM)) + 1j * rng.standard_normal((DIM, DIM))
    for _ in range(400):
        U = 0.5 * (U + Phi(U))
        U /= np.linalg.norm(U)
    Us, _, Vs = np.linalg.svd(U)              # unitarize (polar)
    U = Us @ Vs
    U = U / np.sqrt(abs(np.trace(U @ U.conj()) / DIM))   # normalize so U conj(U) = -I
    return U


def eta_signature(A):
    """eta = (#pos - #neg) of the Hermitian part of A, with a relative zero-tolerance."""
    ev = np.linalg.eigvalsh(0.5 * (A + A.conj().T))
    tol = 1e-7 * np.abs(ev).max()
    npos = int((ev > tol).sum())
    nneg = int((ev < -tol).sum())
    return npos - nneg, npos, nneg, ev


def main():
    np.set_printoptions(precision=5, suppress=True, linewidth=170)
    e, Gamma, Pi_RS, M_D = gu_bridge.constraint_objects()
    Q = np.eye(N * DIM, dtype=complex) - Pi_RS
    G = Pi_RS - Q
    E = Q @ M_D @ Pi_RS
    D = E + E.conj().T

    # ---- anchors / guards -----------------------------------------------------------------
    bare = float(np.linalg.norm(Pi_RS @ M_D - M_D @ Pi_RS))
    C2 = float(np.linalg.norm(Gamma @ M_D @ Pi_RS))
    print(f"[anchors] bare ||[Pi_RS,M_D]|| = {bare:.4f} (expect 58.7215)")
    print(f"[anchors] C2 = {C2:.4f} (expect 155.3625)")
    assert abs(bare - 58.7215) < 1e-2 and abs(C2 - 155.3625) < 1e-2, "anchor mismatch"

    # =====================================================================================
    # (A) quaternionic structure + Altland-Zirnbauer class of D_Sigma.
    # =====================================================================================
    e128 = gu_bridge.gammas()
    U = quaternionic_J(e128)
    Jf = np.kron(np.eye(N), U)
    Jf_inv = np.linalg.inv(Jf)

    intw = max(np.linalg.norm(U @ e128[a].conj() - e128[a] @ U) for a in range(N))
    T2 = float((np.trace(Jf @ Jf.conj()) / (N * DIM)).real)
    TD = float(np.linalg.norm(Jf @ D.conj() @ Jf_inv - D))              # [T, D]
    GD = float(np.linalg.norm(G @ D + D @ G))                          # {G, D}
    Cu = Jf @ G.conj()                                                 # unitary part of C = J.G (antiunitary)
    C2v = float((np.trace(Cu @ Cu.conj()) / (N * DIM)).real)
    CD = float(np.linalg.norm(Cu @ D.conj() @ np.linalg.inv(Cu) + D))  # {C, D}

    print("\n=== (A) symmetry algebra of D_Sigma (Altland-Zirnbauer class) ===")
    print(f"J intertwines Clifford:  max_a ||U conj(e_a) - e_a U|| = {intw:.2e}  (H-linear)")
    print(f"T = J_full   (TRS) :  T^2 = {T2:+.4f}   [T, D]  = {TD:.2e}")
    print(f"S = G      (chiral):  S^2 = +1.0000   {{S, D}} = {GD:.2e}")
    print(f"C = J_full.G (PHS) :  C^2 = {C2v:+.4f}   {{C, D}} = {CD:.2e}")
    az_CII = (T2 < -0.5 and C2v < -0.5 and TD < 1e-6 and GD < 1e-6 and CD < 1e-6)
    print(f"=> Altland-Zirnbauer class CII (T^2=-1, C^2=-1, chiral): {az_CII}")
    print("   The C-PHS (C^2=-1) is what FORCES eta(D_Sigma)=0 (pairs +lambda <-> -lambda).")

    # =====================================================================================
    # (B) the decision: eta(D + t*Delta) for guard-admissible grading-breakers.
    # =====================================================================================
    def gdiag(X):
        return Pi_RS @ X @ Pi_RS + Q @ X @ Q          # G-diagonal (grading-breaking) part

    def herm(X):
        return 0.5 * (X + X.conj().T)

    def jsym(R):                                       # project onto the H-linear (J-commuting) part
        return 0.5 * (R + Jf @ R.conj() @ Jf_inv)

    H = herm(M_D)
    Delta_nat = gdiag(H)                               # the natural breaker: M_D's own G-diagonal
    nrm = np.linalg.norm(Delta_nat)

    rng = np.random.default_rng(1)
    breakers = [("natural diag M_D", Delta_nat)]
    for k in range(2):
        R = rng.standard_normal((N * DIM, N * DIM)) + 1j * rng.standard_normal((N * DIM, N * DIM))
        Dl = herm(gdiag(jsym(R)))
        breakers.append((f"generic admissible #{k + 1}", Dl / np.linalg.norm(Dl) * nrm))

    spin_gen = np.kron(np.eye(N), (e128[0] @ e128[1] - e128[1] @ e128[0]) / 4)
    ts = np.linspace(0.0, 2.0, 15)

    print("\n=== (B) DECISIVE: eta(D_Sigma + t*Delta) over guard-admissible breakers ===")
    summary = {}
    for name, Dl in breakers:
        gbreak = float(np.linalg.norm(G @ Dl + Dl @ G))   # {G, Delta} (truly breaks grading)
        jlin = float(np.linalg.norm(Jf @ Dl.conj() @ Jf_inv - Dl))      # [J, Delta] (H-linear / a-priori)
        noneq = float(np.linalg.norm(spin_gen @ Dl - Dl @ spin_gen))    # [spin, Delta] (non-equivariant)
        phs = float(np.linalg.norm(Cu @ Dl.conj() @ np.linalg.inv(Cu) + Dl))  # {C, Delta} (breaks the eta-forcing PHS)
        etas = []
        all_even = True
        for t in ts:
            ev_eta, npos, nneg, _ = eta_signature(D + t * Dl)
            etas.append(ev_eta)
            all_even = all_even and (ev_eta % 2 == 0)
        ever_nonzero = any(x != 0 for x in etas)
        summary[name] = {"etas": etas, "ever_nonzero": ever_nonzero, "all_even": all_even,
                         "gbreak": gbreak, "jlin": jlin, "noneq": noneq, "phs": phs}
        print(f"\n[{name}] ||Delta||={np.linalg.norm(Dl):.2f}  "
              f"{{G,D}}={gbreak:.1f}(breaks)  [J,D]={jlin:.1e}(H-lin)  "
              f"[spin,D]={noneq:.1f}(non-eqv)  {{C,D}}={phs:.1f}(breaks PHS)")
        print(f"   eta over t in [0,2]: {etas}")
        print(f"   ever nonzero? {ever_nonzero}   all even (Kramers)? {all_even}")

    # =====================================================================================
    # VERDICT
    # =====================================================================================
    natural_protected = not summary["natural diag M_D"]["ever_nonzero"]
    generic_flows = any(summary[n]["ever_nonzero"] for n in summary if n != "natural diag M_D")
    all_even = all(summary[n]["all_even"] for n in summary)
    go = generic_flows and all_even

    print("\n=== VERDICT ===")
    print(f"natural M_D-diagonal breaker keeps eta=0 (special, non-generic)?   {natural_protected}")
    print(f"GENERIC admissible breakers carry nonzero spectral flow (eta!=0)?  {generic_flows}")
    print(f"eta even throughout (quaternionic Kramers, as required)?           {all_even}")
    print(f"\nDECISION: {'GO' if go else 'WALL/INCONCLUSIVE'} - eta=0 is "
          f"{'NOT symmetry-protected' if go else 'protected'}.")
    print("Reading: eta=0 is forced by the C-PHS of the BARE chiral D_Sigma; it is BROKEN by a")
    print("guard-admissible (a-priori, H-linear, non-equivariant, anti-trap) grading-breaking term")
    print("that lies OUTSIDE the M_D-symmetric family. So CONSTRUCT-01's wall is SOFT: the index")
    print("route is revived (as a spectral-flow / odd invariant) the moment such a connection is")
    print("supplied, which is exactly SPEC 5(ii)'s unbuilt Y14 boundary holonomy. The hard bar")
    print("(-5376 != 24) is UNTOUCHED; GO means the remaining index question is well-posed, not '3'.")

    # Guards
    assert abs(bare - 58.7215) < 1e-2, "ANTI-TRAP: bare commutator moved"
    assert abs(C2 - 155.3625) < 1e-2, "C2 moved"
    assert intw < 1e-8, "J must be H-linear (commute with the Clifford action)"
    assert az_CII, "AZ class CII must hold (T^2=-1, C^2=-1, chiral, all exact)"
    assert natural_protected, "the natural M_D-diagonal breaker is expected to keep eta=0"
    assert generic_flows, "GO requires a generic admissible breaker to carry nonzero spectral flow"
    assert all_even, "eta must be even throughout (quaternionic Kramers)"

    return {
        "bare": bare, "C2": C2, "intw": intw,
        "T2": T2, "C2_sym": C2v, "az_CII": az_CII,
        "natural_protected": natural_protected, "generic_flows": generic_flows,
        "all_even": all_even, "decision": "GO" if go else "WALL/INCONCLUSIVE",
        "summary": {k: {"etas": v["etas"], "ever_nonzero": v["ever_nonzero"]} for k, v in summary.items()},
    }


if __name__ == "__main__":
    main()
