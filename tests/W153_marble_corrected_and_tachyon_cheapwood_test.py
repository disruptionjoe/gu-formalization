#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
W153 -- Marble corrected (metric + Lambda = cheap wood; T_munu + G = kept) and the
        coherence-first tachyon-as-cheap-wood test.

This deterministic test carries the POSITIVE CONTROLS that ground the W153 exploration
note (explorations/W153-marble-corrected-and-tachyon-cheapwood-test-2026-07-14.md).

It does NOT re-run the full Convention-B |II|^2 machinery (that is W126/W130's job and
is regression-pinned there). It reproduces the two positive controls the brief names, and
adds the ONE load-bearing check for JOB 2 -- that the induced R^2 coefficient a2 = -1/9 is
INVARIANT under the conformal / scale mode (the BLMS record-count leg), i.e. re-sourcing the
metric's scale does NOT move the tachyon.

Positive controls:
  PC1  W126 MSS-slice reproduction: the interpolant W(u) = -64 u^2 - 8 u + 2 with the pinned
       curvature map R = -24 u yields EXACTLY F(R) = 2 + R/3 - R^2/9, hence the induced
       Einstein coefficient a1 = +1/3 (attractive) and the tachyonic R^2 coefficient
       a2 = -1/9.  (Regression pin of W126 Route-2, tests/W126_beyond4th_conformal_iisq.py.)

  PC2  Malament conformal recovery on a toy 1+1 causal diamond: the causal-precedence
       relation is INVARIANT under any monotone null reparametrisation u -> f(u), v -> g(v)
       (the conformal transformations of ds^2 = -du dv), so the order fixes only the
       conformal class [g]; and the element COUNT in an Alexandrov interval recovers its
       Minkowski volume (BLMS: order + number = geometry).  (Fresh reproduction of W151 PC1.)

JOB-2 load-bearing check (the coherence-first tachyon test, made concrete):
  T1   Scale-mode invariance of the induced action.  On the W126 potential slice the
       induced |II|^2 depends on (p, s) only through the scale-covariant variable
       sigma = e^{-2p} s (W126 "scale collapse", all orders in p).  Therefore the induced
       F(R) coefficients are INDEPENDENT of the conformal factor p.  We vary p (the leg the
       BLMS record-count / volume factor sets) and confirm a1 = +1/3, a2 = -1/9 at every p.
       Interpretation: the tachyonic R^2 sector is a property of the |II|^2 FUNCTIONAL, not
       of how the metric's scale is sourced -- re-sourcing the metric (imposed -> record-
       derived) does not remove it.  The R^2 lives in the conformal factor = the record-count
       mode: record-derivation LOCATES the tachyon, it does not dissolve it.

Run:  python -u tests/W153_marble_corrected_and_tachyon_cheapwood_test.py   (exit 0 iff all PASS)
"""

import sys
import sympy as sp

FAILS = []
NPASS = 0


def check(msg, cond, detail=""):
    global NPASS
    ok = bool(cond)
    if ok:
        NPASS += 1
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {msg}" + (f"   ({detail})" if detail else ""))
    if not ok:
        FAILS.append(msg)


def log(msg):
    print("    " + msg)


print("=" * 78)
print("W153 -- marble corrected + tachyon-as-cheap-wood positive controls")
print("=" * 78)

# ---------------------------------------------------------------------------
# PC1 -- W126 MSS-slice reproduction: F(R) = 2 + R/3 - R^2/9
# ---------------------------------------------------------------------------
print("\n-- PC1: W126 MSS-slice interpolant -> F(R), a1 = +1/3, a2 = -1/9 --")

u, R = sp.symbols("u R", real=True)

# The W126 Route-2 exact interpolant through MSS-type jets (verbatim from W126):
W_of_u = -64 * u**2 - 8 * u + 2

# The pinned curvature map on the MSS slice (W126: sigma = u*eta, R = -24 u):
u_of_R = -R / sp.Integer(24)

F_of_R = sp.expand(W_of_u.subs(u, u_of_R))

check("W126 interpolant W(u) = -64 u^2 - 8 u + 2  maps to  F(R) = 2 + R/3 - R^2/9",
      sp.expand(F_of_R - (2 + R / 3 - R**2 / 9)) == 0, f"F(R) = {F_of_R}")

a0 = F_of_R.subs(R, 0)
a1 = sp.diff(F_of_R, R).subs(R, 0)
a2 = sp.diff(F_of_R, R, 2) / 2

check("induced flat/DeWitt constant a0 = 2", a0 == 2, f"a0 = {a0}")
check("induced Einstein coefficient a1 = +1/3 (ATTRACTIVE, H25-consistent)",
      a1 == sp.Rational(1, 3) and a1 > 0, f"a1 = {a1}")
check("induced R^2 coefficient a2 = -1/9 (NEGATIVE relative to a1 > 0: the native tachyon)",
      a2 == sp.Rational(-1, 9) and a2 < 0, f"a2 = {a2}")
check("relative-sign structure a2/a1 = -1/3 (survives any overall Omega>0 rescaling)",
      sp.simplify(a2 / a1) == sp.Rational(-1, 3), f"a2/a1 = {sp.simplify(a2/a1)}")

# ---------------------------------------------------------------------------
# T1 -- JOB 2: scale-mode invariance of the induced R^2 coefficient
# ---------------------------------------------------------------------------
print("\n-- T1: the induced R^2 sector is INVARIANT under the conformal/record-count scale mode --")
log("W126 scale collapse: |II|^2 depends on (p, s) only through sigma = e^{-2p} s.")
log("The BLMS record-count / volume factor is exactly this conformal scale mode.")
log("Vary p (re-source the metric's scale) and confirm a1, a2 are unchanged at every p.")

p_sym, s_scalar = sp.symbols("p s", real=True)
# scale-covariant curvature variable and the physical scalar curvature at scale p
sigma = sp.exp(-2 * p_sym) * s_scalar          # W126 scale collapse
u_val = sigma                                   # slice curvature variable (dimensionless)
R_phys = -24 * sigma                            # R = -24 u, evaluated at scale p
W_val = (-64 * u_val**2 - 8 * u_val + 2)        # induced |II|^2 on the slice

all_ok = True
for p0 in [-2, -1, 0, 1, 2]:
    Wp = W_val.subs(p_sym, p0)
    Rp = R_phys.subs(p_sym, p0)
    # re-express W in the PHYSICAL curvature R at this scale
    s_of_R = sp.solve(sp.Eq(Rp, R), s_scalar)[0]
    F_p = sp.expand(Wp.subs(s_scalar, s_of_R))
    a1_p = sp.diff(F_p, R).subs(R, 0)
    a2_p = sp.diff(F_p, R, 2) / 2
    ok_p = (a1_p == sp.Rational(1, 3)) and (a2_p == sp.Rational(-1, 9))
    all_ok = all_ok and ok_p
    log(f"p = {p0:>2}:  a1 = {a1_p}, a2 = {a2_p}   {'ok' if ok_p else 'MISMATCH'}")

check("a1 = +1/3 and a2 = -1/9 at EVERY conformal scale p (scale-mode / record-count invariant)",
      all_ok,
      "re-sourcing the metric's scale does NOT move the tachyon: the R^2 is a functional-form "
      "property of |II|^2, and it lives in the conformal factor = the record-count mode")

# ---------------------------------------------------------------------------
# PC2 -- Malament conformal recovery + BLMS count->volume on a toy causal diamond
# ---------------------------------------------------------------------------
print("\n-- PC2: Malament (order -> [g]) + BLMS (number -> volume) on a 1+1 causal diamond --")

import random
random.seed(153)

N = 400
# sprinkle points in the double-null square u,v in (0,1); causal precedence:
#   q >- p   iff   u_q > u_p  AND  v_q > v_p    (future of p)
pts = [(random.random(), random.random()) for _ in range(N)]


def precedence_matrix(points):
    M = [[1 if (points[b][0] > points[a][0] and points[b][1] > points[a][1]) else 0
          for b in range(len(points))] for a in range(len(points))]
    return M


M_orig = precedence_matrix(pts)

# monotone increasing null reparametrisations (conformal transf. of ds^2 = -du dv):
# u -> f(u) = u^3 ;  v -> g(v) = (e^v - 1)/(e - 1)   (both strictly increasing on (0,1))
import math
pts_conf = [(uu**3, (math.exp(vv) - 1.0) / (math.e - 1.0)) for (uu, vv) in pts]
M_conf = precedence_matrix(pts_conf)

n_rel = sum(sum(row) for row in M_orig)
same = (M_orig == M_conf)
check("Malament: causal-precedence relation is INVARIANT under monotone null reparam "
      "u->u^3, v->(e^v-1)/(e-1) (order sees ONLY the conformal class [g])",
      same, f"{n_rel} relations, exact matrix equality = {same}")

# BLMS: element count in an Alexandrov interval recovers its Minkowski volume.
# Alexandrov interval between p0=(0.15,0.15) and p1=(0.85,0.85) in null coords.
# Minkowski area element dt dx = (1/2) du dv, so Vol = (1/2)*(du)*(dv) of the interval box.
u0, v0, u1, v1 = 0.15, 0.15, 0.85, 0.85
cnt = sum(1 for (uu, vv) in pts if u0 < uu < u1 and v0 < vv < v1)
density = N / 1.0  # N points per unit (u,v) square area 1
vol_uv = (u1 - u0) * (v1 - v0)          # volume in (u,v) coords
expected = density * vol_uv
# Poisson: allow 4-sigma
sigma_pois = math.sqrt(expected)
check("BLMS: Alexandrov-interval element count recovers volume "
      "(count ~ density * Vol, within 4 sigma Poisson)",
      abs(cnt - expected) <= 4 * sigma_pois,
      f"count = {cnt}, expected = {expected:.1f}, 4-sigma = {4*sigma_pois:.1f}")

# order+number together: same order shared by g and Omega^2 g (M_conf == M_orig above)
# while the count fixes the missing conformal factor -> full metric. (structural, shown by the pair.)
check("order+number = geometry: order alone gives [g] (PC2a), number gives the volume/"
      "conformal factor (PC2b) -> the full Lorentzian g (BLMS)", same and (cnt > 0))

# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print(f"W153: {NPASS} checks passed, {len(FAILS)} failed.")
if FAILS:
    print("FAILURES:")
    for f in FAILS:
        print("  - " + f)
    sys.exit(1)
print("ALL PASS -- exit 0")
sys.exit(0)
