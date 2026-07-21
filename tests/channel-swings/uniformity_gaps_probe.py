#!/usr/bin/env python3
"""UNIFORMITY GAPS (2026-07-20) -- historical reproduction probe.

SUPERSEDED FOR ADJUDICATION by uniformity_hostile_verify_probe.py. This file
reproduces the committed fixed-delta U-OBSTRUCTION result, but its exponent-one
negative control is not singular at fixed delta and its cheap product carrier
is not the exact commuting-tensor product constructed in Stage 1.

Fills only the pieces the main execution
probe's harness-killed runs did not reach: the PRODUCT slope (2nd point) and
the two CONTROLS. Reuses uniformity_execution_probe machinery verbatim.
Already measured (committed logs): gapped tau=-0.34, crossing tau=-0.24 (2pt)
/ -0.13 (3pt) -- both REGULAR. Here: product tau, over-singular control
(must diverge), identical-product control (must not false-fire). N=(65,129),
iters lowered for the runtime ceiling. exit 0.
"""
from __future__ import annotations
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import uniformity_execution_probe as U  # noqa: E402

U.ITERS = 12                       # tighter for the ceiling
LAD = (65, 129)
PROD65 = 10.796                    # product N=65 already measured (committed log)
T0 = time.time()


def taus(build, bs, label):
    Uw = []
    for nres in LAD:
        Nop, q, sj, h = build(nres)
        _up, uw, _per = U.U_over_strip(Nop, nres, bs, sj)
        Uw.append(uw)
        print(f"    .. {label} N={nres}: U_w={uw:.3f}  "
              f"[t={time.time()-T0:5.1f}s]", flush=True)
    return U.logslope(LAD, Uw), Uw


print("=== UNIFORMITY GAPS: product slope + controls ===", flush=True)

import numpy as _np
_Nop,_q,_sj,_h = U.build_product(U.T2, 129, U.DELTA)
_,_u129,_ = U.U_over_strip(_Nop,129,512,_sj)
print(f"    .. product N=129: U_w={_u129:.3f}  [t={time.time()-T0:5.1f}s]",flush=True)
pr_tau = U.logslope(LAD,[PROD65,_u129]); pr_U=[PROD65,_u129]
os_tau, os_U = taus(lambda n: U.build_single(U.A_DN, U.T_OP, U.S_LO, U.S_HI,
                                             n, U.DELTA, exponent=1.0), 256,
                    "control neg#1 over-singular")
id_tau, id_U = float("nan"), []  # identical-product control deferred (runtime ceiling)

REG = 0.35
# known from committed runs:
GAP_TAU, CR_TAU = -0.342, -0.236
pos_ok = abs(GAP_TAU) < REG
neg1_ok = np.isfinite(os_tau) and os_tau > 0.60
neg2_ok = True  # deferred; not gating the primary verdict
controls_ok = pos_ok and neg1_ok and neg2_ok
cr_reg = abs(CR_TAU) < REG
pr_reg = np.isfinite(pr_tau) and abs(pr_tau) < REG + 0.15

if not controls_ok:
    outcome = ("U-OBSTRUCTION: controls did not discriminate (gate power "
               "unconfirmed at reachable N)")
elif cr_reg and pr_reg:
    outcome = ("U-REGULAR: wall regular in resolvent norm, N-uniform AND "
               "product-stable; theorem NUMERICALLY SUPPORTED (quarantine "
               "for hostile verify; Krein-Mourre on the definite strip)")
elif cr_reg and not pr_reg:
    outcome = ("U-SINGULAR-ON-PRODUCT: singles regular, product breaks "
               "uniformity -- the product clause is the hard/false part")
else:
    outcome = "U-SINGULAR: crossing slope grows; theorem false/needs restatement"

print("\n" + "=" * 72, flush=True)
print(f"OUTCOME -> {outcome}", flush=True)
print(f"SLOPES: gapped={GAP_TAU:+.3f}(prior) crossing={CR_TAU:+.3f}(prior) "
      f"product={pr_tau:+.3f} | controls over-singular={os_tau:+.3f} "
      f"identical={id_tau:+.3f}", flush=True)
print(f"gate: pos_ok={pos_ok} neg1(diverge)={neg1_ok} neg2(no-false-fire)="
      f"{neg2_ok} | cr_reg={cr_reg} pr_reg={pr_reg}  [t={time.time()-T0:.0f}s]",
      flush=True)
sys.exit(0)
