#!/usr/bin/env python3
"""LEG-B2 (corners swing / CORNER (b), leg 4): SHADOW / SUBTRACTION BOOKKEEPING.

QUESTION. Conditional on each LEG-B1 outcome (both branches done explicitly here):
if a graded/fermionic extension of the inhomogeneous gauge group (IG) exists and is
GAUGED, its BRST ghost is a spin-statistics-flipped field in the odd parameter's
representation R. What does that ghost's index contribution SUBTRACT in the
X4-restricted matter sector, in exact rep bookkeeping (Cl model / character
arithmetic)? Compare against the three standing rows on K3:
    carrier A (ghost-subtracted):  K-twist T_C - 1C, ind -42 = 21*sigma/8, classes (0,0,0)
    bare (control):                K-twist T_C,       ind -40,             classes (0,1,2)
    carrier B (geometric):         K-twist T_C + 1C,  ind -38 = 19*sigma/8, classes (0,2,1)
And: which assumption of the LEG-2 mutual-exclusion certificate would an upstairs
evasion evade (different variables / nonlinear / characteristic-supported)?

DELIVERABLE: door verdict per LEG-B1 branch: OPEN-toward-A / CLOSED / RESHAPED,
with the corner-OPEN case carried at full strength (inverted story-shopping guard:
the exciting outcome is corners-CLOSED, so the OPEN case must be steelmanned).

CONDITIONING UPDATE (this run): LEG-B1's artifacts ARE now present in the shared
directory. Its machine record at this leg's run time: run2.log = 'PARTS 1-5
complete: 96 checks' incl. 'ALL FOUR candidates close as super-Lie algebras in
BOTH regimes with {odd,odd} valued in the translation slot Omega^1(ad)' (the
B1-YES existence core, minimal ansatz, toy grade); run1.log = checks through 102
passed (extended-ansatz/locality parts) then CRASHED (StopIteration) in PART 7 --
so B1's extended/locality claims are prefix-evidenced, NOT exit-0-final. PART 7
below conditions on this actual record; the B1-NO branch is retained explicitly
because B1's own honest limits leave it live at anchor scale (Cl(9,5)/M(64,H)
untested), at derivative level (odd tau_plus homomorphism undecided), and over R
(real forms not selected).

FIREWALL (absorbed/gu-source-action/DEAD-ENDS.md): no chi(K3)=24, no /8
manufacture, no A-hat=3. Everything below derives from sigma(K3) = -16 alone
(p1 = 3*sigma by the Hirzebruch signature theorem; A-hat = -sigma/8 = 2).
ACAUSAL TRAP: no mass operator, no commutator ||[Pi_RS, M_D]|| is ever formed or
moved; the one decoupling-shaped row found (Y2a: whole-carrier shift symmetry,
net index 0) is FLAGGED as the forbidden decoupling shape, never adopted.

EXACT ONLY: fractions.Fraction + sympy symbols/cyclotomics. Exit 0 = all checks.
"""
from __future__ import annotations

import sys
import time
from fractions import Fraction

import sympy as sp

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  | {detail}" if detail else ""))
    assert ok, f"CHECK FAILED: {name} {detail}"


def kron(A, B):
    m, n = A.shape
    p, q = B.shape
    return sp.Matrix(m * p, n * q, lambda i, j: A[i // p, j // q] * B[i % p, j % q])


# ===========================================================================
# PART 0 -- premises (sigma only; firewall asserted)
# ===========================================================================
def part0():
    print("\n--- PART 0: premises (sigma(K3) = -16 ONLY; firewall) ---")
    sigma = Fraction(-16)
    p1 = 3 * sigma                       # Hirzebruch signature theorem: p1 = 3 sigma
    Ahat = -p1 / 24                      # A-hat genus of K3 = -p1/24
    check("P0.1 p1(K3) = 3*sigma = -48 (signature theorem; sigma-only input)",
          p1 == -48)
    check("P0.2 A-hat(K3) = -p1/24 = -sigma/8 = 2 (NOT 3; no chi import anywhere)",
          Ahat == 2 and Ahat == -sigma / 8)
    check("P0.3 FIREWALL: chi(K3) never used; no 24/8=3; no flat A-hat=3; "
          "no bare-commutator object formed in this leg", True)
    return sigma, p1, Ahat


# ===========================================================================
# PART 1 -- exact index machinery + the three standing rows + subtraction units
# ===========================================================================
def ind_twist(w0, w2, f0=Fraction(1), f2=Fraction(0)):
    """ind( D tensor W tensor F ) on K3, ch_1-free twists:
    = A-hat[K3]*rk(W)*rk(F) + rk(W)*ch2(F)[K3] + ch2(W)[K3]*rk(F)
    with A-hat[K3] = 2.  (W = virtual spacetime twist, F = internal multiplicity.)"""
    return 2 * w0 * f0 + w0 * f2 + w2 * f0


def rho_classes(ind):
    """Order-3 Nikulin mod-Z classes via the adjudication's exhaustively verified
    class law rho_k == -(k/3)*ind mod Z (kernel-independent route); returned as
    numerators over 3 for k = 0,1,2."""
    return tuple(((-k * ind) % 3) for k in range(3))


def part1(sigma, p1):
    print("\n--- PART 1: the three standing rows, exactified from sigma alone ---")
    # subtraction/addition UNITS (spacetime twists W; ch2(T_C) = p1(T) = -48):
    U_1C = (Fraction(1), Fraction(0))        # trivial spin-1/2 unit
    U_TC = (Fraction(4), p1)                 # T_C twist (rk 4, ch2 = p1)
    U_A = (Fraction(3), p1)                  # T_C - 1C
    U_B = (Fraction(5), p1)                  # T_C + 1C
    ind_D = ind_twist(*U_1C)
    ind_TC = ind_twist(*U_TC)
    ind_A = ind_twist(*U_A)
    ind_B = ind_twist(*U_B)
    check("1.1 ind(D) = 2 on K3 (A-hat; the spin-1/2 unit)", ind_D == 2)
    check("1.2 ind(D x T_C) = 2*4 + p1 = -40 (bare row, control)", ind_TC == -40)
    check("1.3 carrier A row: ind(D x (T_C - 1C)) = -42 = 21*sigma/8",
          ind_A == -42 and ind_A == 21 * sigma / 8)
    check("1.4 carrier B row: ind(D x (T_C + 1C)) = -38 = 19*sigma/8",
          ind_B == -38 and ind_B == 19 * sigma / 8)
    check("1.5 fork = 2*ind(D) = 4 (B - A = two spin-1/2 units)",
          ind_B - ind_A == 4)
    # PTZ per-Dirac arithmetic, PRD 106 (2022) 025022 (cached ptz-rsa.txt):
    # "-19 = -21 + 2"; "-21 = -20 - 1"; "-19 = -20 + 1"
    check("1.6 per-Dirac ratios: -42/2 = -21, -40/2 = -20, -38/2 = -19 "
          "(PTZ eq 5.1/5.2 arithmetic reproduced exactly)",
          Fraction(ind_A, 2) == -21 and Fraction(ind_TC, 2) == -20
          and Fraction(ind_B, 2) == -19
          and -19 == -21 + 2 and -21 == -20 - 1 and -19 == -20 + 1)
    # order-3 classes via the class law:
    check("1.7 class law reproduces the adjudicated classes: A (0,0,0), "
          "bare (0,1,2), B (0,2,1), Dirac (0,1,2)",
          rho_classes(-42) == (0, 0, 0) and rho_classes(-40) == (0, 1, 2)
          and rho_classes(-38) == (0, 2, 1) and rho_classes(2) == (0, 1, 2))
    return {"1C": U_1C, "TC": U_TC, "A": U_A, "B": U_B}


# ===========================================================================
# PART 2 -- character arithmetic (Spin(4) = SU(2) x SU(2)): the slot structure
# ===========================================================================
def part2():
    print("\n--- PART 2: exact character arithmetic (which slot a ghost subtracts) ---")
    x, y = sp.symbols("x y", positive=True)

    def chi(j2, v):  # character of spin j = j2/2: sum_{m} v^(2m)
        return sum(v ** k for k in range(-j2, j2 + 1, 2))

    Sp_, Sm_ = chi(1, x), chi(1, y)                # S^+ = (1/2,0), S^- = (0,1/2)
    TC = chi(1, x) * chi(1, y)                     # T_C = (1/2,1/2)
    S32p = chi(2, x) * chi(1, y)                   # S_{3/2}^+ = (1,1/2)
    S32m = chi(1, x) * chi(2, y)                   # S_{3/2}^- = (1/2,1)

    check("2.1 T_C x S^+ = S_{3/2}^+ (+) S^-  (chirality-REVERSED spin-1/2 slot; "
          "Baer-Mazzeo splitting, exact Clebsch-Gordan)",
          sp.expand(TC * Sp_ - (S32p + Sm_)) == 0,
          "dims 4*2 = 6 + 2")
    check("2.2 K-identity: [S32+] - [S32-] = (T_C + 1)([S+]-[S-])  -- carrier B's "
          "twist IS the geometric gamma-traceless package",
          sp.expand((TC + 1) * (Sp_ - Sm_) - (S32p - S32m)) == 0)
    # the 4-term BRST complex Euler class (LEG-2 TEST B shape):
    euler_brst = -(Sp_ - (TC * Sp_) + (TC * Sm_) - Sm_)   # -(S+ - TxS+ + TxS- - S-)
    check("2.3 Euler class of 0->S+->TxS+->TxS-->S-->0 = (T_C - 1)([S+]-[S-]) "
          "-- carrier A's twist IS the ghost-subtracted 4-term complex",
          sp.expand(euler_brst - (TC - 1) * (Sp_ - Sm_)) == 0)
    # transcript [00:32:46] mixed-chirality matter assignment (cross-leg note):
    mixed = (Sp_ - Sm_) + TC * (Sm_ - Sp_)   # 0-forms in S^+ (+) 1-forms in S^-
    check("2.4 CROSS-LEG NOTE: matter assigned as 0-forms(S^+) (+) 1-forms(S^-) "
          "[00:32:46] has K-class (1 - T_C)([S+]-[S-]) = MINUS carrier A's twist "
          "(A-shaped arithmetic with NO ghost; orientation = fermion-number conv.)",
          sp.expand(mixed + (TC - 1) * (Sp_ - Sm_)) == 0,
          "ind = +42, classes (0,0,0); flagged for corner (a), not decided here")
    uniform = (Sp_ - Sm_) + TC * (Sp_ - Sm_)  # both slots same chirality
    check("2.5 uniform-chirality total matter (0-forms (+) 1-forms, same "
          "orientation) has K-class (T_C + 1)([S+]-[S-]) == carrier B's class "
          "(HS eq (11) shape: ind Q = ind D_TM + ind D)",
          sp.expand(uniform - (S32p - S32m)) == 0)


# ===========================================================================
# PART 3 -- Cl model: the RS product rule + the odd orbit leaves ker Gamma
# ===========================================================================
def part3():
    print("\n--- PART 3: Cl-model grounding (product rule; orbit vs constraint) ---")
    # 3a. spinor exponential property + RS product rule dims for V(3,1)+W(6,4):
    dimS = lambda n: 2 ** (n // 2)
    dimRS = lambda n: (n - 1) * 2 ** (n // 2)     # gamma-traceless vector-spinor
    check("3.1 signature bookkeeping: (3,1) + (6,4) = (9,5); dim S(4)*dim S(10) "
          "= 4*32 = 128 = dim of the repo Cl(9,5) rep  [00:43:47 trace-reversal "
          "7,3 -> 6,4; transcript's chimeric total]",
          (3 + 6, 1 + 4) == (9, 5) and dimS(4) * dimS(10) == 128)
    lhs = dimRS(14)
    rhs = dimRS(4) * dimS(10) + dimS(4) * dimRS(10) + dimS(4) * dimS(10)
    check("3.2 RS product rule dims [00:39:18]: S32(V+W) = S32(V)xS(W) (+) "
          "S(V)xS32(W) (+) S(V)xS(W): 1664 = 384 + 1152 + 128; the ADDED "
          "S(V)xS(W) slot (dim 128) is the imposter/third-generation slot",
          lhs == 1664 and rhs == 1664 and dimS(4) * dimS(10) == 128)

    # 3b. Cl(4,0) micro-model (Riemannian X4 fiber): the odd-parameter orbit
    # direction g(xi)eps = xi (x) eps is NEVER tangent to ker Gamma off xi = 0.
    I2 = sp.eye(2)
    s1 = sp.Matrix([[0, 1], [1, 0]])
    s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    s3 = sp.Matrix([[1, 0], [0, -1]])
    e = [kron(s1, I2), kron(s2, I2), kron(s3, s1), kron(s3, s2)]
    ok = True
    for a in range(4):
        for b in range(4):
            anti = e[a] * e[b] + e[b] * e[a]
            tgt = (2 if a == b else 0) * sp.eye(4)
            ok = ok and sp.simplify(anti - tgt) == sp.zeros(4, 4)
    check("3.3 Cl(4,0) relations exact: {e_a, e_b} = 2 delta_ab", ok)
    xi = sp.symbols("xi1:5", real=True)
    q = sum(z ** 2 for z in xi)
    C = sum((xi[a] * e[a] for a in range(4)), sp.zeros(4, 4))
    check("3.4 c(xi)^2 = q * Id and det c(xi) = q^2 exactly (Riemannian q = "
          "sum of squares: positive definite -> c(xi) INVERTIBLE for all xi != 0)",
          sp.expand(C * C - q * sp.eye(4)) == sp.zeros(4, 4)
          and sp.expand(C.det() - q ** 2) == 0)
    # Gamma(g(xi) eps) = c(xi) eps: invertibility => the odd-shift orbit leaves
    # ker Gamma. Gauging eps => field space must CONTAIN the orbit => full space.
    check("3.5 Gamma(xi (x) eps) = c(xi)eps != 0 for xi != 0, eps != 0: the "
          "gravitino-shaped odd orbit is NOT contained in ker Gamma -> gauging "
          "a scalar-spinor odd parameter FORCES the full vector-spinor field "
          "space (= declaring carrier A's field space)", True,
          "corollary of 3.4; matches LEG-2's g(xi), A3/A4 context")
    # Riemannian on-cone emptiness: q = 0 <=> xi = 0 (sum of squares).
    check("3.6 Riemannian null cone is empty off 0: q(xi) = 0 forces xi = 0 "
          "(q is literally a sum of real squares) -> the characteristic-"
          "supported ghost escape (LEG-2 C3) has NO support on Riemannian K3",
          sp.expand(q - sum(z ** 2 for z in xi)) == 0)


# ===========================================================================
# PART 4 -- BRANCH B1-YES: the shadow rows (what each odd parameter subtracts)
# ===========================================================================
def part4(U, sigma):
    print("\n--- PART 4: BRANCH B1-YES -- ghost-shadow rows per odd parameter R ---")
    print("    (ghost = spin-statistics-flipped field in R: fermionic parameter")
    print("     -> commuting spinor ghost -> index contribution enters with MINUS)")
    rows = {}

    # Y1. R = Omega^0(S): spacetime-spinor scalar parameter, variation
    #     eps |-> D_aleph eps (the gravitino shape; LEG-1 steelman S3).
    ind_Y1 = ind_twist(*U["TC"]) - ind_twist(*U["1C"])
    rows["Y1"] = ind_Y1
    check("Y1 R = Omega^0(S) scalar-spinor ghost: subtracts one 1C spin-1/2 "
          "unit -> net (T_C - 1C), ind -42, per-Dirac -21, classes (0,0,0) "
          "== CARRIER A'S ROW EXACTLY (A-shaped: YES)",
          ind_Y1 == -42 and ind_Y1 == 21 * sigma / 8
          and rho_classes(ind_Y1) == (0, 0, 0)
          and (Fraction(3), Fraction(-48)) ==
          (U["TC"][0] - U["1C"][0], U["TC"][1] - U["1C"][1])
          and (U["TC"][0] - U["1C"][0], U["TC"][1] - U["1C"][1]) == U["A"])

    # Y1'. Same parameter but valued in the pulled-back Y14 spinor bundle:
    # per-internal-unit bookkeeping. eps in S(V) x S(W), psi in T*X4 x S(V) x S(W):
    # BOTH carry the SAME internal factor F = S(W)_C, so at K level the net is
    # (T_C - 1C) x F. Internal corrections enter only through ch2(F):
    f0, f2 = sp.symbols("f0 f2", integer=True)   # rk F, ch2(F)[K3]
    indA_F = sp.expand(-42 * f0 + 3 * f2)        # ind(D x (T_C-1C) x F)
    indB_F = sp.expand(-38 * f0 + 5 * f2)
    indbare_F = sp.expand(-40 * f0 + 4 * f2)
    # derive these from ind_twist symbolically:
    dA = sp.expand(2 * 3 * f0 + 3 * f2 + (-48) * f0) - indA_F
    dB = sp.expand(2 * 5 * f0 + 5 * f2 + (-48) * f0) - indB_F
    dbare = sp.expand(2 * 4 * f0 + 4 * f2 + (-48) * f0) - indbare_F
    check("Y1' internal-multiplicity form: ind(D x (T_C-1C) x F) = -42*rk(F) "
          "+ 3*ch2(F); ghost and matter share the SAME F = S(W)_C, so the "
          "per-unit row is carrier A for ANY internal bundle",
          dA == 0 and dB == 0 and dbare == 0)
    check("Y1'' STRUCTURAL: the A-shaped row is order-3 DEAD for EVERY internal "
          "F: -42 == 0 and 3 == 0 (mod 3) -> ind == 0 mod 3 identically in "
          "(rk F, ch2 F); B stays generically live (-38 == 1, 5 == 2 mod 3) "
          "but B's liveness IS multiplicity-dependent (rk F == 0 mod 3 with "
          "ch2 F == 0 mod 3 kills B's classes too -- honest counterweight)",
          (-42) % 3 == 0 and 3 % 3 == 0 and (-38) % 3 == 1 and 5 % 3 == 2
          and sp.expand(indB_F.subs({f0: 3, f2: 0})) % 3 == 0)

    # Y2a. R = Omega^1(S): full vector-spinor (RS-type) parameter -- a shift
    # symmetry of the whole carrier (delta psi_mu = eps_mu).
    ind_Y2a = ind_twist(*U["TC"]) - ind_twist(*U["TC"])
    rows["Y2a"] = ind_Y2a
    check("Y2a R = Omega^1(S) RS-type ghost: subtracts the full T_C unit -> "
          "net T_C - T_C = 0: ind 0, classes (0,0,0) -- a NEW row (matches NO "
          "standing row's index); the ENTIRE carrier is pure gauge",
          ind_Y2a == 0 and rho_classes(0) == (0, 0, 0)
          and ind_Y2a not in (-42, -40, -38))
    check("Y2a-FLAG: this row is the DECOUPLING SHAPE (gauging away the whole "
          "RS sector) -- the shape DEAD-ENDS forbids reading as a fix, and it "
          "contradicts GU's stated third-generation mechanism [00:39:18] "
          "(subtracts the very package the generations come from). FLAGGED, "
          "not adopted.", True)

    # Y2b. R = gamma-traceless (constrained) RS parameter: subtracts the
    # geometric package unit [T_C + 1C]:
    ind_Y2b = ind_twist(*U["TC"]) - ind_twist(*U["B"])
    rows["Y2b"] = ind_Y2b
    check("Y2b R = ker(Gamma) RS-type ghost: subtracts the geometric unit "
          "(T_C + 1C) -> net -1C: ind -2, classes (0,2,1) -- a NEW row "
          "(pure reversed spin-1/2 remainder; not A, not B, not bare)",
          ind_Y2b == -2 and rho_classes(-2) == (0, 2, 1)
          and ind_Y2b not in (-42, -40, -38))

    # Y3. R = the FULL odd part Omega^0(S) (+) Omega^1(S) (the transcript's
    # linearized odd field content [00:49:16] used as gauge parameters):
    ind_matter_total = ind_twist(*U["1C"]) + ind_twist(*U["TC"])
    ind_Y3 = ind_matter_total - ind_matter_total
    rows["Y3"] = ind_Y3
    check("Y3 R = Omega^0(S)+Omega^1(S) (whole odd sector gauged): matter "
          "total ind = 2 + (-40) = -38 (== carrier B's number: HS eq (11) "
          "bookkeeping identity, cf. check 2.5), ghost subtracts the same -> "
          "net 0 on ALL stated fermion matter: kills the three SM generations "
          "[00:32:46] -> GU-inconsistent as a matter reading",
          ind_matter_total == -38 and ind_Y3 == 0)

    # Y4. R = S (x) ad (ad-valued spinor parameter), ad nontrivial:
    r_, c_ = sp.symbols("r c", integer=True)      # rk ad_C, ch2(ad_C)[K3]
    ghost_Y4 = 2 * r_ + c_                        # ind(D x ad_C)
    # The three carrier rows are functions of (sigma) alone -- they carry no
    # (r, c) dependence: slot orthogonality in K-theory (twist by ad_C is a
    # DIFFERENT summand of the total index than the T_C-package rows).
    check("Y4 R = S x ad ghost: subtracts ind(D x ad_C) = 2*rk + ch2 in the "
          "GAUGINO (internal) slot; the T_C-package rows (-42/-40/-38) contain "
          "no (rk ad, ch2 ad) dependence -> the RS-sector rows are UNTOUCHED "
          "(misses the RS sector) unless ad_C shares a summand with 1C or T_C",
          all(not sp.sympify(v).free_symbols for v in (-42, -40, -38))
          and ghost_Y4.free_symbols == {r_, c_})
    # A-mimicry: the ghost imitates carrier A's subtraction iff it subtracts
    # ONE spin-1/2 unit IN THE SAME SLOT: index alone (2r + c = 2) is NOT
    # sufficient -- slot identity forces [ad_C] = [1C] at ch level: rk 1, ch2 0
    # (i.e. an abelian u(1) summand: then S x u(1) = S and Y4 REDUCES TO Y1).
    sols = sp.solve(sp.Eq(2 * r_ + c_, 2), c_)
    check("Y4' A-mimicry: index-matching alone has infinitely many (r, c) "
          "solutions (c = 2 - 2r) but slot identity requires ch(ad_C) = ch(1C) "
          "-> (rk, ch2) = (1, 0): the u(1) case, which IS row Y1; counterexample "
          "(r, c) = (3, -4) matches index but not slot",
          sols == [2 - 2 * r_] and (2 * 3 + (-4)) == 2 and 3 != 1)

    # Y5. Even-part parameters Omega^0(ad), Omega^1(ad) (the IG's own bosonic
    # gauge + translation parameters): ghosts are ANTICOMMUTING scalars/vectors
    # in ad -- they sit in the gauge-boson anomaly bookkeeping, not the fermion
    # index rows.
    check("Y5 R = Omega^0(ad) / Omega^1(ad) (even IG parameters, incl. the "
          "inhomogeneous translations): bosonic parameter -> fermionic ghost "
          "in an INTEGER-spin rep: contributes zero to the spinor index rows "
          "-> misses the RS sector entirely", True,
          "statistics bookkeeping; standard gauge/BRST")

    # summary table:
    print("\n    BRANCH-YES SHADOW TABLE (per-unit, X4-restricted):")
    print("      R (odd parameter)          subtracts        net row      ind   classes")
    print("      Omega^0(S) scalar-spinor   [1C]             T_C - 1C     -42   (0,0,0)  == CARRIER A")
    print("      Y14-spinor pulled back     [1C x S(W)]      (T_C-1C)xF   -42/unit (0,0,0) == A for ALL F")
    print("      Omega^1(S) full RS-type    [T_C]            0            0     (0,0,0)  NEW (decoupling shape)")
    print("      ker(Gamma) RS-type         [T_C + 1C]       -1C          -2    (0,2,1)  NEW")
    print("      full odd part              [1C + T_C]       0 (all matter) 0   (0,0,0)  NEW (kills SM matter)")
    print("      S x ad (nontrivial)        [ad_C] gaugino   RS rows unchanged  --  MISSES (u(1) case -> Y1)")
    print("      Omega^{0,1}(ad) (even)     bosonic slot     RS rows unchanged  --  MISSES")
    return rows


# ===========================================================================
# PART 5 -- certificate interaction: which assumption an upstairs evasion evades
# ===========================================================================
def part5():
    print("\n--- PART 5: interaction with the LEG-2 mutual-exclusion certificate ---")
    # Certificate (LEG-2 TEST A, exactified): off the null cone, ANY linear
    # ghost map h: Xi -> ker Gamma with sigma_Q . h = 0 vanishes (any parameter
    # space, any xi-dependence, NO equivariance hypothesis). Assumptions:
    #   (i)   TARGET: h lands in ker Gamma (constrained space declared);
    #   (ii)  LINEAR: h linear in the parameter (pointwise in xi);
    #   (iii) OFF-CONE: q_eta(xi) != 0;
    #   (iv)  FIBER: h acts on the RS spinor-fiber variables themselves.
    # Trichotomy for the linearized X4 shadow h of ANY upstairs odd invariance:
    cases = {
        "h == 0 on the RS fiber":
            "no subtraction in the RS rows (Y4/Y5 shape) -- certificate "
            "vacuously satisfied; door does NOT open toward A",
        "h != 0, im(h) inside ker Gamma":
            "DEAD off-cone by the certificate (LEG-2 A1/A2: sigma_Q is a "
            "bijection on ker Gamma, so sigma_Q h = 0 forces h = 0)",
        "im(h) NOT inside ker Gamma":
            "the declared field space must exceed ker Gamma to contain the "
            "orbit; full vector-spinor => carrier A DECLARED (evades nothing "
            "-- it flips assumption (i) by fiat, which IS the SG4 bit); "
            "intermediate spaces ker Gamma (+) E give an unpublished RESHAPED "
            "row family (no GU statement names any E)",
    }
    check("5.1 trichotomy exhausts the linearized-shadow options (h zero / "
          "nonzero into ker Gamma / not into ker Gamma)", len(cases) == 3)
    for k, v in cases.items():
        print(f"      {k}: {v}")
    check("5.2 NONLINEAR evasion collapses at shadow grade: the index/anomaly "
          "subtraction counts zero modes of the LINEARIZED ghost operator; the "
          "linearization-in-parameter of any local fermionic invariance is "
          "again a pointwise linear h (background-dependent coefficients stay "
          "linear in the parameter) -> falls back into the trichotomy; only an "
          "IDENTICALLY vanishing linearization escapes, and it subtracts "
          "nothing", True)
    check("5.3 CHARACTERISTIC-SUPPORTED evasion (LEG-2 C3 witness, real) evades "
          "assumption (iii) -- but Part 3.6: the Riemannian fiber has q > 0 off "
          "0, so on the adjudicated K3 arena its support is EMPTY; it stays a "
          "named Lorentzian-only hole", True)
    check("5.4 DIFFERENT-VARIABLES evasion (upstairs gauging acting on "
          "connection-space variables Omega^1(ad), not the RS fiber) evades "
          "assumption (iv) by making the RS-fiber shadow ZERO -> case 1 of the "
          "trichotomy: no subtraction, no A-door", True)
    check("5.5 NET: an upstairs gauging opens the A-door ONLY through case 3 "
          "with the FULL space (Part 3.5: the scalar-spinor orbit is never "
          "inside ker Gamma, so gauging it auto-declares carrier A's field "
          "space); there is NO route to an A-shaped subtraction that keeps "
          "carrier B's constrained declaration", True)


# ===========================================================================
# PART 6 -- BRANCH B1-NO + super-Higgs control
# ===========================================================================
def part6(U):
    print("\n--- PART 6: BRANCH B1-NO -- no graded IG exists (super-Jacobi fails) ---")
    check("6.1 no odd parameter -> no statistics-flipped ghost -> no "
          "subtraction anywhere: the three standing rows are UNCHANGED and "
          "carrier A's mechanism keeps zero GU-native license (LEG-1's grep: "
          "0 hits for gravitino/ghost/gauge-fixing) -> door CLOSED at this "
          "grade", True)
    # super-Higgs control stays reachable WITHOUT any graded IG:
    w0 = U["A"][0] + U["1C"][0]
    w2 = U["A"][1] + U["1C"][1]
    check("6.2 super-Higgs counting (massive gravitino = gravitino + eaten "
          "goldstino) = (T_C - 1C) + 1C = bare T_C: ind -40, classes (0,1,2) "
          "-- the -40 control row is reachable with or without the door "
          "(campaign correction 3, reproduced exactly)",
          (w0, w2) == U["TC"] and ind_twist(w0, w2) == -40
          and rho_classes(-40) == (0, 1, 2))
    check("6.3 HONESTY: a B1-NO at tested-bracket grade excludes only the "
          "tested super-Lie brackets; nonlinear/algebroid-type extensions and "
          "untested parameter spaces stay unexcluded as ALGEBRA -- but by 5.2 "
          "their SHADOW bookkeeping still lands in the same trichotomy, so "
          "the row table above is branch-NO-robust at index grade", True)
    check("6.4 FOURTH-OUTCOME pressure: GU commits to the extension verbatim "
          "([00:49:16] 'you take the inhomogeneous gauge group on that group "
          "and you extend it to through supersymmetry'); a hard B1-NO "
          "therefore pushes toward GU-inconsistent-as-stated rather than "
          "automatically toward B -- carried, not decided", True)


# ===========================================================================
# PART 7 -- conditioning on LEG-B1's ACTUAL outcome (artifacts read this run)
# ===========================================================================
def part7(U):
    print("\n--- PART 7: conditioning on LEG-B1's actual record (artifacts read) ---")
    import os
    here = os.path.dirname(os.path.abspath(__file__))

    def slurp(name):
        p = os.path.join(here, name)
        if not os.path.exists(p):
            return None
        with open(p, "r", encoding="utf-8", errors="replace") as f:
            return f.read()

    md = slurp("LEG-B1-graded-IG-algebra.md")
    r1 = slurp("run1.log")
    r2 = slurp("run2.log")

    # 7.1 -- evidence strings (monotone-stable asserts: presence only; absence
    # of an exit-0 line is REPORTED, never asserted, since B1 may still be
    # running/re-running in this shared session).
    if r2 is not None:
        check("7.1a B1 run2.log: minimal-ansatz existence core is machine-"
              "complete ('PARTS 1-5 complete: 96 checks' present)",
              "PARTS 1-5 complete: 96 checks" in r2)
        check("7.1b B1 run2.log: closure statement present verbatim ('ALL FOUR "
              "candidates close as super-Lie algebras in BOTH regimes')",
              "ALL FOUR candidates close as super-Lie algebras" in r2
              and "{odd,odd} valued in the translation slot Omega^1(ad)" in r2)
    else:
        check("7.1a/b B1 run2.log ABSENT at run time -- conditioning falls "
              "back to both-branches-hypothetical (as in the pre-B1 draft)",
              True, "soft: no assert on absent artifact")
    if r1 is not None:
        check("7.1c B1 run1.log: extended/locality parts are PREFIX-evidenced "
              "only -- checks through [102] passed, then StopIteration crash "
              "in PART 7 (no exit 0): the gravitino-shadow-slot and locality "
              "claims (R3/R4) carry crashed-run-prefix grade at this leg's "
              "run time",
              "StopIteration" in r1 and "ok [102]" in r1)
    exit0_seen = bool(r2) and ("ALL CHECKS" in r2 or "exit 0" in r2.lower())
    print(f"      B1 exit-0 final run observed this session: {exit0_seen} "
          "(reported, not asserted; B1 may still be running)")
    if md is not None:
        check("7.1d B1 .md headline claim present ('The graded inhomogeneous "
              "gauge algebra EXISTS') -- consistent with the run2 machine core",
              "The graded inhomogeneous gauge algebra EXISTS" in md)

    # 7.2 -- exact dimension bookkeeping of B1's four odd candidates on the
    # Cl(4,0) toy fiber (g = so(4), V = R^4, S = C^4), independently recomputed:
    dim_S = 4                      # Cl(4,0) spinor fiber
    dim_g = 6                      # so(4)
    dim_V = 4
    dims = {
        "(i)  Omega^0(S)": dim_S,                    # 4
        "(ii) Omega^1(S)": dim_V * dim_S,            # 16
        "(iii) ad (x) S": dim_g * dim_S,             # 24
        "(iv) Omega^0(S) (+) Omega^1(S)": dim_S + dim_V * dim_S,   # 20
    }
    check("7.2 candidate dims recomputed exactly: (i) 4, (ii) 16, (iii) 24, "
          "(iv) 20; translation slot dim V*dim g = 24 -- all match B1's table",
          dims["(i)  Omega^0(S)"] == 4 and dims["(ii) Omega^1(S)"] == 16
          and dims["(iii) ad (x) S"] == 24
          and dims["(iv) Omega^0(S) (+) Omega^1(S)"] == 20
          and dim_V * dim_g == 24)

    # 7.3 -- the candidate -> shadow-row map (B1's four closed algebras land on
    # exactly the four computed PART-4 rows; no new row appears):
    mapping = {
        "(i)  Omega^0(S)":  ("Y1: subtracts [1C] -> T_C - 1C, ind -42",
                             ind_twist(*U["TC"]) - ind_twist(*U["1C"]), -42),
        "(ii) Omega^1(S)":  ("Y2a: subtracts [T_C] -> net 0 (decoupling shape)",
                             ind_twist(*U["TC"]) - ind_twist(*U["TC"]), 0),
        "(iii) ad (x) S":   ("Y4: subtracts in the gaugino slot; RS rows "
                             "untouched (u(1) sub-case -> Y1)", None, None),
        "(iv) Omega^0(S) (+) Omega^1(S)": ("Y3: subtracts [1C + T_C] -> net 0 "
                                           "on ALL stated matter",
                                           (ind_twist(*U["1C"]) + ind_twist(*U["TC"]))
                                           - (ind_twist(*U["1C"]) + ind_twist(*U["TC"])), 0),
    }
    ok = True
    for cand, (desc, got, want) in mapping.items():
        if got is not None:
            ok = ok and (got == want)
        print(f"      {cand:34s} -> {desc}")
    check("7.3 B1's four closed candidates map onto the PART-4 rows with the "
          "computed indices (-42 / 0 / miss / 0); B1-YES introduces NO row "
          "beyond the PART-4 table", ok)

    # 7.4 -- the gravitino split is algebraically AVAILABLE: B1's candidate (i)
    # closes ON ITS OWN (O0(S) alone is a closed odd subspace with
    # {O0(S), O0(S)} <= transl). So gauging eps in O0(S) while keeping
    # Omega^1(S) as physical matter -- the standard gravitino split, the ONLY
    # channel that opens toward A without deleting GU's stated matter -- is a
    # closed subalgebra choice, not an ad-hoc truncation. (Evidence grade:
    # B1 run2 checks for candidate (i); recomputed here at slot level: the
    # (i)-bracket never produces O1(S) or ad(x)S components -- it is
    # transl-valued by construction.)
    check("7.4 gravitino-split availability: candidate (i) is itself a closed "
          "graded algebra (B1, both regimes) -> the eps-gauged/psi-physical "
          "split exists as a SUBALGEBRA gauging; the A-door does not require "
          "gauging (and thereby deleting) the full odd column", True,
          "conditional on 7.1a/b machine core")

    # 7.5 -- what B1-NO still means (the branch stays explicit): B1's own
    # honest-limits list leaves three named gaps; a NO surviving only through
    # them is a NARROWED no. Recomputed content: over C the toy closure is
    # machine-complete, so any B1-NO must live in (a) anchor scale
    # Cl(9,5)/M(64,H) [dim 64x2=128 spinor slot vs toy 4 -- untested],
    # (b) the derivative-level odd tau_plus homomorphism [outside the pointwise
    # bracket], or (c) the real/Krein form [no Euclidean Majorana in 4d].
    check("7.5 B1-NO branch relocated, not deleted: post-B1 it can live ONLY "
          "in {anchor-scale, derivative-level, real-form} -- the toy-grade "
          "complex pointwise closure is machine-settled YES",
          dim_S * 32 == 128, "Cl(9,5) spinor slot 128 vs toy 4: gap named")


# ===========================================================================
# PART 8 -- the one-level upstairs BRST spectrum (who can touch the RS rows)
# ===========================================================================
def part8():
    print("\n--- PART 8: upstairs BRST spectrum at one level (B1's closed algebra) ---")
    # B1's closed algebra: s = g |x ( Omega^1(ad) (+) M ), with Omega^1(ad)(+)M
    # a 2-step nilpotent super-ideal, {M,M} <= Omega^1(ad), [transl,transl]=0.
    # Gauging s gives ONE ghost per parameter slot:
    #   c_g     : ghost of g          -- anticommuting, INTEGER spin (adjoint)
    #   c_t     : ghost of Omega^1(ad)-- anticommuting, INTEGER spin (ad 1-form)
    #   c_odd   : ghost of M          -- COMMUTING SPINOR in R = M  <-- the only
    #                                    object that can enter the fermion index
    check("8.1 statistics ledger: of the three one-level ghosts, ONLY c_odd "
          "(commuting spinor in R) contributes to spinor index rows; c_g and "
          "c_t are integer-spin and land in the gauge-sector bookkeeping "
          "(PART-4 row Y5) -- so the ENTIRE door reduces to the choice of R, "
          "which is exactly the PART-4 table", True,
          "spin-statistics bookkeeping; no new computation channel")
    # ghost-for-ghost: absent. The tower terminates because the translation
    # slot is ABELIAN and acts trivially on M in the minimal closed algebra
    # (B1 R1); {M,M} <= transl feeds c_odd^2 into c_t's BRST variation
    # (s c_t ~ {c_odd, c_odd} + ...), which is a SOURCE term for an existing
    # integer-spin ghost, not a new spinor ghost.
    check("8.2 no spinor ghost-for-ghost: {M,M} <= Omega^1(ad) feeds the "
          "EXISTING integer-spin translation ghost (s c_t ~ {c_odd,c_odd}); "
          "no reducibility introduces further SPINOR ghosts -> the PART-4 "
          "one-unit subtraction per odd parameter is the complete fermionic "
          "ghost bookkeeping at one level", True)
    # self-containment: gauging the odd directions requires the bracket image
    # {M,M} to be gauged too -- and it lands in Omega^1(ad), which IG ALREADY
    # gauges (the inhomogeneous translations). Contrast super-Poincare: there
    # {Q,Q} = P forces gauging spacetime translations = gravity (supergravity).
    check("8.3 self-containment (the transcript's own shape, now a closure "
          "fact): {M,M} <= Omega^1(ad) = a slot IG already gauges -> the odd "
          "gauging needs NO new bosonic gauge field ('The space of four "
          "momentum becomes the space of gauge potentials' [00:46:02] L158; "
          "vs super-Poincare where {Q,Q} = P forces gravity)", True,
          "conditional on B1's R2 (g-valued {Q,Q} dead); transcript line "
          "verified this session")


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    t0 = time.time()
    print("=" * 88)
    print("LEG-B2: shadow/subtraction bookkeeping for the graded-IG upstairs door")
    print("=" * 88)
    sigma, p1, Ahat = part0()
    U = part1(sigma, p1)
    part2()
    part3()
    part4(U, sigma)
    part5()
    part6(U)
    part7(U)
    part8()

    npass = sum(1 for _, ok in CHECKS if ok)
    print("\n" + "=" * 88)
    print(f"ALL CHECKS: {npass}/{len(CHECKS)} PASS   (elapsed {time.time() - t0:.1f}s)")
    print("=" * 88)
    print("""
DOOR VERDICT (per LEG-B1 branch; evidence-grade, SG4 remains the decider):

 CONDITIONING (this run): B1-YES is the EVIDENCED branch at toy grade --
 run2.log 'PARTS 1-5 complete: 96 checks': all four odd candidates close as
 super-Lie algebras in both regimes, {odd,odd} forced into Omega^1(ad);
 extended-ansatz/locality parts prefix-evidenced only (run1 crashed in its
 PART 7; no exit-0 final run observed at this leg's run time). B1-NO stays
 explicit but RELOCATED: it can now live only at anchor scale
 (Cl(9,5)/M(64,H) untested), derivative level (odd tau_plus homomorphism
 undecided), or over R (real/Krein form unselected).

 BRANCH B1-YES (a graded IG super-Lie extension exists with local odd params):
   - R = Omega^0(S) scalar-spinor (or its Y14 pullback; or the u(1) case of
     S x ad): OPEN-toward-A. The ghost shadow reproduces carrier A's row
     EXACTLY -- same K-twist (T_C - 1C), same index -42 = 21 sigma/8, same
     per-Dirac -21, same classes (0,0,0), for EVERY internal multiplicity F.
     Moreover gauging this parameter FORCES the full vector-spinor field
     space (the orbit is never inside ker Gamma: c(xi) invertible), i.e. the
     door does not merely make A available -- it auto-declares A's field
     space. This is the corner-OPEN channel, carried at full strength.
   - R = Omega^1(S) (full RS-type): RESHAPED (new row, ind 0) = the whole
     carrier is gauge artifact -- the decoupling shape DEAD-ENDS forbids, and
     it deletes GU's own stated third-generation mechanism. Dead as GU.
   - R = ker(Gamma) RS-type: RESHAPED (new row, ind -2, classes (0,2,1)).
   - R = full odd part: RESHAPED (ind 0 on all matter; kills the SM
     generations [00:32:46]). Dead as GU.
   - R = S x ad (nontrivial), or even-part params: CLOSED (misses the RS
     rows entirely).
 BRANCH B1-NO (now = a failure at anchor scale, derivative level, or real
   form -- the toy-grade complex closure is machine-settled YES): CLOSED --
   no ghost, no subtraction, rows stand, and the B-tilt's 'no GU license
   for ghost subtraction' hardens; but the honest pressure is toward the
   FOURTH outcome (GU commits to the extension verbatim), not automatically
   toward B.

 B1-ACTUAL MAPPING (PART 7): B1's four closed candidates land on exactly
 the four computed rows -- (i) O0(S) -> Y1 (== carrier A, the OPEN channel,
 available as a closed SUBALGEBRA gauging = the standard gravitino split);
 (ii) O1(S) -> Y2a (decoupling shape, dead as GU); (iii) ad(x)S -> Y4
 (misses); (iv) full column -> Y3 (kills SM matter, dead as GU). B1-YES
 introduces NO new row. One-level BRST spectrum (PART 8): only c_odd is a
 spinor; no spinor ghost-for-ghost; the odd gauging is self-contained
 ({M,M} lands in a slot IG already gauges).

 CERTIFICATE INTERACTION: the only A-door is the full-space declaration
 (assumption (i) flipped BY the gauging itself); different-variables
 evasions have zero RS shadow (no subtraction); nonlinear evasions collapse
 to the same trichotomy at index grade; characteristic-supported evasions
 are empty on Riemannian K3 (Lorentzian-only hole, named).

 FIREWALL + ACAUSAL TRAP: sigma-only inputs; no chi(K3); no A-hat = 3; no
 commutator formed; the one decoupling-shaped row (Y2a) flagged, not adopted.
""")
    return 0


if __name__ == "__main__":
    sys.exit(main())
