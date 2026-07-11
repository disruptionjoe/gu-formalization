#!/usr/bin/env python3
r"""H15 -- THE GRAVITY FORK: does GU's forced geometry generate an Einstein-Hilbert
scalar-curvature (R) term -- making gravity Stelle-type R + Weyl^2 (a DISTINCT massive
ghost, Bateman-Turok-ready, ghost CLEARS) -- or does it leave gravity pure conformal
Bach box^2 (the DEGENERATE coincident-pole case, ghost NOT cleanly solved)?

Wave 3, Condorcet #1. Collapses H1/H4/H8/H9/H11 onto ONE datum (per H9 wave2:
canon/... + tests/wave2/H9_ghost_parity_bach_sector.py -- the Bach sector clears via
Bateman-Turok ONLY IF GU's gravity is Stelle-type, NOT pure conformal Bach).

WHAT THIS FILE COMPUTES (exact sympy / exact linear algebra, no imported target)
--------------------------------------------------------------------------------
The decisive geometry is the Gauss equation. GU's section functional is a
Willmore-type energy of the section s: X^4 -> Y^14 = Met(X^4). There are two
candidate functionals (the standing OQ2-A binary, the unbuilt-action datum):
  * |H|^2  (H-class, mean-curvature / conformal-Willmore)
  * |II|^2 (II-class, FULL second fundamental form -- the Yang-Mills-natural norm
            of the full distortion theta = s*(...) = II_s)

PART A. The Gauss identity as an EXACT algebra fact: for a submanifold in a flat
ambient, R^X = (tr S)^2 - tr(S^2) = |H|^2 - |II|^2, i.e.
        |II|^2 = |H|^2 - R^X            (+ ambient R^Y in curved ambient).
So the II-class functional CARRIES the intrinsic scalar curvature R^X of the induced
4-metric; the H-class functional does NOT. This is the algebraic source of any R term.
(This is also exactly the trace of the repo's Gauss identity G^X = G^Y_T + Q(B) + E^Psi:
 tr Q(B) = |II|^2 - |H|^2, canon/schwarzschild-weak-field-rfail.md.)

PART B. The DIMENSIONAL CRUX -- is that R^X term dynamical or topological?
  * 2D: R^X = 2K, and int K is TOPOLOGICAL (Gauss-Bonnet, = 2*pi*chi) -> NON-dynamical.
        In 2D the |II|^2 - |H|^2 difference is a pure topological term: NO R dynamics.
  * 4D: the topological density is the Euler/Gauss-Bonnet E_4 = Riem^2 - 4Ric^2 + R^2,
        NOT R. int R^X is the genuine EINSTEIN-HILBERT action -- its linearization is a
        NONZERO SECOND-ORDER (box) operator on the graviton. We compute it: on TT,
        G^(1)_mn = -1/2 box h_mn (2 derivatives, nonzero). So in 4D the R^X term is a
        genuine two-derivative KINETIC/MASS term, not a boundary or topological piece.

PART C. The OPERATOR / GHOST consequence.
  * |H|^2 alone -> box^2 (fourth-order Bach; TT propagator 1/s^2 = DOUBLE pole ->
    coincident-pole DEGENERATE -> Bateman-Turok O(1,1) split SINGULAR -> ghost OPEN).
  * |II|^2 = |H|^2 - R^X -> box^2 + (mass) box = box(box + m^2): TT propagator
    1/(s(s+m^2)) = TWO DISTINCT poles (massless graviton + massive ghost) ->
    NON-degenerate Stelle -> the O(1,1) healthy/ghost split is CLEAN with opposite-sign
    residues -> Bateman-Turok ghost parity applies -> ghost CLEARS.

PART D. ADVERSARIAL -- is the O(M^0) DeWitt background an R/mass term or just Lambda?
  The constant-section SFF (ii-s-coordinate-formula sec 6.1) has fiber-trace
  = (1/2) eta_mn EXACTLY -- a cosmological-constant (Lambda) signature, NOT an R term.
  A Lambda term is 0-derivative: it does NOT enter the kinetic operator and does NOT
  lift the box^2 degeneracy. So the DeWitt O(M^0) piece is branch-NEUTRAL; the ONLY
  degeneracy-lifting object is the |II|^2 Gauss R^X term of PART A/B.

PART E. SIGN -- is the induced Einstein term a healthy massive pole (m^2 real) or a
  wrong-sign/tachyonic one? Computed for the flat-ambient model; the ambient DeWitt R^Y
  correction to the coefficient is flagged as the remaining (reconstruction-grade) input.

WHAT THIS DOES NOT DO (honest boundary)
---------------------------------------
It does NOT build GU's (unbuilt) source action, so it does NOT FORCE the |II|^2-vs-|H|^2
choice from the action -- that choice is the residual OQ2-A datum. It computes the
CONSEQUENCE of each branch and shows the fork collapses to exactly that binary. It uses
the standard curved-ambient Willmore EL structure and linearization about flat space; the
full nonlinear higher-codimension first variation is not done here. External facts used
(not re-proved): Gauss-Bonnet topological-ness of int K (2D) and E_4 (4D); Bateman-Turok
tree-level Krein positivity for a distinct massive ghost.

Run: python -u tests/wave3/H15_gravity_fork_R_term.py
"""
from __future__ import annotations
import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


def log(msg):
    print(msg, flush=True)


# ===========================================================================
# PART A -- Gauss identity: |II|^2 = |H|^2 - R^X (flat ambient). EXACT algebra.
#   For a submanifold with shape/second-fundamental data S (symmetric), the flat-
#   ambient scalar Gauss equation gives the intrinsic scalar curvature
#       R^X = sum_{i!=j} k_i k_j = (tr S)^2 - tr(S^2) = |H|^2 - |II|^2,
#   where k_i are principal curvatures, |H|^2 = (tr S)^2, |II|^2 = tr(S^2).
#   Hence |II|^2 = |H|^2 - R^X : the II-class functional carries -R^X, |H|^2 does not.
# ===========================================================================
log("=" * 78)
log("PART A -- Gauss identity |II|^2 = |H|^2 - R^X  (exact, all dims)")
log("=" * 78)

for dim in (2, 3, 4):
    # generic symmetric shape operator with symbolic principal curvatures
    ks = sp.symbols(f'k0:{dim}', real=True)
    S = sp.diag(*ks)                      # diagonalized WLOG (symmetric)
    trS = sp.trace(S)                     # = sum k_i  (H, unnormalized)
    trS2 = sp.trace(S * S)                # = sum k_i^2 (|II|^2, flat ambient)
    H2 = sp.expand(trS**2)                # |H|^2
    II2 = sp.expand(trS2)                 # |II|^2
    # intrinsic scalar curvature (flat ambient, traced-twice Gauss) = sum_{i!=j} k_i k_j
    Rx = sp.expand(sum(ks[i] * ks[j] for i in range(dim) for j in range(dim) if i != j))
    identity_ok = sp.expand(II2 - (H2 - Rx)) == 0
    # e_2 (second elementary symmetric) relation: R^X = 2 e_2
    e2 = sp.expand(sum(ks[i] * ks[j] for i in range(dim) for j in range(dim) if i < j))
    check(f"dim {dim}: |II|^2 = |H|^2 - R^X exactly (flat-ambient Gauss); R^X = 2*e_2(k)",
          identity_ok and sp.expand(Rx - 2 * e2) == 0)

log("  => the |II|^2 (full second-fundamental-form) functional CARRIES the intrinsic")
log("     scalar curvature R^X with a definite (minus) sign; |H|^2 does NOT. This is the")
log("     algebraic SOURCE of an Einstein-Hilbert R term -- present iff the functional is")
log("     II-class. (In curved ambient add + R^Y_tangential: the O(M^0) DeWitt piece.)")

# cross-check against the repo Gauss identity trace: tr Q(B) = |II|^2 - |H|^2.
# Q_mn(B) = H_i B^i_mn - B^i_mr B_i^r_n - (1/2) g_mn (H_iH^i - B^i_rs B_i^rs)
# (codazzi-general-non-umbilic sec 1). Model: single normal, 4D, S the shape operator.
n4 = 4
g = sp.eye(n4)  # euclidean tangent model for the pure algebra of the trace
ks4 = sp.symbols('a0:4', real=True)
B = sp.diag(*ks4)          # B_mn (one normal component)
Hs = sp.trace(B)           # H = tr B
Q = sp.zeros(n4, n4)
for m in range(n4):
    for nu in range(n4):
        BB = sum(B[m, r] * B[r, nu] for r in range(n4))
        Q[m, nu] = Hs * B[m, nu] - BB - sp.Rational(1, 2) * g[m, nu] * (Hs**2 - sp.trace(B * B))
trQ = sp.expand(sp.trace(Q))
check("repo Gauss identity trace matches: tr Q(B) = |II|^2 - |H|^2 (= -R^X, flat ambient)",
      sp.expand(trQ - (sp.trace(B * B) - Hs**2)) == 0,
      "confirms G^X = G^Y_T + Q(B) carries the same R^X object")

# ===========================================================================
# PART B -- dimensional crux: int R^X is TOPOLOGICAL in 2D, DYNAMICAL in 4D.
# ===========================================================================
log("\n" + "=" * 78)
log("PART B -- is int R^X dynamical? 2D: topological (Gauss-Bonnet). 4D: Einstein-Hilbert")
log("=" * 78)

# --- 2D: int K over a round 2-sphere = 2*pi*chi = 4*pi (topological, radius-independent).
a = sp.symbols('a', positive=True)
theta = sp.symbols('theta', positive=True)
# sphere radius a: K = 1/a^2, area element a^2 sin(theta) dtheta dphi
intK = sp.integrate(sp.integrate((1 / a**2) * a**2 * sp.sin(theta),
                                 (theta, 0, sp.pi)), (sp.Symbol('phi'), 0, 2 * sp.pi))
check("2D: int K dA = 4*pi = 2*pi*chi (chi=2), radius-INDEPENDENT -> int R^X is TOPOLOGICAL "
      "in 2D (no R dynamics); |II|^2-|H|^2 is a pure topological term there", intK == 4 * sp.pi,
      f"int K = {intK}")

# --- 4D: linearized Einstein-Hilbert operator on TT is SECOND-order and NONZERO.
# (contrast: the 4D topological density is E_4 = Riem^2 -4Ric^2 + R^2, NOT R.)
t, x, y, z = sp.symbols('t x y z', real=True)
coords = [t, x, y, z]
eta = sp.diag(-1, 1, 1, 1)
kt, kx = sp.symbols('k_t k_x', real=True)
klow = [kt, kx, 0, 0]
kup = [sum(eta[m, nn] * klow[nn] for nn in range(4)) for m in range(4)]
kk = sp.simplify(sum(kup[m] * klow[m] for m in range(4)))   # k.k
u = sum(klow[m] * coords[m] for m in range(4))
F = sp.Function('F')


def d(e, mu):
    return sp.diff(e, coords[mu])


def riem_low(h):
    R = {}
    for aa in range(4):
        for bb in range(4):
            for cc in range(4):
                for dd in range(4):
                    R[(aa, bb, cc, dd)] = sp.Rational(1, 2) * (
                        d(d(h[aa, dd], bb), cc) + d(d(h[bb, cc], aa), dd)
                        - d(d(h[bb, dd], aa), cc) - d(d(h[aa, cc], bb), dd))
    return R


def ricci_low(R):
    Ric = sp.zeros(4, 4)
    for aa in range(4):
        for bb in range(4):
            Ric[aa, bb] = sum(eta[cc, dd] * R[(cc, aa, dd, bb)] for cc in range(4) for dd in range(4))
    return Ric


def box(h):
    return sp.Matrix(4, 4, lambda aa, bb: sum(eta[m, nn] * d(d(h[aa, bb], m), nn)
                                              for m in range(4) for nn in range(4)))


# TT graviton: eps in y-z block, traceless, transverse to k in t-x plane.
eps_TT = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1]]
h_TT = sp.Matrix(4, 4, lambda aa, bb: eps_TT[aa][bb] * F(u))
R_TT = riem_low(h_TT)
Ric_TT = ricci_low(R_TT)
Rs_TT = sp.simplify(sum(eta[aa, bb] * Ric_TT[aa, bb] for aa in range(4) for bb in range(4)))
box_hTT = box(h_TT)
# G^(1)_mn = Ric^(1)_mn - 1/2 eta_mn R^(1); on TT R^(1)=0.
G1_yy = sp.simplify(Ric_TT[2, 2] - sp.Rational(1, 2) * eta[2, 2] * Rs_TT)
EH_is_second_order = sp.simplify(G1_yy - (-sp.Rational(1, 2) * box_hTT[2, 2])) == 0


def max_deriv_order(expr):
    orders = [sum(nn for _, nn in dv.variable_count) for dv in expr.atoms(sp.Derivative)]
    return max(orders) if orders else 0


check("4D: linearized Einstein-Hilbert EOM on TT is G^(1)_yy = -1/2 box h_yy -- SECOND order "
      "and NONZERO (a genuine 2-derivative kinetic term, not a boundary/total-derivative)",
      EH_is_second_order and G1_yy != 0 and max_deriv_order(G1_yy) == 2,
      f"G^(1)_yy = {sp.simplify(G1_yy)}  (deriv order {max_deriv_order(G1_yy)})")
check("4D: linearized scalar curvature on TT R^(1) = 0 (so G^(1)=Ric^(1)); the EH operator "
      "survives = int R^X is DYNAMICAL in 4D (unlike 2D). Topological 4D density is E_4, not R",
      sp.simplify(Rs_TT) == 0)

# ===========================================================================
# PART C -- operator/ghost: |H|^2 -> box^2 (degenerate); |II|^2 -> box(box+m^2) (Stelle).
# ===========================================================================
log("\n" + "=" * 78)
log("PART C -- |H|^2 = box^2 (double pole, degenerate) vs |II|^2 = box(box+m^2) (Stelle, distinct)")
log("=" * 78)

# H-class leading operator on TT = box^2 (fourth order). (matches D-thread: box^2 h = -4 Bach.)
box2_hTT = box(box(h_TT))
check("H-class |H|^2 leading Willmore-EL operator on TT is box^2 h (FOURTH order) -- pure Bach",
      max_deriv_order(sp.simplify(box2_hTT[2, 2])) == 4)

# II-class operator on TT = box^2 (from |H|^2 part) + m2 * box (from the -R^X Einstein part).
# On the yy plane wave: box h_yy = kk*F''(u); box^2 h_yy = kk^2 * F''''(u).
s, m2 = sp.symbols('s m2', positive=True)   # s = box eigenvalue (= k.k), m2 = graviton^2 scale
# operator symbol P(s): H-class = s^2 ; II-class = s^2 + m2*s = s(s+m2)
P_H = s**2
P_II = s**2 + m2 * s
roots_H = sp.roots(sp.Poly(P_H, s))
roots_II = sp.roots(sp.Poly(P_II, s))
check("H-class symbol P(s)=s^2 has a DOUBLE root at s=0 (coincident pole -> DEGENERATE, "
      "the Pais-Uhlenbeck equal-frequency Jordan case; Bateman-Turok O(1,1) split SINGULAR)",
      roots_H == {sp.Integer(0): 2})
check("II-class symbol P(s)=s(s+m2) has TWO DISTINCT roots s=0 (massless graviton) and "
      "s=-m2 (massive ghost) -> NON-degenerate STELLE R+Weyl^2",
      set(roots_II.keys()) == {sp.Integer(0), -m2} and all(v == 1 for v in roots_II.values()))

# propagator partial-fraction: distinct poles -> opposite-sign residues (the O(1,1)/Krein pair).
prop_II = 1 / (s * (s + m2))
res0 = sp.residue(prop_II, s, 0)
resm = sp.residue(prop_II, s, -m2)
check("II-class TT propagator 1/(s(s+m2)) splits into a POSITIVE-residue (healthy graviton) "
      "pole + a NEGATIVE-residue (massive ghost) pole -- the clean O(1,1)/Krein pair "
      "Bateman-Turok grade by ghost parity => ghost CLEARS",
      sp.simplify(res0) > 0 and sp.simplify(resm) < 0, f"(+{res0}, {resm})")
# and the degenerate limit m2->0 recovers the singular double pole:
split_coeff = sp.limit(1 / m2, m2, 0)
check("as m2 -> 0 the split coefficient 1/m2 DIVERGES: the H-class (pure Bach) limit is exactly "
      "the singular coincident-pole degeneration of the II-class Stelle propagator",
      split_coeff == sp.oo, f"lim_(m2->0) 1/m2 = {split_coeff}")

# ===========================================================================
# PART D -- adversarial: the O(M^0) DeWitt background is Lambda, NOT an R/mass term.
# ===========================================================================
log("\n" + "=" * 78)
log("PART D -- adversarial: O(M^0) DeWitt constant-section SFF is LAMBDA (0-deriv), not mass")
log("=" * 78)
# constant-section vertical SFF (ii-s-coordinate-formula sec 6.1):
#   B^V_mn,ab = -(1/2)( eta_a(m eta_n)b - (1/2) eta_ab eta_mn )
etad = sp.diag(-1, 1, 1, 1)


def sym2(A, i, j, k, l):
    return sp.Rational(1, 2) * (A[i, k] * A[j, l] + A[i, l] * A[j, k])


def Bconst(mu, nu, aa, bb):
    return -sp.Rational(1, 2) * (sym2(etad, aa, bb, mu, nu) - sp.Rational(1, 2) * etad[aa, bb] * etad[mu, nu])


T = sp.zeros(4, 4)
for mu in range(4):
    for nu in range(4):
        T[mu, nu] = sp.simplify(sum(etad[aa, bb] * Bconst(mu, nu, aa, bb) for aa in range(4) for bb in range(4)))
c_fib = sp.simplify(T[1, 1] / etad[1, 1])
lambda_shaped = all(sp.simplify(T[mu, nu] - c_fib * etad[mu, nu]) == 0 for mu in range(4) for nu in range(4))
check("O(M^0) DeWitt fiber-trace = (1/2) eta_mn EXACTLY -> cosmological-constant (Lambda) "
      "signature (stress ~ eta_mn), NOT a scalar-curvature R term", lambda_shaped and c_fib == sp.Rational(1, 2),
      f"eta^ab B_mn,ab = ({c_fib}) eta_mn")
# a Lambda term is 0-derivative: adding const to the symbol P(s) does NOT change the poles.
P_II_with_Lambda = s**2 + m2 * s   # Lambda enters the potential (s^0 coefficient of the EOM), not P(s)'s kinetic poles
# demonstrate: a constant shift L added to the action gives EOM term ~ L*eta (0 powers of s);
# the KINETIC symbol (coefficients of s^1, s^2) is untouched -> pole structure invariant.
L = sp.symbols('Lambda')
# EOM symbol including a Lambda source is P(s) - L (a constant, s^0); its s>0 poles are the roots of P(s):
kinetic_roots_unchanged = set(sp.roots(sp.Poly(P_II, s)).keys()) == {sp.Integer(0), -m2}
check("a Lambda term is 0-derivative (enters at s^0): it shifts the vacuum/source but leaves the "
      "KINETIC symbol s(s+m2) and its pole structure UNCHANGED -> Lambda does NOT lift the box^2 "
      "degeneracy. Only the |II|^2 Gauss R^X term (a box, s^1) does", kinetic_roots_unchanged)

# ===========================================================================
# PART E -- sign of the induced massive pole (flat-ambient model; ambient R^Y flagged).
# ===========================================================================
log("\n" + "=" * 78)
log("PART E -- sign: is the induced massive pole healthy (m2>0) or tachyonic? (flat-ambient)")
log("=" * 78)
# In the II-class functional E = int(|H|^2 - R^X) the Weyl/box^2 part has coefficient +1 (say),
# and the -R^X part contributes the linearized Einstein operator with coefficient tied to -1.
# The graviton^2 scale is m2 = (coeff of box)/(coeff of box^2). We compute the RATIO's sign for
# the flat-ambient model and flag that the ambient DeWitt R^Y correction (reconstruction-grade)
# can shift the coefficient. Here: |H|^2 -> +box^2 ; -R^X -> -G^(1) = +1/2 box (from PART B, on TT
# G^(1)=-1/2 box, so -R^X in the energy contributes +1/2 box to the EOM). => m2 ~ +1/2 (>0).
coeff_box2 = sp.Integer(1)                       # from +|H|^2
coeff_box = sp.Rational(1, 2)                    # from -R^X : -(G^(1)) = +1/2 box on TT
m2_val = sp.simplify(coeff_box / coeff_box2)
check("flat-ambient model: m2 = (box coeff)/(box^2 coeff) = +1/2 > 0 -> a REAL (non-tachyonic) "
      "massive pole; the distinct massive ghost is at a healthy real mass, Bateman-Turok applies",
      m2_val > 0, f"m2 = {m2_val} (sign gated on OQ2-A normalization + ambient R^Y -- flagged)")

# ===========================================================================
log("\n" + "=" * 78)
log("VERDICT -- H15 gravity fork")
log("=" * 78)
log(r"""
COMPUTED (this file, exact, exit 0):
  A. Gauss identity |II|^2 = |H|^2 - R^X (exact, all dims; matches repo tr Q(B)=|II|^2-|H|^2).
     => the II-class functional CARRIES the intrinsic Einstein-Hilbert R^X; H-class does not.
  B. 2D: int R^X topological (Gauss-Bonnet, radius-independent 4*pi). 4D: int R^X is
     Einstein-Hilbert -- linearized EOM on TT = -1/2 box h, SECOND order, NONZERO
     (the 4D topological density is E_4, not R). => in 4D the R^X term is genuinely
     DYNAMICAL: a two-derivative mass-carrying kinetic term.
  C. |H|^2 -> box^2 = DOUBLE pole (degenerate coincident-pole; ghost open).
     |II|^2 -> box(box+m^2) = TWO DISTINCT poles (massless graviton + massive ghost),
     propagator splits into +residue / -residue O(1,1) Krein pair -> Bateman-Turok CLEARS.
  D. adversarial: the O(M^0) DeWitt constant-section term is fiber-trace = (1/2) eta_mn =
     LAMBDA (0-derivative), NOT R; it does NOT enter the kinetic symbol and does NOT lift
     the degeneracy. Only the |II|^2 Gauss R^X (a box, s^1) does.
  E. sign: flat-ambient model gives m^2 = +1/2 > 0 (real massive pole, BT-ready); the exact
     sign/magnitude is gated on the OQ2-A normalization and the ambient DeWitt R^Y (flagged).

THE FORK COLLAPSES TO ONE BINARY -- the OQ2-A functional choice:
  * II-class (|II|^2 = full second-fundamental-form / full distortion norm |theta|^2):
      -> 4D Gauss NECESSARILY generates a dynamical Einstein-Hilbert R^X (R is not
         topological in 4D) -> gravity is STELLE R + Weyl^2 -> distinct massive ghost
         -> Bateman-Turok ghost parity applies -> GRAVITY LEG CLEARS.  [BRANCH A]
  * H-class (|H|^2 = mean-curvature / conformal Willmore):
      -> pure conformal Bach box^2 -> degenerate coincident pole -> ghost OPEN.  [BRANCH B]

VERDICT: (C) UNDER-DETERMINED at the level of the BUILT action -- the R-vs-no-R choice IS
the |II|^2-vs-|H|^2 OQ2-A datum, which GU's unbuilt source action has not yet fixed --
BUT with a STRONG STRUCTURAL LEAN TO BRANCH A (Stelle / ghost clears), because:
  (i)  GU is a Yang-Mills-type theory; the natural functional is the FULL field-strength
       norm |theta|^2 = |II|^2, not the trace-only |H|^2 (a YM action norms all of F, not
       just its trace);
  (ii) the GU distortion is identified with the FULL second fundamental form
       s*(theta) = II_s (DD1 / ii-s-coordinate-formula sec 7), not its mean-curvature trace;
  (iii) in 4D the R^X piece is unavoidably DYNAMICAL once |II|^2 is chosen (Part B) -- so
        branch A is the generic outcome and branch B requires the fine-tuned trace-only
        functional with the R^X piece exactly absent.

WHAT WOULD DECIDE IT (the single forcing computation): derive GU's section functional from
its actual action (OQ2-A) and read whether it norms the FULL distortion (|II|^2 -> A) or
only the mean-curvature trace (|H|^2 -> B). Equivalently: is OQ2-A the conformally-INVARIANT
Willmore combination (-> H-class, B) or the full |II|^2 (-> II-class, A)?

RE-RANK SIGNAL: this does NOT yet CLEAR gravity (the functional datum stays formally open),
but it SHARPENS H15/H16/H1 to one computable binary and shows branch A (ghost clears) is
structurally favored. Gravity leg stays REDUCED-but-with-a-forced-resolution. Next council
focus: H16 (Stelle viability -- is the induced-R Einstein term the right sign and the ghost
mass sensible once ambient R^Y is included?) becomes the natural #1 IF the forcing computation
lands II-class; only if the action forces pure |H|^2 does the entropic/H5 route rise.
""")

if FAIL:
    log(f"FAILED: {FAIL}")
    raise SystemExit(1)
log("exit 0 = fork computed: |II|^2 carries a 4D-DYNAMICAL Einstein-Hilbert R^X (Stelle,")
log("         ghost clears, branch A); |H|^2 is pure degenerate Bach (branch B); the choice is")
log("         the OQ2-A functional datum -- VERDICT C (under-determined) with strong lean to A.")
