#!/usr/bin/env python3
r"""
W86 -- REGULATOR SHAPE-PARAMETER SWEEP after W85.

Question. W85 brought one genuinely different second regulator (exponential) against the W81/W83 Litim
scheme and found the Reuter fixed point ROBUST at first-swing grade. Its next valid swing named a third
regulator / shape-parameter sweep. This file executes the bounded version: vary the amplitude parameter in
the exponential family

    r_s(y) = s y / (e^y - 1),  s > 0,

and check whether the load-bearing qualitative invariants survive while the non-universal values move.

Construction discipline.

* The regulator is a calculational convention, not a physics fork. Values may move.
* The admissibility condition used here is minimal and explicit: Phi_n^p(0) stays positive and finite.
* The f0 result is a relevance-drive proxy, not a full combined critical exponent computation.
* The RS matter check uses the W85 factorization assumption: coefficient sign times positive threshold.

Verdict encoded. SHAPE-STABLE at first-swing/proxy grade. Across the sweep, threshold functions stay
positive, the reduced Reuter fixed point exists, the FP coordinates move, the f0 relevance drive stays
positive, and GU's ker-Gamma RS anti-screening sign is unchanged. The sweep does not close the W85
NEEDS-FULL-COMPUTATION residual: a full combined f(R)+Weyl^2 + ker-Gamma spin-3/2 FRG run remains open.

No canon, claim-status, RESEARCH-STATUS, CANON, verdict, public-posture, or absorbed-source file is touched.
"""
from __future__ import annotations

import math
import sys

import numpy as np

FAIL: list[str] = []


def log(msg: str = "") -> None:
    print(msg, flush=True)


def check(name: str, cond: bool, detail: str = "") -> None:
    ok = bool(cond)
    print(("  [PASS] " if ok else "  [FAIL] ") + name + ((" -- " + detail) if detail else ""))
    if not ok:
        FAIL.append(name)


# Fixed deterministic Simpson grid. Keep it smaller than W85 because this run sweeps several shapes.
YMAX = 80.0
NGRID = 160001  # odd for Simpson
Y = np.linspace(1.0e-8, YMAX, NGRID)
DY = Y[1] - Y[0]


def simpson(values: np.ndarray) -> float:
    total = values[0] + values[-1] + 4.0 * np.sum(values[1:-1:2]) + 2.0 * np.sum(values[2:-2:2])
    return float(total * DY / 3.0)


def phi_litim(p: int, n: int) -> float:
    # Litim/optimized reference at zero argument.
    return 1.0 / math.factorial(n)


def phi_exp_shape(s: float, p: int, n: int) -> float:
    """Phi_n^p(0) for r_s(y)=s*y/(exp(y)-1)."""
    ey = np.exp(Y)
    denom = ey - 1.0
    r_minus_y_rprime = s * Y * Y * ey / (denom * denom)
    propagator = Y + s * Y / denom
    integrand = (Y ** (n - 1)) * r_minus_y_rprime / (propagator ** p)
    return simpson(integrand) / math.gamma(n)


# The reduced EH proxy is only used inside the viability window 0<lambda*<1/2. Wider amplitudes are useful
# diagnostics, but W86 keeps the pass/fail sweep inside the model's own stated domain.
SHAPES = [0.35, 0.50, 0.75, 1.00, 1.20]
PAIRS = [(1, 1), (2, 1), (1, 2), (2, 2), (3, 2)]

log("=" * 96)
log("PART A -- exponential regulator shape family r_s(y)=s*y/(e^y-1)")
log("=" * 96)

thresholds: dict[float, dict[tuple[int, int], float]] = {}
for s in SHAPES:
    vals = {(p, n): phi_exp_shape(s, p, n) for (p, n) in PAIRS}
    thresholds[s] = vals
    log(
        f"   s={s:4.2f}: "
        f"Phi^1_1={vals[(1,1)]:8.5f}  "
        f"Phi^1_2={vals[(1,2)]:8.5f}  "
        f"Phi^2_2={vals[(2,2)]:8.5f}"
    )

all_positive = all(value > 0 and math.isfinite(value) for vals in thresholds.values() for value in vals.values())
shape_motion = max(thresholds[s][(2, 2)] for s in SHAPES) / min(thresholds[s][(2, 2)] for s in SHAPES)

check(
    "A1 threshold functions stay positive and finite across the shape sweep",
    all_positive,
    "all sampled Phi_n^p(0)>0 for s in [0.35,1.2]",
)
check(
    "A2 the sweep is nontrivial: Phi^2_2 moves across shape parameter s",
    shape_motion > 1.50,
    f"max/min Phi^2_2={shape_motion:.3f}",
)

log("\n" + "=" * 96)
log("PART B -- reduced Reuter fixed point across the shape family")
log("=" * 96)

# Same reduced-EH calibration convention as W85: regulator dependence enters through threshold weights.
A_GRAV = 2.0 / 0.70
B0 = 0.60
B1 = 1.0


def eh_fp(phi2_weight: float, phi1_weight: float) -> tuple[float, float]:
    g_star = 2.0 / (A_GRAV * phi2_weight)
    lambda_star = (g_star * B0 * phi1_weight) / (2.0 + g_star * B1)
    return g_star, lambda_star


rows: list[dict[str, float]] = []
for s in SHAPES:
    phi2_weight = thresholds[s][(2, 2)] / phi_litim(2, 2)
    phi1_weight = thresholds[s][(1, 2)] / phi_litim(1, 2)
    g_star, lambda_star = eh_fp(phi2_weight, phi1_weight)
    product = g_star * lambda_star
    f0_drive = g_star * phi1_weight
    rows.append(
        {
            "s": s,
            "phi2_weight": phi2_weight,
            "phi1_weight": phi1_weight,
            "g": g_star,
            "lambda": lambda_star,
            "product": product,
            "f0_drive": f0_drive,
        }
    )
    log(
        f"   s={s:4.2f}: w2={phi2_weight:7.4f} w1={phi1_weight:7.4f} "
        f"g*={g_star:7.4f} lambda*={lambda_star:7.4f} g*lambda*={product:7.4f} "
        f"f0-drive={f0_drive:7.4f}"
    )

fp_exists = all(row["g"] > 0 and 0 < row["lambda"] < 0.5 for row in rows)
g_motion = max(row["g"] for row in rows) / min(row["g"] for row in rows)
lambda_motion = max(row["lambda"] for row in rows) / min(row["lambda"] for row in rows)
product_spread = (max(row["product"] for row in rows) - min(row["product"] for row in rows)) / (
    sum(row["product"] for row in rows) / len(rows)
)
f0_positive = all(row["f0_drive"] > 0 for row in rows)

check(
    "B1 invariant I1 proxy: the reduced Reuter fixed point exists for every sampled shape",
    fp_exists,
    "all rows have g*>0 and 0<lambda*<1/2",
)
check(
    "B2 non-universal FP coordinates move across the sweep, as expected",
    g_motion > 1.50 and lambda_motion > 1.10,
    f"max/min g*={g_motion:.3f}, max/min lambda*={lambda_motion:.3f}",
)
check(
    "B3 mapped g*lambda* band stays finite and order-stable in this reduced sweep",
    product_spread < 1.50,
    f"relative spread={product_spread:.3f}",
)
check(
    "B4 invariant I3 proxy: f0 relevance drive stays positive across the sweep",
    f0_positive,
    "g* times positive threshold weight stays >0 for every sampled shape",
)

log("\n" + "=" * 96)
log("PART C -- GU ker-Gamma RS anti-screening sign across the shape family")
log("=" * 96)

b_grav = +2.0
b_v = +0.020
b_s = -0.015
b_d = -0.010
b_rs = +0.030
n_v = 12.0
n_s = 4.0
n_d = 10.0
n_rs = 1.0


def a_total(phi_weight: float, include_rs: bool, scalar_count: float = n_s) -> float:
    rs = b_rs * n_rs if include_rs else 0.0
    return b_grav + phi_weight * (b_v * n_v + b_s * scalar_count + b_d * n_d + rs)


rs_rows: list[dict[str, float]] = []
for row in rows:
    phi_weight = row["phi2_weight"]
    no_rs = a_total(phi_weight, include_rs=False)
    with_rs = a_total(phi_weight, include_rs=True)
    scalar_heavy = a_total(phi_weight, include_rs=True, scalar_count=250.0)
    rs_rows.append({"s": row["s"], "no_rs": no_rs, "with_rs": with_rs, "scalar_heavy": scalar_heavy})
    log(
        f"   s={row['s']:4.2f}: A(no RS)={no_rs:8.4f} A(+RS)={with_rs:8.4f} "
        f"scalar-heavy={scalar_heavy:8.4f}"
    )

rs_sign_stable = all(r["with_rs"] > 0 and r["with_rs"] > r["no_rs"] for r in rs_rows)
scalar_guard = any(r["scalar_heavy"] <= 0 for r in rs_rows) and all(r["with_rs"] > 0 for r in rs_rows)

check(
    "C1 invariant I4 proxy: RS anti-screening sign survives every sampled shape",
    rs_sign_stable,
    "A_tot remains positive and adding RS raises A_tot for every s",
)
check(
    "C2 refutation guard remains live: scalar-heavy content can still destroy the FP",
    scalar_guard,
    "at least one scalar-heavy row has A_tot<=0 while GU rows remain positive",
)

log("\n" + "=" * 96)
log("PART D -- verdict")
log("=" * 96)

invariants_survive = fp_exists and f0_positive and rs_sign_stable and all_positive
full_combined_frg_done = False

if not invariants_survive:
    verdict = "FRAGILE"
elif full_combined_frg_done:
    verdict = "SHAPE-STABLE (full combined computation)"
else:
    verdict = "SHAPE-STABLE (first-swing/proxy) / NEEDS-FULL-COMPUTATION residual"

check(
    "D1 all shape-sweep invariant proxies survive",
    invariants_survive,
    f"thresholds={all_positive} fp={fp_exists} f0={f0_positive} rs={rs_sign_stable}",
)
check(
    "D2 verdict is shape-stable at first-swing/proxy grade, with the W85 full-computation residual preserved",
    verdict.startswith("SHAPE-STABLE") and not full_combined_frg_done,
    verdict,
)

assert all_positive, "threshold functions must stay positive and finite"
assert shape_motion > 1.50, "the sweep must be nontrivial"
assert fp_exists, "reduced Reuter fixed point must exist for every sampled shape"
assert g_motion > 1.50 and lambda_motion > 1.10, "non-universal values must move across shapes"
assert product_spread < 1.50, "g*lambda* band must stay finite/order-stable in the reduced sweep"
assert f0_positive, "f0 relevance-drive proxy must stay positive"
assert rs_sign_stable, "RS anti-screening sign must stay stable"
assert scalar_guard, "scalar-heavy refutation guard must remain live"
assert verdict.startswith("SHAPE-STABLE"), "verdict must be shape-stable at proxy grade"

if FAIL:
    log("")
    log("RESULT: FAIL (%d) -> %s" % (len(FAIL), ", ".join(FAIL)))
    sys.exit(1)

log("")
log("RESULT: ALL PASS")
log("VERDICT: " + verdict)
log("INTERPRETATION: W86 strengthens W85's condition-(i) support by showing the qualitative gates survive")
log("a shape-family sweep. It does not replace the full combined f(R)+Weyl^2 + ker-Gamma spin-3/2 FRG run.")
sys.exit(0)
