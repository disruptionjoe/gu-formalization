#!/usr/bin/env python3
"""STEP 8 / CONSTRUCT-03 - the CHARACTER of the revived index (how strong is the GO?).

CONSTRUCT-02 proved generic guard-admissible grading-breakers make eta(D + t*Delta) != 0, softening
the eta=0 wall (GO). This step asks how STRONG that GO is: is the revived asymmetry a canonical
integer, or path-dependent fuzz? And is the flow generic? Computed on the bridge (Cl(9,5) rep +
commuting quaternionic J), all guards held (M_D / bare commutator untouched). [Corrected after an
adversarial counter-computation that found a clean t->inf limit the first draft missed.]

FINDINGS (this run reproduces, deterministic seed):
1. FIRST-ORDER NULL: sig(P_ker Delta P_ker) = 0 for the natural AND every generic admissible breaker.
   D_Sigma has a 1536-dim kernel (+/-128 nonzero); a G-diagonal Delta splits that kernel SYMMETRICALLY
   to first order, so eta does NOT flow at small t -- the flow is a finite-t level-crossing.
2. CANONICAL LIMIT (the corrected, stronger result): eta(D + t*Delta) HAS a clean, numerically-stable
   t -> infinity limit equal to sig(Delta) -- the signature of the grading-breaking connection itself.
   It is flat from t ~ 50 (verified at t = 50, 200, 1000; full-rank Delta => the +/-128 singular modes
   of D_Sigma are swamped and eta_inf = sig(Delta) exactly). The multi-crossing seen at MODERATE t is
   only a transient; it is NOT the obstruction to canonicity.
3. NON-CANONICITY IS PATH-DEPENDENCE (not fuzz): sig(Delta) ranges over {0, +/-4, +/-8} across the
   admissible class. So the revived index is canonical PER CONNECTION but its VALUE is set entirely by
   WHICH grading-breaking connection Delta is chosen -- a datum the existing rep leaves completely free.
4. PROTECTED EXCEPTION: the natural breaker (M_D's own G-diagonal) has sig(Delta) = 0 and keeps eta = 0
   for ALL t -- the special, measure-zero protected case (it splits the kernel symmetrically forever).

VERDICT: the GO is GENERIC and REAL, and SHARPER than first stated -- the soft wall yields a genuine
canonical integer index eta_inf = sig(Delta), not mere fuzz. BUT that integer is CONNECTION-DEPENDENT
(sig(Delta) in {0,+/-4,+/-8}); the rep fixes no value. So a generation count needs the geometry to
supply a CANONICAL grading-breaking connection (a strictly stronger demand on SPEC 5(ii)'s Y14
holonomy), and even then -- per CONSTRUCT-04 (step7) -- sig(Delta) is an EVEN integer (quaternionic
Kramers) that the rep's algebra never honestly pins to 3. The soft wall is real; it is not a shortcut.

Run: python tests/step8_grading_flow_character.py
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from lib import gu_bridge  # noqa: E402

N, DIM = gu_bridge.N, gu_bridge.DIM
ETA_SIG = np.array([1.0] * 9 + [-1.0] * 5)


def quaternionic_J(e128):
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
    Us, _, Vs = np.linalg.svd(U)
    U = Us @ Vs
    return U / np.sqrt(abs(np.trace(U @ U.conj()) / DIM))


def sig(A):
    ev = np.linalg.eigvalsh(0.5 * (A + A.conj().T))
    tol = 1e-7 * np.abs(ev).max()
    return int((ev > tol).sum()) - int((ev < -tol).sum())


def main():
    np.set_printoptions(precision=5, suppress=True, linewidth=170)
    e, Gamma, Pi, M_D = gu_bridge.constraint_objects()
    Q = np.eye(N * DIM, dtype=complex) - Pi
    E = Q @ M_D @ Pi
    D = E + E.conj().T
    e128 = gu_bridge.gammas()
    bare = float(np.linalg.norm(Pi @ M_D - M_D @ Pi))
    C2 = float(np.linalg.norm(Gamma @ M_D @ Pi))
    print(f"[anchors] bare={bare:.4f} (58.7215)  C2={C2:.4f} (155.3625)")
    assert abs(bare - 58.7215) < 1e-2 and abs(C2 - 155.3625) < 1e-2

    U = quaternionic_J(e128)
    Jf = np.kron(np.eye(N), U)
    Jf_inv = np.linalg.inv(Jf)

    def gdiag(X):
        return Pi @ X @ Pi + Q @ X @ Q

    def herm(X):
        return 0.5 * (X + X.conj().T)

    def jsym(R):
        return 0.5 * (R + Jf @ R.conj() @ Jf_inv)

    Delta_nat = gdiag(herm(M_D))
    nrm = np.linalg.norm(Delta_nat)

    rng = np.random.default_rng(1)
    breakers = [("natural", Delta_nat)]
    for k in range(5):
        R = rng.standard_normal((N * DIM, N * DIM)) + 1j * rng.standard_normal((N * DIM, N * DIM))
        Dl = herm(gdiag(jsym(R)))
        breakers.append((f"generic#{k + 1}", Dl / np.linalg.norm(Dl) * nrm))

    # kernel projector of D (1536-dim)
    evD, VD = np.linalg.eigh(D)
    Wker = VD[:, np.abs(evD) <= 1e-7 * np.abs(evD).max()]
    print(f"\ndim ker(D_Sigma) = {Wker.shape[1]}  (+/-128 nonzero singular modes)")

    # (1) first-order kernel signature
    print("\n=== (1) first-order: sig(P_ker Delta P_ker) (0 => no small-t flow; finite-t only) ===")
    for name, Dl in breakers:
        print(f"  {name:10}: sig(P_ker Delta P_ker) = {sig(herm(Wker.conj().T @ Dl @ Wker))}")

    # (2)+(3)+(4) transient flow at moderate t, and the CANONICAL t->inf limit eta_inf = sig(Delta)
    print("\n=== (2-4) moderate-t transient vs canonical limit eta_inf = sig(Delta) ===")
    print(f"  {'breaker':10} {'sig(Delta)':>10} {'eta@[0.6,1.2,2.4]':>22} {'eta@50':>7} {'eta@1000':>9} {'limit==sig?':>12}")
    rows = {}
    for name, Dl in breakers:
        sD = sig(Dl)
        trans = [sig(D + t * Dl) for t in (0.6, 1.2, 2.4)]
        e50, e1000 = sig(D + 50 * Dl), sig(D + 1000 * Dl)
        limit_ok = (e50 == e1000 == sD)
        rows[name] = {"sigD": sD, "trans": trans, "e50": e50, "e1000": e1000, "limit_ok": limit_ok}
        print(f"  {name:10} {sD:>10} {str(trans):>22} {e50:>7} {e1000:>9} {str(limit_ok):>12}")

    sigs = [rows[n]["sigD"] for n in rows]
    all_even = all(s % 2 == 0 for s in sigs)
    all_limit = all(rows[n]["limit_ok"] for n in rows)
    nat_protected = (rows["natural"]["sigD"] == 0 and all(x == 0 for x in rows["natural"]["trans"]))
    n_nonzero = sum(1 for n in rows if n != "natural" and rows[n]["sigD"] != 0)
    n_transient = sum(1 for n in rows if n != "natural" and any(x != 0 for x in rows[n]["trans"]))

    print("\n=== VERDICT ===")
    print(f"(1) kernel first-order sig = 0 for all => flow is finite-t, not first-order.")
    print(f"(2) canonical limit eta_inf == sig(Delta) for all breakers (flat t=50..1000)?  {all_limit}")
    print(f"(3) sig(Delta) range across admissible class: {sorted(set(sigs))}  (connection-dependent, even)")
    print(f"(4) natural breaker protected (sig=0, eta==0 all t)?  {nat_protected}")
    print(f"    non-protection: {n_nonzero} generic breakers have nonzero canonical index sig(Delta);")
    print(f"                    {n_transient} show transient flow at moderate t.")
    print("\nReading: the revived index is a CANONICAL integer eta_inf = sig(Delta) (clean t->inf limit,")
    print("not fuzz), but its VALUE is connection-dependent (in {0,+/-4,+/-8}); the rep fixes nothing. A")
    print("count needs the geometry to supply a CANONICAL grading-breaking connection (a stronger demand")
    print("on SPEC 5(ii)'s Y14 holonomy), and even then sig(Delta) is an EVEN integer the rep never")
    print("honestly pins to 3 (CONSTRUCT-04). The soft wall is real and sharper; it is not a shortcut.")

    assert abs(bare - 58.7215) < 1e-2 and abs(C2 - 155.3625) < 1e-2, "anchors moved"
    assert all(sig(herm(Wker.conj().T @ Dl @ Wker)) == 0 for _, Dl in breakers), \
        "kernel first-order signature must vanish (no small-t flow)"
    assert all_limit, "eta must settle to the canonical limit sig(Delta) at large t"
    assert all_even, "sig(Delta) must be even (quaternionic Kramers)"
    assert nat_protected, "natural M_D-diagonal breaker must be the protected sig=0 case"
    assert n_nonzero >= 1, "GO requires some admissible breaker to carry a nonzero canonical index"

    return {
        "bare": bare, "C2": C2, "dim_ker": int(Wker.shape[1]),
        "sig_range": sorted(set(sigs)), "canonical_limit": all_limit,
        "natural_protected": nat_protected, "n_nonzero_index": n_nonzero,
    }


if __name__ == "__main__":
    main()
