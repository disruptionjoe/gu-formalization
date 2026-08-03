#!/usr/bin/env python3
"""PRONG-1 SCOPE CHECKS (2026-07-20) -- small VALIDATING checks for the
uniformity-numerics METHOD scope (explorations/prong1-uniformity-method-
scope-2026-07-20.md). NOT a result probe: these are minutes-bounded checks
that substantiate three method decisions, reusing the operator_grade_end
geometry verbatim (imported, not re-derived).

  C1  the factor-4 gate confound: min_j|q(s_j)| on the fixed collar grid
      WOBBLES non-monotonically with N (grid-wall alignment) -- the
      mechanism behind the resolvent last-pair wobble 0.0066/0.0357/0.0099
      that failed the factor-4 gate at 5.4. A gate thresholding that ratio
      measures grid alignment, not divergence.
  C2  the wall-aligned-grid remedy: centering the collar window on s* and
      laddering by ODD N keeps the wall on the central node, so min_j|q_j|
      -> 0 MONOTONICALLY (controlled ~ h = O(1/N)); the confound is removed
      and a growth-rate gate on the LIMIT object becomes meaningful.
  C3  carrier-combination relocates/creates walls: a gapped block (q_A>0)
      plus a crossing block (q_B sign-changing) gives a combined scalar
      q_A+q_B whose zero sits where NEITHER factor vanishes -- an emergent
      product wall, so the 2-block product toy MUST use distinct-wall blocks
      (identical blocks only double multiplicity: the referee's artifact).
Deterministic; reuses operator_grade_end_probe geometry; no RNG.
"""
from __future__ import annotations
import importlib.util
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "generation-sector"))
_spec = importlib.util.spec_from_file_location(
    "ope", os.path.join(HERE, "operator_grade_end_probe.py"))
ope = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ope)  # runs the [T] geometry stage (~7s)

xi_of, qform, ray = ope.xi_of, ope.qform, ope.ray
A_DN, A_UP = ope.A_CONF_DN, ope.A_CONF_UP
T_OP, S_STAR, S_LO, S_HI = ope.T_OP, ope.S_STAR_OP, ope.S_LO, ope.S_HI

print(f"\n[geometry] t_op={T_OP:.4f} s*={S_STAR:.4f} window=[{S_LO:.3f},"
      f"{S_HI:.3f}] dq/ds|wall={ope.QPRIME:.2f}")


def qc(s, alpha=A_DN, t=None):
    return qform(xi_of(T_OP if t is None else t, ray(alpha, float(s))))


# -- C1: the fixed-grid confound. min|q| ~ dist(nearest node, s*) * |dq/ds|,
# and dist is the SAWTOOTH frac((s*-s_lo)/h) in N -- NOT monotone. A gate on
# a ratio of these values reads grid alignment, not divergence. (Power-of-2 N
# can accidentally sample a monotone subsequence; scan N densely to expose it.)
print("\n=== C1  factor-4 gate confound: fixed-grid min|q| sawtooth ===")
c1_rows = []
for N in range(120, 141):
    h = (S_HI - S_LO) / (N + 1)
    sj = S_LO + h * np.arange(1, N + 1)
    qs = np.array([qc(s) for s in sj])
    j = int(np.argmin(np.abs(qs)))
    c1_rows.append((N, float(np.min(np.abs(qs))), float(abs(sj[j] - S_STAR))))
minq = [r[1] for r in c1_rows]
signflips = sum(1 for i in range(1, len(minq) - 1)
                if (minq[i] - minq[i - 1]) * (minq[i + 1] - minq[i]) < 0)
lo_i = int(np.argmin(minq))
hi_i = int(np.argmax(minq))
print(f"  N in [120,140]: min|q| ranges {min(minq):.4f} (N={c1_rows[lo_i][0]})"
      f" .. {max(minq):.4f} (N={c1_rows[hi_i][0]}); adjacent-N wobble ratio "
      f"up to {max(minq)/max(1e-9,min(minq)):.1f}x")
print(f"  -> {signflips} direction reversals across 21 consecutive N: min|q| "
      f"is a SAWTOOTH in N (grid-wall alignment). The resolvent last-pair "
      f"difference ~1/min|q| inherits it; the factor-4 gate on that ratio "
      f"(failed 5.4) measures alignment, not a divergence trend.")
# hard checks: C1's claim is a non-monotone sawtooth whose alignment wobble
# alone exceeds the factor-4 gate.
assert signflips > 0, "C1: fixed-grid min|q| shows no direction reversal in N"
assert max(minq) > 4.0 * max(1e-9, min(minq)), (
    f"C1: wobble ratio {max(minq)/max(1e-9, min(minq)):.2f}x does not exceed "
    f"the factor-4 gate; the confound claim is unsupported")

# -- C2: wall-aligned ladder -- center window on s*, odd N -> node on wall
print("\n=== C2  wall-aligned remedy: s* on central node, ladder odd N ===")
L = min(S_STAR - S_LO, S_HI - S_STAR)          # symmetric half-window
c2_rows = []
for N in (65, 129, 257, 513):                  # odd => unique central node
    h = 2 * L / (N + 1)
    sj = (S_STAR - L) + h * np.arange(1, N + 1)
    qs = np.array([qc(s) for s in sj])
    jc = int(np.argmin(np.abs(sj - S_STAR)))    # central node index
    c2_rows.append((N, float(np.min(np.abs(qs))), float(abs(sj[jc] - S_STAR)),
                    h))
    print(f"  N={N:4d}: min|q|={c2_rows[-1][1]:.5f}  dist(central node,s*)="
          f"{c2_rows[-1][2]:.2e}  h={h:.5f}")
mq2 = [r[1] for r in c2_rows]
mono = all(mq2[i] <= mq2[i - 1] + 1e-9 for i in range(1, len(mq2)))
print(f"  -> min|q| monotone-decreasing (controlled ~h): {mono}; the grid-"
      f"alignment degree of freedom is removed, so a log-log growth-rate "
      f"gate on the LIMIT resolvent norm is now well posed.")
# hard checks: the remedy must actually pin the wall to the central node and
# drive min|q| to ~0 monotonically.
assert all(r[2] < 1e-9 for r in c2_rows), "C2: central node is not on the wall s*"
assert all(r[1] < 1e-3 for r in c2_rows), (
    f"C2: wall-aligned min|q| not driven to ~0: {mq2}")
assert mono, f"C2: min|q| not monotone-decreasing on the odd-N ladder: {mq2}"

# -- C3: carrier-combination relocates/creates walls. NAMED FINDING FIRST:
# a strongly-gapped block MASKS a weak crossing (q_A+q_B stays >0), so the
# 2-block toy must use COMPARABLE CROSSING blocks, not gapped+crossing.
print("\n=== C3  2-block product: emergent wall needs distinct crossing blocks"
      " ===")
ss = np.linspace(S_LO, S_HI, 600)


def zero_cross(x, y):
    idx = np.where(np.sign(y[:-1]) != np.sign(y[1:]))[0]
    return [float(x[i] - y[i] * (x[i + 1] - x[i]) / (y[i + 1] - y[i]))
            for i in idx]


qA = np.array([qc(s, alpha=A_UP) for s in ss])          # gapped
qBw = np.array([qc(s, alpha=A_DN) for s in ss])          # weak crossing
masked_walls = zero_cross(ss, qA + qBw)
print(f"  masking check: gapped q_A in [{qA.min():.1f},{qA.max():.1f}] + weak "
      f"crossing q_B (min {qBw.min():.2f}) -> sum walls "
      f"{['%.4f' % z for z in masked_walls] or 'NONE (masked)'}")
# hard check: the NAMED FINDING is that the gapped block MASKS the weak
# crossing (the sum has NO wall).
assert not masked_walls, (
    f"C3: gapped+weak-crossing sum has walls at {masked_walls}; masking claim fails")

# two COMPARABLE crossing blocks at different loop coords -> distinct walls
def wall_at_t(t):
    sv = np.linspace(0.05, 1.3, 80)
    qv = [qc(s, t=t) for s in sv]
    if qv[0] <= 0 or min(qv) > 0:
        return None
    j = next(i for i in range(1, len(qv)) if qv[i] < 0)
    lo, hi = sv[j - 1], sv[j]
    for _ in range(50):
        m = 0.5 * (lo + hi)
        lo, hi = (m, hi) if qc(m, t=t) > 0 else (lo, m)
    return 0.5 * (lo + hi)


t2 = None
for tt in np.linspace(T_OP - 0.25, T_OP + 0.25, 60):
    w = wall_at_t(float(tt))
    if w is not None and abs(w - S_STAR) > 0.12 and 0.2 < w < 1.1:
        t2 = float(tt)
        break
if t2 is not None:
    w2 = wall_at_t(t2)
    ss2 = np.linspace(0.15, min(S_STAR, w2) + 0.6, 600)
    qC1 = np.array([qc(s) for s in ss2])                # wall at S_STAR
    qC2 = np.array([qc(s, t=t2) for s in ss2])          # wall at w2
    zsum = zero_cross(ss2, qC1 + qC2)
    print(f"  block A wall s={S_STAR:.4f} (t={T_OP:.3f});  block B wall "
          f"s={w2:.4f} (t={t2:.3f})")
    print(f"  combined q_A+q_B walls at s = {['%.4f' % z for z in zsum]}  "
          f"-> product carrier has its OWN (relocated/multiplied) wall set, "
          f"absent from either factor at that location. 2-block toy = TWO "
          f"COMPARABLE CROSSING blocks with DISTINCT walls.")
    # hard checks: an emergent wall must exist, and it must sit where NEITHER
    # factor vanishes (else it is not relocated, just an inherited wall).
    assert len(zsum) >= 1, "C3: combined q_A+q_B has no wall"
    for z in zsum:
        qa_z, qb_z = qc(z), qc(z, t=t2)
        assert min(abs(qa_z), abs(qb_z)) > 1e-3, (
            f"C3: combined wall s={z:.4f} coincides with a factor wall "
            f"(q_A={qa_z:.2e}, q_B={qb_z:.2e}); not an emergent wall")
else:
    print("  (no second distinct-wall crossing t found in scan; execution "
          "should widen the t-scan)")
    raise SystemExit(1)  # C3's emergent-wall demonstration was NOT produced

print("\n[prong1 scope checks complete]")
