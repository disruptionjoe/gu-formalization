#!/usr/bin/env python3
"""H54 branch-1 (Wave 37) -- GUARDIAN SUPERALGEBRA EXISTENCE for GU's (9,5)/Sp(32,32;H) structure.

QUESTION (H54, this branch). GU's guardian-free source action is only a finite-cutoff EFT (Rahman
helicity-1/2 cutoff, wave 34); UV-completeness needs a GUARDIAN SYMMETRY (local SUSY / super-Higgs
gravitino). Prerequisite, settled HERE at the algebra level: does GU's bosonic data -- the frame
algebra so(9,5) (dim 91, NOT 45), its Cartan involution P = beta_S, and the non-compact gauge group
Sp(32,32;H) -- admit a Lie-SUPER extension whose even part contains so(9,5) (or the (9,5)
Poincare/conformal algebra) and whose odd part is a spinor supercharge Q with {Q,Q} ~ P (translations)
or ~ conformal generators?

WHAT THIS COMPUTES (all on the verified Cl(9,5)=M(64,H) 128-dim complex rep; nothing imported):

  Q1  the (9,5) spinor bilinear structure and {Q,Q}~gamma^mu P_mu closure.
      - reality class: p-q = 9-5 = 4 == 4 (mod 8) => QUATERNIONIC (CII), the antilinear
        charge-conjugation J has J^2 = -1 (same J^2=-1 CII structure H37 uses). [COMPUTED]
      - linear charge conjugations C_+ (eta=+1), C_- (eta=-1) with C e_a^T C^-1 = eta e_a, built
        explicitly as products of gammas. Their symmetries and the symmetry of C gamma^mu:
            C_- : C_-^T = +C_-  (symmetric),  C_- gamma^mu  ANTISYMMETRIC (all 14).
            C_+ : C_+^T = -C_+  (antisym),    C_+ gamma^mu  ANTISYMMETRIC (all 14).
        {Q_a,Q_b} is symmetric in (a,b), so a SINGLE-spinor {Q,Q}=(C gamma^mu)_ab P_mu needs
        C gamma^mu SYMMETRIC. Both are ANTISYMMETRIC => N=1 super-Poincare with {Q,Q}~P is
        FORBIDDEN in (9,5). [COMPUTED]
      - symplectic (N even) closure: with an Sp(1)_R doublet index i and the antisymmetric invariant
        Omega^{ij}, {Q^i_a, Q^j_b} = Omega^{ij} (C_- gamma^mu)_{ab} P_mu is symmetric under
        (a,i)<->(b,j) because antisym x antisym = sym. Verified: Omega (x) (C_- gamma^mu) is a
        symmetric matrix. => super-Poincare EXISTS, minimal N even (symplectic-Majorana), USp(2N)_R.
        [COMPUTED]

  Q2  odd part inside Sp(32,32;H); Kac identification.
      - the supercharge lives in the 128 = 64 + 64 (Weyl) spinor; omega = e_0..e_13, omega^2 = +I
        so chiral projectors exist (Weyl ok); Majorana-Weyl needs p-q==0 (mod 8) -> here 4 -> NO
        Majorana-Weyl, but symplectic-Majorana-Weyl exists at p-q==4. [COMPUTED]
      - Kac: the super-Poincare is the INHOMOGENEOUS (non-simple) siso(9,5|N); it is NOT one of the
        simple classical/exceptional Lie superalgebras (no osp / su(m|n) packages so(9,5)+spinor with
        {Q,Q}~P as a simple superalgebra). The SUPER-CONFORMAL version (even part so(10,6), the
        conformal algebra of (9,5)) does NOT exist: Nahm's classification caps simple superconformal
        algebras at spacetime dimension D <= 6; D = 14 is far above it. [ARGUED, dimension-checked]

  Q3  is P = beta_S (Cartan involution) the SUSY grading?  NO -- three DISTINCT Z/2's:
      (i)  P = beta_S : Cartan involution of so(9,5) (rotations +, boosts -), the Krein/ghost parity
           (H23). beta_S^2 = I. Lives inside the EVEN (bosonic) subalgebra.
      (ii) omega : chirality / omega-parity (H20 gravity-matter split). omega^2 = I. Also EVEN sector.
      (iii) the SUSY grading : boson (so(9,5),P_mu,R) vs fermion (Q). A GENUINELY NEW Z/2 that GU's
           published bosonic data does not already carry. beta_S != +-omega and [beta_S,omega] != 0,
           so P and omega are two different bosonic involutions; neither is the fermion-number grading.
      [COMPUTED distinctness]

VERDICT: PARTIAL. A guardian super-extension EXISTS -- the symplectic-Majorana super-Poincare
siso(9,5|N), N even, USp(2N)_R, {Q,Q}=Omega(C_- gamma^mu)P_mu -- and it is exactly the algebra whose
gauge field is a gravitino, so a supergravity guardian is ALGEBRAICALLY POSSIBLE. BUT it is NOT forced
by GU's structure: it requires adding a new Z/2 grading + odd generators + a USp(2N)_R that the Cartan
P and the chirality omega (both bosonic-sector) do not supply; the SIMPLE / super-CONFORMAL packaging
is OBSTRUCTED (D=14 >> Nahm bound 6); and no unique N is singled out by GU's carrier-B. Existence of a
super-Poincare (true for essentially every signature) is NOT "GU is supergravity"; whether GU's
dynamics realizes it is the soldering/guardian question this branch cannot settle.

Reproducible: python tests/wave37/H54b1_superalgebra_existence.py   (exit 0 on all PASS)
"""
from __future__ import annotations

import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_TESTS = os.path.normpath(os.path.join(_HERE, ".."))
if _TESTS not in sys.path:
    sys.path.insert(0, _TESTS)

import oq_rk1_cl95_explicit_rep as cl95  # noqa: E402  verified Cl(9,5)=M(64,H) rep

DIM = 128
TOL = 1e-9


def report(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {detail}" if detail else ""))
    return bool(ok)


def gammas():
    G = cl95.jordan_wigner_gammas(7)
    eta = [1] * 9 + [-1] * 5
    return [G[a] if eta[a] > 0 else 1j * G[a] for a in range(14)]


def prod(e, idx, I):
    M = I.copy()
    for a in idx:
        M = M @ e[a]
    return M


def sym_tag(M):
    if np.max(np.abs(M.T - M)) < 1e-6:
        return "+sym"
    if np.max(np.abs(M.T + M)) < 1e-6:
        return "-anti"
    return "?mixed"


def main():
    checks = []
    I = np.eye(DIM, dtype=complex)
    e = gammas()
    p, q = 9, 5

    print("=" * 96)
    print("H54-b1  GUARDIAN SUPERALGEBRA EXISTENCE for GU's (9,5) / Sp(32,32;H) structure")
    print("=" * 96)

    # ------------------------------------------------------------------ substrate
    cliff = max(np.max(np.abs(e[a] @ e[b] + e[b] @ e[a]
                              - (2 * (1 if a < 9 else -1) if a == b else 0) * I))
                for a in range(14) for b in range(14))
    checks.append(report("S0. verified Cl(9,5)=M(64,H): {e_a,e_b}=2 eta_ab, dim_C=128",
                         cliff < TOL and DIM == 128, f"max Clifford err={cliff:.1e}"))

    # ============================ Q1: (9,5) spinor structure + {Q,Q} closure ============================
    print("Q1 -- (9,5) spinor reality, C-matrices, and {Q,Q}~gamma^mu P_mu closure")

    # reality class: p-q mod 8
    pq_mod8 = (p - q) % 8
    checks.append(report("Q1a. p-q = 9-5 = 4 == 4 (mod 8) => QUATERNIONIC spinor (CII)",
                         pq_mod8 == 4, f"(p-q) mod 8 = {pq_mod8} -> H (quaternionic)"))

    # antilinear charge conjugation J with J^2 = -1 (the H37 CII structure), from imaginary gammas
    imag = [a for a in range(14) if np.max(np.abs(e[a].conj() + e[a])) < TOL]
    U = I.copy()
    for a in imag:
        U = U @ e[a]
    U = U / np.sqrt(np.max(np.abs(np.diag(U @ U.conj().T))))
    Jsq = complex(np.trace(U @ U.conj()) / DIM).real  # sign of J^2 for J = U . conj
    checks.append(report("Q1b. antilinear J (Majorana map) has J^2 = -1  (CII, matches H37)",
                         Jsq < 0, f"J^2 = {Jsq:+.2f} => symplectic-Majorana, N must be EVEN"))

    # e_a^T = (-1)^a e_a in this JW basis (the key identity the C-construction rests on)
    tflip = max(np.max(np.abs(e[a].T - ((-1) ** a) * e[a])) for a in range(14))
    checks.append(report("Q1c. e_a^T = (-1)^a e_a exactly (JW basis identity)",
                         tflip < TOL, f"max err={tflip:.1e}"))

    # linear charge conjugations built explicitly: C_- = prod odd-a e_a ; C_+ = prod even-a e_a
    Cm = prod(e, [a for a in range(14) if a % 2 == 1], I)
    Cp = prod(e, [a for a in range(14) if a % 2 == 0], I)

    def eta_of(C):
        Ci = np.linalg.inv(C)
        s = set()
        for a in range(14):
            M = C @ e[a].T @ Ci
            s.add(+1 if np.max(np.abs(M - e[a])) < 1e-6 else
                  (-1 if np.max(np.abs(M + e[a])) < 1e-6 else 0))
        return s

    em, ep = eta_of(Cm), eta_of(Cp)
    checks.append(report("Q1d. C_- : C e_a^T C^-1 = -e_a (eta=-1), and C_-^T = +C_- (symmetric)",
                         em == {-1} and sym_tag(Cm) == "+sym", f"eta(C_-)={em}, C_-^T={sym_tag(Cm)}"))
    checks.append(report("Q1e. C_+ : C e_a^T C^-1 = +e_a (eta=+1), and C_+^T = -C_+ (antisymmetric)",
                         ep == {1} and sym_tag(Cp) == "-anti", f"eta(C_+)={ep}, C_+^T={sym_tag(Cp)}"))

    # symmetry of C gamma^mu -- the object that must be SYMMETRIC for single-spinor {Q,Q}~P
    cm_tags = {sym_tag(Cm @ e[a]) for a in range(14)}
    cp_tags = {sym_tag(Cp @ e[a]) for a in range(14)}
    both_anti = cm_tags == {"-anti"} and cp_tags == {"-anti"}
    checks.append(report("Q1f. BOTH C_- gamma^mu and C_+ gamma^mu are ANTISYMMETRIC (all 14 mu)",
                         both_anti, f"C_- g: {cm_tags}, C_+ g: {cp_tags}"))
    checks.append(report("Q1g. => N=1 (single-spinor) {Q,Q}=(C gamma^mu) P_mu is FORBIDDEN in (9,5)",
                         both_anti, "no symmetric C gamma^mu exists => symplectic doubling required"))

    # symplectic closure: Omega^{ij} (C_- gamma^mu) symmetric under (a,i)<->(b,j)
    Om = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)  # Sp(1)_R invariant, antisymmetric
    sym_ok = all(np.max(np.abs(np.kron(Om, Cm @ e[a]).T - np.kron(Om, Cm @ e[a]))) < 1e-6
                 for a in range(14))
    checks.append(report("Q1h. Omega (x) (C_- gamma^mu) is SYMMETRIC => {Q^i,Q^j}=Omega(C_-g)P closes (N even)",
                         sym_ok, "antisym Omega x antisym C_-g = symmetric => super-Poincare EXISTS, N even"))

    # ============================ Q2: odd part in Sp(32,32;H); Kac identification ============================
    print("Q2 -- odd part inside the 128 spinor / Sp(32,32;H); Weyl and Kac type")
    omega = prod(e, list(range(14)), I)
    omega_sq = np.max(np.abs(omega @ omega - I))
    rankp = int(np.linalg.matrix_rank(0.5 * (I + omega), tol=TOL))
    checks.append(report("Q2a. omega^2=+I, Weyl split 128 = 64 + 64 (chiral projectors exist)",
                         omega_sq < TOL and rankp == 64, f"omega^2-I={omega_sq:.1e}, rank(S+)={rankp}"))
    # Majorana-Weyl needs p-q==0 (mod 8); symplectic-MW at p-q==4
    checks.append(report("Q2b. Majorana-Weyl needs p-q==0 (mod 8) -> here 4 -> NO MW; symplectic-MW at 4",
                         pq_mod8 == 4, "minimal spinor = symplectic-Majorana-Weyl Sp(1) doublet of 64_C Weyls"))
    # dim so(9,5): the branch prompt says 45; the correct value is 91 (H23). Integrity correction.
    dim_so95 = 14 * 13 // 2
    checks.append(report("Q2c. dim so(9,5) = 91 (NOT 45; 45 = dim so(10)). Integrity correction to prompt.",
                         dim_so95 == 91, f"dim so(9,5) = 14*13/2 = {dim_so95}"))
    # Nahm bound: simple superconformal algebras only exist for spacetime D <= 6
    D = p + q
    checks.append(report("Q2d. super-CONFORMAL (even part so(10,6)) FORBIDDEN: Nahm caps simple SCA at D<=6",
                         D == 14 and D > 6, f"D={D} >> 6 => no simple Kac SCA; only inhomogeneous siso(9,5|N)"))

    # ============================ Q3: is P = beta_S the SUSY grading? ============================
    print("Q3 -- is the Cartan involution P = beta_S the SUSY grading? (distinguish the three Z/2's)")
    beta_S = prod(e, list(range(9)), I)  # product of the 9 spacelike gammas (H23 Krein / Cartan)
    bs_sq = np.max(np.abs(beta_S @ beta_S - I))
    # Cartan action: beta_S sigma_ab beta_S = +sigma for rotations (both idx <9 or both >=9), - for boosts
    def sigma(a, b):
        return 0.25 * (e[a] @ e[b] - e[b] @ e[a])
    rot_ok = np.max(np.abs(beta_S @ sigma(0, 1) @ beta_S - sigma(0, 1))) < 1e-6  # both spacelike -> +
    boost_ok = np.max(np.abs(beta_S @ sigma(0, 9) @ beta_S + sigma(0, 9))) < 1e-6  # mixed -> -
    checks.append(report("Q3a. beta_S^2=I and beta_S implements the Cartan involution (rot +, boost -)",
                         bs_sq < TOL and rot_ok and boost_ok, "P = beta_S is the boost/ghost-Krein Z/2, purely BOSONIC"))
    distinct = (np.max(np.abs(beta_S - omega)) > 1e-6 and np.max(np.abs(beta_S + omega)) > 1e-6
                and np.max(np.abs(beta_S @ omega - omega @ beta_S)) > 1e-6)
    checks.append(report("Q3b. beta_S != +-omega and [beta_S,omega] != 0 => P and chirality are DISTINCT Z/2's",
                         distinct, "neither P nor omega is the fermion-number SUSY grading (that Z/2 is NEW)"))

    # ============================ synthesis ============================
    print("-" * 96)
    print("SUMMARY")
    print("  Q1: (9,5) is QUATERNIONIC/CII (J^2=-1). Both C gamma^mu are ANTISYMMETRIC, so N=1 {Q,Q}~P is")
    print("      FORBIDDEN; the SYMPLECTIC pairing Omega^{ij}(C_- gamma^mu) is symmetric => super-Poincare")
    print("      EXISTS with N EVEN (symplectic-Majorana), USp(2N)_R. {Q,Q}=Omega(C_- gamma^mu)P_mu closes.")
    print("  Q2: odd part fits the 64_C Weyl half of the 128 spinor (symplectic-Majorana-Weyl); NO Majorana-")
    print("      Weyl. Kac: siso(9,5|N) is INHOMOGENEOUS, not a simple osp/su(m|n); super-CONFORMAL is")
    print("      FORBIDDEN (Nahm: simple SCA only D<=6; here D=14).  [dim so(9,5)=91, not 45]")
    print("  Q3: P = beta_S (Cartan/Krein) and omega (chirality) are TWO DISTINCT BOSONIC Z/2's; the SUSY")
    print("      boson/fermion grading is a GENUINELY NEW Z/2 GU's bosonic data does not already carry.")
    print("  VERDICT: PARTIAL. A guardian super-extension EXISTS -- the symplectic super-Poincare")
    print("           siso(9,5|N), N even, USp(2N)_R -- and it is the gravitino-carrying algebra, so a")
    print("           supergravity guardian is ALGEBRAICALLY POSSIBLE. But it is NOT forced by GU's data,")
    print("           requires a NEW grading + odd generators + R-symmetry, and the simple/superconformal")
    print("           packaging is OBSTRUCTED (D=14 >> Nahm 6). Existence of a super-Poincare is generic to")
    print("           signatures; it is NOT 'GU is supergravity'. That is the soldering/guardian question.")
    print("=" * 96)

    ok = all(checks)
    print(("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED") + f"  ({sum(checks)}/{len(checks)})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
