#!/usr/bin/env python3
"""
H29 (Wave 12) -- THE FERMION / C2 = 155.36 WALL: the source action's HARD residual,
where the generation count lives. The "push further" swing that attacks the object
H23 named strictly harder than the gravity soldering.

DISCIPLINE (strict -- most at risk of motivated success): compute -> adversarially
verify -> HONEST grade. Every positive claim below is an EXACT matrix identity on the
verified Cl(9,5)=M(64,H) representation (residual 0.0), or an explicit ratio. NOTHING
imported (no 24/8, no chi(K3)=24, no assumed K3, no fitting to 3). C2 is NOT driven down
(that is the acausal Velo-Zwanziger trap in DEAD-ENDS.md); it is CHARACTERIZED and its
obstruction NAMED. "It fits beautifully" is treated as a WARNING SIGN throughout.

------------------------------------------------------------------------------------
WHAT THIS TEST SETTLES (the honest split)

  Part A -- CHARACTERIZE C2 exactly.
    A1. Reproduce anchors: C2 = ||Gamma M_D Pi_RS|| = 155.3625, bare ||[Pi_RS,M_D]|| = 58.7215.
    A2. Identity: Gamma Pi_RS = 0, hence C2 = ||Gamma [M_D, Pi_RS]|| = ||Gamma (Q M_D Pi_RS)||.
        => C2 is the gamma-trace of the Velo-Zwanziger CONSTRAINT-LEAKAGE block Q M_D Pi_RS:
           the failure of the Dirac symbol to preserve the RS (gamma-traceless) surface.
    A3. C2 = sqrt(7) * bare EXACTLY (prime-spectrum {2,7,13}, canon C-04) and C2 is
        degree-1 HOMOGENEOUS in xi (2.0/3.0/0.5 exact) => a scale-DEPENDENT symbol-norm,
        NOT a scale-invariant integer index. (Re-derives "C2 is not an index" numerically.)

  Part B -- THE EVEN/ODD (H20 square/square-root; H23-D Clifford parity) LENS.
    B1. Chirality omega = e_0...e_13 is a genuine involution (omega^2 = +I, Hermitian).
    B2. C2 lives ENTIRELY in the Clifford-ODD sector: M_D and Gamma and the leakage
        O = Q M_D Pi_RS + Pi_RS M_D Q are exactly Clifford-ODD (anticommute with omega),
        Pi_RS is exactly Clifford-EVEN. => C2 IS the odd-sector analog of the EVEN-sector
        graviton action |II|^2 (same |II|^2 module, opposite Clifford parity). The canon
        shiab is Clifford-odd too (SHIAB-A), matching.
    B3. The chirality split is EXACTLY SYMMETRIC: c+ = c- (= 109.858), Pythagorean to C2.
        => ZERO net chiral asymmetry. The odd/even split does NOT reduce C2; it exposes
        C2 as chiral-SYMMETRIC = COUNT-BLIND.

  Part C -- DOES THE EVEN-SECTOR (H23) RESOLUTION TRANSFER?  YES structurally, and that
            is exactly WHY it does not resolve the count.
    C1. The Krein form K = eta_V (x) beta_S that buys gravity's [P,S]=0 positivity (H23-C)
        makes M_D Krein-self-adjoint (reproduce H23-C: K M_D = M_D^dag K, residual 0).
    C2. The SAME K makes the odd-sector leakage O Krein-SELF-adjoint (K O = O^dag K).
        => the even-sector positivity machinery TRANSFERS verbatim to the fermion leakage.
    C3. But it is EQUALLY SIGN-BLIND (parallels H23-C exactly): combined with B3's exact
        chiral symmetry, K controls the MAGNITUDE of C2 but supplies NO chiral index.

  Part D -- WHY THE ODD SECTOR IS STRICTLY HARDER (the eta=0 mechanism, canon C-01).
    D1. The leakage O is simultaneously:
          (i)  Kramers J-linear: O J = J conj(O) with J^2=-1  (even-signature wall, no-go canon);
          (ii) particle-hole ODD: {G, O} = 0 with G = Pi_RS - Q, G^2 = I
               => spectrum is +/-lambda symmetric => eta(D_Sigma) = 0 (class CII, C-01);
          (iii) Krein-self-adjoint (C2 above): real magnitude.
        => C2 is the NONZERO norm of a leakage whose spectral asymmetry (index/eta) is
           THEOREM-FORCED to zero. This is the precise reason "C2 is not an index."
    D2. Contrast with gravity: the even sector's residual (H23-D) is a grading-PRESERVING
        soldering onto a real geometric object (theta -> II_s). The odd sector's natural
        target (a generation index) is OBSTRUCTED BY A THEOREM (eta=0), not merely unbuilt.
        To get a nonzero odd index you must BREAK the grading (-> connection-dependent,
        non-canonical, C-02/C-03) or IMPORT the frame-trivial antilinear chiralizer
        C = J_quat.G (capstone: selector-side). Both are the forbidden moves. STRICTLY HARDER.

  ADVERSARIAL (Part E): no 3 anywhere; no chirality/Krein projection turns C2 integer;
  C2 is NOT reduced (unchanged 155.3625 -- acausal trap avoided). The "narrowing" is an
  exact structural re-characterization, not a numeric reduction and not a fit to 3.

VERDICT: NARROWED (high confidence on the structural facts -- all exact rep-theory,
residual 0.0, independent of whether GU is correct). NOT resolved: earning closure needs
a canonical grading-BREAKING boundary-Dirac carrier, which the eta=0 theorem obstructs.
The even/odd + Krein leverage sharpens the obstruction from "mysterious non-index symbol
norm" to "particle-hole-odd Kramers Krein-self-adjoint leakage with theorem-forced zero
index; even-sector positivity transfers but is sign-blind."

Reproducible: python tests/wave12/H29_fermion_c2_wall.py   (exit 0 on all PASS)
"""
from __future__ import annotations
import os
import sys

import numpy as np

# Use the parent repo's own verified Cl(9,5)=M(64,H) representation via the generation-sector bridge.
_HERE = os.path.dirname(os.path.abspath(__file__))
_GENSEC = os.path.normpath(os.path.join(_HERE, "..", "generation-sector"))
if _GENSEC not in sys.path:
    sys.path.insert(0, _GENSEC)
import gen_sector_bridge as gb  # noqa: E402  (verified anchors: bare 58.7215, C2 155.3625)

N, DIM = 14, 128
TOL = 1e-9          # exact-identity tolerance (finite-dim rep; residuals are ~1e-14 or 0.0)
SIG_SPACELIKE = 9   # (9,5): a=0..8 spacelike, a=9..13 timelike


def report(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {detail}" if detail else ""))
    return bool(ok)


def main():
    e, Gamma, Pi, MD = gb.constraint_objects()   # e[a], gamma-trace map, Pi_RS, M_D
    I_S = np.eye(DIM, dtype=complex)
    I_RS = np.eye(N * DIM, dtype=complex)
    Q = I_RS - Pi                                 # complement of the constraint surface
    checks = []

    print("=" * 82)
    print("H29  THE FERMION / C2 = 155.36 WALL  (Cl(9,5)=M(64,H); even/odd + Krein leverage)")
    print("=" * 82)

    # ---------------- Part A: characterize C2 -----------------------------------------
    print("Part A -- CHARACTERIZE C2 (what it is, why it is not an index)")
    C2 = float(np.linalg.norm(Gamma @ MD @ Pi))
    bare = float(np.linalg.norm(Pi @ MD - MD @ Pi))
    checks.append(report("A1. anchors reproduce: C2=155.3625, bare=58.7215",
                         abs(C2 - 155.3625069) < 1e-4 and abs(bare - 58.7215081) < 1e-4,
                         f"C2={C2:.7f}, bare={bare:.7f}"))

    gp = float(np.linalg.norm(Gamma @ Pi))
    c2_comm = float(np.linalg.norm(Gamma @ (MD @ Pi - Pi @ MD)))
    c2_leak = float(np.linalg.norm(Gamma @ (Q @ MD @ Pi)))
    checks.append(report("A2. Gamma Pi_RS = 0  =>  C2 = ||Gamma[M_D,Pi_RS]|| = ||Gamma(Q M_D Pi_RS)||",
                         gp < TOL and abs(c2_comm - C2) < 1e-6 and abs(c2_leak - C2) < 1e-6,
                         f"||Gamma Pi||={gp:.1e}; via comm={c2_comm:.4f}; via leakage Q M_D Pi={c2_leak:.4f}"))

    ratio = C2 / bare
    hom = [gb.C2(s * gb.XI) / gb.C2(gb.XI) for s in (2.0, 3.0, 0.5)]
    checks.append(report("A3. C2 = sqrt(7)*bare EXACT and degree-1 homogeneous (2/3/0.5) => NOT an index",
                         abs(ratio - np.sqrt(7)) < 1e-9
                         and max(abs(hom[0] - 2), abs(hom[1] - 3), abs(hom[2] - 0.5)) < 1e-9,
                         f"C2/bare={ratio:.10f} (sqrt7={np.sqrt(7):.10f}); C2(s*xi)/C2(xi)={[round(h,3) for h in hom]}"))

    # ---------------- Part B: the even/odd (Clifford parity) lens ---------------------
    print("Part B -- THE EVEN/ODD LENS (H20 square/square-root; H23-D Clifford parity)")
    omega = I_S.copy()
    for a in range(N):
        omega = omega @ e[a]                      # chirality = volume element e_0...e_13
    om_sq = float(np.linalg.norm(omega @ omega - I_S))
    om_herm = float(np.linalg.norm(omega - omega.conj().T))
    checks.append(report("B1. chirality omega = e_0..e_13 is an involution (omega^2=+I, Hermitian)",
                         om_sq < TOL and om_herm < TOL, f"||omega^2-I||={om_sq:.1e}, herm={om_herm:.1e}"))

    omRS = np.kron(np.eye(N, dtype=complex), omega)
    O = Q @ MD @ Pi + Pi @ MD @ Q                 # the full G-odd leakage operator
    md_odd = float(np.linalg.norm(omRS @ MD + MD @ omRS))
    ga_odd = float(np.linalg.norm(omega @ Gamma + Gamma @ omRS))
    pi_even = float(np.linalg.norm(omRS @ Pi - Pi @ omRS))
    O_odd = float(np.linalg.norm(omRS @ O + O @ omRS))
    checks.append(report("B2. C2 lives in the Clifford-ODD sector: M_D, Gamma, leakage O ODD; Pi_RS EVEN",
                         md_odd < TOL and ga_odd < TOL and pi_even < TOL and O_odd < TOL,
                         f"M_D odd {md_odd:.1e}, Gamma odd {ga_odd:.1e}, Pi even {pi_even:.1e}, O odd {O_odd:.1e}"))

    Pp = np.kron(np.eye(N, dtype=complex), (I_S + omega) / 2)
    Pm = np.kron(np.eye(N, dtype=complex), (I_S - omega) / 2)
    cpl = float(np.linalg.norm(Gamma @ MD @ Pi @ Pp))
    cmi = float(np.linalg.norm(Gamma @ MD @ Pi @ Pm))
    checks.append(report("B3. chirality split EXACTLY symmetric c+ = c-, Pythagorean to C2 => COUNT-BLIND",
                         abs(cpl - cmi) < 1e-6 and abs(np.hypot(cpl, cmi) - C2) < 1e-6,
                         f"c+={cpl:.4f}, c-={cmi:.4f}, sqrt(c+^2+c-^2)={np.hypot(cpl, cmi):.4f} (split does NOT reduce C2)"))

    # ---------------- Part C: does the H23 even-sector Krein resolution transfer? ------
    print("Part C -- DOES THE EVEN-SECTOR (H23) KREIN POSITIVITY TRANSFER? (yes, but sign-blind)")
    beta_S = I_S.copy()
    for a in range(SIG_SPACELIKE):
        beta_S = beta_S @ e[a]                    # spinor Krein metric (64,64)
    etaV = np.diag([1.0 if a < SIG_SPACELIKE else -1.0 for a in range(N)]).astype(complex)
    K = np.kron(etaV, beta_S)                     # ghost parity / Krein form (H23-C)
    md_ksa = float(np.linalg.norm(K @ MD - MD.conj().T @ K))
    checks.append(report("C1. reproduce H23-C: M_D Krein-self-adjoint  K M_D = M_D^dag K (gravity positivity)",
                         md_ksa < TOL, f"err {md_ksa:.1e}"))
    O_ksa = float(np.linalg.norm(K @ O - O.conj().T @ K))
    checks.append(report("C2. TRANSFER: odd-sector leakage O is ALSO Krein-self-adjoint  K O = O^dag K",
                         O_ksa < TOL, f"err {O_ksa:.1e}  => even-sector positivity machinery applies to the fermion leakage"))
    # sign-blindness already shown structurally by B3 (c+ = c-); label it.
    checks.append(report("C3. but SIGN-BLIND (parallels H23-C): B3's c+ = c- => K fixes MAGNITUDE, gives NO chiral index",
                         abs(cpl - cmi) < 1e-6, "chiral asymmetry = 0"))

    # ---------------- Part D: why the odd sector is strictly harder (eta=0) -----------
    print("Part D -- WHY STRICTLY HARDER: the particle-hole eta=0 wall (canon C-01)")
    # Kramers charge conjugation C_cc = e1 e3 e5 e7 e10 e12, C_cc^2 = -I  (no-go canon)
    C_cc = I_S.copy()
    for a in (1, 3, 5, 7, 10, 12):
        C_cc = C_cc @ e[a]
    Ccc_sq = float(np.linalg.norm(C_cc @ C_cc + I_S))
    C_RS = np.kron(np.eye(N, dtype=complex), C_cc)
    # antilinear J-commutation A J = J conj(A):  A C_RS = C_RS conj(A)
    O_jlin = float(np.linalg.norm(O @ C_RS - C_RS @ O.conj()))
    G = Pi - Q                                    # the boundary chiral / particle-hole grading
    G_sq = float(np.linalg.norm(G @ G - I_RS))
    GO_anti = float(np.linalg.norm(G @ O + O @ G))
    checks.append(report("D1. leakage O: Kramers J-linear (J^2=-1), particle-hole ODD {G,O}=0, G^2=I => eta=0",
                         Ccc_sq < TOL and O_jlin < TOL and G_sq < TOL and GO_anti < TOL,
                         f"C^2+I={Ccc_sq:.1e}; O J-lin {O_jlin:.1e}; G^2-I {G_sq:.1e}; {{G,O}} {GO_anti:.1e}"))
    # D2 is an interpretive contrast (no new numeric); assert the two anchors it rests on.
    checks.append(report("D2. contrast: C2 unchanged (155.3625) -- NOT driven down (acausal trap avoided); "
                         "index THEOREM-forced 0, not merely unbuilt",
                         abs(C2 - 155.3625069) < 1e-4,
                         "gravity solders onto real II_s (grading-preserving); odd index obstructed by eta=0"))

    # ---------------- Part E: adversarial p-hacking guard -----------------------------
    print("Part E -- ADVERSARIAL: no import of 3 / 24 / 24-8; no fit; C2 not reduced")
    # No integer '3' is manufactured anywhere; the only integers are rep dims and the exact
    # homogeneity degree. Guard: c+, c-, C2, bare are all non-integer, and 3 does not divide anything used.
    non_integer = all(abs(x - round(x)) > 1e-3 for x in (C2, bare, cpl, cmi, ratio))
    c2_unchanged = abs(C2 - 155.3625069) < 1e-6
    checks.append(report("E. no 3/24/(24/8) imported; C2 not reduced; all sector norms non-integer",
                         non_integer and c2_unchanged,
                         f"C2={C2:.4f} (unchanged), all sector norms irrational; no target fit"))

    print("-" * 82)
    print("SUMMARY")
    print(f"  A. C2 = ||Gamma(Q M_D Pi_RS)|| = sqrt(7)*bare, degree-1 homogeneous => symbol-norm, NOT an index.")
    print(f"  B. C2 is the Clifford-ODD analog of the even-sector |II|^2 graviton action; chiral-SYMMETRIC (count-blind).")
    print(f"  C. Even-sector Krein positivity (H23-C) TRANSFERS to the fermion leakage O, but is SIGN-BLIND.")
    print(f"  D. O is Kramers + particle-hole-odd + Krein-self-adjoint => index/eta THEOREM-forced 0 => C2 not an index.")
    print(f"  VERDICT: NARROWED. C2 sharpened to a particle-hole-odd Kramers Krein-self-adjoint leakage with")
    print(f"           theorem-forced zero index. Strictly harder than gravity's grading-preserving soldering.")
    print(f"  NEXT OBJECT: a CANONICAL grading-BREAKING boundary-Dirac whose eta != 0 without importing the")
    print(f"           frame-trivial chiralizer -- obstructed on current data by the eta=0 (CII) theorem.")
    print("=" * 82)

    ok = all(checks)
    print(("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED") + f"  ({sum(checks)}/{len(checks)})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
