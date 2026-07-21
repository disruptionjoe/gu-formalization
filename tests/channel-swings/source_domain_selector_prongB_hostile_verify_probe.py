"""
HOSTILE-VERIFY probe for Prong B (source-domain-selector no-go).

Attacks the NONCOMPACT TRANSFER. Prong B computes its domain moduli on a
COMPACT collar [a,b], where a regular first-order d x d system AUTOMATICALLY
has deficiency (d,d) and a full U(d) of extensions -- so "multiplicity" there
is nearly free and may say nothing about GU's true noncompact fiber. On the
noncompact fiber the honest question is Weyl LIMIT-POINT / LIMIT-CIRCLE at each
end, and the moduli DIMENSION is set by the deficiency indices, i.e. the number
of L^2 solutions of (A - lambda)u = 0 (Im lambda != 0) at each end.

We do NOT need GU's exact operator to make the structural point: we need a
model whose END-ASYMPTOTICS can be DIALED so the moduli dimension CHANGES.
Canonical Weyl model  -y'' + q(s) y = lambda y  on [1, inf)  (a scalar
reduction of a first-order Dirac-type system), at lambda = i.

L^2 COUNT (robust, non-oscillatory WKB-amplitude criterion). The two WKB
solutions are  y_pm ~ (q-lambda)^{-1/4} exp( +- int sqrt(q-lambda) ).  Hence
  |y_pm(s)|^2 = |q-lambda|^{-1/2} exp( +- 2 int_1^s Re sqrt(q-lambda) dt ).
The exponent integrand Re sqrt(q-lambda) is SMOOTH and NON-oscillatory, so
int |y_pm|^2 is computed with no phase/amplitude drift. n = #{ signs pm :
int_1^inf |y_pm|^2 < inf } = deficiency index at the infinite end.
(Direct oscillatory ODE integration of |y|^2 is deliberately AVOIDED here: over
hundreds of wavelengths RK amplitude drift corrupts the tail; the WKB envelope
is the honest asymptotic object that decides L^2 membership.)

DIAL (classical Weyl/Titchmarsh), q = c*s^p, lambda = i:
    * q = -s^p, p < 2 (slow -inf)  : LIMIT-POINT  n=1
    * q = -s^p, p = 2 (borderline) : LIMIT-POINT  n=1
    * q = -s^p, p > 2 (fast -inf)  : LIMIT-CIRCLE n=2  (a U(1) of BCs survives)
    * q = +s^p (confining, c>0)    : LIMIT-POINT  n=1  (unique domain-end)
Crossing p=2 with FIXED sign flips n between 1 and 2 -> the moduli dimension is
a FUNCTION OF THE END-ASYMPTOTICS, which for GU is the SOURCE-SILENT D2 datum
(Prong A). A limit-point end KILLS a torus factor; limit-circle KEEPS it.

CONTROLS:
  (C1) COMPACT COLLAR: on a FIXED finite [1,3] BOTH branches are L^2 for EVERY
       p -> "n=2 always". Compactness MANUFACTURES full deficiency (d,d),
       blind to LP/LC. Prong B's T^2 (dim 2) and U(1) floor live here.
  (C2) Independent NON-WKB cross-check: the confining q=+s^3 end integrated as
       a DIRECT (monotone, non-oscillatory) ODE -> one exp-decaying (L^2) + one
       exp-growing solution -> n=1, confirming the WKB count.
  (C3) FIRST-ORDER Dirac tie-in: H = -i s2 d_s + m s1 at lambda=i has REAL
       coefficient eigenvalues +- sqrt(1+m^2) -> one decay + one grow -> n=1
       for ANY constant mass. Full first-order boundary freedom requires the
       PRINCIPAL COEFFICIENT to DEGENERATE at the end (GU's wall C_0=q^{1/2}->0)
       -- again the D2 asymptotic datum, not fixed by sources.

Deterministic, foreground, no network, no file writes. Exit 0 = assertions held.
"""

import numpy as np
from scipy.integrate import cumulative_trapezoid, solve_ivp

LAM = 1j  # non-real spectral parameter: deficiency indices well-defined here


# ---------------------------------------------------------------------------
# WKB-amplitude L^2 counter for -y'' + q y = lambda y on [1, R].
# ---------------------------------------------------------------------------
def l2_count(qfun, R, N=300000):
    s = np.linspace(1.0, R, N)
    qm = qfun(s) - LAM                       # q - lambda (complex)
    reg = np.real(np.sqrt(qm))               # Re sqrt(q-lambda): smooth, non-osc
    Phi = cumulative_trapezoid(reg, s, initial=0.0)   # \int_1^s Re sqrt
    half_log = 0.5 * np.log(np.abs(qm))      # (1/2) log|q-lambda|
    detail = {}
    for sign in (+1, -1):
        logint = -half_log + sign * 2.0 * Phi         # log |y_sign|^2
        if logint[-1] > 50.0:                          # integrand exploding
            detail[sign] = (False, float("inf")); continue
        integ = np.exp(logint)
        I = cumulative_trapezoid(integ, s, initial=0.0)
        Ifull, Ihalf = I[-1], I[int(0.7 * N)]
        conv = (Ifull < 1e12) and (Ifull - Ihalf) < 0.03 * max(Ifull, 1e-30)
        detail[sign] = (bool(conv), float(Ifull))
    n = sum(1 for sg in detail if detail[sg][0])
    return n, detail


def report(name, qfun, R):
    n, d = l2_count(qfun, R)
    tag = "LIMIT-CIRCLE (U(1) of BCs survives)" if n == 2 else \
          "LIMIT-POINT (no boundary freedom)"
    print(f"  {name:22s} R={R:>7g}:  int|y_+|^2={d[+1][1]:.3e} (L2={d[+1][0]}), "
          f"int|y_-|^2={d[-1][1]:.3e} (L2={d[-1][0]})  ->  n={n}  {tag}")
    return n


print("=== HOSTILE-VERIFY: noncompact LP/LC transfer for the domain moduli ===\n")

# ---------------------------------------------------------------------------
# DIAL: q = c*s^p. The deficiency index (=> moduli-end dimension) changes.
# ---------------------------------------------------------------------------
print("[DIAL] -y''+q y = i y : deficiency index n is set by END-ASYMPTOTICS")
n_lp_slow = report("q = -s^1.5  (p<2)", lambda s: -s**1.5, 1e4)
n_border  = report("q = -s^2    (p=2)", lambda s: -s**2,  1e4)
n_lc      = report("q = -s^3    (p>2)", lambda s: -s**3,  1e4)
n_conf    = report("q = +s^3  (confine)", lambda s: s**3,  8.0)

assert n_lp_slow == 1, ("p=1.5 must be LIMIT-POINT n=1", n_lp_slow)
assert n_border == 1,  ("p=2 borderline must be LIMIT-POINT n=1", n_border)
assert n_lc == 2,      ("p=3 must be LIMIT-CIRCLE n=2", n_lc)
assert n_conf == 1,    ("confining must be LIMIT-POINT n=1", n_conf)
print(f"\n  DIAL RESULT: same family q=-s^p, moduli-end deficiency n changes "
      f"{n_lp_slow} (p=1.5) = {n_border} (p=2)  ->  {n_lc} (p=3).")
print(f"  A limit-point end (n=1) KILLS a boundary/torus factor; a limit-circle")
print(f"  end (n=2) KEEPS a U(1) of boundary conditions. Which one GU's fiber is")
print(f"  in depends on end-asymptotics of B, W~ = the SOURCE-SILENT D2 datum.\n")

# ---------------------------------------------------------------------------
# CONTROL C1: COMPACT COLLAR artifact. On FIXED finite [1,3] both branches are
# L^2 for EVERY asymptotic choice -> "n=2 always". Compactness manufactures
# full deficiency (d,d); it is blind to the LP/LC that governs the real fiber.
# ---------------------------------------------------------------------------
print("[CONTROL C1] compact collar [1,3]: full deficiency regardless of asymptotics")


def collar_norms(qfun, R=3.0, N=60000):
    # On a FINITE interval the L^2 count is trivial: BOTH branch integrals are
    # FINITE (continuous solutions on a compact set are automatically L^2).
    s = np.linspace(1.0, R, N)
    qm = qfun(s) - LAM
    Phi = cumulative_trapezoid(np.real(np.sqrt(qm)), s, initial=0.0)
    hl = 0.5 * np.log(np.abs(qm))
    out = {}
    for sign in (+1, -1):
        out[sign] = float(np.trapezoid(np.exp(-hl + sign * 2.0 * Phi), s))
    return out


for tag, q in [("q=-s^3", lambda s: -s**3),
               ("q=-s^1.5", lambda s: -s**1.5),
               ("q=+s^3", lambda s: s**3)]:
    nm = collar_norms(q)
    both = np.isfinite(nm[+1]) and np.isfinite(nm[-1]) and max(nm.values()) < 1e6
    print(f"  {tag:9s}: int|y_+|^2={nm[+1]:.3e}, int|y_-|^2={nm[-1]:.3e} "
          f"-> both FINITE on collar (n=2) = {both}")
    assert both, "on a compact interval every solution is L^2 -> full deficiency"
print("  => Prong B's T^2 (dim 2) and U(1) floor are COMPACT-COLLAR artifacts:")
print("     on [a,b] you ALWAYS get the full U(d); the deck-commutant torus is")
print("     the residue of a deficiency that is AUTOMATIC on a compact interval")
print("     and NOT guaranteed on the true noncompact fiber.\n")

# ---------------------------------------------------------------------------
# CONTROL C2: independent NON-WKB cross-check of the confining LP count via a
# DIRECT monotone (non-oscillatory) ODE integration of the fundamental matrix.
# q=+s^3: one super-exp-decaying (L^2) + one growing solution -> n=1.
# ---------------------------------------------------------------------------
print("[CONTROL C2] direct (non-WKB) ODE cross-check, confining q=+s^3")

def _rhs(s, v):
    Y = np.ascontiguousarray(v, float).view(complex).reshape(2, 2)
    A = np.array([[0.0, 1.0], [s**3 - LAM, 0.0]], dtype=complex)
    return (A @ Y).ravel().view(float)

Rc = 6.0
sol = solve_ivp(_rhs, (1.0, Rc), np.eye(2, dtype=complex).ravel().view(float),
                rtol=1e-11, atol=1e-14, method="RK45")
assert sol.success
Y = np.ascontiguousarray(sol.y[:, -1], float).view(complex).reshape(2, 2)
sv = np.linalg.svd(Y, compute_uv=False)
ratio = sv[0] / sv[1]
print(f"  fundamental matrix at s={Rc}: singular values = "
      f"({sv[0]:.3e}, {sv[1]:.3e}), ratio = {ratio:.3e}")
print(f"  one direction grows ~exp((2/5)s^5/2), one decays -> exactly 1 L^2 "
      f"solution (n=1), confirming the WKB count.")
assert ratio > 1e6, "confining end must show one dominant + one recessive (n=1)"
print()

# ---------------------------------------------------------------------------
# CONTROL C3: FIRST-ORDER Dirac tie-in. H = -i s2 d_s + m s1 with the PRINCIPAL
# coefficient B = -i s2 (invertible). (H-lambda)u=0 => u' = i s2 (lambda-m s1)u;
# at lambda=i the constant coefficient has REAL eigenvalues +- sqrt(1+m^2) ->
# one decay + one grow -> n=1 (LIMIT-POINT) for ANY mass. Crucially the decay
# rate = sqrt(1+m^2) >= |Im lambda| = 1 is BOUNDED BELOW: you CANNOT dial into
# limit-circle by changing the mass -- a NON-DEGENERATE Dirac end is ROBUSTLY
# limit-point (the Chernoff/complete-end default: unique domain, NO multiplicity).
# Leaving that default requires a SINGULAR end: the principal coefficient B must
# DEGENERATE (become non-invertible) at the fiber end -- exactly GU's wall where
# C_0 = q^{1/2} -> 0. Whether the fiber end is regular-type or singular is the
# asymptotic (D2) datum the sources do not fix.
# ---------------------------------------------------------------------------
print("[CONTROL C3] first-order Dirac  H = -i s2 d_s + m s1  at lambda=i "
      "(B = -i s2 invertible)")
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
rates = []
for m in [0.0, 1.0, 3.0]:
    Amat = 1j * s2 @ (LAM * np.eye(2) - m * s1)
    re = np.sort(np.linalg.eigvals(Amat).real)
    lp = (re[0] < -1e-9) and (re[1] > 1e-9)
    rates.append(abs(re).min())
    print(f"  m={m}: coeff real eigenvalues = {re.round(6)} -> "
          f"one decay + one grow (n=1, LIMIT-POINT) = {lp}; "
          f"decay rate = {abs(re).min():.4f}")
    assert lp, ("constant-mass Dirac end must be limit-point n=1", m)
assert min(rates) >= 1.0 - 1e-9, \
    "decay rate is bounded below by |Im lambda|=1: non-degenerate Dirac end is robustly LP"
print(f"  decay rate >= |Im lambda| = 1 for ALL masses -> a non-degenerate Dirac")
print(f"  end is ROBUSTLY limit-point (unique domain). LC (n=2, boundary freedom)")
print(f"  requires the PRINCIPAL COEFFICIENT B to DEGENERATE at the end (GU's")
print(f"  wall C_0->0) -- the singular-end / asymptotic (D2) datum, SOURCE-SILENT.")
print()

print("=== SUMMARY ===")
print(" noncompact deficiency n is DIALABLE by end-asymptotics: LP(n=1) <-> "
      "LC(n=2) across p=2, and confining -> LP.")
print(" compact collar forces n=2 for ALL asymptotics (Prong B's T^2/U(1) live here).")
print(" first-order Dirac is LP(n=1) for any constant mass; LC needs coefficient")
print("   DEGENERATION at the end -- the wall/asymptotic (D2) datum, SOURCE-SILENT.")
print("EXIT 0")
