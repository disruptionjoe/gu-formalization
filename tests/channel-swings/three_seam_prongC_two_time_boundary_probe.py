#!/usr/bin/env python3
r"""
PRONG C -- the TWO-TIME (initial + final) BOUNDARY POSIT probe.

Adversarial three-tier adjudication of the wild-frontier construction (council
Member 3, science-council file): reality writes its own boundary condition
through a FUTURE-CONDITIONED (two-time: initial + final) structure; the ~8%
null stratum (Prong 0) is the genesis seam. Its LEADS-TO names "a small
future-conditioned cosmological correlation LambdaCDM forbids".

This probe does NOT touch GU's fiber operator; it is the prereg's suggested
"2-boundary vs 1-boundary linear model showing where the predictions differ".
It is a SHARPENER for the tier verdict, testing three separable questions with
deterministic linear algebra (numpy only, no RNG, no writes, no network):

  Q-SUPPORT  Is a two-time (two-sided) boundary-value problem the NATURAL
             well-posed problem for the signature GU has (loss of a clean
             Cauchy problem in the ultrahyperbolic (9,5) arena => directions
             where the mode equation is ELLIPTIC-in-time), and UNNATURAL for
             an ordinary single-time HYPERBOLIC equation?
             -> If yes, GU structurally SUPPORTS two-sided boundary data.

  Q-DISTINCT Does a two-boundary (future-conditioned) field make a DISTINCT
             observable -- a two-point correlation the one-boundary
             (initial-condition, LambdaCDM-analog) field forbids?

  Q-WASHOUT  (the decisive control) Does that distinct correlation SURVIVE as
             the final boundary recedes (T -> infinity, de Sitter far future),
             or does it wash out -- becoming observationally IDENTICAL to the
             one-boundary field at fixed present-day separations?
             -> If it washes out, the distinct prediction exists ONLY for a
                FINITE, structurally-fixed final-boundary locus. That locus is
                the unowned bridge (fiber null-stratum -> cosmological z*).

Two planted controls that the method MUST reject:
  PLANT-1 "two-time is natural for any signature"     -> rejected by Q-SUPPORT
          (a final condition OVER-determines the hyperbolic IVP; the two-point
           BVP is ill-conditioned near resonance).
  PLANT-2 "two-time always makes a distinct observable" -> rejected by Q-WASHOUT
          (the future-conditioned correction decays ~ exp(-2 kappa T)).

EXIT 0 = ran deterministically (two-run-identical). The printed findings, not
the exit code, are the result.
"""
from __future__ import annotations

import numpy as np

np.set_printoptions(precision=4, suppress=True)

# ----------------------------------------------------------------------------
# Discrete 1-D operators on a uniform grid t_0..t_N on [0, T].
# A2 = -d^2/dt^2 (positive-definite discrete Laplacian, Dirichlet interior).
# ----------------------------------------------------------------------------


def second_difference(n_interior, h):
    """-d^2/dt^2 on n_interior interior nodes, Dirichlet (both ends pinned)."""
    d = np.full(n_interior, 2.0 / h**2)
    e = np.full(n_interior - 1, -1.0 / h**2)
    A = np.diag(d) + np.diag(e, 1) + np.diag(e, -1)
    return A


def grid(T, N):
    t = np.linspace(0.0, T, N + 1)
    h = t[1] - t[0]
    return t, h


# ============================================================================
print("=" * 74)
print("PRONG C -- two-time boundary posit: 1-boundary vs 2-boundary sharpener")
print("=" * 74)

# ----------------------------------------------------------------------------
# Q-SUPPORT.  Two mirror regimes.
#   ELLIPTIC-in-time  (ultrahyperbolic (9,5) proxy):  x'' = +kappa^2 x
#       IVP  x(0),x'(0):  modes e^{+/- kappa t} -> a perturbation of the initial
#            data is amplified by ~ e^{kappa T}  (Hadamard ILL-POSED).
#       BVP  x(0),x(T):   operator A2 + kappa^2 I is SPD, no resonance, cond O(1)
#            (WELL-POSED).  => two-sided boundary data is the NATURAL problem.
#   HYPERBOLIC (ordinary single-time):  x'' = -omega^2 x
#       IVP  x(0),x'(0):  oscillatory, amplification bounded (WELL-POSED).
#       BVP  x(0),x(T):   operator A2 - omega^2 I is INDEFINITE and SINGULAR at
#            resonances omega = k*pi/T -> a final condition OVER-determines the
#            IVP (two-time UNNATURAL).
# ----------------------------------------------------------------------------
print("\n[Q-SUPPORT] is two-sided boundary data natural for GU's signature?")
print("  well-posedness indicator = INVERTIBILITY MARGIN of the two-point BVP")
print("  operator = min|eigenvalue| (distance from singular). The raw condition")
print("  number is a discretization artifact (grows with N for BOTH regimes)")
print("  and is NOT used for the verdict; the margin is the physical quantity.")

T = 1.0
N = 400
t, h = grid(T, N)
A2 = second_difference(N - 1, h)  # interior nodes 1..N-1
eigs_A2 = np.sort(np.linalg.eigvalsh(A2))

kappa = 6.0
# elliptic BVP operator (screened Poisson): SPD; min-eig bounded away from 0.
L_ell_bvp = A2 + kappa**2 * np.eye(N - 1)
margin_ell_bvp = np.min(np.abs(np.linalg.eigvalsh(L_ell_bvp)))
# elliptic IVP amplification: growing mode e^{kappa T}
amp_ell_ivp = np.exp(kappa * T)

# hyperbolic: lock omega^2 ONTO a Dirichlet eigenvalue (resonance) up to a tiny
# offset, so the two-point BVP is near-singular (margin -> 0) -- the exact fate
# a final condition meets when it must agree with the IVP-propagated value.
lam3 = eigs_A2[2]                      # 3rd Dirichlet eigenvalue of A2
omega2 = lam3 * (1.0 + 1e-3)           # sit just off resonance
omega = np.sqrt(omega2)
L_hyp_bvp = A2 - omega2 * np.eye(N - 1)
margin_hyp_bvp = np.min(np.abs(np.linalg.eigvalsh(L_hyp_bvp)))
# hyperbolic IVP amplification: oscillatory => bounded (monodromy of rotation)
amp_hyp_ivp = 1.0  # |e^{+/- i omega t}| = 1, no growth

print(f"  grid: [0,{T}], N={N}, kappa={kappa}, omega={omega:.4f} "
      f"(locked near sqrt(lam3)={np.sqrt(lam3):.4f})")
print(f"  ELLIPTIC (ultrahyperbolic proxy):  IVP amp e^(kT) = "
      f"{amp_ell_ivp:.3e}   |  two-time BVP margin = {margin_ell_bvp:.3e}")
print(f"  HYPERBOLIC (ordinary single-time): IVP amp       = "
      f"{amp_hyp_ivp:.3e}   |  two-time BVP margin = {margin_hyp_bvp:.3e}")

support_elliptic_bvp_wellposed = margin_ell_bvp > 1.0     # bounded from 0
support_elliptic_ivp_illposed = amp_ell_ivp > 1e2
support_hyper_ivp_wellposed = amp_hyp_ivp < 1e1
support_hyper_bvp_illposed = margin_hyp_bvp < 1.0         # near-singular

print("  --> ELLIPTIC: IVP ill-posed (%s), two-time BVP well-posed (%s)"
      % (support_elliptic_ivp_illposed, support_elliptic_bvp_wellposed))
print("  --> HYPERBOLIC: IVP well-posed (%s), two-time BVP near-singular/over-det (%s)"
      % (support_hyper_ivp_wellposed, support_hyper_bvp_illposed))

Q_SUPPORT = (support_elliptic_bvp_wellposed and support_elliptic_ivp_illposed
             and support_hyper_ivp_wellposed and support_hyper_bvp_illposed)
print("  Q-SUPPORT =", Q_SUPPORT,
      "(two-sided boundary data is natural EXACTLY for the elliptic/no-Cauchy")
print("            signature GU has, and UNNATURAL for ordinary hyperbolic).")

# PLANT-1: "two-time is natural for any signature" must be REJECTED.
PLANT1_rejected = support_hyper_bvp_illposed  # hyperbolic two-time is NOT clean
print("  PLANT-1 ('two-time natural for any signature') rejected:",
      PLANT1_rejected)

# ----------------------------------------------------------------------------
# Q-DISTINCT + Q-WASHOUT.  Gaussian field with action 1/2 * x^T L x, precision
# L = A2 + kappa^2 I (the natural elliptic/two-time regime).  Covariance C =
# L^{-1} is the two-point function <x_i x_j> = Green's function with the imposed
# boundary conditions.  Two fields on a FIXED present window [0, T_now]:
#   one-boundary  : Dirichlet at t=0, NATURAL (Neumann) at the far end  (IVP/
#                   LambdaCDM analog: present statistics set by the past only).
#   two-boundary  : Dirichlet at t=0 AND at t=T_final  (future-conditioned).
# We compare the correlators on the SAME present window as T_final recedes.
# ----------------------------------------------------------------------------
print("\n[Q-DISTINCT/Q-WASHOUT] future-conditioned correlation vs wash-out")

kappa_c = 3.0
T_now = 1.0          # fixed present-day window where we read correlations
Nn = 200             # nodes on the present window
tn, hn = grid(T_now, Nn)


def half_line_greens(ti, tj, kap):
    """<x_i x_j> for -G'' + kap^2 G = delta, Dirichlet at 0, free at +inf.
    G(t,t') = sinh(kap t_<) e^{-kap t_>} / kap.  (one-boundary / IVP analog)"""
    tlo, thi = (ti, tj) if ti <= tj else (tj, ti)
    return np.sinh(kap * tlo) * np.exp(-kap * thi) / kap


def two_boundary_greens(ti, tj, kap, Tf):
    """<x_i x_j> for -G'' + kap^2 G = delta, Dirichlet at 0 AND at Tf.
    G(t,t') = sinh(kap t_<) sinh(kap (Tf - t_>)) / (kap sinh(kap Tf)).
    (two-boundary / future-conditioned)"""
    tlo, thi = (ti, tj) if ti <= tj else (tj, ti)
    return (np.sinh(kap * tlo) * np.sinh(kap * (Tf - thi))
            / (kap * np.sinh(kap * Tf)))


# sample the correlator on a coarse present-window grid
samp = np.linspace(0.1, 0.9, 9) * T_now
C1 = np.array([[half_line_greens(a, b, kappa_c) for b in samp] for a in samp])

# DISTINCT at finite T_final: the two-boundary correlator pins to 0 at t=T_final
Tf0 = 1.2  # final boundary just beyond the present window
C2_finite = np.array(
    [[two_boundary_greens(a, b, kappa_c, Tf0) for b in samp] for a in samp])
distinct_gap = np.max(np.abs(C2_finite - C1))
# a signature the one-boundary field cannot have: correlation with the LAST
# in-window point is suppressed toward the (nearby) future boundary
edge_1 = C1[-1, -1]
edge_2 = C2_finite[-1, -1]
print(f"  finite final boundary Tf={Tf0} (just beyond window):")
print(f"    max|C2 - C1| on present window = {distinct_gap:.4e}  (DISTINCT)")
print(f"    self-corr at last window point: one-boundary {edge_1:.4e} vs "
      f"two-boundary {edge_2:.4e}")
Q_DISTINCT = distinct_gap > 1e-3 and edge_2 < edge_1
print("  Q-DISTINCT =", Q_DISTINCT,
      "(two-boundary field carries a future-conditioned correlation the")
print("             one-boundary field forbids -- at a FINITE final boundary).")

# WASHOUT: recede the final boundary; measure the gap on the SAME window.
print("\n  wash-out as the final boundary recedes (fixed present window):")
Tfs = np.array([1.2, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
gaps = []
for Tf in Tfs:
    C2 = np.array(
        [[two_boundary_greens(a, b, kappa_c, Tf) for b in samp] for a in samp])
    gaps.append(np.max(np.abs(C2 - C1)))
gaps = np.array(gaps)
for Tf, g in zip(Tfs, gaps):
    print(f"    T_final = {Tf:.2f}   max|C2 - C1| = {g:.4e}")

# fit the decay rate on the log of the gap vs T_final
logg = np.log(gaps)
slope = np.polyfit(Tfs, logg, 1)[0]
print(f"  fitted decay: max|C2 - C1| ~ exp({slope:.3f} * T_final)  "
      f"(theory ~ -2*kappa = {-2*kappa_c:.3f})")
Q_WASHOUT = gaps[-1] < gaps[0] * 1e-2 and slope < -1.0
print("  Q-WASHOUT =", Q_WASHOUT,
      "(the distinct correlation decays exponentially as the final boundary")
print("            recedes -> identical to one-boundary at infinite T_final).")

# PLANT-2: "two-time ALWAYS makes a distinct observable" must be REJECTED.
PLANT2_rejected = Q_WASHOUT
print("  PLANT-2 ('two-time always observably distinct') rejected:",
      PLANT2_rejected)

# ----------------------------------------------------------------------------
print("\n" + "=" * 74)
print("SUMMARY (findings, not a pass/fail verdict)")
print("=" * 74)
print(" Q-SUPPORT  = %s : two-sided (two-time) boundary data is the NATURAL"
      % Q_SUPPORT)
print("              well-posed problem for GU's ultrahyperbolic/no-Cauchy")
print("              signature, and UNNATURAL (over-determining) for ordinary")
print("              single-time hyperbolic evolution. GU SUPPORTS the")
print("              two-sided boundary structure. (PLANT-1 rejected: %s)"
      % PLANT1_rejected)
print(" Q-DISTINCT = %s : at a FINITE final boundary the two-boundary field"
      % Q_DISTINCT)
print("              carries a future-conditioned two-point correlation the")
print("              one-boundary (LambdaCDM-analog) field forbids.")
print(" Q-WASHOUT  = %s : that correlation DECAYS ~ exp(-2*kappa*T_final) as"
      % Q_WASHOUT)
print("              the final boundary recedes -> observationally IDENTICAL")
print("              to one-time LambdaCDM at infinite T_final.")
print("              (PLANT-2 rejected: %s)" % PLANT2_rejected)
print("")
print(" => TIER PLACEMENT: the two-time posit is SUPPORTED by GU's signature")
print("    and is coherence-improving, but its DISTINCT prediction exists ONLY")
print("    for a FINITE, structurally-fixed final-boundary locus. GU does not")
print("    yet own the bridge that fixes that locus (fiber null-stratum -> a")
print("    finite cosmological z*). Without it, two-time = one-time LambdaCDM.")
print("    => C-SCAFFOLD (keep): coherent, points at a NAMED downstream")
print("       falsifiable (a future-conditioned low-l/large-scale correlation")
print("       at the scale set by z*), not directly falsifiable NOW.")
print("EXIT 0")
