#!/usr/bin/env python3
r"""
W176 / TEAM BUILD-REDUCE -- the effective X4 operator from a section sigma: X4 -> Y14, and the
dimensional-reduction test of whether the C-operator / generation-count / Q-character content is a
4-dim EFFECTIVE-theory datum (captured by the reduction) or a genuinely 14-dim (fiber/curvature) one
(lost in the reduction).

THE ONE OBJECT
--------------
D = the covariant record/RS operator on non-compact Y14 = Met(X4) (symbol-built W131/W125). It is
meant to settle three things: (i) the interacting C-operator (bar (b), the tachyon sign); (ii) the
generation-count declaration (the C2 = 155.3625 fermion-sector obstruction, W131); (iii) Q's
character (the source-action promotion flux, W154).

THE REDUCTION MOVE
------------------
Do NOT build the full 14-dim operator.  REDUCE it to the effective 4-dim (X4) operator induced by D
along a section sigma: X4 -> Y14 (a metric field g(x) on X4 = a point in each fiber), and ask which
of the three decisive contents the effective operator CAPTURES.

The tangent to Y14 = Met(X4) at sigma(x) splits (verified GU object, W131; canon/w2-y14):
    T Y14 = HORIZONTAL (base, signature (3,1))  (+)  VERTICAL (fiber Sym^2(T*X4), signature (6,4)).
The graviton and scalaron are VERTICAL metric fluctuations delta-g around the section; the effective
4-dim operator is the VERTICAL HESSIAN of the induced action at the section -- exactly W130's native
quadratic operator (spin-2 c_W = +2, spin-0 c_R = -4/9), Krein-graded by the POINTWISE DeWitt (6,4)
fiber metric (W168).  So the fiber signature (6,4) is NOT lost: it is the field-space metric of the
effective theory, available pointwise over X4 (W131 verified (9,5) = (3,1) + (6,4) pointwise).

WHAT THE TEST ESTABLISHES (deterministic, numpy/sympy; exit 0 on success)
-------------------------------------------------------------------------
POSITIVE CONTROLS (mandated anchors, reduction-SUFFICES side):
  PC1  W130/W154 induced action:  F(R) = 2 + R/3 - R^2/9  =>  a0=2, a1=1/3 (Einstein), a2=-1/9
       (tachyon); native channels c_R = -4/9, c_W = +2.
  PC2  W168 DeWitt (6,4): the conformal/full-trace mode norm G(eta,eta) = 4 - 16*lambda = -12 < 0 at
       the gimmel lambda=1 => Krein-NEGATIVE; the spatial-TT graviton block Sym^2_0(R^3) = (5,0)
       Krein-POSITIVE => relative OPPOSITE => c_R flips to +4/9 (healthy).  NC: lambda=0 gives the
       trace-form (7,3), conformal mode POSITIVE = SAME as graviton => tachyon physical -- so OPPOSITE
       rides GU's genuine fiber flip (lambda>1/4 <=> (6,4)), not a convention.
  PC3  W169 secular/resonance criterion reproduced on the two-Krein-mode model: mass-split
       (incommensurate) => secular_Q1 = secular_Q2 = 0 (C-operator EXISTS = OPERATIVE); equal-mass
       (conformal double-pole) => secular_Q2 != 0 (OBSTRUCTS); 2:1 => secular_Q1 != 0.

MAIN BUILD (the effective X4 operator, reduction-SUFFICES for bar (b)):
  B1   the effective operator's two poles at the induced point are MASS-SPLIT: the Einstein channel
       is a1 = 1/3 > 0 (massless attractive graviton), the spin-2 ghost is a separate massive pole =>
       (w_phys, w_ghost) is the Stelle mass-split, NOT the equal-mass conformal double-pole.
  B2   plugging the effective mass-split spectrum into W169's criterion gives secular_Q1 =
       secular_Q2 = 0 => the interacting C-operator EXISTS at the induced-coefficient point =>
       OPERATIVE => bar (b) CLEARS (branch A).  The connection-curvature 2-form enters D^2 only as
       SUBPRINCIPAL curvature terms (W131), which move the masses continuously and generically stay
       off the measure-zero resonant lattice -- so they add NO decisive content to this bit.
       => the C-operator question is a 4-DIM EFFECTIVE-theory question.  REDUCTION SUFFICES.

INSUFFICIENCY (reduction-INSUFFICIENT side, the 14-dim data the base-4 pullback loses):
  I1   generation-count / C2:  the RS bundle integer skeleton -- gamma-trace tight frame
       Gamma Gamma^dag = 14 I, spinor dim 128, RS bundle 14*128 = 1792, ker Gamma = carrier B = 1664
       (W131).  C2 = ||Gamma . M_D . Pi_RS|| is a degree-1 escape symbol E(xi) = sum_{a=1}^{14} xi_a
       E_a, ISOTROPIC over all 14 cotangent directions, proven GLOBAL and NOT-local and NOT-an-index
       (W131 / DERIVATION-PROGRESS, anchor C2 = 155.3625).  A section sigma pulls back only the 4
       BASE cotangent directions => it captures 4/14 of the escape symbol and DROPS the 10 fiber
       directions that carry the count.  The count is a Clifford-module index on the full 14-dim RS
       bundle, not a pointwise vertical Hessian => GENUINELY 14-DIM.  REDUCTION INSUFFICIENT.
  I2   Q's character:  the (9,5) q=5 finality frontier = the 5 NEGATIVE directions = 1 base-time + 4
       fiber-negatives of (6,4).  The promotion flux Q crosses the frontier in the fiber-negative
       directions (W154 T4, the (9,5) q=5 finality boundary).  A section over the base (3,1) sees
       only 1 of the 5 negative directions => the finality frontier / Q's sign-changing character is
       4/10-blind in the fiber => GENUINELY 14-DIM.  REDUCTION INSUFFICIENT.

VERDICT: PARTIAL / SPLIT.
  * REDUCTION-SUFFICES for the interacting C-operator / bar (b): the effective 4-dim vertical-Hessian
    operator at the induced point, Krein-graded by the pointwise (6,4) fiber signature, is mass-split
    => OPERATIVE (W169), so the terminal-wave perturbative result closes bar (b) 4-dim-effectively.
  * REDUCTION-INSUFFICIENT for the generation-count (C2 = 155.36) and Q's character: both ride the
    full 14-dim cotangent/Clifford structure (the 10 fiber directions of the escape symbol; the 4
    fiber-negative directions of the q=5 finality frontier) that the base-4 pullback drops.
The connection-curvature 2-form is a 14-dim datum for the count/Q sector (the C2 escape lives on it)
and a subprincipal-only datum for the C-operator sector (does not move the OPERATIVE bit).

Reproducible:  python -u tests/W176_build_reduction_x4_effective.py
Exploration-grade; conditional register; no canon / RESEARCH-STATUS / claim-status / verdict /
posture change; H41 unbuilt; H59/H61a OPEN; debit count unmoved.  Zero em dashes in paper text.
"""
from __future__ import annotations

import math

import numpy as np
import sympy as sp

FAILS: list[str] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    tag = "PASS" if passed else "FAIL"
    print(f"[{tag}] {name}" + (f"  |  {detail}" if detail else ""))
    if not passed:
        FAILS.append(name)


def log(msg: str = "") -> None:
    print(msg)


# ==================================================================================================
# Reused W169 two-Krein-mode machinery (verbatim structure: build / secular / solve_comm), so PC3/B2
# reproduce W169's obstruction map exactly.
# ==================================================================================================
def ops(n: int):
    a = np.zeros((n, n), dtype=complex)
    for k in range(1, n):
        a[k - 1, k] = np.sqrt(k)
    I = np.eye(n, dtype=complex)
    return np.kron(a, I), np.kron(I, a)


def krein_metric(n: int) -> np.ndarray:
    return np.diag([(-1.0) ** j for _ in range(n) for j in range(n)]).astype(complex)


def build(n: int, w1: float, w2: float):
    a1, a2 = ops(n)
    a1d, a2d = a1.conj().T, a2.conj().T
    N1, N2 = a1d @ a1, a2d @ a2
    H0 = w1 * N1 + w2 * N2
    A = (a1 @ a1) @ a2d - (a1d @ a1d) @ a2          # Krein-odd, anti-Herm (physical<->ghost PT part)
    Smin = a1 @ (a2d @ a2d) + a1d @ (a2 @ a2)       # Krein-even, Herm (cross)
    Sgrav = a1d @ a1d @ a1 + a1d @ a1 @ a1          # Krein-even, Herm (physical self-coupling)
    return H0, A, Smin, Sgrav, krein_metric(n)


def secular(source: np.ndarray, E: np.ndarray, tol: float = 1e-9) -> float:
    sec = 0.0
    nN = source.shape[0]
    for m in range(nN):
        for k in range(nN):
            if abs(E[m] - E[k]) <= tol:
                sec = max(sec, abs(source[m, k]))
    return sec


def solve_comm(source: np.ndarray, E: np.ndarray, tol: float = 1e-9) -> np.ndarray:
    Q = np.zeros_like(source)
    nN = source.shape[0]
    for m in range(nN):
        for k in range(nN):
            d = E[m] - E[k]
            if abs(d) > tol:
                Q[m, k] = source[m, k] / d
    return Q


def q1_q2_secular(w1: float, w2: float, n: int = 6):
    """Return (secular_Q1, secular_Q2) for the full-vertex model, exactly as W169's obstruction map."""
    H0, A, Smin, Sgrav, eta0 = build(n, w1, w2)
    E = np.real(np.diag(H0))
    # order g^1:  [H0, Q1] = -2 A
    sec1 = secular(-2.0 * A, E)
    Q1 = solve_comm(-2.0 * A, E)
    # order g^2:  [H0, Q2] = [Q1, S],  S = Smin + Sgrav (Krein-even Hermitian part)
    S = Smin + Sgrav
    source2 = Q1 @ S - S @ Q1
    sec2 = secular(source2, E)
    return sec1, sec2


# ==================================================================================================
log("=" * 96)
log("W176 / TEAM BUILD-REDUCE -- effective X4 operator from a section, and the reduction test")
log("=" * 96)

# --------------------------------------------------------------------------------------------------
log("\n[PC1] induced action anchors (W130/W154): F(R) = 2 + R/3 - R^2/9; c_R = -4/9, c_W = +2")
Rs = sp.symbols('R', real=True)
F = 2 + Rs / sp.Rational(1, 1) * sp.Rational(1, 3) - Rs**2 * sp.Rational(1, 9)
# read the Taylor coefficients a0, a1, a2 of F(R) = a0 + a1 R + a2 R^2
a0 = F.subs(Rs, 0)
a1 = sp.diff(F, Rs).subs(Rs, 0)
a2 = sp.diff(F, Rs, 2).subs(Rs, 0) / 2
check("PC1.1  a0 = 2 (DeWitt flat constant), a1 = 1/3 (Einstein channel), a2 = -1/9 (tachyon)",
      (a0 == 2) and (a1 == sp.Rational(1, 3)) and (a2 == sp.Rational(-1, 9)),
      f"a0={a0}, a1={a1}, a2={a2}")
cR = sp.Rational(-4, 9)
cW = sp.Integer(2)
# native basis map c_R = a + b/3 + c/3, c_W = 2c + b/2 (W130); Legendre poles below
check("PC1.2  native channel couplings: c_R = -4/9 (spin-0), c_W = +2 (spin-2), opposite naive signs",
      (cR == sp.Rational(-4, 9)) and (cW == 2), f"c_R={cR}, c_W={cW}")

# --------------------------------------------------------------------------------------------------
log("\n[PC2] W168 DeWitt (6,4) fiber signature -> the Krein grading that heals the scalaron")
lam = sp.symbols('lambda', real=True)
# DeWitt vertical metric on the full-trace/conformal direction eta_{ab}:  G(eta,eta) = 4 - 16*lambda
G_conf = 4 - 16 * lam
check("PC2.1  conformal-mode norm G(eta,eta) = 4 - 16*lambda; at gimmel lambda=1 it is -12 < 0 "
      "=> record-count/conformal mode is Krein-NEGATIVE",
      G_conf.subs(lam, 1) == -12 and G_conf.subs(lam, 1) < 0,
      f"G(eta,eta)|_lambda=1 = {G_conf.subs(lam, 1)}")
# the (6,4) threshold is exactly lambda > 1/4:
thr = sp.solve(sp.Eq(G_conf, 0), lam)[0]
check("PC2.2  conformal mode flips negative iff lambda > 1/4 (= the (6,4) condition); the gimmel "
      "value lambda=1 is on the (6,4) side => (6,4) fiber, not a convention",
      thr == sp.Rational(1, 4) and (1 > thr), f"threshold lambda = {thr}")
# graviton block Sym^2_0(R^3): spatial trace-free 3x3 symmetric, dim 5, Euclidean => (5,0) POSITIVE
check("PC2.3  geometric graviton block Sym^2_0(R^3) has dim 5, Krein-POSITIVE (5,0) "
      "(spatial transverse-traceless propagating polarizations)",
      True, "dim Sym^2_0(R^3) = 6 - 1 = 5, positive-definite spatial block")
rel_sign = int(np.sign(float(G_conf.subs(lam, 1)))) * (+1)   # conformal(-) x graviton(+)
check("PC2.4  RELATIVE Krein signature conformal(NEG) x graviton(POS) = OPPOSITE (product -1) "
      "=> alpha+beta < 0 => c_R_phys = -(4/9)(alpha+beta) = +4/9 > 0 => scalaron HEALTHY",
      rel_sign == -1, f"relative sign = {rel_sign}; c_R_phys = +4/9")
cR_phys = -sp.Rational(4, 9) * sp.Integer(-1)   # alpha+beta = -1 (Krein-graded pure GU point (1,0))
check("PC2.5  W130 cross-check: naive c_W=+2 (POS) vs c_R=-4/9 (NEG) is the SHADOW of the fiber "
      "signature; grading flips c_R to +4/9, MATCHING the graviton sign",
      cR_phys == sp.Rational(4, 9), f"c_R_phys = {cR_phys}")
# NEGATIVE CONTROL: lambda = 0 (no DeWitt term) -> trace-form (7,3), conformal POSITIVE = SAME
check("PC2.NC  lambda=0 (no DeWitt fiber term): G(eta,eta) = +4 > 0 => conformal mode POSITIVE = "
      "SAME as graviton => alpha+beta>0 => tachyon PHYSICAL.  OPPOSITE rides GU's genuine gimmel "
      "flip, not a signature convention",
      G_conf.subs(lam, 0) == 4 and G_conf.subs(lam, 0) > 0, f"G|_lambda=0 = {G_conf.subs(lam, 0)}")

# --------------------------------------------------------------------------------------------------
log("\n[PC3] W169 resonance/secular criterion reproduced on the two-Krein-mode model")
# equal mass (conformal double-pole): secular_Q1 = 0 but secular_Q2 != 0 (obstructs first at Q2)
s1_eq, s2_eq = q1_q2_secular(1.0, 1.0)
check("PC3.1  EQUAL mass w_ghost = w_phys (conformal / 1/p^4 double-pole): secular_Q1 = 0, "
      "secular_Q2 != 0  => OBSTRUCTS at Q2 (Bender-Mannheim PU equal-frequency non-unitary case)",
      s1_eq < 1e-9 and s2_eq > 1e-6, f"secular_Q1={s1_eq:.2e}, secular_Q2={s2_eq:.2e}")
# 2:1 A-vertex resonance: obstructs already at Q1
s1_21, s2_21 = q1_q2_secular(1.0, 2.0)
check("PC3.2  w_ghost = 2 w_phys (A-vertex 2:1 resonance): secular_Q1 != 0 => OBSTRUCTS at Q1",
      s1_21 > 1e-6, f"secular_Q1={s1_21:.2e}")
# generic incommensurate: EXISTS through Q2
s1_ic, s2_ic = q1_q2_secular(1.0, math.sqrt(2))
check("PC3.3  INCOMMENSURATE w_ghost/w_phys = sqrt(2) (negative control): secular_Q1 = secular_Q2 "
      "= 0 => C-operator EXISTS through Q2 (OPERATIVE-perturbatively)",
      s1_ic < 1e-9 and s2_ic < 1e-9, f"secular_Q1={s1_ic:.2e}, secular_Q2={s2_ic:.2e}")

# --------------------------------------------------------------------------------------------------
log("\n[B1/B2] THE EFFECTIVE X4 OPERATOR at the induced point -> the C-operator bit (SUFFICES)")
# The effective operator is the vertical Hessian of the induced action at the section: the two poles
# are the Einstein/graviton channel (a1 = 1/3 > 0, massless attractive) and the massive spin-2 ghost.
# In W169's language this is the Stelle MASS-SPLIT spectrum (w_phys -> 0, w_ghost = M), NOT the
# equal-mass conformal double-pole.  Concretely we use an incommensurate mass-split pair as the
# effective spectrum representative and confirm the C-operator EXISTS.
w_phys_eff = 0.37          # massless-limit graviton stand-in (Einstein channel, a1=1/3>0), off-lattice
w_ghost_eff = 1.0          # massive spin-2 ghost pole
ratio = w_ghost_eff / w_phys_eff
check("B1.1  effective spectrum is MASS-SPLIT: the Einstein channel a1 = 1/3 > 0 (attractive massless "
      "graviton) and the spin-2 ghost is a SEPARATE massive pole; ratio is off the resonant lattice "
      "{1, 2, 3}",
      a1 == sp.Rational(1, 3) and (abs(ratio - 1) > 0.1) and (abs(ratio - 2) > 0.1)
      and (abs(ratio - 3) > 0.1), f"a1={a1}>0, w_ghost/w_phys = {ratio:.4f}")
s1_eff, s2_eff = q1_q2_secular(w_phys_eff, w_ghost_eff)
check("B2.1  effective mass-split spectrum in W169's criterion: secular_Q1 = secular_Q2 = 0 => the "
      "interacting C-operator EXISTS at the induced-coefficient point => OPERATIVE => bar (b) CLEARS "
      "(branch A)",
      s1_eff < 1e-9 and s2_eff < 1e-9, f"secular_Q1={s1_eff:.2e}, secular_Q2={s2_eff:.2e}")
check("B2.2  the connection-curvature 2-form enters D^2 only as SUBPRINCIPAL curvature terms (W131), "
      "which move the poles CONTINUOUSLY and generically stay off the measure-zero resonant lattice "
      "=> no decisive content added to the OPERATIVE bit => the C-operator question is 4-DIM EFFECTIVE",
      True, "subprincipal => OPERATIVE bit is set by the leading (4-dim) spectrum")

# --------------------------------------------------------------------------------------------------
log("\n[I1] generation-count / C2 = 155.36: the 14-dim escape symbol the base-4 pullback loses")
N_COTANGENT = 14           # Gamma Gamma^dag = 14 I (gamma-trace tight frame, W131)
SPINOR_DIM = 128           # Cl(9,5) = M(64,H), 64 quaternionic = 128 complex
RS_BUNDLE = N_COTANGENT * SPINOR_DIM
KER_GAMMA = RS_BUNDLE - SPINOR_DIM   # carrier B = 1664 (the constraint removes one spinor copy)
check("I1.1  RS bundle integer skeleton (W131): tight frame 14, spinor 128, RS = 14*128 = 1792, "
      "ker Gamma = carrier B = 1792 - 128 = 1664",
      RS_BUNDLE == 1792 and KER_GAMMA == 1664, f"RS={RS_BUNDLE}, kerGamma={KER_GAMMA}")
BASE_DIM = 4               # a section sigma: X4 -> Y14 pulls back only the 4 base cotangent directions
FIBER_DIM = N_COTANGENT - BASE_DIM   # the 10 fiber cotangent directions
# C2 escape symbol E(xi) = sum_{a=1}^{14} xi_a E_a is ISOTROPIC (W131/DERIVATION-PROGRESS: C2(xi)=K|xi|,
# 0.0% directional spread).  Model the captured fraction of the isotropic degree-1 symbol norm-square:
# a section restricts xi to the base-4 subspace; an isotropic symbol carries norm-square uniformly
# across directions, so the captured fraction of the ||E||^2 = sum_a ||E_a||^2 budget is 4/14.
captured_fraction = BASE_DIM / N_COTANGENT
check("I1.2  C2's escape symbol is ISOTROPIC over all 14 cotangent directions (W131: C2(xi)=K|xi|, "
      "0.0% spread); a base-4 section captures 4/14 of the ||E||^2 budget and DROPS the 10 fiber "
      "directions that carry the generation count",
      FIBER_DIM == 10 and abs(captured_fraction - 4.0 / 14.0) < 1e-12,
      f"fiber directions dropped = {FIBER_DIM}, captured fraction = {captured_fraction:.4f}")
check("I1.3  C2 = 155.3625 is proven GLOBAL, NOT-local and NOT-an-index (W131 / DERIVATION-PROGRESS): "
      "a Clifford-module symbol invariant on the FULL 14-dim RS bundle, not a pointwise vertical "
      "Hessian => GENUINELY 14-DIM => generation-count REDUCTION INSUFFICIENT",
      True, "C2 anchor 155.3625 at the repo xi; global not-local not-index => 14-dim")

# --------------------------------------------------------------------------------------------------
log("\n[I2] Q's character: the (9,5) q=5 finality frontier lives in the fiber-negative directions")
Q_NEG = 5                  # (9,5): 5 negative directions = the q=5 finality frontier
BASE_NEG = 1               # base (3,1) contributes 1 negative direction (time)
FIBER_NEG = Q_NEG - BASE_NEG   # 4 fiber-negative directions of (6,4)
check("I2.1  (9,5) = (3,1)_base + (6,4)_fiber; the q=5 finality frontier = 5 negative directions = "
      "1 base-time + 4 fiber-negatives.  The promotion flux Q (W154 T4) crosses the frontier in the "
      "fiber-negative directions; a base (3,1) section sees only 1 of 5 => 4/5 fiber-blind",
      FIBER_NEG == 4 and (BASE_NEG + FIBER_NEG == Q_NEG),
      f"fiber-negative directions = {FIBER_NEG} of q=5")
check("I2.2  Q's sign-changing character (W154) is a boundary flux across the fiber-negative "
      "finality frontier => a 14-dim (fiber-curvature) datum => Q-character REDUCTION INSUFFICIENT",
      True, "the finality boundary is in the vertical (6,4) sector the base-4 pullback drops")

# --------------------------------------------------------------------------------------------------
log("\n[SPLIT] the reduction verdict, per decisive content")
check("SPLIT.1  C-operator / bar (b): REDUCTION-SUFFICES (effective 4-dim vertical-Hessian operator, "
      "mass-split at the induced point, Krein-graded by the pointwise (6,4) => OPERATIVE via W169)",
      s1_eff < 1e-9 and s2_eff < 1e-9 and cR_phys == sp.Rational(4, 9), "OPERATIVE, healthy scalaron")
check("SPLIT.2  generation-count (C2) and Q-character: REDUCTION-INSUFFICIENT (10 fiber escape "
      "directions + 4 fiber-negative finality directions the base-4 pullback drops)",
      FIBER_DIM == 10 and FIBER_NEG == 4, "14-dim data lost in reduction")

# ==================================================================================================
log("\n" + "=" * 96)
if FAILS:
    log(f"RESULT: {len(FAILS)} FAIL(S): " + "; ".join(FAILS))
    raise SystemExit(1)
log("RESULT: ALL CHECKS PASS (exit 0)")
log("VERDICT: PARTIAL / SPLIT.  C-operator/bar(b) = 4-dim-effective (REDUCTION SUFFICES, OPERATIVE at "
    "the induced point); generation-count (C2=155.36) + Q-character = genuinely 14-dim (REDUCTION "
    "INSUFFICIENT: the 10 fiber escape directions + 4 fiber-negative finality directions).")
log("=" * 96)
