#!/usr/bin/env python3
r"""
PRONG 1 -- GEOMETRY (shard-cycle swing). Is sigma the ORIENTATION CLASS of a
CANONICAL 1-cycle in the observerse?  Adversarial truth-test, MAXIMUM skepticism.

sigma is typed (source-packet GU-COFLIP-HOLONOMY-FREEZE-2026-07-20) as the
co-flip HOLONOMY over F = GL(4,R)/O(3,1), with pi_1(F) = Z/2 (F retracts onto
RP^3). The MODEL under test (prereg-oriented-shard-cycle-swing) asserts

    sigma = "the orientation of the shard circle"  (Z/2 = the two orientations
             of S^1, which would EXPLAIN why the bit is Z/2),

and that the cycle "closes through the q<0 / null-K_S stratum."

This probe DECIDES that, on the SAME canonical construction the habitat probe
uses (verbatim generator loop), by separating three distinct Z/2 data that the
model's slogan conflates:

  (i)  w1(T S^1)  -- the orientation class of the CYCLE ITSELF (the "two
       orientations of a circle").  A circle is ORIENTABLE, so this is 0.
  (ii) w1(L_time) -- the first Stiefel-Whitney class of the tautological
       TIMELIKE-LINE bundle over the loop (the arrow-of-time direction; the
       -1 eigenline of the metric-involution).  This is the Moebius class, != 0.
  (iii) the double cover realizing sigma's -1 monodromy: is it an ORIENTATION
       double cover (would be disconnected over orientable RP^3) or the SPIN
       cover S^3 -> RP^3 (connected)?

If sigma = (i) the model's slogan holds.  If sigma = (ii)/(iii) but NOT (i),
the slogan is FALSE and a corrected canonical object survives (G-PARTIAL).

PLANT CONTROL (mandatory): "any Z/2 bit is the orientation of SOME circle."
Rejected here iff w1(T S^1) = 0 while sigma != 0 -- i.e. the test separates the
cycle's own orientation (a trivial-class torsor) from a nontrivial line-bundle
w1.  A method that returned the same Z/2 for both would have no power.

NULL-STRATUM check: does the canonical holonomy loop pass through the q<0 /
null-K_S stratum?  Compute the minimum singular value of the transported K_S
along the loop (never 0 => the flip is by INVERTIBLE rotation, not degeneration)
and show the q<0 stratum sits at the NONCOMPACT flat-geodesic ends that the
retraction onto compact RP^3 removes (Prong 0 owns the ~8% end-crossing count).

Deterministic, foreground, numpy only, no writes, no network.  Exit 0 = all the
true-state assertions below hold.
"""
from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "generation-sector"))
import gen_sector_bridge as gb  # noqa: E402

N_DIRS, DIM = 14, 128
ETA = np.array([1.0] * 9 + [-1.0] * 5)
ETA4 = np.diag([1.0, 1.0, 1.0, -1.0])
RNG = np.random.default_rng(20260721)

RESULTS = []


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    return ok


# --- the actual W229 Krein form ----------------------------------------------
e = gb.gammas()
K_S = e[0].copy()
for a in range(1, 9):
    K_S = K_S @ e[a]                      # K_S = e_0 e_1 ... e_8


def rot(n, a, b, th):
    A = np.eye(n)
    A[a, a] = np.cos(th)
    A[b, b] = np.cos(th)
    A[a, b] = -np.sin(th)
    A[b, a] = np.sin(th)
    return A


def signature(g, tol=1e-9):
    w = np.linalg.eigvalsh(g)
    return int(np.sum(w > tol)), int(np.sum(w < -tol))


def kprod(frame_cols):
    """K_S rebuilt in the frame whose columns are frame_cols (the 9 +legs)."""
    out = np.eye(DIM, dtype=complex)
    for c in range(9):
        gen = sum(frame_cols[d, c] * e[d] for d in range(N_DIRS))
        out = out @ gen
    return out


# --- [T] setup ---------------------------------------------------------------
herm = float(np.max(np.abs(K_S - K_S.conj().T)))
invol = float(np.max(np.abs(K_S @ K_S - np.eye(DIM))))
check("T", "K_S Hermitian, K_S^2 = I (two Krein anchors); this is the object "
           "whose loop-transport IS sigma", herm < 1e-9 and invol < 1e-9,
      f"herm {herm:.1e} invol {invol:.1e}")
check("T", "F = GL(4,R)/O(3,1) retracts onto RP^3 = {I - 2P, P rank-1 "
           "timelike}; the base point eta4 = diag(1,1,1,-1) has one timelike "
           "leg", bool(signature(ETA4) == (3, 1)))


# =============================================================================
# Part A -- pi_1(F) = Z/2, CANONICAL (verbatim generator loop of the packet)
# =============================================================================
# generator loop of timelike lines: v(t) = (sin pi t, 0, 0, cos pi t)
ts = np.linspace(0.0, 1.0, 401)
lift, w_prev = [], None
for t in ts:
    w = np.array([np.sin(np.pi * t), 0.0, 0.0, np.cos(np.pi * t)])
    if w_prev is not None and float(w @ w_prev) < 0.0:
        w = -w
    lift.append(w)
    w_prev = w
mono1 = float(lift[-1] @ lift[0])
lift2, w_prev = [], None
for t in np.linspace(0.0, 2.0, 801):
    w = np.array([np.sin(np.pi * t), 0.0, 0.0, np.cos(np.pi * t)])
    if w_prev is not None and float(w @ w_prev) < 0.0:
        w = -w
    lift2.append(w)
    w_prev = w
mono2 = float(lift2[-1] @ lift2[0])
check("E", "pi_1(F) generator: continuous lift of the loop returns "
           "ANTI-periodic (monodromy -1); the SQUARED loop closes (+1) -- the "
           "class has order exactly 2, so pi_1(F) = Z/2 (RP^3)",
      mono1 < -0.999 and mono2 > 0.999, f"m1={mono1:+.3f} m2={mono2:+.3f}")


# =============================================================================
# Part B -- THE CRUX: separate the CYCLE's orientation from the LINE-bundle w1
# =============================================================================
# The loop realized as a loop of Lorentzian FORMS g(t) = B_t^T eta4 B_t,
# B_t = rot(0,3,pi t). g has period 1 (g(1) = eta4 = g(0)).
def g_of(t):
    B = rot(4, 0, 3, np.pi * t)
    return B.T @ ETA4 @ B


def taut_section(t):
    """The tautological TIMELIKE line: the -1 eigenvector of g(t)."""
    w, v = np.linalg.eigh(g_of(t))
    return v[:, 0]                         # unique negative eigenvector


# (i) w1(T S^1): the CYCLE's own orientation class.  Tangent to the loop in
#     form-space, dg/dt, is smooth and PERIODIC (g has period 1) => a globally
#     nonvanishing tangent frame that returns to ITSELF => the circle is
#     ORIENTABLE => w1(T S^1) = 0.
h = 1e-6
T0 = (g_of(0.0 + h) - g_of(0.0 - h)) / (2 * h)
T1 = (g_of(1.0 + h) - g_of(1.0 - h)) / (2 * h)
T0 /= np.linalg.norm(T0)
T1 /= np.linalg.norm(T1)
tang_return = float(np.sum(T0 * T1))      # Frobenius inner product
w1_TS1 = 0 if tang_return > 0.999 else 1
check("E", "w1(T S^1) = 0: the loop's own tangent frame is periodic (returns "
           "to ITSELF, not negated) -- the shard circle is ORIENTABLE, so its "
           "'two orientations' form a TRIVIAL-class Z/2 torsor",
      w1_TS1 == 0, f"<T(1),T(0)>_F = {tang_return:+.4f} -> w1(TS^1)={w1_TS1}")

# (ii) w1(L_time): the tautological TIMELIKE-line bundle.  Its continuous unit
#      section flips sign around the loop => Moebius => w1 != 0.  This IS the
#      arrow-of-time / record direction (the -1 eigenline), and its
#      non-orientability IS the co-flip.
sec, w_prev = [], None
for t in np.linspace(0.0, 1.0, 401):
    v = taut_section(t)
    if w_prev is not None and float(v @ w_prev) < 0.0:
        v = -v
    sec.append(v)
    w_prev = v
sec_return = float(sec[-1] @ sec[0])
w1_Ltime = 1 if sec_return < -0.999 else 0
check("E", "w1(L_time) = 1: the tautological timelike-line (arrow-of-time) "
           "bundle over the loop is the Moebius bundle -- its unit section "
           "FLIPS sign (co-flip). This is a NONtrivial Z/2 class",
      w1_Ltime == 1, f"<v(1),v(0)> = {sec_return:+.4f} -> w1(L_time)={w1_Ltime}")

# (iii) sigma itself = loop-transport of the ACTUAL K_S, at 14-dim grade:
#       the mixed (0,9) plane loop sends K_S -> -K_S (nontrivial).
F1 = np.linalg.inv(rot(N_DIRS, 0, 9, np.pi))
K_trans = kprod(F1)
sigma = 1 if float(np.max(np.abs(K_trans + K_S))) < 1e-9 else 0
check("E", "sigma = loop-transport of the actual K_S = -K_S (nontrivial Z/2 "
           "holonomy over F), matching w1(L_time)", sigma == 1,
      f"|K_trans + K_S| = {float(np.max(np.abs(K_trans + K_S))):.1e}")

# THE DISCRIMINATOR: sigma = w1(L_time) != w1(T S^1).  So sigma is the
# orientation class of the ARROW-OF-TIME LINE BUNDLE, NOT of the cycle.
check("E", "DISCRIMINATOR: sigma = w1(L_time) = 1  !=  0 = w1(T S^1). sigma is "
           "the orientation class of the TIME-DIRECTION LINE BUNDLE, NOT the "
           "orientation of the shard circle -- the model's slogan is FALSIFIED",
      sigma == w1_Ltime and sigma != w1_TS1,
      f"sigma={sigma} w1(L_time)={w1_Ltime} w1(TS^1)={w1_TS1}")


# =============================================================================
# Part C -- the double cover is the SPIN cover S^3 -> RP^3, not orientation
# =============================================================================
# The -1 monodromy corresponds to the double cover v ~ -v : S^3 -> RP^3.  That
# cover is CONNECTED (there is a path in S^3 from v(0) to -v(0) = the lift of
# the loop).  An ORIENTATION double cover of an ORIENTABLE manifold is
# DISCONNECTED (two copies).  RP^3 is orientable.  Hence sigma's cover is a
# SPIN-type (belt-trick) cover, not an orientation cover.
path_connected = float(np.linalg.norm(lift[-1] - (-lift[0]))) < 1e-6
check("E", "sigma's double cover is v ~ -v : S^3 -> RP^3, CONNECTED (the lift "
           "runs from v(0) to -v(0) inside the cover). An orientation double "
           "cover of the ORIENTABLE RP^3 would be DISCONNECTED -- so sigma's "
           "cover is the SPIN cover, not an orientation cover",
      path_connected, f"|v_lift(1) - (-v(0))| = "
      f"{float(np.linalg.norm(lift[-1] - (-lift[0]))):.1e}")

# corroborate orientability of the ambient: the frame monodromy of the ambient
# RP^3 tangent around the loop is orientation-PRESERVING (det = +1).  We use
# the congruence frame B_t^{-1}: det(B_t) is constant +1 (rotations), so the
# ambient orientation is carried around the loop unchanged.
dets = [float(np.linalg.det(rot(4, 0, 3, np.pi * t))) for t in ts]
check("E", "ambient orientation preserved around the loop: det(B_t) = +1 for "
           "all t (RP^3 orientable; w1(T RP^3) = 0) -- consistent with the "
           "orientation class being trivial while sigma is not",
      max(abs(d - 1.0) for d in dets) < 1e-9,
      f"max|det-1| = {max(abs(d - 1.0) for d in dets):.1e}")


# =============================================================================
# Part D -- NULL-STRATUM closure: does the canonical loop pass through null-K_S?
#   (Honest finding: the FIRST pass over-claimed "the loop avoids null." The
#    computation REFUTED that. Reported truthfully below.)
# =============================================================================
# D0: K_S and -K_S are ISOSPECTRAL. K_S = e_0..e_8 has signature (+64,-64), so
#     -K_S also has (+64,-64). A null-crossing is therefore NOT topologically
#     forced: an invertible (isospectral / conjugation) path connecting them
#     EXISTS. Whether a given loop crosses null is REALIZATION-dependent.
evK = np.linalg.eigvalsh(K_S)
sig_KS = (int(np.sum(evK > 0.5)), int(np.sum(evK < -0.5)))
check("E", "K_S is signature (+64,-64) => K_S and -K_S are ISOSPECTRAL; a "
           "null-crossing of the co-flip loop is NOT topologically forced (an "
           "invertible connecting path exists) -- so 'NECESSARILY through the "
           "null stratum' cannot hold from topology alone",
      sig_KS == (64, 64), f"sig(K_S) = {sig_KS}")

# D1: BUT the canonical CONGRUENCE realization (packet's loop) DOES transit the
#     null cone: the transported K_S(t) = kprod(A_t^{-1}) goes EXACTLY singular
#     at the light-cone crossings t = 1/4, 3/4, where the moving '+' leg
#     f_0(t) = cos(pi t) e_0 - sin(pi t) e_9 becomes eta-NULL
#     (Clifford square eta(f_0,f_0) = cos(2 pi t) = 0). This is the SAME q=0
#     light-cone wall Prong 0 names (spacelike<->timelike exchange).
smin = {}
for t in [0.0, 0.25, 0.5, 0.75, 1.0]:
    Kt = kprod(np.linalg.inv(rot(N_DIRS, 0, 9, np.pi * t)))
    smin[t] = float(np.linalg.svd(Kt, compute_uv=False)[-1])
crosses_null = smin[0.25] < 1e-9 and smin[0.75] < 1e-9
check("E", "the canonical CONGRUENCE realization DOES transit the null cone: "
           "transported K_S(t) is EXACTLY singular at t=1/4, 3/4 (a '+' leg "
           "goes eta-null crossing the light cone) -- the same q=0 wall as "
           "Prong 0. So the co-flip loop, as canonically realized, crosses "
           "null-K_S", crosses_null,
      f"sigma_min at 1/4={smin[0.25]:.1e}, 3/4={smin[0.75]:.1e}")

# D2: the crossing is MID-ARC, not at the JOIN. At t=0 (K_S) and t=1 (-K_S) and
#     t=1/2 the form is invertible; the nulls are at the quarter-turns. The
#     model says the cycle "closes THROUGH the null stratum" (null AT the join);
#     the join is NONdegenerate -- so the placement in the model is not matched.
join_ok = smin[0.0] > 0.9 and smin[1.0] > 0.9 and smin[0.5] > 0.9
check("E", "the null transit is MID-ARC (quarter-turns), NOT at the closure: "
           "K_S(t) is invertible at t=0 (K_S), t=1/2, t=1 (-K_S). The model's "
           "'closes THROUGH the null at the join' is not matched -- the join "
           "is nondegenerate", join_ok,
      f"sigma_min at 0={smin[0.0]:.2f} 1/2={smin[0.5]:.2f} 1={smin[1.0]:.2f}")

# D3: the METRIC signature stays (9,5) along the loop (Sylvester). Only the
#     transported KREIN matrix degenerates (a '+' leg goes null); the base
#     metric never does.
sig_const = all(signature(rot(N_DIRS, 0, 9, np.pi * t).T @ np.diag(ETA)
                @ rot(N_DIRS, 0, 9, np.pi * t)) == (9, 5)
                for t in np.linspace(0.0, 1.0, 21))
check("E", "the base metric signature (9,5) is CONSTANT along the loop "
           "(Sylvester); only the transported Krein matrix degenerates (a '+' "
           "leg goes null), not the metric", sig_const)

# D4: the q<0 stratum PROPER is at the NONCOMPACT flat-geodesic ends (Prong 0,
#     ~8% of genuine ends). Those ends are retracted away onto compact RP^3 and
#     are a DIFFERENT locus from the compact loop's mid-arc light-cone crossing.
H_end = np.diag([0.0, 0.0, 0.0, 1.0])
norms = [float(np.linalg.norm(np.diag(np.exp(s * np.diag(H_end))).T @ ETA4
         @ np.diag(np.exp(s * np.diag(H_end))))) for s in [0.0, 4.0]]
end_noncompact = norms[-1] > 50.0 * norms[0]
loop_bounded = max(np.linalg.norm(g_of(t)) for t in ts) < 3.0
check("E", "Prong 0's q<0 stratum is at the NONCOMPACT ends (||g_s|| blows "
           "up), retracted away; the loop stays BOUNDED. The loop's light-cone "
           "transit and the end-stratum are distinct loci -- the model's "
           "identification of the join with Prong 0's ends is not established",
      end_noncompact and loop_bounded,
      f"||g_s|| {norms[0]:.1f}->{norms[-1]:.0f}; loop<= "
      f"{max(np.linalg.norm(g_of(t)) for t in ts):.2f}")


# =============================================================================
# Part E -- PLANT CONTROL (mandatory)
# =============================================================================
# Plant: "any Z/2 bit is the orientation of SOME circle."  If true, sigma (a
# nontrivial Z/2) would BE the orientation class of the cycle, i.e. predict
# w1(T S^1) = sigma = 1.  Test: w1(T S^1) = 0 (computed above) while sigma = 1.
plant_prediction = 1                       # plant says the circle's orient. = sigma
plant_holds = (w1_TS1 == plant_prediction)
check("F", "PLANT REJECTED: 'any Z/2 is a circle's orientation' predicts "
           "w1(T S^1) = sigma = 1; the computed circle-orientation class is 0. "
           "A circle is orientable, so NO nontrivial Z/2 is its orientation "
           "class -- the plant conflates a trivial-class torsor with a "
           "nontrivial holonomy", not plant_holds,
      f"plant predicts w1(TS^1)=1, computed w1(TS^1)={w1_TS1}")

# Power check: the discriminator is NOT vacuous -- it returns DIFFERENT Z/2 for
# the two objects on the SAME loop (0 for the tangent, 1 for the taut bundle).
# A method with no power would return the same for both.
check("F", "POWER: the test distinguishes the cycle's orientation (w1=0) from "
           "a genuine line-bundle twist (w1=1) on the SAME loop -- so it CAN "
           "reject the plant; it is not the vacuous 'both are some Z/2' move",
      w1_TS1 != w1_Ltime, f"w1(TS^1)={w1_TS1} vs w1(L_time)={w1_Ltime}")


# --- headline ----------------------------------------------------------------
nE = sum(1 for tg, _n, ok in RESULTS if tg == "E")
nF = sum(1 for tg, _n, ok in RESULTS if tg == "F")
nT = sum(1 for tg, _n, ok in RESULTS if tg == "T")
all_ok = all(ok for _t, _n, ok in RESULTS)
print()
print(f"HEADLINE: {nE} [E] + {nF} [F] = {nE + nF}   (setup [T] = {nT} "
      f"excluded)   {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")
print("VERDICT INPUT: sigma = w1(L_time) [arrow-of-time line bundle] != "
      "w1(T S^1) = 0 [cycle orientation] => model's circle-orientation slogan "
      "FALSIFIED. Null stratum: congruence realization DOES cross null at the "
      "light-cone quarter-turns, but crossing is NOT forced (K_S,-K_S "
      "isospectral) and is mid-arc not at the join => 'necessarily closes "
      "through the null stratum' unestablished. => G-PARTIAL.")
sys.exit(0 if all_ok else 1)
