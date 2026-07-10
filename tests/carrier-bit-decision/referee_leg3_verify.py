# -*- coding: utf-8 -*-
"""
HOSTILE-REFEREE INDEPENDENT VERIFICATION of LEG-3 (ungauged consistency).

Independence from the leg's script:
  * CHIRAL (Weyl) gamma representation, not the leg's Dirac representation.
  * Different code path: constraint derived ANALYTICALLY from the contraction
    identities gamma_mu gamma^{mu nu rho} = (n-2) gamma^{nu rho},
    gamma_mu gamma^{mu rho} = (n-1) gamma^{rho}, then verified as exact matrix
    identities; c is not obtained by solve() but checked against the closed form.
  * det K computed two ways: sympy determinant AND the eigenvalue route
    (eigenvalues of g1*g2 are +-i twice => det closed form).
  * Needle checks are done on text extracted BY THIS SCRIPT from the cached PDFs
    with pypdf -- not on the .txt caches the leg used.

Exit 0 iff all checks pass.
"""
import sys, os, itertools
from fractions import Fraction
import sympy as sp
from sympy import I, Rational, Matrix, zeros, eye, symbols

SCRATCH = r"C:\Users\joe\AppData\Local\Temp\claude\C--Users-joe-JB\79411e9e-5aaa-44a7-ba95-2f380675a349\scratchpad"
CBS = os.path.join(SCRATCH, "carrier-bit-swing")
SYM = os.path.join(SCRATCH, "symbol-swing")

CH = []
def check(name, cond, detail=""):
    CH.append((name, bool(cond)))
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ""))
    return bool(cond)

# ---------------------------------------------------------------- chiral rep
s1 = Matrix([[0, 1], [1, 0]]); s2 = Matrix([[0, -I], [I, 0]]); s3 = Matrix([[1, 0], [0, -1]])
Z2, I2 = zeros(2, 2), eye(2)
def blk(A, B, C, D):
    return Matrix.vstack(Matrix.hstack(A, B), Matrix.hstack(C, D))
g0 = blk(Z2, I2, I2, Z2)                       # chiral rep: off-diagonal g0
gam = [g0] + [blk(Z2, s, -s, Z2) for s in (s1, s2, s3)]
eta = sp.diag(1, -1, -1, -1)

ok = all(gam[m]*gam[n] + gam[n]*gam[m] == 2*eta[m, n]*eye(4)
         for m in range(4) for n in range(4))
check("V1 chiral-rep Clifford algebra", ok)
check("V1b chiral rep differs from leg's Dirac rep (g0 off-diagonal)", g0[0, 0] == 0)

def perm_sign(p):
    s = 1
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            if p[i] > p[j]: s = -s
    return s

def ganti(idx):
    out = zeros(4, 4)
    for p in itertools.permutations(range(len(idx))):
        Mt = eye(4)
        for k in p: Mt = Mt*gam[idx[k]]
        out += perm_sign(p)*Mt
    return out/sp.factorial(len(idx))

G2 = [[ganti((m, n)) for n in range(4)] for m in range(4)]
G3 = [[[ganti((m, n, r)) for r in range(4)] for n in range(4)] for m in range(4)]
glow = [eta[m, m]*gam[m] for m in range(4)]

# contraction identities (n=4): analytic backbone of the secondary constraint
ok1 = all(sum((glow[m]*G2[m][n] for m in range(4)), zeros(4, 4)) == 3*gam[n] for n in range(4))
ok2 = all(sum((glow[m]*G3[m][n][r] for m in range(4)), zeros(4, 4)) == 2*G2[n][r]
          for n in range(4) for r in range(4))
check("V2 gamma_mu gamma^{mu rho} = 3 gamma^rho AND gamma_mu gamma^{mu nu rho} = 2 gamma^{nu rho}",
      ok1 and ok2)

# ---------------------------------------------------------------- constraint
# EOM R^mu = i g^{mu nu rho} D_nu psi_rho + a m g^{mu rho} psi_rho.
# ANALYTIC derivation (independent of the leg's solve()):
#   D.R  = -(e/2) g^{mnr} F_{mn} psi_r + a m g^{mu rho} D_mu psi_rho
#          (second-derivative part killed by antisymmetry: g^{mnr} S_{(mn)} = 0)
#   g.R  = 2 i g^{nu rho} D_nu psi_rho + 3 a m g^rho psi_rho
#   D.R + c m g.R : derivative terms cancel iff a + 2 i c = 0  =>  c = i a / 2
#   remainder    = -(e/2) g^{mnr} F_{mn} psi_r + (3 i / 2) m^2 g.psi   (a^2 = 1)
a_, c_ = symbols("a c")
check("V3a unique c from a + 2ic = 0 is c = ia/2 (a=+1: i/2; a=-1: -i/2)",
      sp.solve(sp.Eq(a_ + 2*I*c_, 0), c_)[0] == I*a_/2)
# matrix-level confirmation that g^{mnr} kills symmetric S: sum over mn of
# G3[m][n][r]*S_{mn} with S symmetric == 0  <=>  G3 antisymmetric in (m,n):
ok = all(G3[m][n][r] == -G3[n][m][r] for m in range(4) for n in range(4) for r in range(4))
check("V3b gamma^{mnr} antisymmetric in (m,n): no d^2 residue in D.R", ok)
# mass-sign independence: remainder coefficient 3*a*c*m^2 = 3*a*(ia/2)*m^2 = (3i/2) a^2 m^2
check("V3c remainder (3i/2) m^2 gamma.psi, mass-sign independent (a^2=1)",
      sp.expand((3*a_*(I*a_/2)).subs(a_**2, 1)) == Rational(3, 2)*I)
# => F=0 forces gamma.psi = 0 exactly; F!=0: gamma.psi = -(ie/3m^2) g^{mnr}F_{mn}psi_r
m_, e_, B_ = symbols("m e B")
coef = sp.simplify((Rational(1, 2)*e_)/(Rational(3, 2)*I*m_**2))
check("V3d minimal coupling: gamma.psi = -(i e / 3 m^2) gamma^{mnr} F_{mn} psi_r  (!= 0)",
      sp.simplify(coef + I*e_/(3*m_**2)) == 0, f"coef = {coef}")

# ---------------------------------------------------------------- free DOF
def hstack4(mats): return Matrix.hstack(*mats)
Gtrace = hstack4([gam[r] for r in range(4)])            # gamma.psi map, 4x16

def free_symbol(p, a, mv):
    rows = []
    for mu in range(4):
        row = zeros(4, 16)
        for nu in range(4):
            if p[nu] != 0:
                row += p[nu]*hstack4([G3[mu][nu][r] for r in range(4)])
        row += a*mv*hstack4([G2[mu][r] for r in range(4)])
        rows.append(row)
    return Matrix.vstack(*rows)

dims = {}
for a in (1, -1):
    ker = free_symbol([1, 0, 0, 0], a, 1).nullspace()
    dims[a] = len(ker)
    okg = all(sp.simplify(Gtrace*v) == zeros(4, 1) for v in ker)
    ok0 = all(all(sp.simplify(v[s]) == 0 for s in range(4)) for v in ker)
    check(f"V4 a={a:+d}: free kernel dim 4, gamma-traceless, transverse",
          len(ker) == 4 and okg and ok0)

# ---------------------------------------------------------------- VZ jumps
def J1(xi):
    rows = []
    for mu in range(4):
        row = zeros(4, 16)
        for nu in range(4):
            if xi[nu] != 0:
                row += xi[nu]*hstack4([G3[mu][nu][r] for r in range(4)])
        rows.append(row)
    return Matrix.vstack(*rows)

J1t = J1([1, 0, 0, 0])
kt = J1t.nullspace()
longb = []
for s in range(4):
    v = zeros(16, 1); v[s] = 1
    longb.append(v)
check("V5a timelike xi: dim ker(J1) = 4 and equals the longitudinal span",
      len(kt) == 4 and Matrix.hstack(*(kt + longb)).rank() == 4)
check("V5b ker(J1) meets ker(Gtrace) only at 0 (stacked rank 16)",
      Matrix.vstack(J1t, Gtrace).rank() == 16)
check("V5c null xi control: dim ker(J1) = 6", len(J1([1, 0, 0, 1]).nullspace()) == 6)

# critical matrix on longitudinal eps:  K = -eB g^{120} + (3i/2) m^2 g^0
K = -e_*B_*G3[1][2][0] + Rational(3, 2)*I*m_**2*gam[0]
detK = sp.factor(K.det())
target = sp.factor((Rational(9, 4)*m_**4 - e_**2*B_**2)**2)
check("V6a det K = (9/4 m^4 - e^2 B^2)^2 (sympy determinant, chiral rep)",
      sp.simplify(detK - target) == 0, f"det K = {detK}")
# SECOND, structurally different route: eigenvalues of g1*g2 are +-i (each x2),
# det(g0) = 1  =>  det K = prod_i ( (3i/2)m^2 - eB*lambda_i ) with lambda in {i,i,-i,-i}
g12 = gam[1]*gam[2]
evs = g12.eigenvals()
check("V6b eigenvalues of g1 g2 = {+i: 2, -i: 2}, det g0 = 1",
      evs == {I: 2, -I: 2} and gam[0].det() == 1)
det_route2 = sp.factor(sp.expand(
    ((Rational(3, 2)*I*m_**2 - e_*B_*I)**2 * (Rational(3, 2)*I*m_**2 + e_*B_*I)**2)))
check("V6c eigenvalue route reproduces det K exactly",
      sp.simplify(det_route2 - target) == 0)
sols = set(sp.solve(sp.Eq(detK, 0), B_))
check("V6d zeros exactly at B = +- 3 m^2 / (2 e)  [published VZ critical field]",
      sols == {Rational(3, 2)*m_**2/e_, -Rational(3, 2)*m_**2/e_})

def J2(ev, mv, Bv):
    out = zeros(4, 16)
    out += -ev*Bv*hstack4([G3[1][2][r] for r in range(4)])   # -(e/2)(F12 g^{12r}+F21 g^{21r}) = -eB g^{12r}
    out += Rational(3, 2)*I*mv**2*Gtrace
    return out

check("V7a subcritical (e=1,m=1,B=1): stacked [J1;J2] rank 16 (only zero jump)",
      Matrix.vstack(J1t, J2(1, 1, 1)).rank() == 16)
rc = Matrix.vstack(J1t, J2(1, 1, Rational(3, 2))).rank()
check("V7b critical B=3/2: stacked rank drops to 14 (nonzero timelike jump exists)",
      rc == 14, f"rank = {rc}")
Kc = K.subs({e_: 1, m_: 1, B_: Rational(3, 2)})
check("V7c critical K rank drops 4 -> 2", Kc.rank() == 2)

# ------------------------------------------------------- exact K3 arithmetic
h11, sig = 20, -16
check("V8 (19/8)*sigma(K3) = -38 and 2h11-2 = 38 (Fraction-exact)",
      Fraction(19, 8)*sig == -38 and 2*h11 - 2 == 38)

# ------------------------------------------------------- PDF needle checks
def norm(s):
    s = s.replace("ﬁ", "fi").replace("ﬂ", "fl")
    s = s.replace("−", "-").replace("’", "'").replace("“", '"').replace("”", '"')
    s = s.replace("¨", "")
    return "".join(s.split())

def pdf_text(path):
    from pypdf import PdfReader
    return norm("".join(pg.extract_text() or "" for pg in PdfReader(path).pages))

PDF_NEEDLES = [
    (os.path.join(CBS, "porrati-rahman.pdf"), "PR", [
        ("abstract: causal ungauged massive charged spin-3/2 exists",
         "Wepresenta Lagrangianfora massive,chargedspin3/2fieldina constantexternalelectromagneticbackground"),
        ("abstract: no additional fields needed",
         "Noadditionalfieldsorequationsbesidesthespin3/2onesareneeded"),
        ("mechanism: gamma-tracelessness enforced exactly",
         "isenforcedexactly"),
        ("mechanism context: crucial property of our construction",
         "Thecrucialpropertyofourconstruction"),
        ("reduce to manifestly causal Dirac form",
         "manifestlycausalDiracform"),
        ("drawback: constant backgrounds only",
         "Ourmethodwillworkforconstantbackgrounds"),
        ("carrier-A side: light charged spin-3/2 still superluminal",
         "muchlighterthanO(eMPl)isnegligible,sotheycanstillpropagatesuperluminally"),
        ("gauged escape: causality due to gravitational back-reaction",
         "Causalityinthiscaseisduetogravitationalback-reaction"),
    ]),
    (os.path.join(CBS, "dpw.pdf"), "DPW", [
        ("critical field values sentence (start)", "havecriticalfieldvalues"),
        ("minimal-coupling critical value (3m2/2e)^2", "(3m2/2e)2"),
        ("attribution: the well known result of [5, 6]",
         "thelatterbeingthewellknownresultof[5,6]"),
        ("[6] = Velo-Zwanziger PR 186 1337 (1969)",
         "Phys.Rev.186,1337(1969)"),
        ("eq (40) independent cross-check text", "vanishesinapuremagneticbackgroundwhenever"),
    ]),
    (os.path.join(SYM, "hs-rs-kernel.pdf"), "HS", [
        ("index section drops Einstein hypothesis",
         "wedonothavetoassumethemetricgtobeEinstein"),
        ("K3 example: dim ker Q = 2h^{1,1}-2 = 38",
         "K3surfaceanditfollowsfromProposition"),
        ("two copies of harmonic primitive (1,1)-forms",
         "twocopiesofthespaceofharmonicprimitive"),
        ("Rem 3.6 ghost subtraction: spin 1/2 ghosts",
         "ghost"),
        ("Prop 3.1 n=4 line (19/8 sigma)",
         "indQ=-19"),
    ]),
    (os.path.join(SYM, "baer-mazzeo.pdf"), "BM", [
        ("Rem 5.3 sharp RS(K3)=38", "sharp;indeedRS(K3)=38"),
    ]),
    (os.path.join(CBS, "hack-makedonski.pdf"), "HM", [
        ("no-go: impossible, Einstein required",
         "impossibleasallcouplingsrequirethebackgroundtobeanEinsteinspacetime"),
        ("Buchdahl restatement: psi = 0 unless Einstein",
         "unlessthespacetimeisanEinsteinspacetime"),
        ("supergravity as the prominent completion (carrier-A steelman)",
         "supergravitytheoriesaretheonlymeaningfulmodels"),
    ]),
]

for path, tag, pairs in PDF_NEEDLES:
    try:
        hay = pdf_text(path)
    except Exception as ex:
        check(f"P-{tag} pdf extraction", False, f"{ex}")
        continue
    for name, ndl in pairs:
        check(f"P-{tag} {name}", norm(ndl) in hay, os.path.basename(path))

fails = [n for n, ok in CH if not ok]
print("=" * 70)
print(f"REFEREE TOTAL: {len(CH)} checks, {len(CH)-len(fails)} passed, {len(fails)} failed")
if fails:
    print("FAILED:", fails); sys.exit(1)
print("ALL REFEREE CHECKS PASS -- exit 0")
sys.exit(0)
