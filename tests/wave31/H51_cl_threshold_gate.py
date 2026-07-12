#!/usr/bin/env python3
r"""H51 (Wave 31) -- c_L threshold gate for GU-under-H36's first sub-mm prediction.

Wave 30 (H50) reduced the GU-under-H36 prediction to one still-uncomputed geometric
coefficient:

    rho_Lambda = c_L * mu_DW^4
    m2 = sqrt(m2_eff) * mu_DW
    lambda = hbar_c / m2

This file does NOT compute the geometric DeWitt coefficient c_L. It computes the
decision thresholds H51 has to hit. Given the observed dark-energy scale
rho_Lambda^(1/4) = 2.3 meV and the H25 band m2_eff in [5/6, 5/4], it derives:

  * the predicted Yukawa range as a function of c_L;
  * the exact c_L thresholds corresponding to H50's cited short-range-gravity
    mu_DW floors;
  * the fair alpha=1/3 frontier band inherited from H50's conservative
    argued floor mu_DW in [3.0, 3.6] meV.

Exit 0 means the threshold ledger is internally consistent. The geometric H51
computation remains open: decide c_L from the horizontal-sectional constant and
source-action normalization.

Run: python -u tests/wave31/H51_cl_threshold_gate.py
"""
from __future__ import annotations

import math

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{(' -- ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


def log(message: str = "") -> None:
    print(message, flush=True)


HBAR_C_EV_NM = 197.327
RHO_LAMBDA_QTR_EV = 2.3e-3
M2EFF_LOW = 5.0 / 6.0
M2EFF_HIGH = 5.0 / 4.0

# H50 used these published alpha=1 crossings only as comparison anchors.
ALPHA1_CROSSINGS_UM = {
    "Kapner 2007 alpha=1": 56.0,
    "Tan 2020 alpha=1": 48.0,
    "Lee 2020 alpha=1": 38.6,
}

# H50's fair alpha=1/3 floor is argued from the published curves, not digitized.
ALPHA13_FLOOR_LOW_EV = 3.0e-3
ALPHA13_FLOOR_HIGH_EV = 3.6e-3


def mu_dw_from_c_l(c_l: float) -> float:
    """Return mu_DW from rho_Lambda = c_L * mu_DW^4 for positive c_L."""
    if c_l <= 0:
        raise ValueError("c_L is the positive vacuum-energy coefficient magnitude")
    return RHO_LAMBDA_QTR_EV / c_l ** 0.25


def lambda_um(mu_dw_ev: float, m2eff: float) -> float:
    """Return Yukawa range in microns for m2 = sqrt(m2_eff) * mu_DW."""
    return HBAR_C_EV_NM / (math.sqrt(m2eff) * mu_dw_ev) / 1000.0


def mu_floor_from_lambda_crossing(lambda_crossing_um: float) -> float:
    """Conservative floor: require even the longest H25 range to be below the crossing."""
    return HBAR_C_EV_NM / (math.sqrt(M2EFF_LOW) * lambda_crossing_um * 1000.0)


def c_l_threshold_for_mu_floor(mu_floor_ev: float) -> float:
    """Prediction clears a mu_DW floor iff c_L <= this threshold."""
    return (RHO_LAMBDA_QTR_EV / mu_floor_ev) ** 4


def range_for_c_l(c_l: float) -> tuple[float, float, float]:
    """Return (mu_DW, shortest lambda, longest lambda) for the H25 m2_eff band."""
    mu = mu_dw_from_c_l(c_l)
    shortest = lambda_um(mu, M2EFF_HIGH)
    longest = lambda_um(mu, M2EFF_LOW)
    return mu, shortest, longest


log("=" * 78)
log("H51 c_L THRESHOLD GATE")
log("=" * 78)

# H50 reproduction at c_L = 1.
mu_1, lam_short_1, lam_long_1 = range_for_c_l(1.0)
check(
    "c_L=1 reproduces H50's face-value DE-scale prediction",
    abs(mu_1 - 2.3e-3) < 1e-15 and 76.0 < lam_short_1 < 78.0 and 93.0 < lam_long_1 < 95.0,
    f"mu_DW={mu_1*1e3:.3f} meV, lambda=[{lam_short_1:.2f},{lam_long_1:.2f}] um",
)

# Monotonicity: smaller c_L raises mu_DW and shortens the Yukawa range.
candidates = [1.0, 3.0 / 8.0, 0.25, 0.20, 0.125]
rows = []
for c_l in candidates:
    mu, lam_short, lam_long = range_for_c_l(c_l)
    rows.append((c_l, mu, lam_short, lam_long))

check(
    "smaller c_L monotonically raises mu_DW and shortens both ends of the lambda band",
    all(rows[i + 1][1] > rows[i][1] and rows[i + 1][2] < rows[i][2] and rows[i + 1][3] < rows[i][3]
        for i in range(len(rows) - 1)),
)

log("")
log("Representative positive c_L values:")
for c_l, mu, lam_short, lam_long in rows:
    log(f"  c_L={c_l:7.4f} -> mu_DW={mu*1e3:6.3f} meV, lambda=[{lam_short:6.2f},{lam_long:6.2f}] um")

log("")
log("Exact c_L thresholds from H50's published alpha=1 comparison crossings:")
alpha1_thresholds = {}
for label, lambda_crossing in ALPHA1_CROSSINGS_UM.items():
    mu_floor = mu_floor_from_lambda_crossing(lambda_crossing)
    c_thr = c_l_threshold_for_mu_floor(mu_floor)
    alpha1_thresholds[label] = c_thr
    log(f"  {label:22s}: mu_DW floor={mu_floor*1e3:6.3f} meV -> clear iff c_L <= {c_thr:.6f}")

check(
    "alpha=1 c_L thresholds preserve the H50 ordering Kapner > Tan > Lee",
    alpha1_thresholds["Kapner 2007 alpha=1"]
    > alpha1_thresholds["Tan 2020 alpha=1"]
    > alpha1_thresholds["Lee 2020 alpha=1"],
)
check(
    "c_L=1 fails every published alpha=1 comparison floor",
    all(1.0 > threshold for threshold in alpha1_thresholds.values()),
)

log("")
log("Fair alpha=1/3 frontier band inherited from H50:")
c_l_live_high = c_l_threshold_for_mu_floor(ALPHA13_FLOOR_LOW_EV)
c_l_live_low = c_l_threshold_for_mu_floor(ALPHA13_FLOOR_HIGH_EV)
log(
    f"  floor mu_DW in [{ALPHA13_FLOOR_LOW_EV*1e3:.1f},{ALPHA13_FLOOR_HIGH_EV*1e3:.1f}] meV"
    f" -> live/frontier iff c_L is roughly <= [{c_l_live_low:.3f},{c_l_live_high:.3f}]"
)

mu_3_8, lam_short_3_8, lam_long_3_8 = range_for_c_l(3.0 / 8.0)
mu_02, lam_short_02, lam_long_02 = range_for_c_l(0.20)
check(
    "horizontal-sectional estimate c_L=3/8 remains just below the conservative alpha=1/3 low floor",
    mu_3_8 < ALPHA13_FLOOR_LOW_EV,
    f"mu_DW={mu_3_8*1e3:.3f} meV, lambda=[{lam_short_3_8:.2f},{lam_long_3_8:.2f}] um",
)
check(
    "c_L=0.20 clears the conservative alpha=1/3 low floor but not the high edge",
    ALPHA13_FLOOR_LOW_EV < mu_02 < ALPHA13_FLOOR_HIGH_EV,
    f"mu_DW={mu_02*1e3:.3f} meV, lambda=[{lam_short_02:.2f},{lam_long_02:.2f}] um",
)
check(
    "decision boundary is O(1), not a fine-tuned tiny coefficient",
    0.1 < c_l_live_low < c_l_live_high < 0.4,
    f"threshold band=[{c_l_live_low:.3f},{c_l_live_high:.3f}]",
)

log("")
log("Interpretation:")
log("  H51 does not need a 10^-122 miracle. It needs the positive normalized c_L to land")
log("  below an O(1) threshold: about 0.17-0.35 for the fair alpha=1/3 frontier band.")
log("  Above that band, GU-under-H36 remains face-value excluded; below it, the first")
log("  parameter-linked GU prediction moves back to the live sub-mm frontier.")
log("  The remaining task is geometric: compute c_L from the horizontal-sectional")
log("  constant plus source-action normalization, including sign and normalization choices.")

if FAIL:
    log(f"FAILED: {FAIL}")
    raise SystemExit(1)

log("=" * 78)
log("exit 0 = H51 threshold gate computed; geometric c_L value remains open.")
log("=" * 78)
