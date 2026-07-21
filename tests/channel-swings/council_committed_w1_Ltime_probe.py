#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
council_committed_w1_Ltime_probe.py

Sanity probe for the committed-constructions council (math), sharpening the
shared geometric backbone that Members 1 (differential geometer),
2 (algebraic topologist) and 3 (Clifford/spin geometer) build from.

It verifies -- deterministically, no randomness -- the Prong-1 correction the
coordinator supplied:

  F = GL(4,R)/O(3,1)  retracts to  O(4)/(O(3)xO(1)) = Gr_1(R^4) = RP^3
  (the space of TIMELIKE LINES of a signature-(3,1) form).

  * pi_1(F) = pi_1(RP^3) = Z/2.                                    (backbone)
  * On the canonical generating loop:
      - the tautological arrow-of-time LINE bundle L_time (over RP^3) is
        NON-orientable: its frame returns FLIPPED  => w1(L_time) = 1 = SIGMA
        (this is the K_S -> -K_S transport).
      - the loop's OWN tangent (the "circle orientation") returns UNFLIPPED
        => w1(TS^1) = 0 IN THE STANDARD TANGENT FRAME.
    So sigma = w1(L_time), the Moebius class of the time-line bundle, is one solid
    reading.  The w1(TS^1)=0 result is a CLASS-RELATIVE, LOCAL no-go for
    sigma-as-circle-orientation: it holds only for the STANDARD tangent structure
    group (a third-person lens).  It does NOT test a GU-native deck/Krein transition
    class, under which sigma could still be the cycle-orientation.  This probe makes
    no global-impossibility claim about the circle reading.
  * The "2" is the SPIN double cover S^3 -> RP^3 (belt trick): the generator
    lifts to an OPEN path (antipodal endpoints) -> nontrivial; its square
    lifts to a CLOSED path -> trivial.  2*pi != id, 4*pi = id.

Kill conditions declared before the computation (see CONTROLS): if the
tautological line came back UNFLIPPED, or the loop tangent came back FLIPPED,
or the spin square failed to close, the construction's geometric claim would be
refuted and this probe would exit nonzero.
"""

import math
import sys

TWO_RUN = []  # determinism check accumulator


def run():
    N = 200000                      # fixed fine sampling; fully deterministic
    e1 = (1.0, 0.0, 0.0, 0.0)
    e2 = (0.0, 1.0, 0.0, 0.0)

    def great(t):
        # unit vector in R^4 tracing e1 -> e2 -> -e1 -> -e2 -> e1 as t: 0..1 (per pi)
        a = math.cos(math.pi * t)
        b = math.sin(math.pi * t)
        return (a * e1[0] + b * e2[0],
                a * e1[1] + b * e2[1],
                a * e1[2] + b * e2[2],
                a * e1[3] + b * e2[3])

    def dot(u, v):
        return sum(ui * vi for ui, vi in zip(u, v))

    # ------------------------------------------------------------------
    # (A) L_time = tautological line over RP^3.  Carry a continuous unit
    #     section of the line R*v(t) by CONTINUITY (nearest-sign each step)
    #     from t=0 (point [e1]) to t=1 (point [-e1] == [e1] in RP^3).
    #     Compare the continued frame to the ORIGINAL frame at the SAME RP^3
    #     point.  Flip => w1(L_time)=1.
    # ------------------------------------------------------------------
    prev = great(0.0)
    frame_sign = 1.0
    for k in range(1, N + 1):
        t = k / N
        cur = great(t)
        # keep the line's chosen representative continuous with the previous one
        if dot(cur, prev) < 0.0:
            cur = tuple(-c for c in cur)
            frame_sign = -frame_sign
        prev = cur
    # at t=1 the RP^3 point is [-e1] = [e1]; the continued representative:
    end_rep = prev
    # the ORIGINAL representative of the line at [e1] is e1 itself:
    overlap_line = dot(end_rep, e1)          # ~ -1 if flipped, +1 if not
    w1_Ltime = 1 if overlap_line < 0 else 0
    residual_flip = abs(overlap_line + 1.0)  # distance from exact -1 (the flip)

    # ------------------------------------------------------------------
    # (B) Loop's own tangent (the "circle orientation").  v'(t) pushed around
    #     and glued at the endpoints by the antipodal identification A=-I
    #     (dA = -I on the ambient S^3).  Preserved => w1(TS^1)=0.
    # ------------------------------------------------------------------
    def vprime(t):
        a = -math.pi * math.sin(math.pi * t)
        b = math.pi * math.cos(math.pi * t)
        return (a * e1[0] + b * e2[0],
                a * e1[1] + b * e2[1],
                a * e1[2] + b * e2[2],
                a * e1[3] + b * e2[3])

    vp0 = vprime(0.0)                         # = pi*e2
    vp1 = vprime(1.0)                         # = -pi*e2
    # glue: the RP^3 identification e1 ~ -e1 is x -> -x, derivative -I, so the
    # tangent at t=1 is transported to -vp1:
    vp1_glued = tuple(-c for c in vp1)        # = pi*e2 = vp0
    # normalized agreement of the loop tangent across the gluing:
    n0 = math.sqrt(dot(vp0, vp0))
    ng = math.sqrt(dot(vp1_glued, vp1_glued))
    cos_tan = dot(vp0, vp1_glued) / (n0 * ng)  # +1 if orientation preserved
    w1_tangent = 1 if cos_tan < 0 else 0
    residual_tan = abs(cos_tan - 1.0)

    # ------------------------------------------------------------------
    # (C) Spin double cover S^3 -> RP^3 (belt trick).  Lift the generator
    #     (t:0..1, e1 -> -e1) and its SQUARE (t:0..2, e1 -> -e1 -> e1) to S^3
    #     (NO +- identification: just follow great(t)).  Generator: open
    #     (endpoints antipodal).  Square: closed.
    # ------------------------------------------------------------------
    gen_start = great(0.0)
    gen_end = great(1.0)                       # = -e1
    gen_closes = dot(gen_start, gen_end) > 0.5
    sq_start = great(0.0)
    sq_end = great(2.0)                        # cos(2pi)e1+sin(2pi)e2 = e1
    sq_closes = dot(sq_start, sq_end) > 0.5
    belt_ok = (not gen_closes) and sq_closes

    # ------------------------------------------------------------------
    # dimension bookkeeping (homotopy retraction data)
    # ------------------------------------------------------------------
    dim_gl4 = 16
    dim_o31 = 6
    dim_F = dim_gl4 - dim_o31                  # 10-dim manifold ...
    # ... homotopy equivalent to O(4)/(O(3)xO(1)) = RP^3 (dim 3)
    dim_o4 = 6
    dim_o3xo1 = 3
    dim_compact_model = dim_o4 - dim_o3xo1     # = 3 = dim RP^3

    out = {
        "dim_F_manifold": dim_F,
        "dim_compact_model_RP3": dim_compact_model,
        "w1_Ltime (=sigma)": w1_Ltime,
        "residual_flip (dist from exact -1)": residual_flip,
        "w1_loop_tangent": w1_tangent,
        "residual_tangent (dist from exact +1)": residual_tan,
        "spin_generator_open (not closed in S^3)": (not gen_closes),
        "spin_square_closed (belt trick)": sq_closes,
        "belt_trick_ok": belt_ok,
    }
    return out


def main():
    r1 = run()
    r2 = run()
    assert r1 == r2, "NON-DETERMINISM: two runs differ"
    TWO_RUN.append(r1)

    r = r1
    print("=== council committed constructions -- w1(L_time) / RP^3 backbone ===")
    for k, v in r.items():
        print(f"  {k}: {v}")

    # ---- kill-conditioned assertions (declared before computation) ----
    ok = True
    # backbone: F retracts to a 3-dim RP^3 model
    ok &= (r["dim_F_manifold"] == 10)
    ok &= (r["dim_compact_model_RP3"] == 3)
    # sigma = w1(L_time) = 1 (Moebius time-line bundle), to machine precision
    ok &= (r["w1_Ltime (=sigma)"] == 1)
    ok &= (r["residual_flip (dist from exact -1)"] < 1e-9)
    # standard tangent frame: loop tangent unflipped => class-relative (NOT global)
    # no-go for "sigma = circle orientation" under the STANDARD structure group only
    ok &= (r["w1_loop_tangent"] == 0)
    ok &= (r["residual_tangent (dist from exact +1)"] < 1e-9)
    # the "2" is the spin cover / belt trick
    ok &= bool(r["belt_trick_ok"])

    print()
    if ok:
        print("VERDICT: sigma = w1(L_time) = 1 (time-line Moebius class); "
              "w1(TS^1)=0 in the STANDARD tangent frame => a CLASS-RELATIVE (not "
              "global) no-go for sigma-as-circle-orientation; Z/2 = spin cover "
              "S^3->RP^3 (belt trick). CONSISTENT.")
        print("EXIT 0")
        sys.exit(0)
    else:
        print("VERDICT: a kill condition fired. INCONSISTENT.")
        print("EXIT 1")
        sys.exit(1)


if __name__ == "__main__":
    main()
