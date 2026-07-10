# -*- coding: utf-8 -*-
"""
LEG-3: UNGAUGED-CONSISTENCY -- is carrier B itself consistent as GU matter?

Three parts:
  (i)   RIEMANNIAN: the ungauged Rarita-Schwinger operator on Ricci-flat/hyperkahler
        manifolds is published, well-defined mathematics (cache-verified verbatim
        anchors from Homma-Semmelmann arXiv:1804.10602 and Baer-Mazzeo arXiv:2003.11255,
        plus exact arithmetic coherence of the published K3 numbers).
  (ii)  LORENTZIAN/DYNAMICAL: exact finite Velo-Zwanziger characteristic computation
        in the 4d Clifford model for the massive, minimally coupled Rarita-Schwinger
        field on a constant magnetic background. Machine-reproduces the published
        critical field B = 3 m^2 / (2 e) (Deser-Pascalutsa-Waldron hep-th/0003011,
        "the well known result of [5,6]", [6] = Velo-Zwanziger PR 186 (1969) 1337).
        Plus the structural fact: the acausal jump is purely LONGITUDINAL and carries
        nonzero gamma-trace -- it lives outside carrier B's field space ker(Gamma).
  (iii) MASSLESS-CHIRAL TENSION: needle-verified transcript + canon quotes feeding
        the reconciliation analysis in LEG-3-ungauged-consistency.md (no computation
        can decide (iii); it is a reading fork parked on SG4).

GUARDS (stated, enforced by construction):
  * ACAUSAL TRAP (DEAD-ENDS): this leg touches NO repo dynamics. The bare commutator
    ||[Pi_RS, M_D]|| = 58.72 is not computed, not approximated, not driven anywhere.
    The 4d VZ model below is the standalone published system, not the repo substrate.
  * FIREWALL: no chi(K3)=24, no A-hat=3, no manufactured /8. The only /8 that appears
    is inside the verbatim published Prop 3.1(i) of Homma-Semmelmann, quoted as text.
  * STORY-SHOPPING: every carrier-B-favoring check is paired with the surviving
    carrier-A case (printed at the end and elaborated in the .md).

Exit 0 iff every check passes. sympy exact arithmetic throughout (no floats).
"""

import sys, os, unicodedata
from fractions import Fraction
import sympy as sp
from sympy import I, Rational, Matrix, zeros, eye, symbols, factor, expand, solve

SCRATCH = r"C:\Users\joe\AppData\Local\Temp\claude\C--Users-joe-JB\79411e9e-5aaa-44a7-ba95-2f380675a349\scratchpad"
CBS = os.path.join(SCRATCH, "carrier-bit-swing")
SYM = os.path.join(SCRATCH, "symbol-swing")
REPO = r"C:\Users\joe\JB\CapacityOS\repos\public\gu-formalization"

CHECKS = []
def check(name, cond, detail=""):
    CHECKS.append((name, bool(cond)))
    status = "PASS" if cond else "FAIL"
    print(f"[{status}] {name}" + (f"  :: {detail}" if detail else ""))
    if not cond:
        print("  ^^^ HARD FAIL")
    return bool(cond)

# ----------------------------------------------------------------------------
# Text-anchor machinery: normalized substring search on cached fetched texts.
# Normalization: strip ALL whitespace, unify unicode minus/quotes, expand fi/fl
# ligatures, drop diaeresis marks. Needles are written in the same normal form.
# ----------------------------------------------------------------------------
def normalize(s):
    s = s.replace("ﬁ", "fi").replace("ﬂ", "fl")
    s = s.replace("−", "-").replace("’", "'").replace("”", '"').replace("“", '"')
    s = s.replace("¨", "")  # diaeresis artifact from pdftotext ("hyperk¨ ahler")
    return "".join(s.split())

def load(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return normalize(f.read())

def needle(name, hay, s, src):
    return check(name, normalize(s) in hay, f"verbatim anchor present in {src}")

print("=" * 78)
print("PART A -- RIEMANNIAN HOME TURF (published, cache-verified)")
print("=" * 78)

hs = load(os.path.join(SYM, "hs2018.txt"))
bm = load(os.path.join(SYM, "baer-mazzeo.txt"))
hm = load(os.path.join(CBS, "hack-makedonski.txt"))

# A1: the operator is DEFINED with no gauge symmetry anywhere -- pure spin geometry.
needle("A1a HS definition of Q (projection of twisted Dirac, no gauge structure)",
       hs, "The operator Q : Γ(S 3/ 2) → Γ(S 3/ 2) with Q = pr S3/ 2 ◦ DT M|Γ(S 3/ 2) is called Rarita-Schwinger",
       "hs2018.txt (arXiv:1804.10602, Sec. 2)")
needle("A1b HS: RS field = P*psi=0 and Q psi=0 (constraint definitional, not gauge-fixed)",
       hs, "In the physics literature a Rarita-Schwinger field is a section ψ of S 3/ 2 satisfying the equations P ∗ψ = 0 and Qψ = 0",
       "hs2018.txt Sec. 2")
# A2: the index formula needs NO curvature hypothesis at all (not even Einstein).
needle("A2a HS index section drops the Einstein hypothesis",
       hs, "In this section we do not have to assume the metric g to be Einstein",
       "hs2018.txt Sec. 3")
needle("A2b HS eq (11): ind Q = A-hat(TM)(ch(TM_C)+1)[M] = ind D_TM + ind D",
       hs, "(11) ind Q = ˆA(TM ) (ch(TM C) + 1)[M] = ind DT M + ind D",
       "hs2018.txt eq (11)")
needle("A2c HS Prop 3.1(i): n=4: ind Q = -19 A-hat(M) = 19/8 sigma(M)",
       hs, "n = 4 : ind Q = − 19 ˆA(M) = 19 8 σ(M)",
       "hs2018.txt Prop 3.1(i)")
# A3: ghost subtraction is the OTHER convention -- supergravity's, explicitly.
needle("A3a HS Rem 3.6: ghost subtraction motivated by gauge modes",
       hs, "discarding zero modes that ca n be gauged away or that violate gauge conditions",
       "hs2018.txt Rem 3.6 (quoting Witten [43] p.252)")
needle("A3b HS Rem 3.6: cancelled by spin-1/2 ghost fields",
       hs, "cancelled by zero modes of the spin 1 2 ghost fields",
       "hs2018.txt Rem 3.6")
needle("A3c HS Rem 3.6: subtract the spin-1/2 ghost index (supergravity convention)",
       hs, "subtract from index of the Rarit a-Schwinger field the corresponding index of the spin 1 2 ghosts",
       "hs2018.txt Rem 3.6")
# A4: K3 -- carrier B's arena -- has a completely computed, sharp kernel.
needle("A4a HS Example (1): K3, dim ker Q = 2h^{1,1} - 2 = 38",
       hs, "n = 2 : then M is a K3 surface and it follows from Proposition 4.6 that dim kerQ = 2h1, 1 − 2 = 38",
       "hs2018.txt Example to Prop 4.6")
needle("A4b HS: K3 RS fields = two copies of harmonic primitive (1,1)-forms",
       hs, "the space of Rarita-Schwinger fields is isomorphic to two copies of the space of harmonic primitive (1 , 1)-forms",
       "hs2018.txt Example to Prop 4.6")
needle("A4c HS 4.7: hyperkahler manifolds are spin, Ricci-flat, Q^2 = standard Laplacian",
       hs, "hyperk¨ ahler manifolds are spin, Ricci-flat and Q2 coincides with the standard Laplace operator",
       "hs2018.txt Sec. 4.7")
needle("A4d Baer-Mazzeo abstract: ungauged geometric definition (divergence-free 3/2-spinors)",
       bm, "The Rarita-Schwinger operator is the twisted Dirac operato r re- stricted to 3/2-spinors",
       "baer-mazzeo.txt (arXiv:2003.11255) abstract")
needle("A4e Baer-Mazzeo Rem 5.3: RS(K3) = 38, sharp",
       bm, "This is sharp; indeed RS(K3) = 38",
       "baer-mazzeo.txt Rem 5.3")
# A5: Hack-Makedonski -- the curved-background consistency window for the UNGAUGED field.
needle("A5a HM: consistency forces Einstein backgrounds (background restriction, not gauging)",
       hm, "We find that this is impossible as all couplings require th e background to be an Einstein spacetime for consistency",
       "hack-makedonski.txt (arXiv:1106.6327) abstract")
needle("A5b HM restating Buchdahl 1958: psi = 0 unless Einstein spacetime",
       hm, "this equation can only be satisfied by ψ ≡ 0 unless the spacetime is an Einstein spacetime",
       "hack-makedonski.txt Sec. 1 (Buchdahl, Nuovo Cim. 10 (1958) 96)")

# A6: exact arithmetic coherence of the published K3 numbers (Fraction, no floats).
# Inputs (published): h^{1,1}(K3) = 20, sigma(K3) = -16 (standard); HS Prop 4.6 n=2.
h11 = 20; sigma_K3 = -16
dimker = 2 * h11 - 2                      # HS Prop 4.6: dim ker Q = -2 + 2*h^{1,1}
indQ_46 = 2 + 2 * (-1) ** 1 * h11         # HS Prop 4.6: ind Q = 2 + 2*sum (-1)^p h^{1,p}
indQ_31 = Fraction(19, 8) * sigma_K3      # HS Prop 3.1(i) applied to published sigma(K3)
check("A6a HS Prop 4.6 on K3: dim ker Q = 38", dimker == 38, f"2*{h11}-2 = {dimker}")
check("A6b HS Prop 4.6 on K3: ind Q = -38", indQ_46 == -38, f"2-2*{h11} = {indQ_46}")
check("A6c coherence with Prop 3.1(i): (19/8)*sigma(K3) = -38 = ind Q",
      indQ_31 == Fraction(-38) and indQ_31 == indQ_46,
      "published formula x published signature; nothing manufactured")
check("A6d |ind Q| = dim ker Q on K3 (kernel one-sided; matches canon carrier-B row -38)",
      abs(indQ_46) == dimker)

# ----------------------------------------------------------------------------
print()
print("=" * 78)
print("PART B -- 4d CLIFFORD EXACT: the free massive UNGAUGED RS field is")
print("self-constraining matter (no gauge symmetry needed for its constraints)")
print("=" * 78)

# Dirac representation, eta = diag(+,-,-,-). All entries exact Gaussian rationals.
s1 = Matrix([[0, 1], [1, 0]]); s2 = Matrix([[0, -I], [I, 0]]); s3 = Matrix([[1, 0], [0, -1]])
def blk(A, B, C, D):
    return Matrix(sp.BlockMatrix([[A, B], [C, D]])).as_explicit() if False else Matrix.vstack(
        Matrix.hstack(A, B), Matrix.hstack(C, D))
Z2 = zeros(2, 2); I2 = eye(2)
g0 = blk(I2, Z2, Z2, -I2)
gam = [g0] + [blk(Z2, s, -s, Z2) for s in (s1, s2, s3)]  # gamma^mu, UPPER index
eta = sp.diag(1, -1, -1, -1)

ok = True
for mu in range(4):
    for nu in range(4):
        ok &= (gam[mu] * gam[nu] + gam[nu] * gam[mu] == 2 * eta[mu, nu] * eye(4))
check("B1a Clifford relations {gamma^mu, gamma^nu} = 2 eta^{mu nu}", ok)

import itertools
def perm_sign(perm):
    sgn = 1
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] > perm[j]:
                sgn = -sgn
    return sgn

def gamma_anti(idx):
    """Fully antisymmetrized product gamma^{i1 i2 ...} (upper indices)."""
    n = len(idx); out = zeros(4, 4)
    for perm in itertools.permutations(range(n)):
        sgn = perm_sign(perm)
        M = eye(4)
        for p in perm:
            M = M * gam[idx[p]]
        out += sgn * M
    return out / sp.factorial(n)

G2 = [[gamma_anti((m, n)) for n in range(4)] for m in range(4)]
G3 = [[[gamma_anti((m, n, r)) for r in range(4)] for n in range(4)] for m in range(4)]
gam_lower = [eta[m, m] * gam[m] for m in range(4)]

ok1 = all(sum((gam_lower[m] * G2[m][n] for m in range(4)), zeros(4, 4)) == 3 * gam[n]
          for n in range(4))
ok2 = all(sum((gam_lower[m] * G3[m][n][r] for m in range(4)), zeros(4, 4)) == 2 * G2[n][r]
          for n in range(4) for r in range(4))
ok3 = all(sum((G3[m][n][r] * gam_lower[r] for r in range(4)), zeros(4, 4)) == 2 * G2[m][n]
          for m in range(4) for n in range(4))
check("B1b gamma_mu gamma^{mu nu} = 3 gamma^nu (n-1 factor, n=4)", ok1)
check("B1c gamma_mu gamma^{mu nu rho} = 2 gamma^{nu rho} (n-2 factor)", ok2)
check("B1d gamma^{mu nu rho} gamma_rho = 2 gamma^{mu nu} (n-2 factor)", ok3)

# --- B2: exact operator-calculus derivation of the secondary constraint --------
# Field: psi_rho (lower index), stacked as 16-vector, component (rho, s) -> 4*rho+s.
# EOM:  R^mu = i gamma^{mu nu rho} D_nu psi_rho + a m gamma^{mu rho} psi_rho,  a = +-1.
# Operator calculus: D_mu D_nu = S_{(mu nu)} + (i e / 2) F_{mu nu},
# with [D_mu, D_nu] = i e F_{mu nu} (constant background F, symbolic entries).
m_, e_, c_, B_ = symbols("m e c B", positive=None)
Fs = {}
for mu in range(4):
    for nu in range(mu + 1, 4):
        Fs[(mu, nu)] = symbols(f"F{mu}{nu}")
def Fsym(mu, nu):
    if mu == nu: return sp.Integer(0)
    return Fs[(mu, nu)] if mu < nu else -Fs[(nu, mu)]

def hblocks(mats):  # list of 4 (4x4) blocks over rho -> 4x16
    return Matrix.hstack(*mats)

def run_constraint(a):
    # R^mu = sum_nu G1[mu][nu] D_nu psi + G0[mu] psi   (each 4x16)
    G1 = [[hblocks([I * G3[mu][nu][rho] for rho in range(4)]) for nu in range(4)]
          for mu in range(4)]
    G0 = [hblocks([a * m_ * G2[mu][rho] for rho in range(4)]) for mu in range(4)]
    # D.R = D_mu R^mu :
    #   second order:  sum G1[mu][nu] (S_{mu nu} + (i e/2) F_{mu nu})
    #   first order :  sum G0[mu] D_mu
    Scoef = {}
    for mu in range(4):
        for nu in range(4):
            key = (min(mu, nu), max(mu, nu))
            Scoef[key] = Scoef.get(key, zeros(4, 16)) + G1[mu][nu]
    Fconst = zeros(4, 16)
    for mu in range(4):
        for nu in range(4):
            Fconst += Rational(1, 2) * I * e_ * Fsym(mu, nu) * G1[mu][nu]
    Dcoef_DR = {nu: G0[nu] for nu in range(4)}
    # gamma.R = gamma_mu R^mu :
    A1 = {nu: sum((gam_lower[mu] * G1[mu][nu] for mu in range(4)), zeros(4, 16))
          for nu in range(4)}
    A0 = sum((gam_lower[mu] * G0[mu] for mu in range(4)), zeros(4, 16))
    # combination  C = D.R + c m gamma.R : demand ALL derivative terms vanish
    okS = all(M == zeros(4, 16) for M in Scoef.values())
    eqs = []
    for nu in range(4):
        Mat = Dcoef_DR[nu] + c_ * m_ * A1[nu]
        eqs.extend([sp.expand(x) for x in Mat])
    sol = solve([sp.Eq(x, 0) for x in eqs if x != 0], c_, dict=True)
    okC = (len(sol) == 1)
    cstar = sol[0][c_] if okC else None
    const_term = sp.expand(Fconst + cstar * m_ * A0) if okC else None
    return okS, cstar, const_term

okS_p, c_p, C_p = run_constraint(+1)
okS_m, c_m, C_m = run_constraint(-1)
check("B2a second-derivative (S) coefficients vanish identically (both mass signs)",
      okS_p and okS_m, "antisymmetry of gamma^{mu nu rho}: no d^2 residue")
check("B2b unique c kills ALL first-derivative terms: c = i a/2",
      c_p == I / 2 and c_m == -I / 2, f"c(+1)={c_p}, c(-1)={c_m}")
check("B2c the algebraic secondary constraint is mass-sign independent",
      sp.expand(C_p - C_m) == zeros(4, 16))

# The constraint:  C = -(e/2) gamma^{mu nu rho} F_{mu nu} psi_rho + (3 i/2) m^2 gamma.psi = 0
Gtrace = hblocks([gam[rho] * eta[rho, rho] for rho in range(4)])   # gamma.psi = gamma^rho psi_rho
# NOTE index care: psi_rho carries a LOWER index; gamma.psi = gamma^rho psi_rho needs
# UPPER gamma^rho contracted with lower psi_rho -> blocks gam[rho] (upper) ... but our
# G-blocks were built with all-upper gammas against lower psi: consistent contraction
# gamma^{...rho} psi_rho. For the trace use gam[rho] directly:
Gtrace = hblocks([gam[rho] for rho in range(4)])
C_expected = zeros(4, 16)
for mu in range(4):
    for nu in range(4):
        C_expected += -Rational(1, 2) * e_ * Fsym(mu, nu) * hblocks(
            [G3[mu][nu][rho] for rho in range(4)])
C_expected += Rational(3, 2) * I * m_ ** 2 * Gtrace
check("B2d constraint = -(e/2) gamma^{mnr} F_{mn} psi_r + (3i/2) m^2 gamma.psi",
      sp.expand(C_p - C_expected) == zeros(4, 16))
check("B2e F -> 0: constraint forces gamma.psi = 0 EXACTLY (rank 4 trace map)",
      Gtrace.rank() == 4,
      "the free massive UNGAUGED RS field enforces carrier B's field space ON-SHELL")

# --- B3: free DOF certificate at rest-frame momentum ---------------------------
# Plane wave psi = u exp(-i p.x): D_nu -> -i p_nu (F=0). Symbol:
#   M(p) = gamma^{mu nu rho} p_nu + a m gamma^{mu rho}  (i's cancel)
def free_symbol(p_lower, a, mval):
    rows = []
    for mu in range(4):
        row = zeros(4, 16)
        for nu in range(4):
            if p_lower[nu] != 0:
                row += p_lower[nu] * hblocks([G3[mu][nu][rho] for rho in range(4)])
        row += a * mval * hblocks([G2[mu][rho] for rho in range(4)])
        rows.append(row)
    return Matrix.vstack(*rows)

dims = {}
for a in (+1, -1):
    Msym = free_symbol([1, 0, 0, 0], a, 1)   # p = (m,0,0,0), m=1 exact
    ker = Msym.nullspace()
    dims[a] = len(ker)
    if ker:
        okg = all(sp.simplify(Gtrace * v) == zeros(4, 1) for v in ker)
        ok0 = all(all(sp.simplify(v[s]) == 0 for s in range(4)) for v in ker)  # u_0 = 0
        check(f"B3a a={a:+d}: kernel gamma-traceless AND transverse (u_0 = 0)", okg and ok0)
check("B3b free massive RS: 4 polarizations per energy sign (2s+1 = 4, s = 3/2)",
      dims[+1] == 4 and dims[-1] == 4, f"dim ker = {dims}")

# ----------------------------------------------------------------------------
print()
print("=" * 78)
print("PART C -- EXACT VZ CHARACTERISTIC COMPUTATION (minimal coupling, constant B)")
print("=" * 78)
# Jump analysis (Courant-Hilbert discontinuities, as in DPW sec. 4):
#   [d_nu psi_rho] = xi_nu Psi_rho across the characteristic surface.
#   J1 (jump of the EOM, first-order part):   gamma^{mu nu rho} xi_nu Psi_rho = 0
#   J2 (jump of the DIFFERENTIATED secondary constraint, constant F):
#       -(e/2) gamma^{mnr} F_{mn} Psi_r + (3i/2) m^2 gamma.Psi = 0
# Timelike xi admits a nonzero jump  <=>  the constrained system degenerates.

def J1_of_xi(xi_lower):
    rows = []
    for mu in range(4):
        row = zeros(4, 16)
        for nu in range(4):
            if xi_lower[nu] != 0:
                row += xi_lower[nu] * hblocks([G3[mu][nu][rho] for rho in range(4)])
        rows.append(row)
    return Matrix.vstack(*rows)

# C1: timelike xi = (1,0,0,0)
J1t = J1_of_xi([1, 0, 0, 0])
kerJ1 = J1t.nullspace()
long_basis = []
for s in range(4):
    v = zeros(16, 1); v[s] = 1        # Psi_rho = xi_rho eps  (xi lower = (1,0,0,0))
    long_basis.append(v)
span_test = Matrix.hstack(*(kerJ1 + long_basis))
check("C1a timelike xi: ker(J1) is exactly the LONGITUDINAL modes Psi_rho = xi_rho eps",
      len(kerJ1) == 4 and span_test.rank() == 4,
      f"dim ker = {len(kerJ1)}, joint rank = {span_test.rank()}")
stacked = Matrix.vstack(J1t, Gtrace)
check("C1b ker(J1) ^ ker(gamma-trace) = 0 at timelike xi",
      stacked.rank() == 16,
      "every candidate acausal jump carries NONZERO gamma-trace: it lives OUTSIDE ker(Gamma)")

# C2: null control xi = (1,0,0,1): genuine (light-cone) characteristics are bigger
J1n = J1_of_xi([1, 0, 0, 1])
kerJ1n = len(J1n.nullspace())
check("C2 null xi control: characteristic kernel strictly larger than longitudinal",
      kerJ1n > 4, f"dim ker(J1)|null = {kerJ1n} > 4")

# C3: constant magnetic field along z: F_{12} = B (all other components 0).
# J2 restricted to the longitudinal modes -> 4x4 critical matrix on eps:
#   K(B) = -e B gamma^{120} + (3i/2) m^2 gamma^0
K = -e_ * B_ * G3[1][2][0] + Rational(3, 2) * I * m_ ** 2 * gam[0]
detK = sp.factor(K.det())
expected = sp.factor((Rational(9, 4) * m_ ** 4 - e_ ** 2 * B_ ** 2) ** 2)
check("C3a det K(B) = (9/4 m^4 - e^2 B^2)^2  EXACTLY",
      sp.simplify(detK - expected) == 0, f"det K = {detK}")
sols = solve(sp.Eq(detK, 0), B_)
check("C3b real zeros exactly at |B| = 3 m^2 / (2 e)",
      set(sols) == {Rational(3, 2) * m_ ** 2 / e_, -Rational(3, 2) * m_ ** 2 / e_},
      f"B = {sols}  [matches DPW hep-th/0003011: 'B2 = (3m2/2e)2 ... the well known "
      f"result of [5, 6]', [6] = Velo-Zwanziger, Phys. Rev. 186, 1337 (1969)]")
check("C3c free-field control: B = 0 => det K = (81/16) m^8 != 0 (no timelike front)",
      sp.simplify(detK.subs(B_, 0) - Rational(81, 16) * m_ ** 8) == 0)
check("C3d subcritical control: B = m^2/e => det K != 0",
      sp.simplify(detK.subs(B_, m_ ** 2 / e_)) == Rational(25, 16) * m_ ** 8)
Kcrit = K.subs({e_: 1, m_: 1, B_: Rational(3, 2)})
check("C3e critical instance (e=1, m=1, B=3/2): rank K drops 4 -> 2",
      Kcrit.rank() == 2, f"rank = {Kcrit.rank()}")

# C4: full stacked jump system [J1; J2] on the 16-dim jump space, exact ranks.
def J2_of_B(eval_, mval, Bval):
    out = zeros(4, 16)
    F = {(1, 2): Bval}
    for (mu, nu), val in F.items():
        out += -Rational(1, 2) * eval_ * val * (
            hblocks([G3[mu][nu][rho] for rho in range(4)])
            - hblocks([G3[nu][mu][rho] for rho in range(4)]))
    out += Rational(3, 2) * I * mval ** 2 * Gtrace
    return out

full_sub = Matrix.vstack(J1t, J2_of_B(1, 1, 1))                    # subcritical
full_crit = Matrix.vstack(J1t, J2_of_B(1, 1, Rational(3, 2)))      # critical
check("C4a subcritical B: stacked [J1; J2] rank 16 -> jump = 0 (causal sector)",
      full_sub.rank() == 16)
check("C4b critical B = 3m^2/2e: stacked [J1; J2] rank 14 < 16 -> NONZERO timelike jump exists",
      full_crit.rank() < 16, f"rank = {full_crit.rank()}")

# ----------------------------------------------------------------------------
print()
print("=" * 78)
print("PART D -- PUBLISHED-TEXT ANCHORS FOR (ii) AND (iii) (needle-verified)")
print("=" * 78)

pr = load(os.path.join(CBS, "porrati-rahman.txt"))
dpw = load(os.path.join(CBS, "dpw.txt"))
tr = load(os.path.join(REPO, r"papers\drafts\Transcript into the impossible.md"))
cap = load(os.path.join(REPO, r"canon\carrier-dirac-mass-capstone-RESULTS.md"))
adj = load(os.path.join(REPO, r"canon\gamma-traceless-38-adjudication-RESULTS.md"))
de = load(os.path.join(REPO, r"absorbed\gu-source-action\DEAD-ENDS.md"))

needle("D1a PR abstract: causal ungauged massive charged spin-3/2 EXISTS (constant F)",
       pr, "We present a Lagrangian for a massive, charged spin 3/2 field in a constant external electromagnetic background, which correctly propagates only physical degrees of freedom inside the light cone",
       "porrati-rahman.txt (arXiv:0906.1432) abstract")
needle("D1b PR: minimal coupling produced faster-than-light signals (VZ statement)",
       pr, "minimal coupling to external electromagnetic fields resulted in equations of motion which exhibited faster-than-light propagation of signals",
       "porrati-rahman.txt intro")
needle("D1c PR: VZ problem manifests already for constant backgrounds",
       pr, "it does take care of the original Velo-Zwanziger problem, which manifests itself already for constant backgrounds",
       "porrati-rahman.txt")
needle("D1d PR: the cure is enforcing the gamma-tracelessness constraint EXACTLY",
       pr, "The crucial property of our construction is that the standard gamma-tracelessness constraint",
       "porrati-rahman.txt")
needle("D1e PR: constraint + EOM reduce to manifestly causal Dirac form",
       pr, "one can reduce equations of motion (4) to a standard, manifestly causal Dirac form",
       "porrati-rahman.txt")
needle("D1f PR: no additional fields needed (non-supergravity escape exists)",
       pr, "No additional fields or equations besides the spin 3/2 ones are needed to solve the problem",
       "porrati-rahman.txt abstract")
needle("D1g PR carrier-A side: light charged spin-3/2 without SUGRA relation stays superluminal",
       pr, "the gravitational back- reaction of spin 3/2 particles much lighter than O(eMPl) is negligible, so they can still propagate superluminally",
       "porrati-rahman.txt intro")
needle("D2a DPW: critical fields verbatim (minimal coupling = well-known VZ result)",
       dpw, "critical field values B2 = 3m4/e2 and B2 = (3m2/2e)2, respectively (the latter being the well known result of [5, 6])",
       "dpw.txt (hep-th/0003011)")
needle("D2b DPW ref [6] = Velo-Zwanziger PR 186, 1337 (1969)",
       dpw, "Phys. Rev. 186, 1337 (1969)", "dpw.txt references")
needle("D2c DPW ref [5] = Johnson-Sudarshan (quantization pathology)",
       dpw, "K. Johnson and E. C. Sudarshan", "dpw.txt references")

needle("D3a transcript: 16 flipped chiral spin-3/2 family",
       tr, "one family of 16 flipped chiral spin three halves particles", "transcript [00:40:27]")
needle("D3b transcript: family = conjugate of the internal symmetry representation",
       tr, "just the conjugate of the internal symmetry representation", "transcript [00:40:27]")
needle("D3c transcript: family is electrically CHARGED (VZ trigger at rep-content grade)",
       tr, "Some of these things will be electrically neutral, but lots of them won't be",
       "transcript [00:40:27]")
needle("D3d transcript: VZ passage (spin-3/2 matter coupled to nontrivial acting group)",
       tr, "if you have spin three halves matter that is coupled, to some sort of nontrivial acting group",
       "transcript [00:41:48]")
needle("D3e transcript: the author's no-internal-symmetry escape plea",
       tr, "So if your model differs by having no internal symmetry groups, I have no idea whether it has any kind of a Velo Zwanziger problem",
       "transcript [00:41:48]")
needle("D3f transcript: no spacetime SUSY",
       tr, "We will never find space time Susie", "transcript [00:46:02]")
needle("D3g transcript: mass is a variable (massive branch live)",
       tr, "because the mass is actually a variable", "transcript [00:46:02]")

needle("D4a capstone: carrier vectorlike, Krein (+96,-96), net chirality 0",
       cap, "Krein signature exactly `(+96, -96)`, net chirality 0", "canon capstone")
needle("D4b capstone: Dirac mass ALLOWED, generically massive",
       cap, "The carrier Dirac mass is **ALLOWED, generically massive -- not forbidden, not protected**",
       "canon capstone")
needle("D4c capstone: massive case decouples to ZERO net chiral generations",
       cap, "decouples to ZERO net chiral generations, not three", "canon capstone")
needle("D4d adjudication: selection authority is SG4",
       adj, "Selection authority moved to SG4", "canon adjudication")
needle("D4e adjudication: story-shopping guard verbatim",
       adj, "treating that smell as a verdict would be story-shopping", "canon adjudication")
needle("D5 DEAD-ENDS acausal trap present (this leg complies: no dynamics touched)",
       de, "58.72", "DEAD-ENDS.md")

# ----------------------------------------------------------------------------
print()
print("=" * 78)
print("GUARDS AND CARRIER-A STEELMAN (printed for the record)")
print("=" * 78)
print("""
ACAUSAL-TRAP COMPLIANCE: no quantity in this script is the repo's bare commutator
||[Pi_RS, M_D]|| = 58.72; nothing here dresses, reduces, or decouples any repo
obstruction. The 4d VZ system above is the standalone published model (VZ 1969 /
DPW 2000 / PR 2009), used only to extract published hypotheses and reproduce the
published critical field exactly.

FIREWALL COMPLIANCE: no chi(K3), no A-hat = 3, no manufactured /8. The 19/8 and
-38 appear only as (a) verbatim published text (HS Prop 3.1(i), BM Rem 5.3) and
(b) exact application of those published formulas to the published sigma(K3) = -16,
reproducing canon's existing carrier-B row.

CARRIER-A STEELMAN (what this leg does NOT decide):
 (1) The OTHER published VZ escape is gravitational back-reaction / N=2 gauged
     supergravity (PR intro verbatim; DW hep-th/0112182 abstract) -- the gauged,
     ghost-subtracted reading. Both escapes are published; the leg shows the fork
     between them is exactly the carrier fork, not that B wins it.
 (2) PR's ungauged rescue is CONSTANT-BACKGROUND only ('Our method will work for
     constant backgrounds. While this is a drawback...'); no published ungauged
     rescue covers arbitrary backgrounds, while supergravity's covers dynamical
     gravity (DW: 'propagation is causal in arbitrary E/M backgrounds' within
     Planck-order windows).
 (3) Minimal coupling FORCES gamma.psi != 0 (part B2d): GU cannot both couple
     minimally and keep carrier B's field space on-shell. If SG4's action is
     minimal, the ungauged reading inherits VZ acausality above the critical
     field, and the consistent completions on record are supergravity-shaped.
 (4) The massless-chiral reading of 'flipped chiral 16' (if spacetime-chiral and
     massless at tree level) triggers Grisaru-Pendleton and forces SUSY couplings
     -- the gauged gravitino, carrier A.
 None of this is decided here: the bit stays on SG4.
""")

fails = [n for n, ok in CHECKS if not ok]
print("=" * 78)
print(f"TOTAL: {len(CHECKS)} checks, {len(CHECKS) - len(fails)} passed, {len(fails)} failed")
if fails:
    print("FAILED:", fails)
    sys.exit(1)
print("ALL CHECKS PASS -- exit 0")
sys.exit(0)
